#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import argparse
import json
import os.path
import sys
import time

from redis_queue import RedisQueue
from const import DIR, TEMPLATE_BILL_URL, TWITTER_ACCOUNTS
from settings import TWITTER, FACEBOOK
import facebook
import twitter


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('target')
    return parser.parse_args()


def refine_bill_content(bill, max_field_len=30):
    # bill_id
    bill_id = bill['bill_id']

    # title
    title = bill['title']
    title = truncate(title, max_field_len)
    title_josa = ullul(title.strip('.')[-1])

    # proposer
    proposer = bill['status_dict']['접수']['의안접수정보'][0]['제안자']
    while isinstance(proposer, list):
        proposer = proposer[0]
    try:
        proposer_fullname = proposer[:proposer.index('의원')].strip()
    except ValueError as e:
        proposer_fullname = None
    proposer = truncate(proposer, max_field_len)
    proposer_josa = yiga(proposer.strip('.')[-1])

    return {
        'proposer': proposer,
        'proposer_fullname': proposer_fullname,
        'proposer_josa': proposer_josa,
        'title': title,
        'title_josa': title_josa,
        'bill_id': bill_id,
        'url': TEMPLATE_BILL_URL.format(bill_id)
    }


def post_bills_facebook(new_bills):
    if new_bills:
        print '\t'.join(new_bills)
        post_sentences = []
        post_sentences.append('오늘 국회에서 발의된 %d개의 새 의안 목록입니다.\n' % (len(new_bills)))
        for idx, bill_id in enumerate(new_bills):
            bill = get_bill(bill_id)
            bill = refine_bill_content(bill, None)
            bill['idx'] = idx
            post_sentences.append('%(idx)d. %(proposer)s, "%(title)s" %(url)s' % bill)
        post = "\n".join(post_sentences)
        facebook.post(post)


def post_bills_twitter(new_bills):
    if new_bills:
        cnt = len(new_bills)
        interval_min = TWITTER['INTERVAL'] / 60

        twitter.post('지금부터 %d분간 %d분 간격으로 %d개의 새 의안을 트윗할 예정입니다.' % (interval_min * cnt, interval_min, cnt))

    for bill_id in new_bills:
        bill = get_bill(bill_id)
        post_bill_twitter(bill)
        time.sleep(TWITTER['INTERVAL'])
        print '%s posted' % bill['bill_id']


def post_bill_twitter(bill):
    bill = refine_bill_content(bill)
    try:
        proposer = bill['proposer_fullname']
        if proposer and proposer in TWITTER_ACCOUNTS:
            twitter_handle = TWITTER_ACCOUNTS[proposer]
            if twitter_handle:
                bill['proposer'] = bill['proposer'].replace(proposer,
                        '%s(@%s)' % (proposer, twitter_handle))
    except Exception, e:
        print e
    status = '%(proposer)s%(proposer_josa)s "%(title)s"%(title_josa)s 새로 발의하였습니다. http://pokr.kr/bill/%(bill_id)s' % bill
    twitter.post(status)


def truncate(text, max_len):
    if max_len is None:
        return text

    if len(text) > max_len:
        text = text[:max_len] + '...'
    return text


def yiga(char):
    if (ord(char) - 44032) % 28:
        return '이'
    else:
        return '가'


def ullul(char):
    if (ord(char) - 44032) % 28:
        return '을'
    else:
        return '를'


def guess_session_id(bill_id):
    if bill_id.startswith('DD'):
        return 19
    elif bill_id.startswith('ZZ'):
        return int(bill_id[2:4])
    else:
        return int(bill_id[:2])


def get_bill(bill_id):
    SESSION = guess_session_id(bill_id)
    with open('%s/%d/%s.json' % (DIR['data'], SESSION, bill_id), 'r') as f:
        bill = json.load(f)
    return bill


if __name__ == '__main__':
    args = parse_args()

    if args.target == 'twitter':
        queue = RedisQueue('post_bills_twitter')
        bills = list(queue)
        post_bills_twitter(bills)
    elif args.target == 'facebook':
        queue = RedisQueue('post_bills_facebook')
        bills = list(queue)
        post_bills_facebook(bills)
    else:
        raise Exception('Unknown target')


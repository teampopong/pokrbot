# Caution: You probably don't want to change me

import json

from settings import METADIR, PDFDIR

likms           = 'http://likms.assembly.go.kr/bill/jsp'
PAGE_SIZE       = 50            # number of bills in list page (for crawling)
META_HEADERS    = ["bill_id","status","title","link_id","proposer_type","proposed_date","decision_date","decision_result","has_summaries","status_detail"]
HTML_FIELDS     = ['specifics', 'proposers', 'withdrawers', 'summaries']

TEMPLATE_BILL_URL = 'http://pokr.kr/bill/{0}'

DIR = {
    'pdf'          : PDFDIR + '/pdf',
    'meta'         : METADIR + '/meta',
    'data'         : METADIR + '/json',
    'txt'          : METADIR + '/txt',
    'list'         : METADIR + '/sources/list',
    'summaries'    : METADIR + '/sources/summaries',
    'specifics'    : METADIR + '/sources/specifics',
    'proposers'    : METADIR + '/sources/proposers',
    'withdrawers'  : METADIR + '/sources/withdrawers'
}

BASEURL = {
    'list'         : likms + '/BillSearchResult.jsp?',
    'summaries'    : likms + '/SummaryPopup.jsp?bill_id=',
    'specifics'    : likms + '/BillDetail.jsp?bill_id=',
    'specifics_old': likms + '/BillDetailBudget.jsp?bill_id=',
    'proposers'    : likms + '/CoactorListPopup.jsp?bill_id=',
    'withdrawers'  : likms + '/ReturnListPopup.jsp?bill_id='
}

X = {
    'columns'      : 'descendant::td',
    'spec_table'   : '//table[@width="940"]',
    'spec_entry'   : 'descendant::tr[@bgcolor="#EAF2ED"]/following-sibling::tr/td/div',
    'spec_status'  : '//td[@background="/bill/WebContents/BillDetail/circle_11.gif"]/text()',
    'spec_timeline': '//td[@bgcolor="#FEFFEF" and not(@id="SUMMARY_CONTENTS")]/table//tr',
    'spec_timeline_statuses'    : 'descendant::td[@width="59"]/node()',
    'spec_timeline_status_infos': 'descendant::td[@style="display:none"]/textarea/text()',
    'spec_title'   : '//td[@height="33" and @class="title_large"]/text()',
    'summary'      : '//span[@class="text6_1"]/text()',
    'proposers'    : '//td[@width="10%" and @height="20"]/text()',
    'table'        : '//table[@width="970"]//table[@width="100%"]//table[@width="100%"]//tr[not(@bgcolor="#DBDBDB")][position()>1]',
    'withdrawers'  : '//td[@width="10%" and @height="20"]/text()'
}

import os.path
current_dir = os.path.dirname(os.path.abspath(__file__))
with open(os.path.join(current_dir, 'twitter_accounts.json')) as f:
    TWITTER_ACCOUNTS = json.load(f)

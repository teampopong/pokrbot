# @pokrbot

Facebook, Twitter robots for publishing legislations.


## Twitter

### Setup

You first need to create `settings.py`.

    $ cp settings.py.sample settings.py

#### 1. Create Twitter Consumer Key 

1. Create an app in <https://apps.twitter.com/>
1. Raise the access level to 'Read and Write'
1. Copy *consumer key* and *consumer secret*
1. Fill in the variables in `settings.py`: `TWITTER_CONSUMER_KEY`, `TWITTER_CONSUMER_SECRET` of `settings.py`

#### 2. Create OAuth Token

1. Run

    $ python twitter.py
1. Open the link given by the program.
1. Copy and paste the verification code given in the browser, into the command line.<br>
   Then you'll get *oauth token* and *oauth token secret*
1. Fill in the variables in `settings.py`: `TWITTER_OAUTH_TOKEN`, `TWITTER_OAUTH_TOKEN_SECRET`

#### 3. ????

#### 4. Profit!


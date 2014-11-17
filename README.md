# @pokrbot

Facebook, Twitter robots for publishing legislations.

## Setup

    $ sudo apt-get install redis-server redis-tools
    $ redis-server
    $ pip install -r requirements.txt
    $ cp settings.py.sample settings.py

### Twitter

1. Create Twitter Consumer Key
    - Create an app at <https://apps.twitter.com/>
    - Raise the access level to 'Read and Write'
    - Copy *consumer key* and *consumer secret* to `TWITTER_CONSUMER_KEY`, `TWITTER_CONSUMER_SECRET` in `settings.py`

2. Create OAuth Token

         $ python twitter.py

     - Open the link given by the program. (Make sure to login as the user that you want to tweet posts)
     - Copy and paste the verification code given in the browser into the command line.<br>
     - Then you'll get *oauth token* and *oauth token secret*.
     - Copy and paste them into the blanks of `settings.py`: `TWITTER_OAUTH_TOKEN`, `TWITTER_OAUTH_TOKEN_SECRET`

### Facebook

1. Create Facebook Client ID
    1. [Create new App](https://developers.facebook.com/quickstarts/?platform=web)
    2. Copy *App ID*, *App Secret* to `FACEBOOK_CLIENT_ID`, `FACEBOOK_CLIENT_SECRET` in `settings.py`

1. Create page short access token
    - Go to the [Graph API Explorer](http://developers.facebook.com/tools/explorer/)
    - Choose your app from the dropdown menu
    - Click "Get Access Token"
    - Choose the `manage_pages` permission
    - Copy `Access Token` and paste to `FACEBOOK_OAUTH_TOKEN` in `settings.py`

1. Create page long access token

## Usage

    $ ./post.py facebook --test # Uploads post to `pokrbottest`
    $ ./post.py facebook
    $ ./post.py twitter --test
    $ ./post.py twitter

## References

### Facebook

- [Publishing new statuses](https://developers.facebook.com/docs/graph-api/reference/v2.2/page/feed#publish)
- [See my apps](https://developers.facebook.com/apps)

## License

- Apache 2.0

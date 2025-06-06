# dashboard/twitter_api.py

import tweepy

def get_user_tweets(screen_name):
    """
    Fetches the 5 most recent tweets for a given Twitter handle.
    
    NOTE: Replace placeholder keys with your actual Twitter Developer API credentials.
    """
    # --- IMPORTANT ---
    # It's highly recommended to store these secrets in environment variables
    # or a Django settings configuration instead of hardcoding them.
    consumer_key = 'YOUR_CONSUMER_KEY'
    consumer_secret = 'YOUR_CONSUMER_SECRET'
    access_token = 'YOUR_ACCESS_TOKEN'
    access_token_secret = 'YOUR_ACCESS_TOKEN_SECRET'

    try:
        # Authenticate with the Twitter API
        auth = tweepy.OAuth1UserHandler(consumer_key, consumer_secret, access_token, access_token_secret)
        api = tweepy.API(auth)
        
        # Fetch timeline tweets
        # The 'extended' mode ensures you get the full text of the tweet
        tweets = api.user_timeline(screen_name=screen_name, count=5, tweet_mode="extended")
        
        return tweets
    except tweepy.errors.TweepyException as e:
        # Handle potential API errors gracefully
        print(f"Error fetching tweets: {e}")
        return [{"full_text": f"Error fetching tweets for @{screen_name}: {e}"}]
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return [{"full_text": "An unexpected error occurred while fetching tweets."}]

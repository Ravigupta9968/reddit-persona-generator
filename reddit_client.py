import praw
from datetime import datetime
from typing import List, Tuple, Dict

class RedditClient:
    def __init__(self, client_id: str, client_secret: str, user_agent: str):
        """Initialize Reddit API client."""
        self.reddit = praw.Reddit(
            client_id=client_id,
            client_secret=client_secret,
            user_agent=user_agent
        )

    def extract_user_info(self, username: str, limit: int = 100) -> Tuple[List[Dict], List[Dict]]:
        """Extract posts and comments from a Reddit user."""
        try:
            redditor = self.reddit.redditor(username)
            posts = []
            comments = []

            for submission in redditor.submissions.new(limit=limit):
                posts.append({
                    'id': submission.id,
                    'title': submission.title if submission.title else '',
                    'text': submission.selftext if hasattr(submission, 'selftext') and submission.selftext else '',
                    'subreddit': submission.subreddit.display_name if submission.subreddit else 'unknown',
                    'timestamp': datetime.fromtimestamp(submission.created_utc) if submission.created_utc else datetime.now()
                })

            for comment in redditor.comments.new(limit=limit):
                comments.append({
                    'id': comment.id,
                    'text': comment.body if comment.body else '',
                    'subreddit': comment.subreddit.display_name if comment.subreddit else 'unknown',
                    'timestamp': datetime.fromtimestamp(comment.created_utc) if comment.created_utc else datetime.now()
                })

            return posts, comments
        except Exception as e:
            print(f"Error extracting user info for {username}: {e}")
            return [], []
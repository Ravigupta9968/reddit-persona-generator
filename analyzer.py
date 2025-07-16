import re
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
from collections import defaultdict
from typing import List, Dict
from datetime import datetime

nltk.download('vader_lexicon', quiet=True)

class Analyzer:
    def __init__(self):
        """Initialize sentiment analyzer and persona dictionary."""
        self.sia = SentimentIntensityAnalyzer()
        self.persona = {
            'interests': defaultdict(int),
            'demographics': {},
            'behavior': {},
            'sentiments': []
        }

    def reset_persona(self) -> None:
        """Reset the persona dictionary for a new user."""
        self.persona = {
            'interests': defaultdict(int),
            'demographics': {},
            'behavior': {},
            'sentiments': []
        }

    def clean_text(self, text: str) -> str:
        """Clean text by removing URLs and special characters."""
        if not text:
            return ''
        text = re.sub(r'http\S+', '', text)
        text = re.sub(r'[^\w\s]', '', text)
        return text.strip()

    def analyze_content(self, posts: List[Dict], comments: List[Dict]) -> None:
        """Analyze posts and comments to build user persona."""
        try:
            for post in posts:
                if not all(key in post for key in ['id', 'title', 'text', 'subreddit', 'timestamp']):
                    print(f"Skipping invalid post: {post}")
                    continue
                subreddit = post['subreddit'].lower()
                self.persona['interests'][subreddit] += 1
                # Sentiment analysis for post
                text_to_analyze = post['title'] + (' ' + post['text'] if post['text'] else '')
                sentiment = self.sia.polarity_scores(self.clean_text(text_to_analyze))
                self.persona['sentiments'].append({
                    'type': 'post',
                    'id': post['id'],
                    'subreddit': subreddit,
                    'compound': sentiment['compound']
                })

            for comment in comments:
                if not all(key in comment for key in ['id', 'text', 'subreddit', 'timestamp']):
                    print(f"Skipping invalid comment: {comment}")
                    continue
                subreddit = comment['subreddit'].lower()
                self.persona['interests'][subreddit] += 1
                # Sentiment analysis for comment
                sentiment = self.sia.polarity_scores(self.clean_text(comment['text']))
                self.persona['sentiments'].append({
                    'type': 'comment',
                    'id': comment['id'],
                    'subreddit': subreddit,
                    'compound': sentiment['compound']
                })

            all_text = ' '.join([p['title'] + (' ' + p['text'] if p['text'] else '') for p in posts] + 
                              [c['text'] for c in comments])
            word_count = len(all_text.split())
            self.persona['demographics']['activity_level'] = (
                f"Active (based on {len(posts)} posts and {len(comments)} comments analyzed)"
            )
            self.persona['demographics']['language_complexity'] = (
                f"Moderate (based on average {word_count/(len(posts) + len(comments) + 1):.1f} words per contribution)"
            )

            timestamps = [p['timestamp'] for p in posts] + [c['timestamp'] for c in comments]
            if timestamps:
                hours = [t.hour for t in timestamps]
                avg_hour = sum(hours) / len(hours)
                self.persona['behavior']['active_time'] = (
                    f"Most active around {int(avg_hour)}:00 UTC (based on post and comment timestamps)"
                )
        except Exception as e:
            print(f"Error analyzing content for user: {e}")
            self.persona['demographics']['activity_level'] = "Unknown (analysis failed)"
            self.persona['demographics']['language_complexity'] = "Unknown (analysis failed)"
            self.persona['behavior']['active_time'] = "Unknown (analysis failed)"
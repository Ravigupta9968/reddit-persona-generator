Reddit Persona Generator
This repository contains a modular Python application that generates user personas based on Reddit user profiles by analyzing their posts and comments. The code is split into separate modules for clarity and maintainability, suitable for a professional submission.

Setup Instructions

Install Python: Ensure Python 3.8+ is installed. Verify with:
python --version


Install Dependencies: Install required packages using pip:
pip install praw nltk


Reddit API Credentials:

Create a Reddit app at https://www.reddit.com/prefs/apps.
Select "script" as the app type, set redirect URI to http://localhost:8000.
Create a config.py file in the project directory with:# config.py
CLIENT_ID = "your_client_id"
CLIENT_SECRET = "your_client_secret"
USER_AGENT = "PersonaGenerator/1.0 by YourRedditUsername"




Directory Setup:

The script creates an output directory for persona files.



Execution Instructions

Run the Script:

To generate personas for sample users (kojied, Hungry-Move-6603, spez):python main.py


To process a new user, edit sample_users in main.py:sample_users = ['new_username']




Output:

Persona files are saved in the output directory as username_persona.txt.
Each file includes:
Interests: Top subreddits with frequencies and citations.
Demographics: Activity level and language complexity.
Behavior: Most active time based on timestamps.
Sentiment: Overall tone with citations.





Notes

Code follows PEP-8 guidelines for readability.
Uses PRAW for Reddit API access and NLTK for sentiment analysis.
Modular design separates concerns (data extraction, analysis, file generation).
Includes error handling for robust operation.
Sample outputs for kojied, Hungry-Move-6603, and spez are included in the output directory.

Sample Output Structure
User Persona for Reddit User: username
==================================================

Interests:
- subreddit1 (mentioned X times) [Citations: Post ID: abc123, Comment ID: def456]
- subreddit2 (mentioned Y times) [Citations: Post ID: ghi789]

Demographics:
- Activity Level: Active (based on X posts and Y comments analyzed)
- Language Complexity: Moderate (based on average Z words per contribution)

Behavior:
- Active Time: Most active around HH:00 UTC (based on post and comment timestamps)

Overall Sentiment:
- General tone: Positive (avg score: 0.XX) [Citations: abc123, def456, ghi789]

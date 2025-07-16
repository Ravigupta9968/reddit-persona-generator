# Reddit Persona Generator

This Python application generates user personas by analyzing Reddit user profiles, extracting their posts and comments to infer interests, demographics, behavior, and sentiment. The code is organized into clean, maintainable modules—suitable for professional submissions.

---

## Setup Instructions

### 1. Install Python

Ensure Python 3.8+ is installed. Confirm using:

```bash
python --version
```

### 2. Install Dependencies: Install required packages using pip:
```bash
pip install praw nltk
```

### 3. Reddit API Credentials:

- Create a Reddit app at https://www.reddit.com/prefs/apps.
- Select "script" as the app type, set redirect URI to http://localhost:8000.
- Create a config.py file in the project directory with:
```bash
#config.py
CLIENT_ID = "your_client_id"
CLIENT_SECRET = "your_client_secret"
USER_AGENT = "PersonaGenerator/1.0 by YourRedditUsername"
```

## Directory Setup:

- The script creates an ```output/``` directory for persona files.



##  Execution Instructions

### Run the Script:

- To generate personas for sample users (```kojied```, ```Hungry-Move-6603```):
```bash
python main.py
```


- To process a new user, edit sample_users in ```main.py```:
```bash
sample_users = ['new_username']
```




## Output:

Persona files are saved in the ```output/``` directory as ```username_persona.txt.```
Each file includes:
- Interests: Top subreddits with frequencies and citations.
- Demographics: Activity level and language complexity.
- Behavior: Most active time based on timestamps.
- Sentiment: Overall tone with citations.


## Notes

- Uses ```PRAW``` for Reddit API access and ```NLTK``` for sentiment analysis.
- Modular design separates concerns (```data extraction```, ```analysis```, ```file generation```).
- Includes error handling for robust operation.
- Sample outputs for ```kojied```, ```Hungry-Move-6603``` are included in the output directory.

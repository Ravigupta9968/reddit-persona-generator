from config import CLIENT_ID, CLIENT_SECRET, USER_AGENT
from reddit_client import RedditClient
from analyzer import Analyzer
from persona_generator import PersonaGenerator

def main():
    reddit_client = RedditClient(CLIENT_ID, CLIENT_SECRET, USER_AGENT)
    analyzer = Analyzer()
    persona_generator = PersonaGenerator()

    sample_users = ['kojied', 'Hungry-Move-6603']
    for user in sample_users:
        print(f"Processing user: {user}")
        analyzer.reset_persona()  
        posts, comments = reddit_client.extract_user_info(user)
        analyzer.analyze_content(posts, comments)
        persona_generator.generate_persona_file(user, analyzer.persona)

if __name__ == "__main__":
    main()
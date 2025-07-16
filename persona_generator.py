import os
from typing import Dict

class PersonaGenerator:
    def __init__(self):
        """Initialize persona generator."""
        pass

    def generate_persona_file(self, username: str, persona: Dict, output_dir: str = "output") -> None:
        """Generate persona text file with citations."""
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

        output_file = os.path.join(output_dir, f"{username}_persona.txt")
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(f"User Persona for Reddit User: {username}\n")
            f.write("=" * 50 + "\n\n")

            # Interests
            f.write("Interests:\n")
            top_interests = sorted(persona['interests'].items(), 
                                key=lambda x: x[1], reverse=True)[:5]
            for interest, count in top_interests:
                # Find citations
                citations = []
                for item in persona['sentiments']:
                    if not isinstance(item, dict) or 'id' not in item or 'subreddit' not in item:
                        print(f"Skipping invalid sentiment item: {item}")
                        continue
                    if item['subreddit'] == interest:
                        citations.append(f"{item['type'].capitalize()} ID: {item['id']}")
                f.write(f"- {interest} (mentioned {count} times) [Citations: {', '.join(citations[:2]) or 'None'}]\n")
            f.write("\n")

            # Demographics
            f.write("Demographics:\n")
            for key, value in persona['demographics'].items():
                f.write(f"- {key.replace('_', ' ').title()}: {value}\n")
            f.write("\n")

            # Behavior
            f.write("Behavior:\n")
            for key, value in persona['behavior'].items():
                f.write(f"- {key.replace('_', ' ').title()}: {value}\n")
            f.write("\n")

            # Sentiment
            f.write("Overall Sentiment:\n")
            valid_sentiments = [s for s in persona['sentiments'] if isinstance(s, dict) and 'compound' in s]
            if valid_sentiments:
                avg_sentiment = sum(s['compound'] for s in valid_sentiments) / len(valid_sentiments)
                sentiment_label = "Positive" if avg_sentiment > 0.1 else "Negative" if avg_sentiment < -0.1 else "Neutral"
                sentiment_citations = [s['id'] for s in valid_sentiments if 'id' in s][:3]
                f.write(f"- General tone: {sentiment_label} (avg score: {avg_sentiment:.2f}) "
                       f"[Citations: {', '.join(sentiment_citations) or 'None'}]\n")
            else:
                f.write("- General tone: Unknown (no valid sentiment data available)\n")

        print(f"Persona file generated: {output_file}")
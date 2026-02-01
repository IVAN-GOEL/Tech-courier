# starting with the api
import feedparser
import time
import requests
from telegram import Bot
import u_inputs
from u_inputs import Input
from u_inputs import get_telegram_id
from timeupdate import getTIME


#time in IST is
timee=getTIME()

# my telegram bot token
TOKEN = "YOUR_TOKEN_HERE"
bot = Bot(token=TOKEN)
CHAT_ID = get_telegram_id()


print(f"Token: {TOKEN}")
print(f"Chat ID: {CHAT_ID}")
print(f"********************\n")

# RSS feeds to check
Feeds = {
    "Hacker News": "https://news.ycombinator.com/rss",
    "Google Tech": "https://news.google.com/rss/search?q=technology",
    "Google AI": "https://news.google.com/rss/search?q=artificial+intelligence",
    "BBC": "http://feeds.bbci.co.uk/news/technology/rss.xml",
    "TechCrunch": "https://techcrunch.com/feed/",
    "The Verge Tech": "https://www.theverge.com/rss/index.xml",
    "Ars Technica": "https://feeds.arstechnica.com/arstechnica/index",
    "OpenAI Blog": "https://openai.com/blog/rss/",
    "Towards Data Science": "https://towardsdatascience.com/feed",
    "MIT AI News": "https://news.mit.edu/rss/topic/artificial-intelligence2",
    "Open Source.com": "https://opensource.com/feed",
    "Linux Foundation": "https://www.linuxfoundation.org/feed/",
    "MLH News": "https://news.mlh.io/posts/feed",
    "Dev.to": "https://dev.to/feed",
    "Stack Overflow Blog": "https://stackoverflow.blog/feed/",
    "FreeCodeCamp": "https://www.freecodecamp.org/news/rss/",
    "GitHub Blog": "https://github.blog/feed/",
    "HackerEarth Challenges": "https://www.hackerearth.com/challenges/feed/",
    "Codeforces Contests": "https://codeforces.com/feeds",
    "Kaggle Competitions": "https://www.kaggle.com/competitions.rss",
    "Y Combinator": "https://www.ycombinator.com/blog/rss",
    "Product Hunt": "https://www.producthunt.com/feed",
    "Indie Hackers": "https://www.indiehackers.com/feed.xml",
    "MIT Technology Review": "https://www.technologyreview.com/feed/",
    "Google AI Hackathons": "https://news.google.com/rss/search?q=AI+hackathon",
    "Google Startup Funding": "https://news.google.com/rss/search?q=startup+funding+technology",
    "Engineering Blogs": "https://engineeringblogs.xyz/feed.xml",
    "High Scalability": "http://feeds.feedburner.com/HighScalability",
    "GitHub Security Advisories": "https://github.com/security-advisories.atom",
    "Open Source Agenda": "https://www.opensourceagenda.com/rss",
    "Python Insider": "https://blog.python.org/feeds/posts/default",
    "Real Python": "https://realpython.com/atom.xml",
    "JavaScript Weekly": "https://javascriptweekly.com/rss",
    "Go Blog": "https://go.dev/blog/feed.atom",
    "CodeChef Contests": "https://www.codechef.com/feeds/news",
    "TopCoder Challenges": "https://www.topcoder.com/challenges/feed/",
    "Papers With Code": "https://paperswithcode.com/rss",
    "Machine Learning Mastery": "https://machinelearningmastery.com/blog/feed/",
    "AWS Blog": "https://aws.amazon.com/blogs/aws/feed/",
    "Google Cloud Blog": "https://cloud.google.com/blog/rss",
    "Azure Blog": "https://azure.microsoft.com/en-us/blog/feed/",
    "Kubernetes Blog": "https://kubernetes.io/feed.xml",
    "Ethereum Blog": "https://blog.ethereum.org/feed.xml",
    "CoinDesk Tech": "https://www.coindesk.com/arc/outboundfeeds/rss/",
    "Web3 Foundation": "https://web3.foundation/rss/",
}

# Store already seen links to avoid duplicates
seen_links = set()

# creating a readable file aswell for the user
file = open("report.txt", "a")


def send_text(text):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    payload = {"chat_id": CHAT_ID, "text": text, "parse_mode": "HTML"}
    print(f"\n Attempting to send message...")
    print(f"URL: {url}")
    print(f" Message: {text[:100]}...")
    response = requests.post(url, data=payload)
    print(f" Response Status: {response.status_code}")
    print(f" Response Body: {response.json()}")
    return response


def send_file(file_path):
    url = f"https://api.telegram.org/bot{TOKEN}/sendDocument"
    payload = {"chat_id": CHAT_ID}
    print(f"\nAttempting to send file: {file_path}")
    with open(file_path, "rb") as f:
        files = {"document": f}
        response = requests.post(url, data=payload, files=files)
        print(f"File send status: {response.status_code}")
        print(f" Response: {response.json()}")
        return response


def topic_match(text, topics):
    # Check if any topic exists in the feeds text
    return any(topic.lower() in text for topic in topics)


# checking the relevant feeds for matches with topics
def check_rss():
    print(f"\n****************************************")
    print(f"Checking RSS feeds for topics: {topics}")
    print(f"****************************************\n")
    matches_found = 0

    for source, url in Feeds.items():
        print(f"Checking {source}...", end=" ")
        try:
            feed = feedparser.parse(url)
            entries_count = len(feed.entries)
            print(f"({entries_count} entries)")

            for entry in feed.entries:
                title = entry.get("title", "").lower()
                link = entry.get("link", "")

                if not link or link in seen_links:
                    continue

                if topic_match(title, topics):
                    seen_links.add(link)
                    matches_found += 1

                    print(f"\n MATCH FOUND!!!!")
                    print(f"[{source}] {entry.get('title')}")
                    print(f" {link}\n")

                    msg = f"<b>[{source}]</b> {entry.get('title')}\n{link}"


                    with open("report.txt", "a") as f:
                        f.write(f"[{source}] {entry.get('title')}\n{link}\n\n")

                    # Send to Telegram
                    send_text(msg)
        except Exception as e:
            print(f"ERROR: {e}")

    print(f"\n********************")
    print(f"Total matches found: {matches_found}")
    print(f"********************\n")

    # Send file only once after all matches are found
    if matches_found > 0:
        send_file("report.txt")
    else:
        print("No matches found. No messages sent to Telegram.")
        print("you might have chosen irrelevant topics")


def main():
    global topics
    topics = Input()

    print(f"\nStarting RSS monitoring for topics: {topics}")
    print(f"Messages will be sent to Telegram Chat ID: {CHAT_ID}\n")

    # Run once immediately for testing
    check_rss()

    # Ask if user wants to continue monitoring
    cont = input("\nDo you want to continue monitoring every 5 minutes? (y/n): ")
    if cont.lower() == 'y':
        while True:
            time.sleep(300)
            check_rss()
    else:
        print("Exiting...")


if __name__ == "__main__":
    main()

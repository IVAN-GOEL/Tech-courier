# TECH COURIER
To stay up to date on subjects that are important to you, like Python, remote jobs, open source, hackathons, or tech news, this script continuously scans a few RSS feeds. The script automatically scans new posts as they are published, eliminating the need to manually check numerous websites every day.

The system reads RSS feeds on a regular basis and examines the title and synopsis of each article. The article is marked as relevant if any of your predetermined keywords appear in the content. By doing this, you can be sure that you only get updates that are relevant to your interests and avoid unneeded or irrelevant information.

After identifying a relevant post, the script analyses the article's text using basic sentiment analysis to ascertain whether the tone is generally positive or negative. This eliminates the need for you to open the entire article right away, allowing you to quickly grasp the nature of the news—whether it's an announcement, an opportunity, or something important. Following content processing, the script produces a concise, readable synopsis that consists of: • The title of the article • A succinct explanation • The sentiment that was identified (positive or negative) • The RSS feed's origin A Telegram bot then uses this summary to automatically send it to your Telegram account, giving you real-time access to critical updates on your desktop or phone.

The script is simple to modify, lightweight, and expandable to accommodate: 
• Several RSS sources 
• Personalised lists of keywords 
• Real-time or daily alerts 
All things considered, this project is an attempt for customised tech news assistant, assisting you in effectively staying informed without experiencing information overload.

You’ll be asked to:
•	Enter number of topics
•	Provide keywords of interest
•	Receive updates directly on Telegram

📬 Sample Telegram Message
📰 New Tech Update Found!
🔹 Title: Python 3.13 Performance Improvements
🔹 Source: Hacker News
🔹 Sentiment: Positive 😊

⚙️ Customization
•	➕ Add RSS feeds in feeds.py
•	🧩 Change keywords anytime
•	⏳ Adjust update frequency using time.sleep()
•	📊 Extend sentiment analysis logic easily

📌 Future Enhancements
•sentiment analysis
•discord integration 
•reddit integration
•summarization

Pull requests are welcome!
If you find bugs or have feature ideas, feel free to open an issue.
Please feel free to contribute!

<img width="1024" height="1024" alt="image" src="https://github.com/user-attachments/assets/832276ef-e7ad-401d-82e4-54d72ac59e3f" />





  

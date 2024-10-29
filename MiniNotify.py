import requests
from plyer import notification


def fetch_news(topic):
    api_key='5905810717644c658abaa601506a6cc0'
    url=f'https://newsapi.org/v2/everything?q={topic}&pagesize=1&apikey={api_key}'

    response =requests.get(url,verify=False)
    if response.status_code == 200:
        news_data = response.json()
        article = news_data['articles'][0]
        title = article['title']
        description = article['description']
        return title, description
    else:
        return "ERROR" , "Could not fetch news"

def show_notification (title,message ):
    max_len=60
    if len(title)>max_len:
        title=title[:max_len]+ "..."
    if len(message)>max_len:
        message=message[:max_len]+ "..."

    notification.notify( 
        title = title,
        message=message,
        timeout=10
    )

topic = "FAB BANK"
title, description = fetch_news(topic)
if title:
    show_notification(title,description)
else:
    show_notification("ERROR" , "Not Able to fetch news")
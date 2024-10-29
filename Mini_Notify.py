import requests
import tkinter as tk
from plyer import notification
import threading 
import time

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
    limit_message=''.join(message.split()[:100])

    notification.notify( 
        title = title,
        message=limit_message,
        app_name="News Notifier",
        timeout=10
    )

def update_news():
    while True:
        topic=topic_entry.get()
        if topic:
            title,description=fetch_news(topic)
            show_notification(title,description)
        else:
            show_notification("No Topic", "PLease enter a new topic")
        time.sleep(500)
def News_update ():
    threading.Thread(target=update_news,daemon=True).start()

def setup_gui():
    global topic_entry

    root =tk.Tk()
    root.title("News Topic Input")
    root.geometry("300x120")
    root.resizable(False,False)

    tk.Label(root,text ="Enter Topic").pack(pady=10)
    topic_entry=tk.Entry(root,width=300)
    topic_entry.pack(pady=5)

    start_button=tk.Button(root,text="Start Update",command=News_update)
    start_button.pack(pady=10)

    root.mainloop()

if __name__=="__main__":
    setup_gui()
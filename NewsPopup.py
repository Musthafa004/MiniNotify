import requests
import tkinter as tk
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


def update_news():
    while True:
        topic=topic_entry.get()
        if topic:
            title,description=fetch_news(topic)
            result_label.config(text=f"Title: {title}\nDescription : {description}")
        else:
            result_label.config(text="No Topic : Please enter a new topic.")
        time.sleep(500)
def News_update ():
    threading.Thread(target=update_news,daemon=True).start()

def setup_gui():
    global topic_entry, result_label

    root =tk.Tk()
    root.title("News Topic Input")
    root.geometry("500x250")
    root.resizable(False,False)

    tk.Label(root,text ="Enter Topic").pack(pady=10)
    topic_entry=tk.Entry(root,width=30)
    topic_entry.pack(pady=5)

    start_button=tk.Button(root,text="Start Update",command=News_update)
    start_button.pack(pady=10)
    result_label =tk.Label(root,text="",wraplength=350)
    result_label.pack(pady=10)

    root.mainloop()

if __name__=="__main__":
    setup_gui()
import tkinter as tk
import nltk
from textblob import TextBlob
from newspaper import Article



    # nltk.download('punkt')
def Summarize():
    url = utext.get('1.0', "end").strip()

    article = Article(url)

    article.download()
    article.parse()

    article.nlp()

    title.config(state = 'normal')
    author.config(state = 'normal')
    publication.config(state = 'normal')
    summary.config(state = 'normal')
    sentiment.config(state = 'normal')
    
    title.delete('1.0', "end")
    title.insert('1.0', article.title)
    
    author.delete('1.0', "end")
    author.insert('1.0', article.authors)
    
    if article.publish_date is not None:
        publication.insert('1.0', str(article.publish_date))
    else: 
        publication.insert('1.0', "Publishing date not available")

    
    summary.delete('1.0', "end")
    summary.insert('1.0', str(article.summary))
    
    analysis = TextBlob(article.text)
    sentiment.delete("1.0", "end")
    sentiment.insert('1.0', f'Polarity: {analysis.polarity}, Sentiment : {"Positive" if analysis.polarity > 0 else "negative" if analysis.polarity < 0 else "neutral"}')

    title.config(state = 'disabled')
    author.config(state = 'disabled')
    publication.config(state = 'disabled')
    summary.config(state = 'disabled')
    sentiment.config(state = 'disabled')

    
root = tk.Tk()
root.title("News Summarizer")
root.configure(bg = '#856ff8')
root.geometry("1200x600")

tlabel = tk.Label(root, text="Title")
tlabel.pack()

title = tk.Text(root, height=1, width=140)
title.config(state='disabled', bg='#dddddd')
title.pack()

alabel = tk.Label(root, text="Author")
alabel.pack()

author = tk.Text(root, height=1, width=140)
author.config(state='disabled', bg='#dddddd')
author.pack()

plabel = tk.Label(root, text="Publishing Date")
plabel.pack()

publication = tk.Text(root, height=1, width=140)
publication.config(state='disabled', bg='#dddddd')
publication.pack()


slabel = tk.Label(root, text="Summary")
slabel.pack()

summary = tk.Text(root, height=20, width=140)
summary.config(state='disabled', bg='#dddddd')
summary.pack()


selabel = tk.Label(root, text="Sentiment Analysis")
selabel.pack()

sentiment = tk.Text(root, height=1, width=140)
sentiment.config(state='disabled', bg='#dddddd')
sentiment.pack()

ulabel = tk.Label(root, text="URL")
ulabel.pack()

utext = tk.Text(root, height=1, width=140)
utext.config( bg='#dddddd')
utext.pack()

button = tk.Button(root, text="Summarize", command = Summarize)
button.pack()

root.mainloop()


import requests
from flask import Flask,render_template,request


app = Flask(__name__,template_folder="template")

url = "https://meme-api.com/gimme"

def Meme():
    response = requests.get(url)
    data = response.json()
    return data["url"] , data["subreddit"] , data["title"]




@app.route("/")
def index():
    img = Meme()[0]
    subreddit = Meme()[1]
    title = Meme()[2]
    return render_template('index.html',img=img,subreddit=subreddit,title=title)
        


app.run(debug=True)
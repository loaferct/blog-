from flask import Flask, render_template
import requests

app = Flask(__name__)
blog_url = 'https://api.npoint.io/56eaedf05bb45b583251'

@app.route('/')
def home():
    response = requests.get(blog_url)
    data = response.json()
    return render_template("index.html", posts = data)

@app.route('/<num>')
def posted(num):
    response = requests.get(blog_url)
    datas = response.json()
    for post in datas:
        if int(post['id']) == int(num):
            blog_title = post['title']
            blog_text = post['body']
    
    return render_template('post.html', title = blog_title, subtitle = blog_text)

if __name__ == "__main__":
    app.run(debug=True)

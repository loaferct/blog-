from flask import Flask, render_template
import requests
import json

app = Flask(__name__)
blog_url = 'https://api.npoint.io/56eaedf05bb45b583251'
response = requests.get(blog_url)
data = response.json()
    
@app.route('/')
def home():
    return render_template("index.html", posts = data)

@app.route('/aboutme')
def aboutme():
    return render_template('about.html')

@app.route('/contact')
def contactme():
    return render_template('contact.html')

@app.route('/post/<num>')
def post(num):
    for post in data:
        if int(post['id']) == int(num):
            blog_title = post['title']
            blog_text = post['body']   
            blog_subtitle = post['subtitle']
    return render_template('post.html', subtitle = blog_subtitle, title = blog_title, text = blog_text)
    
if __name__ == '__main__':
    app.run(debug = True)
    

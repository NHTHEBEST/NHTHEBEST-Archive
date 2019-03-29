from flask import Flask, render_template
import markdown

app = Flask(__name__)


def gethtml(md):
    return markdown.markdown(md,extensions=['fenced_code'])


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/<post>')
def post(post):
    md = ""
    code = 200
    try:
        f = open("markdown/"+post+".md", "r")
        md = f.read()
        f.close()
    except:
        f = open("markdown/404.md", "r")
        md = f.read()
        f.close()
        code = 404
    html = gethtml(md)
    return render_template('post.html', post=html),code

@app.errorhandler(404)
def not_found(error):
    f = open("markdown/404.md", "r")
    md = f.read()
    f.close()
    return render_template('page.html', post=gethtml(md)),404


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0',port=8080)
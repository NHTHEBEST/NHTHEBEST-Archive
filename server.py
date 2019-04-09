from flask import Flask, render_template, send_from_directory
import markdown, os

app = Flask(__name__)


def gethtml(md):
    return markdown.markdown(md,extensions=['fenced_code'])


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static/favicon'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')

@app.route('/p/<post>')
def post(post):
    md = ""
    code = 200
    try:
        f = open("markdown/"+post+".md", "r")
        md = f.read()
        f.close()
    except:
        return not_found()
    html = gethtml(md)
    return render_template('post.html', post=html, title=post)

@app.errorhandler(404)
def not_found(error):
    f = open("markdown/404.md", "r")
    md = f.read()
    f.close()
    return render_template('post.html', post=gethtml(md), title="404 Not Found"),404

# main
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)
    

from flask import Flask, render_template, send_from_directory, request
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


# shuld retune 5 usfull options only 
@app.route('/searchin/<inp>')
def menu(inp):
    return '<option value="HTML">'
# the search function 
@app.route('/search')
def search():
    query = request.args.get("q")
    return query

@app.route('/p/<post>')
def post(post):
    md = ""
    code = 200
    try:
        f = open("markdown/"+post+".md", "r")
        md = f.read()
        f.close()
    except:
        return not_found(None)
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
    

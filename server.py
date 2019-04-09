from flask import Flask, render_template, send_from_directory, request, Markup
import markdown, os, glob

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
    files = glob.glob('markdown/'+inp+'*.md')
    # files = ['markdown\\404.md', 'markdown\\test.md']
    out = ''
    for x in files:
        x = x.replace('markdown\\', '')
        x = x.replace('.md','')
        print(x)
        out = out + '<option value="'+x+'">'
    return out
# the search function 
@app.route('/search')
def search():
    query = request.args.get("q")
    files = glob.glob('markdown/'+query+'*.md')
    # files = ['markdown\\404.md', 'markdown\\test.md']
    equery = ' : "'+str(Markup.escape(query))+'"'
    out = '<h1>Search'+equery+'</h1>\n<ul>\n'
    res = True
    for x in files:
        res = False
        x = x.replace('markdown\\', '')
        x = x.replace('.md','')
        print(x)
        out = out + '<li><h3><a href="/p/'+x+'">'+x+'</a></h3></li>\n'
    if res:
        out = '<h1>Search'+equery+'</h1>\n<h2>No Results</h2>'
    return render_template('post.html', post=out + '</ul>', title=query) 

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
    

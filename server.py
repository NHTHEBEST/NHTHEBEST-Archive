from flask import Flask, render_template, send_from_directory, request, Markup, Response, redirect
import markdown, os, glob, json

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


@app.route('/api/<call>/')
def api(call):
    code = 200
    key = request.args.get("key")
    data = None 
    if key != "":
       # code = 403
        ret = '{"error":{"code":403,"text":"Invalid Key"}}'
    try:
        data = json.load(request.data)
    except:
        code = 400
        ret = '{"error":{"code":400,"text":"Invalid Json Post Data"}}'
        
    if call == 'SET' and code == 200:
        # return code 201
        # make new file
        pass
    elif call == 'DELETE' and code == 200:
        pass# return code 200
    elif call == 'UPDATE' and code == 200:
        pass # return code 201
    elif call == 'GET' and code == 200:
        pass # return code 200
    else:
        code = 404
        ret = '{"error":{"code":404,"text":"NOT A CALL"}}'
    
    resp = Response(response=ret,
                    status=code,
                    mimetype="application/json")
    return resp


@app.route('/searchin/<inp>')
def menu(inp):
    files = glob.glob('markdown/*.md')
    # files = ['markdown\\404.md', 'markdown\\test.md']
    out = ''
    for x in files:
        x = x.replace('markdown\\', '')
        x = x.replace('.md','')
        lq, lx, = inp.lower(),x.lower()
        if lq in lx:
            out = out + '<option value="'+x+'">'
    return out
# the search function 
@app.route('/search')
def search():
    query = request.args.get("q")
    files = glob.glob('markdown/*.md')
    # files = ['markdown\\404.md', 'markdown\\test.md']
    equery = ' : "'+str(Markup.escape(query))+'"'
    out = '<h1>Search'+equery+'</h1>\n<ul>\n'
    res = True
    for x in files:
        res = False
        x = x.replace('markdown\\', '')
        x = x.replace('.md','')
        if x == query:
            return redirect('/p/'+x, code=302)
        lq, lx, = query.lower(),x.lower()
        if lq in lx:
            out = out + '<li><h3><a href="/p/'+x+'">'+x+'</a></h3></li>\n'
    if res:
        out = '<h1>Search'+equery+'</h1>\n<h2>No Results</h2>'
    return render_template('post.html', post=out + '</ul>', title=query) 

@app.route('/p/<post>')
def post(post):
    md = ""
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
    

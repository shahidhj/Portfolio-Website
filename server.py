from flask import Flask,render_template
app = Flask(__name__)

@app.route('/')
def homePage():
    return render_template("index.html")


#@app.route('/about.html')
#def about():
    #return render_template("about.html")


@app.route('/blog')
def blog():
    return "this is my blog"


@app.route('/blog/2020/deepLearning')
def blog2():
    return "these are my blogs on deep learning"

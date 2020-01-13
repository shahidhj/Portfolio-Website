from flask import Flask,render_template
app = Flask(__name__)

@app.route('/')
def homePage():
    return render_template("index.html")

@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_page():

    return 'form submitted'




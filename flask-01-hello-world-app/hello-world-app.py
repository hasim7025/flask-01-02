from flask import Flask 
app = Flask(__name__)

@app.route('/')
def head():
    return "hello world"

@app.route('/second')
def second():
    return "this is the second page"

@app.route('/third')
def third():
    return "flask-01-02/this is the third page"

if __name__ == '__main__':

    app.run(debug=True, port=30000)         # normally it runs on the port:3000
    # app.run(host= '0.0.0.0', port=8081)
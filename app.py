from flask import Flask, request, redirect, jsonify, render_template 

username = None
password = None

app = Flask(__name__) 


@app.route('/order', methods=['POST','GET'])
def order():
    return render_template('order.html')

@app.route('/', methods=['POST','GET'])
@app.route('/index', methods=['POST','GET'])
def index():
    return render_template('index.html')

@app.route('/index.css')
def main1():
    return app.send_static_file('styles/index.css')

@app.route('/index.js')
def main2():
    return app.send_static_file('javascript/index.js')

@app.route('/offline')
def offline():
    return app.send_static_file('offline.html')

@app.route('/asset-manifest.json')
def manifest():
    return app.send_static_file('manifest.json')


if __name__ == "__main__":
    app.run(debug=True)
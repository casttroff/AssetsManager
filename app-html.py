from flask import Flask, request
import werkzeug
from werkzeug.wrappers import BaseRequest
from werkzeug.wsgi import responder
from werkzeug.exceptions import HTTPException, NotFound
import json, os, webbrowser

app = Flask(__name__) #create the Flask app

@app.route("/suma",methods=["GET","POST"])
def sumar():
    if request.method=="POST":
        num1=request.form.get("num1")
        num2=request.form.get("num2")
        return "<h1>El resultado de la suma es {}</h1>".format(str(int(num1)+int(num2)))
    else:
        return '''<form action="/suma" method="POST">
                <label>N1:</label>
                <input type="text" name="num1"/>
                <label>N2:</label>
                <input type="text" name="num2"/><br/><br/>
                <input type="submit"/>
                </form>'''

'''@app.route('/qr', methods=['GET', 'POST']) #allow both GET and POST requests
def qr():
        if request.method == 'POST': #this block is only entered when the form is submitted
                codigoQr = request.form.get('codigoQr')
                filename = os.path.join(app.static_folder, 'data.txt')
                with open(filename) as qr_file:
                        data = json.load(qr_file)
                return data'''
@app.route("/app")
def hello():
    return "Hello Socio!";

@app.route("/ping")
def keepalive():
    return "pong";
@app.errorhandler(werkzeug.exceptions.BadRequest)
def handle_bad_request(e):
    return 'bad request!', 400

if __name__ == '__main__':
        app.run(debug=True, port=5000) #run app in debug mode on port 5000
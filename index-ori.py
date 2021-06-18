from flask import Flask, render_template

from flask import request

from flask import Flask,redirect

app = Flask(__name__)

# Routes to Render Something
@app.route('/app')
def home():
    return render_template("home.html")

@app.route('/help', strict_slashes=False)
def help():
    return render_template("help.html")

@app.route('/ping', strict_slashes=False)
def ping():
    return render_template("ping.html")

@app.route('/backdoor', strict_slashes=False)
def backdoor():
    return render_template("backdoor.html")

@app.route('/success', methods=['POST'])
def success():
    serialNumber = request.form['serialNumber']
    wmsAccount = request.form['wmsAccount']
    deviceState = request.form['deviceState']
    print(serialNumber, wmsAccount,deviceState)
    return render_template("success.html")


if __name__ == '__main__':
    app.run(debug=True)
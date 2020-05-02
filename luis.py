from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

@app.route('/')
def home_page():
    return render_template('ui.html')
@app.route('/wash')
def shell():
    return render_template('wash.html')


#testing a deep link for a  mobile app
@app.route("/linketapp/download")
def linket_station():
    return '<a href="https://luisdiegoandrade.pythonanywhere.com/linketapp/download">[linket]</a>'

if __name__ == '__main__':
    app.run(port="8080")

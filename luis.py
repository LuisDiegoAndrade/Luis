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


    script = '''

      let deeplink = document.getElementById("link");
      let ev = new MouseEvent('click', {
        'view': window,
        'bubbles': true,
        'cancelable': true
      });
      deeplink.dispatchEvent(ev);

      '''

    return '<a id="link" href="linket://deeplink">[deeplink]</a> <script>{}</script>'.format(script)

if __name__ == '__main__':
    app.run(port="8080")

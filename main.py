from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
@app.route('/pytorial')
def index():
    return render_template('main_page.html')


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')

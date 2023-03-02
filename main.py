from flask import Flask, render_template, url_for

app = Flask(__name__)


@app.route('/')
@app.route('/pytorial')
def start():
    return render_template('main_page.html', style=f"href={url_for('static', filename='styles/main_page.css')}")


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')

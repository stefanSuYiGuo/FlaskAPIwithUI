from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    title = 'Flask Web App'
    paragraphs = [
        'Section 1',
        'Section 2',
        'Section 3'
    ]
    return render_template('index.html', title=title, data=paragraphs)


if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5000)

from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy

from config import Config
from forms import RegisterForm

app = Flask(__name__)
bootstrap = Bootstrap(app=app)
db = SQLAlchemy(app)

app.config.from_object(Config)


@app.route('/')
def index():
    title = 'Flask Web App'
    paragraphs = [
        'Section 1',
        'Section 2',
        'Section 3'
    ]
    return render_template('index.html', title=title, data=paragraphs)


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        pass
    return render_template('register.html', form=form)


if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5000)

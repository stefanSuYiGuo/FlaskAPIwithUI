from flask import Flask, render_template, flash

from app import app, bcrypt, db
from app.forms import RegisterForm
from app.models import User


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
        username = form.username.data
        email = form.email.data
        password = bcrypt.generate_password_hash(form.password.data)
        print(username, email, password)
        # print(bcrypt.check_password_hash(hash, password))
        user = User(username=username, email=email, password=password)
        db.session.add(user)
        db.session.commit()
        flash('Congrats, registration success', category='success')
    return render_template('register.html', form=form)

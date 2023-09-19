from flask import render_template, request, redirect, url_for, flash
from app import app, db
from .models import User
from .forms import SignupForm

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = SignupForm()
    if form.validate_on_submit():
        email = form.email.data
        name = form.name.data
        password = form.password.data

        # Perform email validation here (e.g., using regex)
        if not is_valid_email(email):
            flash('Invalid email address', 'error')
            return redirect(url_for('signup'))

        # Check if the email is already in use
        existing_user = User.query.filter_by(email=email).first()
        if existing_user:
            flash('Email already in use', 'error')
            return redirect(url_for('signup'))

        # Create a new user
        new_user = User(email=email, name=name, password=password)
        db.session.add(new_user)
        db.session.commit()

        flash('Account created successfully', 'success')
        return redirect(url_for('login'))

    return render_template('signup.html', form=form)

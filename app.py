import os
import secrets
from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, RadioField, SelectField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Email
from dotenv import load_dotenv  

load_dotenv()

app = Flask(__name__)

app.secret_key = os.getenv('FLASK_SECRET_KEY', secrets.token_hex(16))  

class RegistrationForm(FlaskForm):
    name = StringField("Full name", validators=[DataRequired()])
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired()])
    gender = RadioField("Gender", choices=[('M', 'Male'), ('F', 'Female')], validators=[DataRequired()])
    country = SelectField("Country", choices=[('np', 'Nepal'), ('in', 'India')], validators=[DataRequired()])
    agree = BooleanField("I accept the terms and conditions", validators=[DataRequired()])
    submit = SubmitField('Register')

@app.route('/', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        name = form.name.data
        email = form.email.data
        country = form.country.data
        return(f"Thank you {name} From {country}, your registration is successful!")
    return render_template('register.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)

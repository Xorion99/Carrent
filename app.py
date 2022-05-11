from flask import Flask, render_template, flash, redirect, url_for
from form import registration_form, LoginForm
from flask_bcrypt import Bcrypt

from datetime import datetime
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Database'''
app.config['SECRET_KEY'] = 'jbhkkjbhdnslk98723bkj4sdfjiopesdfjklsfwejklò43583459@fsdokso'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

@app.route('/')
def index():  # put application's code here
    return 'ciao'


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    from model import User
    form = registration_form()
    if form.validate_on_submit():
        if form.Password.data != form.Confirm_password.data:
             flash('password do not match')
        else:
            ashed_password = bcrypt.generate_password_hash(form.Password.data)
            user = User(Email= form.Email.data, Password = ashed_password, Name= form.Name.data,
                        Surname = form.Surname.data, Phone = form.Telephone.data,BirthData = form.Birthdate.data,
                        IdcardNumber = form.CardNumber.data, Municipality = form.Municipality.data,
                        IdcardExp = form.IdcardExp.data, Iban = form.Iban.data, DriveLicense =form.DriveLicense.data,
                        Department = form.Department.data, DriveLicenseExp = form.driveExp.data)
            db.session.add(user)
            db.session.commit()
            print("PIPPO")
            return redirect(url_for('login'))
    return render_template('registration/index.html', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    from model import User
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(Email=form.Email.data).first()
        if user:
            if bcrypt.check_password_hash(user.Password, form.Password.data):
                return redirect(url_for('index'))
            else:
                flash('Wrong Password')
        else:
            flash('Wrong Email')

    return render_template('Login/index.html',form = form)



if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)


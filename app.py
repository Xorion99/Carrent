from flask import Flask, render_template, flash, redirect, url_for, request
from form import registration_form, LoginForm, AddCarForm
from flask_bcrypt import Bcrypt
from flask_uploads import configure_uploads, IMAGES, UploadSet
from flask_uploads.exceptions import UploadNotAllowed

from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Database'''
app.config['SECRET_KEY'] = 'jbhkkjbhdnslk98723bkj4sdfjiopesdfjklsfwejklò43583459@fsdokso'
app.config['UPLOADED_IMAGES_DEST'] = 'uploads/images'

images = UploadSet('images', IMAGES)
configure_uploads(app, images)


db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

@app.route('/')
def index():  # put application's code here
    return render_template('homepage/index.html')

@app.route('/test', methods=['GET', 'POST'])
def test():  # put application's code here
    form = AddCarForm()
    if request.method == "POST":
        print(form.option.data)
        #images.save(form.Photo.data)
    return render_template('/test.html', form = form)



@app.route('/signup', methods=['GET', 'POST'])
def signup():
    from model import User
    form = registration_form()
    if form.validate_on_submit():
        if form.Password.data != form.Confirm_password.data:
             flash('password do not match')
        else:
            ashed_password = bcrypt.generate_password_hash(form.Password.data)
            user = User(form.Email.data, ashed_password,form.Name.data,
                        form.Surname.data, form.Telephone.data,form.Birthdate.data,
                        form.CardNumber.data, form.Municipality.data,
                        form.IdcardExp.data, form.Iban.data, form.DriveLicense.data,
                        form.Department.data,  form.driveExp.data)
            db.session.add(user)
            db.session.commit()
            print("PIPPO")
            return redirect(url_for('login'))
    return render_template('registration/index.html', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    from model import User
    form = LoginForm()
    a = AddCarForm()
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

@app.route('/addcar', methods=['GET', 'POST'])
def AddCar():  # put application's code here
    from model import car
    form = AddCarForm()
    if form.validate_on_submit():
        if (form.Photo.data):
            filename = images.save(form.Photo.data)
        else:
            filename = "nothing.png"

        if(form.AutomaticTransmission.data == True ):
            Automatic = "Automatic Trasmission"
        else:
            Automatic = ""
        if(form.AirConditioning.data == True):
            Air = "Air Conditioning"
        else:
            Air = ""
        if(form.Bluetooth.data == True):
            Blue = "Bluetooth"
        else:
            Blue = ""

        option = Automatic + " " + Air +" "+ Blue

        Car = car(form.Model.data, form.Year.data, form.Plate.data,
                  form.Fuel.data,form.Category.data,form.Number.data,
                  form.PiLocation.data, form.DeLocation.data,
                  option, filename)
        db.session.add(Car)
        db.session.commit()
        if(form.Photo.data):
            images.save(form.Photo.data)
        return redirect(url_for('index'))



    return render_template('Addcar/index.html', form=form)


if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)


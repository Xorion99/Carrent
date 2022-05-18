from flask import Flask, render_template, flash, redirect, url_for, request, session
from form import registration_form, LoginForm, AddCarForm, AddAvailabilityForm, SearchCarForm
from flask_bcrypt import Bcrypt
from flask_uploads import configure_uploads, IMAGES, UploadSet


from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Database'''
app.config['SECRET_KEY'] = 'jbhkkjbhdnslk98723bkj4sdfjiopesdfjklsfwejklò43583459@fsdokso'
app.config['UPLOADED_IMAGES_DEST'] = 'static/uploads'

images = UploadSet('images', IMAGES)
configure_uploads(app, images)



db = SQLAlchemy(app, session_options={
    'expire_on_commit': False
})
bcrypt = Bcrypt(app)
my_car = []
rental_car = []


@app.route('/')
def index():
    from model import car
    global my_car
    return render_template('homepage/index.html', my_car = my_car, cars=car)



@app.route('/addcar', methods=['GET', 'POST'])
def AddCar():
    from model import car
    form = AddCarForm()
    global my_car
    i = 0
    if form.validate_on_submit():

        if (form.Photo.data):
            filename = images.save(form.Photo.data)
        else:
            filename = "nothing.png"

        if(form.AutomaticTransmission.data == True ):
            Automatic = "Automatic Trasmission"
        else:
            Automatic = " "
        if(form.AirConditioning.data == True):
            Air = "Air Conditioning"
        else:
            Air = " "
        if(form.Bluetooth.data == True):
            Blue = "Bluetooth"
        else:
            Blue = " "

        option = Automatic + " " + Air +" "+ Blue

        Car = car(form.Model.data, form.Year.data, form.Plate.data,
                  form.Fuel.data,form.Category.data,form.Number.data,
                  form.PiLocation.data, form.DeLocation.data,form.Price.data,
                  option,filename)
        db.session.add(Car)
        db.session.commit()
        my_car.insert(i, car(form.Model.data, form.Year.data, form.Plate.data,
                      form.Fuel.data,form.Category.data,form.Number.data,
                      form.PiLocation.data, form.DeLocation.data, form.Price.data,
                      option, filename))

        print(my_car[0].Model)
        i = i + 1
        return redirect(url_for('index'))
    return render_template('Addcar/index.html', form=form)







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
            print("ciao")
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
                session['logged_in'] = True
                return redirect(url_for('index'))
            else:
                flash('Wrong Password')
        else:
            flash('Wrong Email')

    return render_template('Login/index.html',form = form)


@app.route('/infocar/<Platecar>', methods=["GET","POST"])
def infocar(Platecar):
    from model import Rented
    global my_car
    global rental_car
    form = AddAvailabilityForm()
    infocar = None
    print(Platecar)
    j = 0
    for i in range(len(my_car)):
        print("jkl")
        if my_car[i].Plate == Platecar:
            infocar = my_car[i]
            if form.validate_on_submit():
                print("ciaoo")
                car_rented = Rented(infocar.Model,infocar.Year,infocar.Plate,
                                    infocar.Fuel,infocar.Category,infocar.NumberOfSeats,
                                    infocar.PickupLocation,infocar.DeliveryLocation,
                                    infocar.DailyPrice, infocar.Optional,infocar.Photo,
                                    form.StartDate.data,form.EndDate.data)
                rental_car.insert(j,car_rented)

                db.session.add(car_rented)
                db.session.commit()
                j = j + 1
                return redirect(url_for('payment'))


    return render_template('Infocar/index.html', infocar = infocar, form = form)


@app.route("/myrental")
def myrental():
    global rental_car
    return render_template('myrental/index.html',rental_car = rental_car)


@app.route("/logout")
def logout():
    form = LoginForm()
    session['logged_in'] = False
    return render_template('homepage/index.html', form = form)


@app.route("/searchcar", methods=['GET', 'POST'])
def search():
    i = 0
    global rental_car
    form = SearchCarForm()
    car = []
    if form.validate_on_submit():
        start = form.StartDate.data
        end = form.EndDate.data
        for i in range(len(rental_car)):
            if rental_car[i].Start == start and rental_car[i].End == end:
                car.insert(i,rental_car[i])
                i = i + 1

    return render_template('Search_Car/index.html', form = form, car = car)


@app.route("/payment")
def payment():
    return render_template('payment/index.html')


if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)


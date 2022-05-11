from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, TelField, SubmitField, EmailField, IntegerField, DateField, FileField, SelectField
from wtforms.validators import InputRequired, Length, ValidationError, Email, DataRequired, NumberRange


class registration_form (FlaskForm):
    Email = EmailField(validators=[InputRequired(), Email()],
                       render_kw={"placeholder": "Email"})
    Password = PasswordField(validators=[InputRequired(), Length(min=8, max=100)],
                             render_kw={"placeholder": "Password"})
    Confirm_password = PasswordField(validators=[InputRequired(), Length(min=8, max=100)],
                                     render_kw={"placeholder": "Confirm password"})
    Name = StringField(validators=[InputRequired()],
                       render_kw={"placeholder": "Name"})
    Surname = StringField(validators=[InputRequired()],
                          render_kw={"placeholder": "Surname"})
    Telephone = TelField(validators=[InputRequired()],
                         render_kw={"placeholder": "Telephone number"})
    Birthdate = DateField(validators=[InputRequired()],
                          render_kw={"placeholder": "Birth date"})

    CardNumber = StringField(validators=[InputRequired()],
                             render_kw={"placeholder": "Identity card number"})

    Municipality = StringField(validators=[InputRequired()],
                               render_kw={"placeholder": "Municipality"})

    IdcardExp = DateField(validators=[InputRequired()])

    Iban = StringField(validators=[InputRequired()],
                       render_kw={"placeholder": "Iban"})
    DriveLicense = StringField(validators=[InputRequired()],
                               render_kw={"placeholder": "Driving licence number"})

    Department = StringField(validators=[InputRequired()],
                             render_kw={"placeholder": "Department of Motor Vehicles"})

    driveExp = DateField(validators=[InputRequired()],
                         render_kw={"placeholder": "Driving licence expiration date"})

    Submit = SubmitField("Sign Up")


class LoginForm(FlaskForm):
    Email = EmailField(validators=[InputRequired(), Email()],
                       render_kw={"placeholder": "Email"})
    Password = PasswordField(validators=[InputRequired()],
                             render_kw={"placeholder": "Password"})
    Submit = SubmitField("Login")

class AddCarForm(FlaskForm):
    Model = StringField(validators=[InputRequired()],
                       render_kw={"placeholder": "Model"})
    Year = StringField(validators=[InputRequired()],
                          render_kw={"placeholder": "Year"})

    Plate = StringField(validators=[InputRequired()],
                       render_kw={"placeholder": "Plate"})

    Category = choices=[('cpp', 'C++'), ('py', 'Python'), ('text', 'Plain Text')]

    Number = StringField(validators=[InputRequired()],
                       render_kw={"placeholder": "Number of seats"})
    PiLocation = StringField(validators=[InputRequired()],
                       render_kw={"placeholder": "Pickup location"})
    DeLocation = StringField(validators=[InputRequired()],
                       render_kw={"placeholder": "Delivery location"})
    Price = StringField(validators=[InputRequired()],
                       render_kw={"placeholder": "Daily price(EUR)"})
    Photo = FileField()


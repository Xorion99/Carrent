from app import db


class User(db.Model):
    Email = db.Column(db.String(20), nullable=False, unique=True, primary_key=True)
    Password = db.Column(db.String(100), nullable=False)
    Name = db.Column(db.String(20), nullable=False)
    Surname = db.Column(db.String(20), nullable=False)
    Phone = db.Column(db.String(20), nullable=False)
    BirthData = db.Column(db.DateTime(20), nullable=False)
    IdcardNumber = db.Column(db.String(20), nullable=False, unique=True)
    Municipality = db.Column(db.String(20), nullable=False)
    IdcardExp = db.Column(db.DateTime(20), nullable=False)
    Iban = db.Column(db.String(25), nullable=False)
    DriveLicense = db.Column(db.String(20), nullable=False, unique=True)
    Department = db.Column(db.String(20), nullable=False)
    DriveLicenseExp = db.Column(db.DateTime(20), nullable=False)

    def __init__(self, Email, Password,Name,Surname,Phone,BirthData,
                 IdcardNumber,Municipality,IdcardExp,Iban,DriveLicense,
                 Department,DriveLicenseExp):
        self.Email = Email
        self.Password = Password
        self.Name = Name
        self.Surname = Surname
        self.Phone = Phone
        self.BirthData = BirthData
        self.IdcardNumber = IdcardNumber
        self.Municipality = Municipality
        self.IdcardExp = IdcardExp
        self.Iban = Iban
        self.DriveLicense = DriveLicense
        self.Department = Department
        self.DriveLicenseExp = DriveLicenseExp


class car(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    Email = db.Column(db.String(20), nullable=False)
    Model = db.Column(db.String(20), nullable=False)
    Year = db.Column(db.Integer, nullable=False)
    Plate = db.Column(db.String(20), nullable=False)
    Fuel = db.Column(db.String(20), nullable=False)
    Category = db.Column(db.String(20), nullable=False)
    NumberOfSeats = db.Column(db.String(20), nullable=False)
    PickupLocation = db.Column(db.String(20), nullable=False)
    DeliveryLocation = db.Column(db.String(20), nullable=False)
    DailyPrice = db.Column(db.Integer, nullable=False)
    Optional = db.Column(db.String(20), nullable=False)
    Photo = db.Column(db.String(20))


    def __init__(self,Email,Model, Year, Plate,Fuel,Category,
                 NumberOfSeats,PickupLocation,DeliveryLocation,DailyPrice,Optional,
                 Photo):
        self.Email = Email
        self.Model = Model
        self.Year = Year
        self.Plate = Plate
        self.Fuel = Fuel
        self.Category = Category
        self.NumberOfSeats = NumberOfSeats
        self.PickupLocation = PickupLocation
        self.DeliveryLocation = DeliveryLocation
        self.DailyPrice = DailyPrice
        self.Optional = Optional
        self.Photo = Photo


class Rented(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    Email = db.Column(db.String(20), nullable=False)
    Model = db.Column(db.String(20), nullable=False)
    Year = db.Column(db.Integer, nullable=False)
    Plate = db.Column(db.String(20), nullable=False)
    Fuel = db.Column(db.String(20), nullable=False)
    Category = db.Column(db.String(20), nullable=False)
    NumberOfSeats = db.Column(db.String(20), nullable=False)
    PickupLocation = db.Column(db.String(20), nullable=False)
    DeliveryLocation = db.Column(db.String(20), nullable=False)
    DailyPrice = db.Column(db.Integer, nullable=False)
    Optional = db.Column(db.String(20), nullable=False)
    Photo = db.Column(db.String(20))
    Start = db.Column(db.DateTime(20), nullable=False)
    End = db.Column(db.DateTime(20), nullable=False)

    def __init__(self,Email,Model,Year,Plate,Fuel,Category,NumberOfSeats,
                 PickupLocation,DeliveryLocation,DailyPrice,Optional,Photo,Start,End):
        self.Email = Email
        self.Model = Model
        self.Year = Year
        self.Plate = Plate
        self.Fuel = Fuel
        self.Category = Category
        self.NumberOfSeats = NumberOfSeats
        self.PickupLocation = PickupLocation
        self.DeliveryLocation = DeliveryLocation
        self.DailyPrice = DailyPrice
        self.Optional = Optional
        self.Photo = Photo
        self.Start =Start
        self.End = End


db.create_all()


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

    def __int__(self, Email, Password,Name,Surname,Phone,BirthData,
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



db.create_all()


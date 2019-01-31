from server import db

import packages.tel_scraper.LocalCH.model as model1
import packages.tel_scraper.TelSearch.model as model2

# Check this in the console if it matches the model
cols = set(model1.db_cols + model2.db_cols)

class Phonebook(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    Kategorie = db.Column(db.String(200), unique=False, nullable=True)
    Website = db.Column(db.String(80), unique=False, nullable=True)
    Ort = db.Column(db.String(80), unique=False, nullable=False)
    URL = db.Column(db.String(200), unique=False, nullable=False)
    PLZ = db.Column(db.Integer(), unique=False, nullable=True)
    Bezeichnung = db.Column(db.String(200), unique=False, nullable=False)
    Region = db.Column(db.String(50), unique=False, nullable=True)
    Werbung = db.Column(db.String(20), unique=False, nullable=True)
    Betriebsart = db.Column(db.String(200), unique=False, nullable=True)
    Hausnummer = db.Column(db.String(10), unique=False, nullable=True)
    Strasse = db.Column(db.String(200), unique=False, nullable=False)
    Telefon = db.Column(db.String(15), unique=False, nullable=True)

    query = db.Column(db.String(50), unique=False, nullable=True)
    created_at = db.Column(db.DateTime(), unique=False, nullable=False)

    def __repr__(self):
        return '<Name %r>' % self.Bezeichnung

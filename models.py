from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Tamu(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nama = db.Column(db.String(100))
    no_hp = db.Column(db.String(20))
    no_polis = db.Column(db.String(50))
    keperluan = db.Column(db.String(200))
    alamat = db.Column(db.Text)
    email = db.Column(db.String(100))

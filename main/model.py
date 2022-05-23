from  main import db

class Degerler(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    toprakNem = db.Column(db.String())
    yagmur = db.Column(db.String())
    isik = db.Column(db.String())
    havaNem = db.Column(db.String())
    havaSicaklik = db.Column(db.String())

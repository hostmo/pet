from PBD_config import db_init as db


class Pet(db.Model):
    __tablename__ = 'pets'
    Pno = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    Pname = db.Column(db.String(255), nullable=False)
    Powner = db.Column(db.String(255), db.ForeignKey('users.Uid'), nullable=False)
    Pimage = db.Column(db.String(255))
    Pgender = db.Column(db.String(255), nullable=False)
    Pvariety = db.Column(db.String(255), nullable=False)
    Pbrith = db.Column(db.Date)

    def to_dict(self):
        return {
            'Pno': self.Pno,
            'Pname': self.Pname,
            'Powner': self.Powner,
            'Pimage': self.Pimage,
            'Pgender': self.Pgender,
            'Pvariety': self.Pvariety,
            'Pbrith': self.Pbrith.strftime('%Y-%m-%d') if self.Pbrith else None
        }

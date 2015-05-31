from . import db


class Share(db.Model):
    __tablename__ = 'share'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(64))
    title = db.Column(db.String(64))
    text = db.Column(db.String(64))

    def __repr__(self):
        return '<Share %r>' % self.name

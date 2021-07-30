from datetime import datetime
from livestic import db, login_manager
from flask_login import UserMixin
import json

@login_manager.user_loader
def load_user(user_id):
	return User.query.get(int(user_id))
 
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Integer, db.ForeignKey('user.id'))
    email = db.Column(db.Integer, db.ForeignKey('user.id'))
    password = db.Column(db.String(120))
    animal=db.relationship('Animal', backref='owner', lazy=True)
    def __repr__(self):
        return f"User('{self.name}', '{self.email}')"

class Animals(db.Model):
    __tablename__ = 'animal'
    id= db.Column(db.Integer, primary_key=True)
    animaTagNum= db.Column(db.Integer, nullable=False)
    size= db.Column(db.Integer(), nullable=False)	
    user_id=db.Column(db.Integer, db.ForeignKey('user.id'), nullable=True)
    def __repr__ (self):
        return f"Post('{self.name}', '{self.animalTagNum}', '{self.size}')"


db.create_all()	
from app import db


class Input(db.Model):
    __tablename__ = 'input'

    id = db.Column('id', db.Integer, primary_key=True)
    user_id = db.Column('user_id', db.String(255))
    amount = db.Column('amount', db.Float(50))
    note = db.Column('note', db.String(255), nullable=True)
    time_created = db.Column(db.DateTime, default=db.func.current_timestamp())


def __init__(self, user_id, amount, note):
    self.user_id = user_id
    self.amount = amount
    self.note = note

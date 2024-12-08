from src.extensions import db
from src.models.base import BaseModel


class Slides(db.Model, BaseModel):
    id = db.Column(db.Integer, primary_key=True)
    slideName = db.Column(db.String(255), nullable=False)
    slidePath = db.Column(db.String(255), nullable=False)
    slideUrl = db.Column(db.String(255), nullable=False)

    def __repr__(self):
        return f'<Slides {self.id}: {self.slideName}>'
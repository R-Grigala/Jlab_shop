from src.extensions import db
from src.models.base import BaseModel


class Category(db.Model, BaseModel):
    __tablename__ = "category"
    id = db.Column(db.Integer, primary_key=True)
    category_name = db.Column(db.String(200), nullable=False)

    def __repr__(self):
        return f'<Category {self.id}: {self.category_name}>'
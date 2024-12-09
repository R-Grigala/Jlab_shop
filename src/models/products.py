from src.extensions import db
from src.models.base import BaseModel


class Category(db.Model, BaseModel):
    __tablename__ = "category"

    id = db.Column(db.Integer, primary_key=True)
    category_name_en = db.Column(db.String(255), nullable=False)
    category_name_ka = db.Column(db.String(255), nullable=False)

    products = db.relationship("Products", back_populates="category", cascade="all, delete-orphan")

    def __repr__(self):
        return f'<Category {self.id}: {self.category_name_en}>'
    

class Products(db.Model, BaseModel):
    __tablename__ = "products"

    id = db.Column(db.Integer, primary_key=True)
    product_name_en = db.Column(db.String(255), nullable=False)
    product_desc_en = db.Column(db.String(255), nullable=False)
    product_name_ka = db.Column(db.String(255), nullable=False)
    product_desc_ka = db.Column(db.String(255), nullable=False)

    category_id = db.Column(db.ForeignKey("category.id"), nullable=False)
    category = db.relationship("Category", back_populates="products")

    def __repr__(self):
        return f'<Products {self.id}: {self.product_name_en}>'
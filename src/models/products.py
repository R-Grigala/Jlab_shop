from src.extensions import db
from src.models.base import BaseModel


class Category(db.Model, BaseModel):
    """
    Represents a product category.
    """
    __tablename__ = "category"

    id = db.Column(db.Integer, primary_key=True)
    category_name_en = db.Column(db.String(255), nullable=False)
    category_name_ka = db.Column(db.String(255), nullable=False)

    brands = db.relationship("Brands", back_populates="category", cascade="all, delete-orphan")

    def __repr__(self):
        return f'<Category {self.id}: {self.category_name_en}>'


class Brands(db.Model, BaseModel):
    """
    Represents a brand under a specific category.
    """
    __tablename__ = "brands"
    id = db.Column(db.Integer, primary_key=True)
    brands_name_en = db.Column(db.String(255), nullable=False)
    brands_name_ka = db.Column(db.String(255), nullable=False)

    category_id = db.Column(db.ForeignKey("category.id"), nullable=False)
    category = db.relationship("Category", back_populates="brands")

    products = db.relationship("Products", back_populates="brand", cascade="all, delete-orphan")

    def __repr__(self):
        return f'<Brands {self.id}: {self.brands_name_en}>'


class Products(db.Model, BaseModel):
    """
    Represents a product under a specific brand.
    """
    __tablename__ = "products"

    id = db.Column(db.Integer, primary_key=True)
    product_name_en = db.Column(db.String(255), nullable=False)
    product_desc_en = db.Column(db.String(255), nullable=False)
    product_name_ka = db.Column(db.String(255), nullable=False)
    product_desc_ka = db.Column(db.String(255), nullable=False)

    brands_id = db.Column(db.ForeignKey("brands.id"), nullable=False)
    brand = db.relationship("Brands", back_populates="products")

    def __repr__(self):
        return f'<Products {self.id}: {self.product_name_en}>'
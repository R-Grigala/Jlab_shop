from src.admin.base import SecureModelView
from wtforms_sqlalchemy.fields import QuerySelectField

from src.models import Category, Brands

class ProductsView(SecureModelView):
    column_list = ['product_name_en', 'product_desc_en', 'brand.brands_name_en', 'brand.category.category_name_en']  # Display category via brand
    column_labels = {
        "product_name_en": "Product Name (English)",
        "product_desc_en": "Description (English)",
        "brand.brands_name_en": "Brand",
        "brand.category.category_name_en": "Category (English)"
    }
    column_searchable_list = ['product_name_en', 'product_name_ka']  # Searchable columns
    column_filters = ['brand.category']  # Add filter for categories through brand
    form_columns = ['product_name_en', 'product_desc_en', 'product_name_ka', 'product_desc_ka', 'brand']

    form_overrides = {
        'brand': QuerySelectField
    }

    form_args = {
        'brand': {
            'query_factory': lambda: Brands.query.all(),
            'get_label': lambda brand: f"{brand.brands_name_en} ({brand.category.category_name_en})",
            'label': 'Brand'
        }
    }

class CategoriesView(SecureModelView):
    column_list = ['category_name_en', 'category_name_ka']
    column_labels = {
        'category_name_en': 'Category (English)',
        'category_name_ka': 'Category (Georgian)',
    }
    form_columns = ['category_name_en', 'category_name_ka']

class BrandsView(SecureModelView):
    column_list = ['brands_name_en', 'brands_name_ka']
    column_labels = {
        'brands_name_en': 'Brands (English)',
        'brands_name_ka': 'Brands (Georgian)',
    }
    form_columns = ['brands_name_en', 'brands_name_ka', 'category']
    form_overrides = {
        'category': QuerySelectField
    }
    form_args = {
        'category': {
            'query_factory': lambda: Category.query.all(),
            'get_label': 'category_name_en',
        }
    }
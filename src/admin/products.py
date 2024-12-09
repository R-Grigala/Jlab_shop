from src.admin.base import SecureModelView
from wtforms_sqlalchemy.fields import QuerySelectField

from src.models import Category

class ProductsView(SecureModelView):
    column_list = ['product_name_en', 'product_desc_en', 'category.category_name_en']  # Display in list view
    column_labels = {
        "category.category_name_en": "Category"
    }
    column_searchable_list = ['product_name_en', 'product_name_ka']  # Searchable columns
    column_filters = ['category']  # Add filter for categories
    form_columns = ['product_name_en', 'product_desc_en', 'product_name_ka', 'product_desc_ka', 'category']

    form_overrides = {
        'category': QuerySelectField
    }

    form_args = {
        'category': {
            'query_factory': lambda: Category.query.all(),  # Provide all categories
            'get_label': 'category_name_en',  # Use English name as label
        }
    }

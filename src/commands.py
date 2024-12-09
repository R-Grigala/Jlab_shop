from flask.cli import with_appcontext
import click

from src.extensions import db
from src.models import User, Role, Category

@click.command("init_db")
@with_appcontext
def init_db_command():
    click.echo("Creating Database")
    init_db()
    click.echo("Database Created")

@click.command("populate_db")
@with_appcontext
def populate_db_command():
    click.echo("Creating Test Populate")
    populate_db()
    click.echo("Test Populate created")

def init_db():
    click.echo("Creating Database")
    db.drop_all()
    db.create_all()
    click.echo("Database Created")

def populate_db():
    # Create sample roles
    click.echo("Creating Roles")
    role = Role(name='Admin', is_admin=True, can_products=True)

    role.create()
    role = Role(name="User")
    role.create()

    click.echo("Creating Admin")
    admin_user = User (
        name="Roma",
        lastname="Grigalashvili",
        email="roma.grigalashvili@iliauni.edu.ge",
        password="Grigalash77",
        role_id=1
    )
    admin_user.create()


    # Create Category
    click.echo("Creating Category")
    category = Category(category_name_en='Phones', category_name_ka ='ტელეფონები')
    category.create()
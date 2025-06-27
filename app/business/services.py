from app.data.models import Product
from app.data.db import db


def get_all_products():
    return Product.query.all()


def get_product(product_id):
    return Product.query.get_or_404(product_id)


def create_product(data):
    product = Product(name=data['name'], price=data['price'])
    db.session.add(product)
    db.session.commit()
    return product


def update_product(product_id, data):
    product = Product.query.get_or_404(product_id)
    product.name = data['name']
    product.price = data['price']
    db.session.commit()
    return product


def delete_product(product_id):
    product = Product.query.get_or_404(product_id)
    db.session.delete(product)
    db.session.commit()
    return product

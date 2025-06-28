from flask import Blueprint, request, jsonify, render_template
from app.business import services

bp = Blueprint('main', __name__)


@bp.route('/')
def index():
    products = services.get_all_products()
    return render_template('index.html', products=products)


@bp.route('/api/products', methods=['GET'])
def get_products():
    products = services.get_all_products()
    return jsonify([{'id': p.id, 'name': p.name, 'price': p.price} for p in products])


@bp.route('/api/products/<int:product_id>', methods=['GET'])
def get_product(product_id):
    product = services.get_product(product_id)
    return jsonify({'id': product.id, 'name': product.name, 'price': product.price})


@bp.route('/api/products', methods=['POST'])
def create_product():
    data = request.get_json()
    product = services.create_product(data)
    return jsonify({'id': product.id, 'name': product.name, 'price': product.price}), 201


@bp.route('/api/products/<int:product_id>', methods=['PUT'])
def update_product(product_id):
    data = request.get_json()
    product = services.update_product(product_id, data)
    return jsonify({'id': product.id, 'name': product.name, 'price': product.price})


@bp.route('/api/products/<int:product_id>', methods=['DELETE'])
def delete_product(product_id):
    services.delete_product(product_id)
    return '', 204

@bp.route('/api/products/expensive/<float:min_price>', methods=['GET'])
def get_expensive(min_price):
    products = services.get_products_above_price(min_price)
    return jsonify([
        {'id': p.id, 'name': p.name, 'price': p.price} for p in products
    ])


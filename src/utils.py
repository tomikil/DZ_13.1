import json


class Category:
    name: str
    description: str
    product: list
    quantity_category = 0
    quantity_unique_products = 0

    def __init__(self, name, description, product):
        self.name = name
        self.description = description
        self.product = product
        Category.quantity_category += 1

    def quantity_products(self):
        Category.quantity_unique_products = len(self.product)
        return Category.quantity_unique_products


class Product:
    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity


def connection_file(f):
    with open(f, 'r', encoding='utf-8') as file:
        data = json.load(file)
        return data


def filling_classes_Category(file):
    category = []
    for item in file:
        category.append(Category(item['name'], item['description'], item['products']))
    return category


def filling_classes_Product(file):
    products = []
    for item in file:
        for items in item['products']:
            products.append(Product(items['name'], items['description'], items['price'], items['quantity']))
    return products


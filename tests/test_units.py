import pytest
import src.utils as utils

file = './products.json'


@pytest.fixture
def category_1():
    return utils.Category('Конфеты', 'Вкусные',
                          [{
                              "name": "Аленка",
                              "description": "Сладкая",
                              "price": 50.0,
                              "quantity": 10
                          }])


def test_init_(category_1):
    assert category_1.name == 'Конфеты'
    assert category_1.description == 'Вкусные'
    assert category_1.product == [{
                              "name": "Аленка",
                              "description": "Сладкая",
                              "price": 50.0,
                              "quantity": 10
                          }]


@pytest.fixture
def category():
    return utils.filling_classes_Category(utils.connection_file(file))


def test_filling_classes_Category(category):
    assert category[0].name == 'Смартфоны'
    assert category[0].description == ('Смартфоны, как средство не только коммуникации, но и получение дополнительных '
                                       'функций для удобства жизни')
    assert category[0].product[0] == {
        "name": "Samsung Galaxy C23 Ultra",
        "description": "256GB, Серый цвет, 200MP камера",
        "price": 180000.0,
        "quantity": 5
      }


@pytest.fixture
def product():
    return utils.Product('Аленка', 'Сладкая', 50.0, 10)


def test_init_product(product):
    assert product.name == 'Аленка'
    assert product.description == 'Сладкая'
    assert product.price == 50.0
    assert product.quantity == 10


@pytest.fixture
def classes_Product():
    return utils.filling_classes_Product(utils.connection_file(file))


def test_filling_classes_Product(classes_Product):
    assert classes_Product[0].name == 'Samsung Galaxy C23 Ultra'

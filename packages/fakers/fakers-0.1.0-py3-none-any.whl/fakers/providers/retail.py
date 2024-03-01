from fakers.providers import ClientLogger
from bl.providers.retail.user import FakeUser, FakeUsers
from bl.providers.retail.order import FakeOrder, FakeOrders
from bl.providers.retail.product import FakeProduct, FakeProducts


class Retail:
    @staticmethod
    def fake_user(locale='en_US'):
        ClientLogger.locale_validator(locale)
        fake_user = FakeUser(locale)
        return fake_user.retrieve()

    @staticmethod
    def fake_users(user_count=5, locale='en_US'):
        ClientLogger.locale_validator(locale)
        fake_users = FakeUsers(user_count, locale)
        return fake_users

    @staticmethod
    def fake_product(locale='en_US'):
        ClientLogger.locale_validator(locale)
        fake_product = FakeProduct(locale)
        return fake_product.retrieve()

    @staticmethod
    def fake_products(user_count=5, locale='en_US'):
        ClientLogger.locale_validator(locale)
        fake_products = FakeProducts(user_count, locale)
        return fake_products

    @staticmethod
    def fake_order(locale='en_US'):
        ClientLogger.locale_validator(locale)
        fake_order = FakeOrder(locale)
        return fake_order.retrieve()

    @staticmethod
    def fake_orders(user_count=5, locale='en_US'):
        ClientLogger.locale_validator(locale)
        fake_orders = FakeOrders(user_count, locale)
        return fake_orders


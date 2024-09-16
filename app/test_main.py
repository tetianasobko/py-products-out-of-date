import datetime
from unittest import mock

from app.main import outdated_products


def test_outdated_products() -> None:
    products = [
        {
            "name": "salmon",
            "expiration_date": datetime.date(2022, 2, 20),
            "price": 600
        },
        {
            "name": "chicken",
            "expiration_date": datetime.date(2022, 2, 15),
            "price": 120
        },
        {
            "name": "duck",
            "expiration_date": datetime.date(2022, 2, 1),
            "price": 160
        }
    ]
    with mock.patch("app.main.datetime") as mocked_date:
        mocked_date.date.today.return_value = datetime.date(2022, 2, 2)
        assert outdated_products(products) == ["duck"]

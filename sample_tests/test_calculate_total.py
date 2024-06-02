def test_calculate_total():
    cart = [{"name": "laptop", "price": 1000}, {"name": "mouse", "price": 50}]
    expected_total = 1050
    total = sum(item["price"] for item in cart)
    assert total == expected_total

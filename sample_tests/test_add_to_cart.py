def test_add_to_cart():
    cart = []
    item = {"name": "laptop", "price": 1000}
    expected_cart = [{"name": "laptop", "price": 1000}]
    cart.append(item)
    assert cart == expected_cart

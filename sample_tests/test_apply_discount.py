def test_apply_discount():
    price = 1000
    discount = 0.1  # 10% discount
    expected_price = 900
    discounted_price = price - (price * discount)
    assert discounted_price == expected_price

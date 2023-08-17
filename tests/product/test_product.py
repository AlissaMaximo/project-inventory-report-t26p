from inventory_report.product import Product


def test_create_product() -> None:
    product = Product(
        "1", "bottle", "wee", "2023/01/01", "2030/02/02", "B1", "drink"
    )

    assert product.id == "1"
    assert product.product_name == "bottle"
    assert product.company_name == "wee"
    assert product.manufacturing_date == "2023/01/01"
    assert product.expiration_date == "2030/02/02"
    assert product.serial_number == "B1"
    assert product.storage_instructions == "drink"

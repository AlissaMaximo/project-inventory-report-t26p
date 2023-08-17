from inventory_report.product import Product


def test_product_report() -> None:
    product = Product(
        "1", "bottle", "wee", "2023/01/01", "2030/02/02", "B1", "drink"
    )
    expected = (
        f"The product {product.id} - {product.product_name} "
        f"with serial number {product.serial_number} "
        f"manufactured on {product.manufacturing_date} "
        f"by the company {product.company_name} "
        f"valid until {product.expiration_date} "
        "must be stored according to the following instructions: "
        f"{product.storage_instructions}."
    )

    assert product.__str__() == expected

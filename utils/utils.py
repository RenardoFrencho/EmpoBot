from dataclasses import dataclass


@dataclass()
class DataForOrder():
    price: int
    type_of_product: str
    delivery_price: int
    final_price: int
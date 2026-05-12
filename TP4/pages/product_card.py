class ProductCard:
    """Représente un produit du catalogue (Bonus 1)"""

    def __init__(self, name: str, price: str):
        self.name = name
        self.price = price

    def to_dict(self) -> dict:
        return {"name": self.name, "price": self.price}

    def __repr__(self) -> str:
        return f"ProductCard(name={self.name!r}, price={self.price!r})"
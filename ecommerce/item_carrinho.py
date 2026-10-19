from ecommerce.categoria import Categoria


class ItemCarrinho:

    def __init__(self, produto: "Produto", quantidade: int) -> None:
        self.produto = produto
        self.quantidade = quantidade
        self.preco_no_momento = produto.preco

    def calcular_subtotal(self) -> float:
        return self.preco_no_momento * self.quantidade


if __name__ == "__main__":
    from ecommerce.categoria import Categoria
    from ecommerce.produto import Produto


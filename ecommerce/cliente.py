from ecommerce.pedido import Pedido

class Cliente:
    def __init__(self, nome: str, email: str):
        self.nome = nome
        self.email = email
        self.carrinho = None
        self._pedidos: list["Pedido"] =[]

    @property
    def pedidos(self) -> list["Pedido"]:
        return list(self._pedidos)

    def possui_carrinho(self) -> bool:
        return self.carrinho is not None

    def finalizar_compra(self) -> "Pedido":
        if self.carrinho is None:
            raise ValueError("Cliente nao possui carrinho")
        if not self.carrinho.itens:
            raise ValueError("Carrinho vazio")
        pedido = self.carrinho.finalizar()
        self._pedidos.append(pedido)
        self.carrinho.esvaziar()
        return pedido

    def adicionar_pedido(self, pedido: "Pedido") -> None:
        self._pedidos.append(pedido)

if __name__ == "__main__":  # 
    c = Cliente("João", "joao@email.com")
    print(f"Cliente: {c.nome}, Email: {c.email}")
    print(f"Possui carrinho: {c.possui_carrinho()}")
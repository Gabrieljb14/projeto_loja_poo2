class Cliente:
    def __init__(self, nome: str, email: str):
        self.nome = nome
        self.email = email
        self.carrinho = None

    def possui_carrinho(self) -> bool:
        return self.carrinho is not None


if __name__ == "__main__":  # 
    c = Cliente("João", "joao@email.com")
    print(f"Cliente: {c.nome}, Email: {c.email}")
    print(f"Possui carrinho: {c.possui_carrinho()}")
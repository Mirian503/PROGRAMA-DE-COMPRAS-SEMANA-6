from item_manager import show_items

class Cart:
    def __init__(self, owner):
        self.set_owner(owner)
        self.items = []

    def items_list(self):
        return self.items

    def add(self, item):
        self.items.append(item)

    def total_amount(self):
        price_list = []
        for item in self.items:
            price_list.append(item.price)
        return sum(price_list)

    def check_out(self):
        if self.owner.wallet.balance < self.total_amount():
            pass    # Elimina esta línea una vez que hayas implementado el método check_out correctamente.

        # Transferir el precio de compra de los artículos del carrito
        # del monedero del propietario del carrito al monedero del propietario del artículo.
        for item in self.items:
            item.owner.wallet.balance += item.price * item.quantity
            self.owner.wallet.balance -= item.price * item.quantity

            # Transferir la propiedad de todos los artículos del carrito al propietario del carrito.
            item.owner = self.owner

        # Vaciar el contenido del carrito.
        self.items = []

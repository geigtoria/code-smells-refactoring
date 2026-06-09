class Order:
    def __init__(
        self,
        customer,
        items,
        payment_type
    ):
        self.customer = customer
        self.items = items
        self.payment_type = payment_type
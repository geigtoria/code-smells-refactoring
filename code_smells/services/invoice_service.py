class InvoiceService:

    @staticmethod
    def generate_invoice(order):
        print(
            f"Nota fiscal gerada para {order.customer.name}"
        )
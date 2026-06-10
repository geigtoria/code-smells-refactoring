class PaymentService:

    @staticmethod
    def process_payment(order):
        print(
            f"Pagamento realizado via {order.payment_type}"
        )
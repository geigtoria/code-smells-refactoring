class EmailService:

    @staticmethod
    def send_confirmation(customer):
        print(
            f"E-mail enviado para {customer.email}"
        )
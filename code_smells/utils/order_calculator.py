class OrderCalculator:

    @staticmethod
    def calculate_total(items):
        return sum(
            item["price"] * item["quantity"]
            for item in items
        )
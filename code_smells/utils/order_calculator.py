class OrderCalculator:

    @staticmethod
    def calculate_total(items):
        return sum(
            item["price"] * item["quantity"]
            for item in items
        )
    @staticmethod
    def validate_items(items):
        if not items:
            return False
        for item in items:
            if "price" not in item or "quantity" not in item:
                return False
            if item["price"] <= 0 or item["quantity"] <= 0:
                return False
        return True

    @staticmethod
    def apply_discount(total, discount_percent):
        if discount_percent < 0 or discount_percent > 100:
            return total
        return total * (1 - discount_percent / 100)
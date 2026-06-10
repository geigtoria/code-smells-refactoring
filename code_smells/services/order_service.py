from utils.order_calculator import OrderCalculator

class OrderService:

    @staticmethod
    def calculate_order_total(order):
        return OrderCalculator.calculate_total(order.items)
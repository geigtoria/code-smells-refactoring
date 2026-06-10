from models.addres import Address
from models.customer import Customer
from models.order import Order

from services.order_service import OrderService
from utils.order_calculator import OrderCalculator


def main():

    address = Address(
        "Rua Principal",
        100,
        "Pau dos Ferros",
        "RN"
    )

    customer = Customer(
        "José Talvan Alves Dias",
        "123.456.789-00",
        "talvan@email.com",
        "(84) 99999-9999",
        address
    )

    items = [
        {
            "name": "Notebook",
            "price": 3500.00,
            "quantity": 1
        },
        {
            "name": "Mouse",
            "price": 100.00,
            "quantity": 2
        }
    ]

    if not OrderCalculator.validate_items(items):
        print("Pedido inválido!")
        return

    order = Order(
        customer,
        items,
        "PIX"
    )

    total = OrderService.calculate_order_total(order)

    print("===== RESUMO DO PEDIDO =====")
    print(f"Cliente: {customer.name}")
    print(f"CPF: {customer.cpf}")
    print(f"Cidade: {customer.address.city}")
    print(f"Pagamento: {order.payment_type}")
    print()

    print("Itens:")
    for item in order.items:
        subtotal = item["price"] * item["quantity"]

        print(
            f"- {item['name']} | "
            f"Qtd: {item['quantity']} | "
            f"Subtotal: R$ {subtotal:.2f}"
        )

    print()
    print(f"Total: R$ {total:.2f}")

    total_com_desconto = OrderCalculator.apply_discount(
        total,
        10
    )

    print(
        f"Total com 10% de desconto: "
        f"R$ {total_com_desconto:.2f}"
    )


if __name__ == "__main__":
    main()
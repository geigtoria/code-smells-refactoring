from models.person import Person

class Customer(Person):
    def __init__(
        self,
        name,
        cpf,
        email,
        phone,
        address
    ):
        super().__init__(name, cpf)

        self.email = email
        self.phone = phone
        self.address = address
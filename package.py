class Package:
    def __init__(
        self,
        id,
        delivery_address,
        delivery_deadline,
        delivery_city,
        delivery_zip,
        package_weight,
        delivery_status,
    ):
        self.id = id
        self.delivery_address = delivery_address
        self.delivery_deadline = delivery_deadline
        self.delivery_city = delivery_city
        self.delivery_zip = delivery_zip
        self.package_weight = package_weight
        self.delivery_status = delivery_status
        self.delivery_time = 800

    def __str__(self):
        return f"{self.id} {self.delivery_address} {self.delivery_deadline} {self.delivery_city} {self.delivery_zip} {self.package_weight} {self.delivery_status} "

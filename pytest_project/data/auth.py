from faker import Faker

class Auth:

    FAKER = Faker()

    def __init__(self):
        self.email = self.FAKER.email()
        self.password = self.FAKER.password()
        self.first_name = self.FAKER.name()
        self.last_name = self.FAKER.name()

    def get_email(self):
        return self.email

    def get_password(self):
        return self.password

    def get_first_name(self):
        return self.first_name

    def get_last_name(self):
        return self.last_name
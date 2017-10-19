"""Customers at Hackbright."""


class Customer(object):
    """Ubermelon customer."""

    # TODO: need to implement this
    def __init__(self, f_name, l_name, email, password):

        self.f_name = f_name
        self.l_name = l_name
        self.email = email
        self.password = password

    def __repr__(self):
        """Convenience method to show information about melon in console."""

        return "<Customer: {f_name}, {l_name}, {email} >".format(
            f_name=self.f_name, l_name=self.l_name, email=self.email)


def read_customers_from_file(filepath):
    """Reads customers from file and creates customer instances."""

    customers = {}

    for line in open(filepath):

        (f_name, l_name, email, password) = line.strip().split("|")

        customers[email] = Customer(f_name, l_name, email, password)

    return customers


def get_by_email(email):
    """takes in an email, returns customer if they exist"""

    return customers.get(email)


customers = read_customers_from_file('customers.txt')

class Customer:
    
    def __init__(self, name, email, membership_type):
        self.name = name
        self.email = email
        self.membership_type = membership_type

    def membership(self):
        return "{} has a {} membership.".format(self.name, self.membership_type)

customers = [Customer("Corey", "cdogwework@fastmail.com", "Gold"),
            Customer("Bradley", "bradleystein@gmail.com", "Bronze")]

# The type pf membership types each customer has
print(customers[0].membership())
print(customers[1].membership())

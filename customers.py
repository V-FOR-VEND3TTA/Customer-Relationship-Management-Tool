class Customer:
    
    def __init__(self, name, email, membership_type):
        self.name = name
        self.email = email
        self.membership_type = membership_type
        
c = Customer("Corey", "cdogwework@fastmail.com", "Gold")
print(c.name, "has a", c.membership_type, "membership type")

c2 = Customer("Brad", "bradleystein@gmail.com", "Bronze")
print(c2.name, "has a", c2.membership_type, "membership type")

customers = [Customer("Corey", "cdogwework@fastmail.com", "Gold"),
            Customer("Bradley", "bradleystein@gmail.com", "Bronze")]

# The type pf membership types each customer has
print(customers[0].name)
print(customers[1].name, "has a", customers[1].membership_type, "membership_type")

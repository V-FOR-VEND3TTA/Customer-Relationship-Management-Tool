class Customer:
    
    def __init__(self, name, email, membership_type):
        self.name = name
        self.email = email
        self.membership_type = membership_type

    def membership(self): # the membership type of a customer
        return "{} has a {} membership.".format(self.name, self.membership_type)

    def email_address(self): # makes it easier to just copy and paste a user's address for sending email purposes
        return "{}'s email address is {}".format(self.name, self.email)

# Store the customers in a list for easy access
customers = [Customer("Corey", "cdogwework@fastmail.com", "Gold"),
            Customer("Bradley", "bradleystein@gmail.com", "Bronze")]

# The type of membership types each customer has
print(customers[0].membership())
print(customers[1].membership())
# Each customer's respective email adsresses
print(customers[0].email_address())
print(customers[1].email_address())


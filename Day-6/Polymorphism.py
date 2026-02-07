# Polymorphism – Payment System (Method Overriding)
print("File is running")

class Payment:
    def pay(self):
        print("Processing generic payment...")


class GooglePay(Payment):
    def pay(self):
        print("Payment done using Google Pay")


class PhonePe(Payment):
    def pay(self):
        print("Payment done using PhonePe")


class CreditCard(Payment):
    def pay(self):
        print("Payment done using Credit Card")


payment1 = GooglePay()
payment2 = PhonePe()
payment3 = CreditCard()

payment1.pay()
payment2.pay()
payment3.pay()

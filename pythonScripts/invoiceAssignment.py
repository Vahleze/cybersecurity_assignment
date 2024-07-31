
#class Invoice:
    def __init__(self, number, description, quantity, price_per_item):
        self.number = number
        self.description = description
        self.quantity = quantity
        self.price_per_item = price_per_item

    def getNumber(self):
        return self.number
    
    def setNumber(self, value):
        return f"{self.number} = {value}"

    def getDescription(self):
        return self.description
    
    def setDescription(self, value):
        return f"{self.description} = {value}"

    def getQuantity(self):
        return self.quantity
    
    def setQuantity(self, value):
        if value < 0:
            return {value}
        else: return f"{self.quantity} = {value}" 

    def getPrice_per_item(self):
        return self.price_per_item 
    
    def setPrice_per_item(self, value):
        if value >=  0:
            return f"{self.price_per_item} = {value}"

    def getInvoiceAmount(self):
        return f"{self.quantity} * {self.price_per_item}"
    
invoice = Invoice("1234", "Hammer", "5", "19.66")

print("number:", invoice.number)
print("description:", invoice.description)
print("quantity:", invoice.quantity)
print("price_per_item:", invoice.price_per_item)
print("Invoice_Amount:", invoice.getInvoiceAmount())



class Invoice:
    def __init__(self, num, desc, qtty, price):
        self.num = num
        self.desc =desc
        self.qtty = qtty
        self.price = price

    def getPrice(self):
        return self.price

    def setPrice(self, price):
        if price > 0:
            self.price = price

    def invoiceAmount(self):
        return self.qtty * self.price
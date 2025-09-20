class Product:
    # class variables shared by all product objects
    inventory = [] # stores all product in a list
    product_counter = 0 # class variable to assign unique product ID

    def __init__(self, product_id, name, category, quantity, price, supplier): #initialize product attributes
        self.product_id = product_id
        self.name = name
        self.category = category
        self.quantity = quantity
        self.price = price
        self.supplier = supplier

    @classmethod # class method to add a new product to inventory
    def add_product(cls, name, category, quantity, price, supplier): # add a new product to the inventory
        cls.product_counter += 1  
        product = Product(cls.product_counter, name, category, quantity, price, supplier)
        cls.inventory.append(product) # store product in inventory
        return "Product added successfully"

    @classmethod # class method to update product details
    def update_product(cls, product_id, quantity=None, price=None, supplier=None):
        for product in cls.inventory: # search for product by ID
            if product.product_id == product_id:
                if quantity is not None:
                    product.quantity = quantity
                if price is not None:
                    product.price = price
                if supplier is not None:
                    product.supplier = supplier
                return "Product information updated successfully"
        return "Product not found"

    @classmethod # class method to delete a product
    def delete_product(cls, product_id):
        for product in cls.inventory:
            if product.product_id == product_id:
                cls.inventory.remove(product) # remove from list
                return "Product deleted successfully"
        return "Product not found"

    @classmethod # class method to display all products in inventory
    def display_inventory(cls):
        if not cls.inventory:
            return "Inventory is empty"
        inventory_list = []
        for product in cls.inventory:
            inventory_list.append(
                f"ID: {product.product_id}, Name: {product.name}, Category: {product.category}, "
                f"Quantity: {product.quantity}, Price: {product.price}, Supplier: {product.supplier}"
            )
        return "\n".join(inventory_list)


class Order: # contructor to create a new product
    def __init__(self, order_id, product_id, quantity, customer_info=""):
        self.order_id = order_id
        self.product_id = product_id
        self.quantity = quantity
        self.customer_info = customer_info

    # plcade order method
    def place_order(self):
        # search product in inventory
        for product in Product.inventory:
            if product.product_id == self.product_id: # check if enough stock is available
                if product.quantity >= self.quantity:
                    product.quantity -= self.quantity # to reduce stock
                    return f"Order placed successfully. Order ID: {self.order_id}"
                else:
                    return "Insufficient stock"
        return "Product not found"

print(Product.add_product("Laptop", "Electronics", 50, 1000, "Supplier A"))
print(Product.add_product("T-Shirt", "Clothing", 100, 25, "Supplier B"))
print(Product.update_product(1, quantity=45, price=950)) # update product info
print(Product.delete_product(2)) # delete a product

order1 = Order(order_id=1, product_id=1, quantity=2, customer_info="John Doe") # place an order
print(order1.place_order())

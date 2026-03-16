class Purchase:
    def __init__(self, user_id, product_id, catalog):
        self.user_id = user_id
        self.product_id = product_id
        self.catalog = catalog

    def initiate_purchase(self):
        product = self.catalog.get_product_details(self.product_id)
        if product:
            return f"Initiating purchase for {product['name']}."
        return "Product not found."

    def confirm_purchase(self):
        product = self.catalog.get_product_details(self.product_id)
        if product:
            # Logic to process payment and finalize purchase
            return f"Purchase confirmed for {product['name']}."
        return "Product not found."

    def send_receipt(self, receipt_details):
        # Logic to send receipt to the user
        return f"Receipt sent to user {self.user_id} for purchase of product ID {self.product_id}."
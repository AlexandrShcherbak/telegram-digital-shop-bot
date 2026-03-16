class AdminPanel:
    def __init__(self, product_catalog):
        self.product_catalog = product_catalog

    def add_product(self, product):
        self.product_catalog.append(product)

    def edit_product(self, product_id, updated_product):
        for index, product in enumerate(self.product_catalog):
            if product['id'] == product_id:
                self.product_catalog[index] = updated_product
                return True
        return False

    def delete_product(self, product_id):
        for index, product in enumerate(self.product_catalog):
            if product['id'] == product_id:
                del self.product_catalog[index]
                return True
        return False
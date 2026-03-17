class AdminPanel:
    def __init__(self, product_catalog):
        self.product_catalog = product_catalog

    def add_product(self, product):
        self.product_catalog.add_product(product)

    def edit_product(self, product_id, updated_product):
        product = self.product_catalog.get_product_details(product_id)
        if product is None:
            return False

        merged_product = {**product, **updated_product, "id": product_id}
        self.product_catalog.add_product(merged_product)
        return True

    def delete_product(self, product_id):
        if self.product_catalog.get_product_details(product_id) is None:
            return False

        return self.product_catalog.remove_product(product_id)

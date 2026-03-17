class ProductCatalog:
    def __init__(self):
        self._products_by_id = {}

    def add_product(self, product):
        product_id = product["id"]
        self._products_by_id[product_id] = product

    def list_products(self):
        return list(self._products_by_id.values())

    def get_product_details(self, product_id):
        return self._products_by_id.get(product_id)

    def remove_product(self, product_id):
        return self._products_by_id.pop(product_id, None) is not None

    def search_products(self, query):
        query_l = query.lower()
        return [
            product
            for product in self._products_by_id.values()
            if query_l in product["name"].lower()
        ]

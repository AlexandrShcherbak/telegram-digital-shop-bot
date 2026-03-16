class ProductCatalog:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def list_products(self):
        return self.products

    def get_product_details(self, product_id):
        for product in self.products:
            if product['id'] == product_id:
                return product
        return None

    def search_products(self, query):
        return [product for product in self.products if query.lower() in product['name'].lower()]
import hashlib

hash_table = {}

def generate_sha256_hash(product_name, category):
    concatenated_string = product_name + category
    return hashlib.sha256(concatenated_string.encode()).hexdigest()

def add_product_to_hash_table(product):
    product_hash = generate_sha256_hash(product['name'], product['category'])
    hash_table[product_hash] = product

def search_product_by_name_and_category(name, category):
    search_hash = generate_sha256_hash(name, category)
    return hash_table.get(search_hash, "Product not found")

product_1 = {"name": "Laptop", "category": "Electronics", "price": 999.99}
product_2 = {"name": "Phone", "category": "Electronics", "price": 699.99}

add_product_to_hash_table(product_1)
add_product_to_hash_table(product_2)

result = search_product_by_name_and_category("Laptop", "Electronics")
print(result)
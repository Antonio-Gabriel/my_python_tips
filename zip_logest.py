from itertools import zip_longest

products = ['Banana', 'Batata', 'Abacate', 'Ananas', 'Maça']
prices = [200, 300, 400, 500, 600]

for index, (product, price) in enumerate(zip_longest(products, prices)):
    print(f"{index}: product name: {product}, price: {price}")


# print(list(
#     range(50)
#     ))

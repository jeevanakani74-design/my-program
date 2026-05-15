def add_item(item, cart=[]):
    cart.append(item)
    return cart
print(add_item("apple"))
print(add_item("banana"))
print(add_item("milk", ["bread"]))
print(add_item("eggs"))
def add_item_fixed(item, cart=None):

    if cart is None:
        cart = []

    cart.append(item)

    return cart


print(add_item_fixed("apple"))
print(add_item_fixed("banana"))
def create_cart(owner, discount=0):

    return {
        "owner": owner,
        "items": [],
        "discount": discount
    }


# Add Items
def add_to_cart(cart, name, price, qty=1):

    item = {
        "name": name,
        "price": price,
        "qty": qty
    }

    cart["items"].append(item)


# Update Tuple Price
def update_price(price_tuple, new_price):

    try:
        price_tuple[1] = new_price

    except TypeError:
        print("Tuple cannot be changed because tuple is immutable")


# Calculate Total
def calculate_total(cart):

    total = 0

    for item in cart["items"]:

        total += item["price"] * item["qty"]

    discount_amount = total * (cart["discount"] / 100)

    final_total = total - discount_amount

    return final_total


# Customer 1
cart1 = create_cart("Alice", 10)

add_to_cart(cart1, "Laptop", 50000, 1)
add_to_cart(cart1, "Mouse", 500, 2)

# Customer 2
cart2 = create_cart("Bob")

add_to_cart(cart2, "Keyboard", 1000, 1)

# Display Carts
print("\nAlice Cart:")
print(cart1)

print("Total:", calculate_total(cart1))

print("\nBob Cart:")
print(cart2)

print("Total:", calculate_total(cart2))


# Tuple Test
price_data = ("Phone", 20000)

update_price(price_data, 25000)


# ==================================
# Discussion Points
# ==================================

# 1. discount=0 is safe because integer is immutable.
#    cart=[] is dangerous because list is mutable.

# 2. Rebinding means assigning new value.
#    Mutating means changing existing object.

# 3. Mutable: list, dict, set
#    Immutable: tuple, str, int

# 4. Yes, changes reflect outside because list is mutable.

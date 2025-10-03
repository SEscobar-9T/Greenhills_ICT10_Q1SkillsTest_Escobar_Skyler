from pyscript import display, document


restaurant_name = '🍫The Chocolate Palace🍫' # string
owner_name = 'Skyler Escobar' # string
year_established = '2025' # integer
popular_item_price = '₱450' # integer
has_delivery = True # boolean
product_names = ['Hot Chocolate', 'Chocolate Cake', 'Chocolate Chip Cookies', 'Chocolate Milkshake', 'Waffles with Belgian Chocolate'] # list
business_hours = ['9am', '9pm'] # list
menu_prices = ['₱99.00', '₱450.00', '₱150.00', '₱100.00', '₱130.00',] # list
common_allergens = ['egg', 'milk', 'wheat'] # list
tax_rate = 0.50 # float


display(f'{restaurant_name}', target='top')
display(f'by {owner_name}', target='div1')
display(f'est. {year_established}', target='div1')
display(f'Open from {business_hours[0]} to {business_hours[1]}', target='bottom')
display(f'{product_names[0]} {menu_prices[0]}', target='div2')
display(f'{product_names[1]} {menu_prices[1]}', target='div3')
display(f'{product_names[2]} {menu_prices[2]}', target='div4')
display(f'{product_names[3]} {menu_prices[3]}', target='div5')
display(f'{product_names[4]} {menu_prices[4]}', target='div6')


def order_form(enter):
    name = document.getElementById('inputName').value
    address = document.getElementById('inputAddress').value
    contact = document.getElementById('inputNumber').value
    
    message = f"""Order:\n
    Name: {name}\t
    Address: {address}\t
    Contact Number: {contact}\t

Receipt:\n
Order for: {name}
Address: {address}
Contact No: {contact}
Price: sum{menu_prices}
"""

    display(message, target="output")

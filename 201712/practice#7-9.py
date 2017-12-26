sandwich_orders = ['pastrami','rougamo','pastrami','tuna','pastrami']
finished_sandwichs = []

print("Pastrami sandwich from deli were sold out.")
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')
    finished_sandwichs = sandwich_orders

print("\nWe have: ")
for f_sandwich in finished_sandwichs:
    print(f_sandwich)
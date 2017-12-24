sandwich_orders = ['Rougamo','Dagwood','Cemita']
finished_sandwichs = []

while sandwich_orders:
    current_order = sandwich_orders.pop()

    print("I made your " + current_order + " sandwich." )
    finished_sandwichs.append(current_order)

print("\nFinished sandwich: ")
for f_sanwich in finished_sandwichs:
    print("\t" + f_sanwich)
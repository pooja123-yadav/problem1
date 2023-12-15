box_capacities = {'XS': 10, 'S': 20, 'M': 40, 'L': 80, 'XL': 160, 'XXL': 320}
city_costs = {
    "Delhi": {"XS": 12, "S": 23, "M": 45, "L": 77.4, "XL": 140, "XXL": 282},
    "Mumbai": {"XS": 14, "M": 41.3, "L": 89, "XL": 130, "XXL": 297},
    "Kolkata": {"XS": 11, "S": 20, "L": 67, "XL": 118}
}
capacity = 1150

output = []

for city, costs in city_costs.items():
    # Calculate cost per unit for each size in the city
    cost_per_unit = {size: cost / box_capacities[size] for size, cost in costs.items()}
    
    # Sort sizes based on cost per unit in increasing order
    sorted_sizes = sorted(cost_per_unit, key=cost_per_unit.get)
    
    current_capacity = 0
    selected_sizes = []
    total_cost = 0

    for size in sorted_sizes:
        while current_capacity + box_capacities[size] <= capacity:
            current_capacity += box_capacities[size]
            selected_sizes.append(size)
            total_cost += costs[size]

    output.append({
        "region": city,
        "total_cost": str(total_cost),
        "boxes": [(size, selected_sizes.count(size)) for size in set(selected_sizes)]
    })

result = {"Output": output}
print(result)

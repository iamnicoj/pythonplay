employees = { 'bob': 250000,
            'Richard': 350000,
            'Jennifer': 450000,
            'Petrosky': 800000,
            'Ginovesky': 850000,
            }

print(employees)

print([(name, val) for name, val in employees.items() if val > 500000])

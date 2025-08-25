def shipping_quote_multi_carrier():
    print("🏨 Welcome to Hotel Shipping Quote Calculator 🏨\n")
    
    # Package dimensions
    length = float(input("Enter package length (in inches): "))
    width = float(input("Enter package width (in inches): "))
    height = float(input("Enter package height (in inches): "))
    
    # Actual weight
    actual_weight = float(input("Enter package actual weight (lbs): "))
    
    # Distance (S/M/L)
    distance_input = input("Distance category? (S = Short/Local, M = Medium, L = Long): ").strip().upper()
    distance_map = {'S': 'Local', 'M': 'Medium', 'L': 'Long'}
    distance = distance_map.get(distance_input, 'Long')
    
    # Carriers info
    carriers = ['FedEx', 'UPS', 'USPS']
    dim_divisors = {'FedEx': 139, 'UPS': 139, 'USPS': 166}
    base_fee = {'FedEx': 8, 'UPS': 8, 'USPS': 5}
    per_lb_rate = {'FedEx': 0.85, 'UPS': 0.85, 'USPS': 0.75}
    distance_multipliers = {'Local': 1.0, 'Medium': 1.25, 'Long': 1.5}
    
    # Calculate carrier costs
    carrier_costs = {}
    print("\n📦 Carrier Shipping Costs:")
    for c in carriers:
        dim_w = length * width * height / dim_divisors[c]
        bill_w = max(actual_weight, dim_w)
        carrier_cost = base_fee[c] + (bill_w * per_lb_rate[c]) * distance_multipliers[distance]
        carrier_costs[c] = carrier_cost
        print(f"{c:6} | Shipping Cost: ${carrier_cost:7.2f}")
    
    # Suggested hotel fee based on cheapest carrier (e.g., 20% of cheapest cost)
    cheapest_cost = min(carrier_costs.values())
    suggested_fee = round(cheapest_cost * 0.2, 2)
    print(f"\n💰 Suggested hotel handling fee (20% of cheapest carrier cost): ${suggested_fee:.2f}")
    
    # Option to change suggested fee
    change_fee = input("Do you want to change the handling fee? (Y/N): ").strip().upper()
    if change_fee == 'Y':
        suggested_fee = float(input("Enter your desired handling fee ($): "))
    
    # Display final pretty table
    print("\n✨ Final Customer Prices ✨")
    print(f"{'Carrier':6} | {'Shipping Cost':14} | {'Hotel Fee':10} | {'Total Price':12}")
    print("-"*55)
    for c, cost in carrier_costs.items():
        total = cost + suggested_fee
        print(f"{c:6} | ${cost:12.2f} | ${suggested_fee:8.2f} | ${total:10.2f}")

# Run the interactive quote
shipping_quote_multi_carrier()


def interactive_shipping_quote():
    print("Welcome to Hotel Shipping Quote Calculator\n")
    
    # Package dimensions
    length = float(input("Enter package length (in inches): "))
    width = float(input("Enter package width (in inches): "))
    height = float(input("Enter package height (in inches): "))
    
    # Actual weight
    actual_weight = float(input("Enter package actual weight (lbs): "))
    
    # Carrier choice (case-insensitive)
    carrier_input = input("Choose carrier (FedEx / UPS / USPS): ").strip().upper()
    carrier_map = {'FEDEX': 'FedEx', 'UPS': 'UPS', 'USPS': 'USPS'}
    if carrier_input not in carrier_map:
        print("Invalid carrier. Defaulting to FedEx.")
        carrier = 'FedEx'
    else:
        carrier = carrier_map[carrier_input]
    
    # Distance (S, M, L) case-insensitive
    distance_input = input("Distance category? (S = Short/Local, M = Medium, L = Long): ").strip().upper()
    distance_map = {'S': 'Local', 'M': 'Medium', 'L': 'Long'}
    if distance_input not in distance_map:
        print("Invalid input. Defaulting to Long distance.")
        distance = 'Long'
    else:
        distance = distance_map[distance_input]
    
    # Hotel fee
    hotel_fee = float(input("Enter your hotel handling fee ($): "))
    
    # DIM divisors and rates
    dim_divisors = {'FedEx': 139, 'UPS': 139, 'USPS': 166}
    base_fee = {'FedEx': 8, 'UPS': 8, 'USPS': 5}
    per_lb_rate = {'FedEx': 0.85, 'UPS': 0.85, 'USPS': 0.75}
    distance_multipliers = {'Local': 1.0, 'Medium': 1.25, 'Long': 1.5}
    
    # Calculate DIM weight and billable weight
    dim_weight = length * width * height / dim_divisors[carrier]
    billable_weight = max(actual_weight, dim_weight)
    
    # Carrier cost
    carrier_cost = base_fee[carrier] + (billable_weight * per_lb_rate[carrier]) * distance_multipliers[distance]
    
    # Final customer price
    total_price = carrier_cost + hotel_fee
    
    print("\n--- Shipping Quote ---")
    print(f"Carrier: {carrier}")
    print(f"Distance Category: {distance}")
    print(f"DIM Weight: {dim_weight:.2f} lbs")
    print(f"Billable Weight: {billable_weight:.2f} lbs")
    print(f"Carrier Cost: ${carrier_cost:.2f}")
    print(f"Hotel Fee: ${hotel_fee:.2f}")
    print(f"Total Customer Price: ${total_price:.2f}")

# Run the interactive quote
interactive_shipping_quote()

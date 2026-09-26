# Function 1: Circle Area Calculation
def calculate_circle_area(radius):
    pi = 3.14159
    area = pi * (radius ** 2)
    return area


# Function 2: Taxes Calculation
def calculate_total_due(money, tax_rate):
    total_due = money + (money * tax_rate)
    return total_due


# Function 3: Temperature Conversion
def convert_fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * (5 / 9)
    return celsius


def main():
    # --- Circle Area Test ---
    print("--- Area of a Circle ---")
    radius = float(input("Enter radius: "))
    area = calculate_circle_area(radius)
    # Formatted to 2 decimal places per instructions
    print(f"Output: {area:.2f}\n")

    # --- Taxes Test ---
    print("--- Taxes Calculation ---")
    money = float(input("Enter money amount: "))
    # Converts percentage input (e.g., 6) into decimal format (0.06)
    tax_input = float(input("Enter tax rate percentage (e.g., 6 for 6%): "))
    tax_rate = tax_input / 100
    total_due = calculate_total_due(money, tax_rate)
    print(f"Output: {total_due:.2f}\n")

    # --- Temperature Test ---
    print("--- Temperature Conversion ---")
    fahrenheit = float(input("Enter temperature in Fahrenheit: "))
    celsius = convert_fahrenheit_to_celsius(fahrenheit)
    print(f"Output: {celsius}\n")


if __name__ == "__main__":
    main()
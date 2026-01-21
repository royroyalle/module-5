class RomanConverter:
    def __init__(self):
        self.roman_map = {
            1000: "M", 900: "CM", 500: "D", 400: "CD",
            100: "C", 90: "XC", 50: "L", 40: "XL",
            10: "X", 9: "IX", 5: "V", 4: "IV", 1: "I"
        }
    def to_roman(self, num):
        roman_numeral = ""
        for value, symbol in self.roman_map.items():
            while num >= value:
                roman_numeral += symbol
                num -= value
        return roman_numeral
def main():
    converter = RomanConverter()
    user_input = int(input("Enter an integer to convert: "))
    
    if user_input <= 0:
        print("Please enter a positive integer.")
    else:
        result = converter.to_roman(user_input)
        print(f"The Roman numeral is: {result}")
if __name__ == "__main__":
    main()
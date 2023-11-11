def get_bit_value(number:int, bit_index:int)->int:
    if number < 0 or number > 255:
        raise ValueError("Number must be in range <0, 255>.")
    if bit_index < 0 or bit_index > 7:
        raise ValueError("Bit index must be in range <0, 7>.")
    return (number >> bit_index) & 1

number = int(input("Give a number (0-255): "))
bit_index = int(input("Give indeks of bit (0-7): "))

bit_value = get_bit_value(number, bit_index)

print(f"Value of bit on position {bit_index} in number {number} is {bit_value}.")

def calculate_area(length, width):
    return length * width

length, width = map(int, input().split())
print(calculate_area(length, width))
# Q.2 Write a function that converts hours into seconds.

def convert_hours_to_seconds(a):
    return a * 3600

a = int(input("Enter the number of hours :"))
print("Seconds: - ", convert_hours_to_seconds(a))
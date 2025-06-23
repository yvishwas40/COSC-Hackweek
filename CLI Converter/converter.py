import argparse

parser = argparse.ArgumentParser(description="Simple Temperature Converter")
parser.add_argument("-c", type=float, help="Convert Celsius to Fahrenheit")
parser.add_argument("-f", type=float, help="Convert Fahrenheit to Celsius")

args = parser.parse_args()

if args.c is not None:
    print(f"{args.c}°C = {(args.c * 9/5) + 32:.2f}°F")
elif args.f is not None:
    print(f"{args.f}°F = {(args.f - 32) * 5/9:.2f}°C")
else:
    print("Please provide -c or -f to convert temperature")

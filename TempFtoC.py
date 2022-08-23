#Script to take temp and change from Farehnheit to Celcius

fahrenheit = float(input("What temperature in fahrenheit would you like converted to celcius? "))
celsius = (fahrenheit - 32) * 5 / 9

print(fahrenheit, "F is", round(celsius, 2), "C")

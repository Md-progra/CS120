#Understand - Input: float double Celsius output:  a list of input float as Kelvin and Fahrenheit

def convertTemp(Celsius):
    ans = []
    Kelvin = Celsius + 273.15
    ans.append(Kelvin)
    Fahrenheit = Celsius * 1.80 + 32.00
    ans.append(Fahrenheit)
    return ans

temperatures = convertTemp(23.00)
print(temperatures)
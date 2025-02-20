class Converter:
    def convert(self, value,unit):
        self.value = value
        self.unit = unit

        pass
class Length(Converter):
    def convert(self,value,unit):
        if unit == "feet":
            return value * 12
        if unit == "inches":
            return value
        elif unit == "yards":
                return value * 36
        elif unit == "miles":
            return value * 63360
        elif unit == "cm":
            return value * 0.393701
        elif unit =="kilometers":
            return value * 39370.1
        elif unit == "millimeters":
            return value * 1000
        else:
            return "Invalid unit"


#Object of class Length
length = Length()
print(length.convert(1,"feet"))
print(length.convert(1,"inches"))
print(length.convert(1,"yards"))
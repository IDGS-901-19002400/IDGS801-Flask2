from form import COLORS

def calculate(firstBand, secondBand, thirdBand, tolerance):
    result  =  int(f"{COLORS. index(firstBand)}{COLORS. index(secondBand)}") *  int(f"1{COLORS. index(thirdBand) *  '0'}")
    minVal = result - (result * float(0.05 if tolerance == 'gold' else 0.1))
    maxVal = result + (result * float(0.05 if tolerance == 'gold' else 0.1))

    return (firstBand, secondBand, thirdBand, tolerance, result, minVal, maxVal)
    
def saveResistance(firstBand, secondBand, thirdBand, tolerance):
    with open('resistance.txt', 'a') as file:
        file. write(f"{firstBand}  {secondBand}  {thirdBand}  {tolerance}\n")

def getValues(firstBand, secondBand, thirdBand, tolerance):
    return (COLORS. index(firstBand), COLORS. index(secondBand), f"1{COLORS. index(thirdBand) *  '0'}", 0.05  if  tolerance  ==  'gold'  else  0.1)

def getResistance():
    with open('resistance.txt', 'r') as file:
        lines  =  file.read().splitlines()
        return [tuple(filter(lambda x : x != '', line.split(' '))) for  line  in  lines]
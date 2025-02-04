#TempConvert.py
#Name: Brooks Conway
#Date: 2/3/2025
#Assignment:Lab 3 Temp Convert


def main():
  #Prompt the user for a Fahrenheit temperature
  #Convert that temperature to celsius, rounding to 1 decimal percision
  #Output converted temperature.
  tempF = input("Enter degrees Fahrenheit: ")

  
tempC=(int(tempF)-32)/1.
  print(tempF, "is ", tempC, "degrees celsius.")
if __name__ == '__main__':
  main()

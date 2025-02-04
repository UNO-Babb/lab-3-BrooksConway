#TempConvert.py
#Name: Brooks Conway
#Date: 2/3/2025
#Assignment:Lab 3 Temp Convert

def main():

  tempF = input("Enter degrees Fahrenheit: ")

  tempC = (int(tempF)-32)/1.8

  Final = round(tempC, 1)

  print(tempF, "is ", Final, "degrees celsius.")
if __name__ == '__main__':
  main()

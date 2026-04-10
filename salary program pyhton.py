#Input
salary = float(input("Enter yor salary"))
years_of_service = int(input("Enter your years of service"))

#check condition
if years_of_service  >  5:
    bonus =salary * 0.05
    print("Eligible for bonus")
    print("salary amount :",bonus)
    print("Total salary with bonus:",salary + bonus)
else:
    print("print you are not eligible for bonus")
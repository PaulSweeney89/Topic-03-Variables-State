# simple program that reads	in two numbers and divides the	
# first	one	by the second and give the integer result and the remainder

x = float(input("Enter 1st number:"))
y = float(input("Enter 2nd number:"))

z = int(x / y)
r = x % y

print("Interger of", x, "/", y, "= ", z)
print("Reminder of", x, "/", y, "= ", r)
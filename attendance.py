h=int(input("Held: "))
a=int(input("Attended: "))
p=(a/h)*100
print("Attendance:",p,"%")
h=int(input("Held: "))
a=int(input("Attended: "))
p=(a/h)*100
s="Eligible" if p>=75 else "Not Eligible"
print(f"Attendance:{p}% Status:{s}")

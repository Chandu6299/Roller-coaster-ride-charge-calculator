print("Welcome to the rollercoaster! ")
h=int(input("What is your height in cm? "))
bill = 0
if h>=120:
  a=int(input("What is your age in years? "))
  if a<12:
    bill = 5
    print("You can ride and pay only $5")
  elif a<=18:
    bill = 7
    print("You can ride and pay only $7")
  else:
    bill =12
    print("You can ride and pay only $12")
    photo = input("Do you want a photo taken? Y or N ")
    if photo == "Y" or photo == "y":
      bill += 3
    print(f"your final bill is {bill}")
else:
  print("You can't ride")

print("Enter temperature")
t = int(input())

print("Is it raining: 1 or 0")
r = str(input())

print("Is rain strong? at 5 to 10")
s = int(input())

if 20<= t <=30 and r == "1":
    print("T-shirt, shorts, raincoat")

elif 20<= t <=30 and r == "0": 
    print("T-shirt, shorts")

elif 0<= t <= 20 and r == "0":
    print("Coat")

elif 0<= t <= 20 and r == "1" and 5<= s <=7:
    print("Coat and raincoat")

elif 0<= t <= 20 and r == "1" and 8<= s <=10:
    print("Coat? umbrella, rubber boots")

elif t<0:
    print("Down jacket")
    

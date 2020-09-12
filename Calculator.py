f_n = float(input("Enter first number:"))
act = input("Enter math action:")
list1 = ["/", "*", "+", "-", "^", "%", "//"]
s_n = float(input("Enter second number:"))
dec = "Sorry, I\'m stupid and don\'t identified this ERROR"
if act not in list1:
    dec = "Your action isn\'t identified, please try again"
if act == "+":
    dec = f_n + s_n
elif act == "-":
    dec = f_n - s_n
    print("Answer is", dec)
elif act == "*":
    dec = f_n * s_n
    print("Answer is", dec)
elif act == "^":
    dec = f_n ** s_n
    print("Answer is", dec)
if s_n == 0:
    dec = "Sorry, but now, we don\'t know how to divide by zero"
else:
    if act == "/":
        dec = f_n / s_n
    elif act == "//":
        dec = f_n // s_n
print(dec)
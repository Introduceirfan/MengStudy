# Write your solution here
gift = float(input("Value of gift: "))
gift_a = (100 + (gift - 5000) * 0.08)
gift_b = (1700 + (gift - 25000) * 0.10)
gift_c = (4700 + (gift - 55000) * 0.12)
gift_d = (22100 + (gift - 200000) * 0.15)
gift_e = (142100 + (gift - 1000000) * 0.17)
if gift > 1000000 :
    print(f"Amount of tax: {gift_e} euros")
elif gift >= 200000 and gift <= 1000000:
    print(f"Amount of tax: {gift_d} euros")
elif gift >= 55000 and gift <= 200000:
    print(f"Amount of tax: {gift_c} euros")
elif gift >= 25000 and gift <= 55000:
    print(f"Amount of tax: {gift_b} euros")
elif gift >= 5000 and gift <= 25000:
    print(f"Amount of tax: {gift_a} euros")
else:
    print(f"No tax!")

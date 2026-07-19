#1
# level : 10 , hitung satu huruf
# def hitung_huruf_a(string) :
#     counter = 0
#     for i in string:
#         if i == "a":
#             counter += 1

#     return counter

# if __name__ == "__main__":
#     print(hitung_huruf_a("jakarta"))

#2, level : 10 , hitung parameter huruf

# def hitung_huruf(string, alp):
#     counter = 0
#     for i in string:
#         if i == alp:
#             counter += 1

#     return counter
# if __name__ == "__main__":
#     print(hitung_huruf("jakarta", "k"))
#     print(hitung_huruf("jakarta", "a"))

#3 level : 11 , cari indeks huruf

# def cari_indeks_huruf(string, alp):
#     for i in range(len(string)):
#         if string[i] == alp:
#             return(i)
#     return (-1)
        
# if __name__ == "__main__":
#     print(cari_indeks_huruf("jakarta", "k"))
#     print(cari_indeks_huruf("jakarta", "z"))

#4 level : 11, membalikkan kata
# def reverse(string):
#     result = ""
#     for i in string:
#         result = i + result
#     return result

# if __name__ == "__main__":
#     print(reverse("kopik"))

#5 level: 12, does it palindrome?
# def reverse(string):
#     result = ""
#     for i in string:
#         result = i + result
#     return result

# def is_palindrome(string):
#     reversed = reverse(string)
#     if string == reversed:
#         return True
#     return False

# if __name__ == "__main__":
#     print(is_palindrome("katak"))

#6 level: 13, is it triangle?
# def triangle(n):
#     i = 1
#     stars = "*"
#     while i <= n:
#         print(f"{stars * i}")
#         i += 1

# if __name__ == "__main__":
#     triangle(4)

#7 level: 13, still is it triangle(reversed)?
# def triangle(n):
#     i = n
#     while i > 0:
#         print("*" * i)
#         i -= 1

# if __name__ == "__main__":
#     triangle(4)

#8 level: 14, still triangle (but right margin)
# def triangle(n):
#     i = 1
#     space = " "
#     star = "*"
#     while i <= n:
#         print(f"{space * (n-i)}{star * i}")
#         i += 1

# if __name__ == "__main__":
#     triangle(4)

#9 level: 15, triangle but more hardway :) this is spruce by the way.
# def triangle(n):
#     i = 1
#     space = " "
#     star = "*"
#     while i <= n:
#         print(f"{space * (n-i)}{star * ((2*i)-1)}")
#         i += 1
#     print(f"{space * (n-1)}{star * ((2*1)-1)}")
# if __name__ == "__main__":
#     triangle(4)
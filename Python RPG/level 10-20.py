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
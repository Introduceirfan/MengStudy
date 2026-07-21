# Write your solution here
def anagrams(string1, string2):
    stre1 = sorted(string1)
    stre2 = sorted(string2)

    if len(stre1) != len(stre2):
        return False
    
    for i in stre1:
        if i in stre2 :
            stre2.remove(i)
    
    if len(stre2) != 0:
        return False
    else:
        return True

if __name__ == "__main__":
    print(anagrams("test", "set"))
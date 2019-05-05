def substring(s1, s2):
    hasil = "bukan substring"
    new_list = []
    if len(s2) > len(s1):
        return "Panjang string s2 tidak boleh lebih dari string s1" 
    if s1 == s2:
        hasil = "sama"
    elif s1 == s2[-1::-1]:
        hasil = "pencerminan"
    else:
        for i in range(len(s1)):
            for j in range(len(s2)):
                if s1[i] == s2[j]:
                    new_list.append(s1[i])
                    break
        if list(s2) == new_list:
            hasil = 'substring'
        else:
            new_list.reverse()
            if s2[0] == new_list[0] or s2[-1] == new_list[-1]:
                hasil = 'substring pencerminan'
    return hasil

def main():
    test_case = int(input())
    arr = []
    for i in range(test_case):
        s1 = input().split()
        arr.append(s1)
    for j in range(len(arr)):
        print(substring(arr[j][0], arr[j][1]))
main()

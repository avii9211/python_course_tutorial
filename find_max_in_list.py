# finding max element in the given list 
abhi = [12,3,4,5,6,9,90,101,98,78,7779,9999,1]
maxi = abhi[0]
for ele in abhi:
    if ele > maxi:
        maxi = ele
print(maxi)
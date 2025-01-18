"""
Given K, find the geometric sum
1+(1/2)+(1/4)+(1/8)+(1/2^K)
"""


def geometric_sum(k):
    if k == 0:
        return 1
    return round(1/(2**k) + geometric_sum(k-1),5)


terms = int(input("Enter the number of terms: "))
print("%.5f"% geometric_sum(terms))

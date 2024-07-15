
"""
    1 <= k <= num.length <= 10^5
    num consists of only digits.
    num does not have any leading zeros except for the zero itself.

"""


def removeKdigits2(num: str, k: int) -> str:
    if k == len(num):
        return str(0)
    k_num = num[:k+1]

    m = max([int(i) for i in k_num])
    new_n = k_num.replace(str(m), "", 1)
    num = num.replace(k_num, new_n, 1)
    k -= 1
    if k == 0:
        while (num[0] == '0'):
            num = num[1:]
        return num
    return removeKdigits2(num, k)

def removeKdigits(num: str, k: int) -> str:
    st = list()
    for n in num:
        while st and k and st[-1] > n:
            st.pop()
            k -= 1

        if st or n is not '0':  # prevent leading zeros
            st.append(n)

    if k:  # not fully spent
        st = st[0:-k]

    return ''.join(st) or '0'


# print(removeKdigits(num="1432219", k=3))
# print(removeKdigits(num="10200", k=1))
# print(removeKdigits(num="10", k=2))
print(removeKdigits(num="1432219", k=3))

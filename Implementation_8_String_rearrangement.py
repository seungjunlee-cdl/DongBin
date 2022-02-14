def solution(S):
    S_div = list(map(str,S))
    num_sum = 0
    sorted_str = []
    for i in range(len(S_div)):
        S_div[i] = ord(S_div[i])
    S_div.sort()
    for i in range(len(S_div)):
        if S_div[i] < 65:
            num_sum += int(chr(S_div[i]))
        else:
            sorted_str.append(chr(S_div[i]))

    sorted_str.append(str(num_sum))
    sorted_str = "".join(sorted_str)

    return sorted_str

# testcase1 = 'K1KA5CB7'   return 'ABCKK13'
# testcase2 = 'AJKDLSI412K4JSJ9D'   return 'ADDIJJJKKLSS20'

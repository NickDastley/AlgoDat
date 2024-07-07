def merge_sort(S):
    n = len(S)
    if n < 2:
        return
    mid = n // 2
    S1 = S[:mid]
    S2 = S[mid:]
    merge_sort(S1)
    merge_sort(S2)
    merge(S1, S2, S)
    print(S)


def merge(S1, S2, S):
    i = j = k = 0
    while i < len(S1) and j < len(S2):
        if S1[i] < S2[j]:
            S[k] = S1[i]
            i += 1
        else:
            S[k] = S2[j]
            j += 1
        k += 1

    while i < len(S1):
        S[k] = S1[i]
        i += 1
        k += 1

    while j < len(S2):
        S[k] = S2[j]
        j += 1
        k += 1


#
# def merge(S1, S2, S):
#     S_iterator = -1
#     S1_iterator = 0
#     S2_iterator = 0
#
#     for i in range(len(S)):
#         S_iterator += 1
#         if S1_iterator >= len(S1):
#             S[S_iterator] = S2[S2_iterator]
#             S2_iterator += 1
#             continue
#
#         if S2_iterator >= len(S2):
#             S[S_iterator] = S1[S1_iterator]
#             S1_iterator += 1
#             continue
#
#         if S1[S1_iterator] <= S2[S2_iterator]:
#             S[S_iterator] = S1[S1_iterator]
#             S1_iterator += 1
#             continue
#
#         if S1[S1_iterator] > S2[S2_iterator]:
#             S[S_iterator] = S2[S2_iterator]
#             S2_iterator += 1
#             continue
#     return

print(merge_sort([3, 6, 2, 4, 7, 2, 6, 7]))

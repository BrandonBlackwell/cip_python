def isAnagram(s, t):
    #         SOLUTION 1 USING SORT METHOD
    # s = list(s)
    # s.sort()
    # t = list(t)
    # t.sort()
    # if s == t:
    #     return True
    # return False
    ######################################################################
    #         SOLUTION 2 USING SORTED FUNCTION
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    s, t = sorted(s), sorted(t)
    if s == t:
        return True
    return False


#######################################################################
#       SOUTION 3 USING DICTIONARY (Does not work because of this case a = aabbbb b = aaaabb)
#         sDict = {}
#         tDict = {}
#         lenOfs = len(s)
#         lenOft = len(t)
# #         s dictionary
#         for i in range(lenOfs):
#             if s[i] in sDict:
#               sDict[s[i]]+=1
#             else:
#               sDict[s[i]]=1
#         # print(sDict)

# #         t dictionary
#         for i in range(lenOft):
#             if t[i] in tDict:
#               tDict[t[i]]+=1
#             else:
#               tDict[t[i]]=1
#         # print(tDict)
#         sVals = list(sDict.values())
#         sVals.sort()
#         # print(sVals)
#         tVals = list(tDict.values())
#         tVals.sort()
#         # print(tVals)
#         if(sVals == tVals and sorted(sDict) == sorted(tDict)):
#             return True
#         return False


def main():
    s = "aabbbb"
    t = "aaaabb"
    print(isAnagram(s, t))


if __name__ == "__main__":
    main()

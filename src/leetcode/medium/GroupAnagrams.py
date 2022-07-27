"""
 * https://leetcode.com/problems/anagrams/
 * <p>
 * Given an array of strings, group anagrams together.
 * <p>
 * For example, given: ["eat", "tea", "tan", "ate", "nat", "bat"],
 * Return:
 * <p>
 * [
 * ["ate", "eat","tea"],
 * ["nat","tan"],
 * ["bat"]
 * ]
 * <p>
 * Note:
 * <p>
 * For the return value, each inner list's elements must follow the lexicographic order.
 * All inputs will be in lower-case.
"""


class GroupAnagrams:
    def groupAnagrams(self, strs):
        result = []
        m = {}

        for i in range(len(strs)):
            word = strs[i]
            word = "".join(sorted(word))

            if m.__contains__(word) is False:
                v = []
                v.append(strs[i])
                result.append(v)
                m[word] = len(result) - 1
            else:
                result[m[word]].append(strs[i])

        for i in range(len(result)):
            result[i] = sorted(result[i])

        return result

    # using multiset
    def groupAnagrams2(self, strs):
        result = []
        m = {}

        for i in range(len(strs)):
            word = strs[i]
            word = "".join(sorted(word))

            if m.__contains__(word) is False:
                m[word] = []

            m[word].append(strs[i])

        for v in m.values():
            result.append(v)

        return result

    # NOTICE: the below solution has been deprecated as the problem has been updated!
    def groupAnagrams3(self, strs):
        result = []
        m = {}

        for i in range(len(strs)):
            word = strs[i]

            # sort it can easy to check they are anagrams of not
            word = "".join(sorted(word))

            # only is not add
            if m.__contains__(word) is False:
                m[word] = i
            else:
                if m[word] >= 0:
                    result.append(strs[m[word]])
                    m[word] = -1

                result.append(strs[i])

        return result


def main():
    obj = GroupAnagrams()
    print(obj.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
    print(obj.groupAnagrams2(["eat", "tea", "tan", "ate", "nat", "bat"]))
    print(obj.groupAnagrams3(["eat", "tea", "tan", "ate", "nat", "bat"]))


if __name__ == '__main__':
    main()

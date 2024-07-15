from typing import List


def removeComments(source: List[str]) -> List[str]:
    mul = False
    for index, s in enumerate(source):
        if str.__contains__(s, "//"):
            i = s.find("//")
            source[index] = s[0:i]
        if s.find("/*") != -1:
            mul = True
            si = s.find("/*")
            if s.find("*/") == -1:
                source[index] = s[0:si]
            else:
                ei = s.find("*/")
                r = s[si:ei+2]
                source[index] = s.replace(r, '')
            continue
        if s.find("*/") != -1:
            ei = s.find("*/")
            source[index] = s[ei+2:]
            mul = False
            continue
        if mul == True:
            source[index] = ''

    return list(filter(lambda x: len(x) > 0, source))


# source = ["/*Test program */", "int main()", "{ ", "  // variable declaration ", "int a, b, c;",
#           "/* This is a test", "   multiline  ", "   comment for ", "   testing */", "a = b + c;", "}"]
# print(source)
# o = removeComments(source)
# print(o)
# e = ["int main()", "{ ", "  ", "int a, b, c;", "a = b + c;", "}"]
# print(o == e)

x = removeComments(["a/*comment", "line", "more_comment*/b"])
print(x)

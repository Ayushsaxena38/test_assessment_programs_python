def common_not_common(a , b):
    common = []
    not_common = []
    common = list(set(a) & set(b))
    not_common = list(set(a) ^ set(b))
    return common , not_common
a = ["One Punch Man","Attack On Titan","One Piece","Sword Art Online","Bleach","Dragon Ball Z","One Piece"]
b = ["Full Metal Alchemist","Code Geass","Death Note","Stein's Gate","The Devil is a Part Timer!","One Piece","Attack On Titan"]

print(common_not_common(a,b))
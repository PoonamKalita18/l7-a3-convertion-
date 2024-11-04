def test(L):
    result = {}
    for item in L:
        result[item[0]] = item[1:]
    return result

students = [[1,'Poonam',44],[2, 'Yoongi'][3,'Jungkook','Jk'],[4,'puspa']]

print("\n Og list :")
print(students)
print("\n Conveted onces :")
print(test(students))
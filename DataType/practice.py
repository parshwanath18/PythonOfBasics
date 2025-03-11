s1 = "Code"
s2 = "World"
s3 = "hello"

'''print(id(s1[1]))
print("Address of  'o in s1 is: ", s1, id(s1))
print(id(s2[1]))
print(s2, id(s2))'''


print("Address of  'o in s1 is:",id(s1[1]))
print("Address of  'o in s1 is:",id( s2[1]))
print("Address of  'o in s1 is:",id( s3[4]))

print("Address of  'l in s1 is:" , id( s2[3]))
print("Address of  'l in s1 is:", id(s3[4]))

#String interning == have all the records of charcaters
#capital and small latters address will deffrent way
#id function is helps to get partical address of the character
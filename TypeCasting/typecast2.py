#bool();
print(bool(12)) # True -- int to bool conversion
print(bool(12.456)) # True -- float to bool conversion
print(bool('Code')) # True -- -- string holding float to bool
print(bool(0)) #false -- int to bool
print(bool('')) #false -- empty string to bool

#float():
print(float(123)) # 123.0 -- int to float conversion
#print(float('Code')) Error -- -- string holding float to float
print(float('123.23')) # 123.23 -- string holding float to float
print(float(True)) # 1.0 -- bool to conversion
print(float(False)) # 0.0 -- bool to conversion

#int():
print(int(123.55)) #123 -- float to int conversion
print(int('123')) # 123 -- stirng holding int to int allowed
print(int(True)) # 1 --boolean to int
print(int(False)) # 0 --boolean to int
print(int('Code')) # Error --String holding String to int
print(int('123.45')) # Error --String holding float to int

'''
int('123.67) -- Not Allowed
int(123.67) -- Allowed
'''
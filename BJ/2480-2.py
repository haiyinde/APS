*_,a,b,c=sorted(input())
print(['1'+b,c][a<b<c]+'000'[a<c:])

# int(False) == 0
# int(True)  ==

# '000'[False:]  == '000'[0:] == '000'
# '000'[True:]   == '000'[1:] == '00'

# ['1' + b, c][False] == ['1' + b, c][0] == '1' + b
# ['1' + b, c][True]  == ['1' + b, c][1] == c

# prefix = c if a < b < c else '1' + b
# suffix = '00' if a < c else '000'
# print(prefix + suffix)
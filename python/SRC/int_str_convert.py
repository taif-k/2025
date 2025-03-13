
check1 = "0123"
print("\nCheck 1")
print("\n ",type(check1),check1)
check1 =  int(check1)
print("\n ",type(check1),check1)

check2 = 0000
print("\nCheck 2")
print("\n ",type(check2),check2)
check2 = str(check2)
print("\n ",type(check2),check2)

check3 = "0000"
print("\nCheck 3")
print("\n ",type(check3),check3)
check3 = int(check3)
print("\n ",type(check3),check3)

check4 = "0x123"  # this will give error because this str is cant be converted to int because invalid literal for int() with base 10: '0x123'
print("\nCheck 4")
print("\n ",type(check4),check4)
check4 = int(check4)  # remove or comment this line to run this without error 
print("\n ",type(check4),check4)

check5 = 0o123  # to take 0123 use it as string, this will give output as 83 
print("\nCheck 5")
print("\n ",type(check5),check5)
check5 = int(check5)
print("\n ",type(check5),check5)

check6 = 1.1e2
print("\nCheck 6")
print("\n ",type(check6),check6)
check6 = int(check6)
print("\n ",type(check6),check6)

# o(octal) ->  8-base number system, (0-7 only) = 8
# ex: 0o777, 0o123 (calculation - 1*16 + 2*8 + 3*1) 
# 0o129 is not octal because it has 9 in it 

# x/X(Hexadecimal) ->  16-base number system, (0-9 plus a/A=10 to f/F=16) = 16
# ex: 0x129, 0X1A3 (calculation - 1*256 + (A)10*16 + 3*1) 
# its better to do ot with octal like 0o123 and not 0x123, here both are correct but different values will be produced,
# above statement depends on what value we need according to the situation.


# e(exponent)/scientific notation - mainly used to represent floating-point numbers
# ex: 1e2 (calculation -> 1 * 10^2) 
# represet number in compact form
# represent power of 10

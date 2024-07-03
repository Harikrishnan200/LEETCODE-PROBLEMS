
# Give a positive int number, op its complement number. the complement strategy is to flip the bits of its binary
# representation (coding mafia)

# input :5 (101) 
# output : 2 (010)


class Solution:
    def __init__(self):
        self.result = ''

    def complementary_number(self,num:int) ->int:

        binary_num = bin(num)[2:]   # [2:] removes the first two characters ('0b'), leaving just the binary digits. So bin(5)[2:] gives '101'.
                                    # for eg, bin(5) gives '0b101'.

        for i in binary_num:
            if i == '0':
                self.result += '1'
            else:
                self.result += '0'
        return int(self.result,2)  # it indicates that the string flipped_binary is a binary (base-2) number. This is necessary because the default base for int() is 10 (decimal), and we need to tell Python to interpret the string as a binary number.


complement_num = Solution().complementary_number(5)
print(f'Complement number : {complement_num}')
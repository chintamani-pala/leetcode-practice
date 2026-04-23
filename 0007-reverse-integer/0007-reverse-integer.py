class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        is_negetive = x < 0
        count = 0
        copy_num = abs(x)
        while copy_num != 0:
            count += 1
            copy_num //= 10
        copy_num = abs(x)
        final_num = 0
        count_abs = 1
        while copy_num != 0:
            last_num = copy_num % 10
            final_num = final_num + (last_num *(10**(count-count_abs)))
            count_abs += 1
            copy_num //= 10
        
        if is_negetive:
            final_num = -final_num
        if final_num>= (2**31)-1 or final_num<=(-2**31):
            return 0
        return final_num

        
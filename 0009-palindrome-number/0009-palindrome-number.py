class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        rev_num = 0
        copy_num = x
        while copy_num > 0:
            rev_num = (rev_num*10) + (copy_num%10)
            copy_num //= 10
        if x != rev_num:
            return False
        return True
        
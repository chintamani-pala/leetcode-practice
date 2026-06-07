class Solution:
    def passwordStrength(self, password: str) -> int:
        password = "".join(list(set(password)))
        ans = 0
        for ch in password:
            hasLowerCase = ch.islower()
            hasUpperCase = ch.isupper() 
            hasNumericCase = ch.isnumeric() 
            hasSpecialChar = ch  in "!@#$"
            if hasLowerCase:
                ans += 1
            if hasUpperCase:
                ans += 2
            if hasNumericCase:
                ans += 3
            if hasSpecialChar:
                ans+=5

        return ans
            
        
import math
class Solution(object):
    def internalAngles(self, sides):
        """
        :type sides: List[int]
        :rtype: List[float]
        """
        a,b,c = sides
        if not (a+b > c and a+c > b and b+c > a):
            return []
        # angle A = cos⁻¹((b² + c² - a²) / (2bc))
        # angle B = cos⁻¹((a² + c² - b²) / (2ac))
        # angle C = cos⁻¹((a² + b² - c²) / (2ab))
        angleA = math.degrees(math.acos(float(b*b + c*c - a*a) / (2.0*b*c)))
        angleB =math.degrees(math.acos(float(a*a + c*c - b*b) / (2.0*a*c)))
        angleC = math.degrees(math.acos(float(a*a + b*b - c*c) / (2.0*a*b)))
        return sorted([angleA, angleB, angleC])
class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        five = 0
        ten = 0
        change = True
        
        for bill in bills:
            if bill == 5:
                five += 1
            elif bill == 10:
                if five > 0:
                    ten += 1
                    five -= 1
                else:
                    change = False
                    return False

            else:
                if ten > 0 and five > 0:
                    ten -= 1
                    five -= 1
                elif ten == 0 and five >= 3:
                    five -= 3
                else:
                    change = False
                    return False

        return change

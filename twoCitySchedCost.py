class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        res = 0
        a = 0
        b = 0
        n = len(costs)//2

        costs = sorted(costs, key=lambda x: abs(x[0]-x[1]), reverse=True)

        print(costs)
        

        for cost in costs:
            mini = min(cost)
            if a < n and b < n:
                if mini == cost[0] :
                    res += cost[0]
                    a += 1
                else:
                    res += cost[1]
                    b += 1
            elif a == n:
                b += 1
                res += cost[1]
            else:
                a += 1
                res += cost[0]
 
        return res
            
                

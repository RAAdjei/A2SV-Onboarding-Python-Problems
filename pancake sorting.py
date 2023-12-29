class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        res = []
        def flip(idx):
            left = 0
            while left < idx:
                arr[left], arr[idx] = arr[idx], arr[left]
                left +=1
                idx -= 1

        for i in range(len(arr)-1, 0, -1):
            for j in range(1, i+1):
                if arr[j] == i+1:
                    flip(j)
                    res.append(j+1)
                    break
                
            flip(i)
            res.append(i+1)

        return res


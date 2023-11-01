class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        nums = [num for num in range(1, n+1)]
        combos = []

        def backtracking(i, combo):
            if len(combo) == k:
                combos.append(combo[:])
                return

            if i >= n:
                return
            combo.append(nums[i])
            backtracking(i+1, combo)
            combo.pop()

            backtracking(i+1, combo)
        
        backtracking(0, [])
        return combos



        # def is_valid_state(state):
        #     if state not in self.state:
        #         return True

        # def get_candidates(state):
        #     for i in range(n):
        #         cand = []
        #         cand.append(i)
        #     return[]

        # def search(state, solutions):
        #     if is_valid_state(state):
        #         solutions.append(state.copy())

        #     for candidiate in get_candidates(state):
        #         state.add(candidate)
        #         search(state, solutions)
        #         state.remove(candidate)
        
        # def solve():
        #     solutions = []
        #     state = set{}
        #     search(state, solutions)
        

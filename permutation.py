class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        def is_valid_state(state):
            if len(state) == len(nums):     
                return True
            return False
            
        def get_candidates(state):
            return [i for i in nums if i not in state]

        def search(state, solutions):
            if is_valid_state(state):
                solutions.append(state.copy())
                # return

            for candidate in get_candidates(state):
                state.append(candidate)
                search(state, solutions)
                state.remove(candidate)

        def solve():
            solutions = []
            state = []
            search(state, solutions)
            return solutions
        return solve()

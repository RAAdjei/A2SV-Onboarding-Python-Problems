class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        queue = deque()
        incoming = defaultdict(int)
        adj = defaultdict(list)

        output = []

        for supply in supplies:
            incoming[supply] = 0


        for recipe in recipes:
            incoming[recipe] = 0

        for recipe in range(len(recipes)):
            for ingredient in ingredients[recipe]:
                adj[ingredient].append(recipes[recipe])
                incoming[recipes[recipe]] += 1

        for num in incoming:
            if incoming[num] == 0:
                queue.append(num)

        while queue:
            curr = queue.popleft()

            if curr not in supplies:
                output.append(curr)

            for nei in adj[curr]:
                incoming[nei] -= 1

                if incoming[nei] == 0:
                    queue.append(nei)

        return output


        

        print(adj)
         

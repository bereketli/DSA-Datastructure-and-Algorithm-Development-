from collections import defaultdict, deque
class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        
        que = deque()
        graph = defaultdict(list)
        indegree = defaultdict(int)
        possible_recipes = []

        #build the grapha and count indegree
        for recipe, pack in zip(recipes, ingredients):
           
            for ingredient in pack:
                graph[ingredient].append(recipe)
                indegree[recipe] += 1

        # search for indepent ingredients
        que.extend(supplies)
      
        
        while que:
            recipe = que.popleft()
            if recipe in recipes:
                possible_recipes.append(recipe)
            for child in graph[recipe]:
                indegree[child] -= 1
                if not indegree[child]:
                    que.append(child)
        
        return possible_recipes

        





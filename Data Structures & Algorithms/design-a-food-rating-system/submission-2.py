import heapq
class FoodRatings:
    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.mp = {}           # cuisine -> heap
        self.foodCuisine = {}  # food -> cuisine
        self.foodRating = {} 
        for i in range(len(foods)):
            self.mp.setdefault(cuisines[i], [])
            heapq.heappush(self.mp[cuisines[i]], (-ratings[i], foods[i]))
            self.foodCuisine[foods[i]]=cuisines[i]
            self.foodRating[foods[i]]=ratings[i]
    def changeRating(self, food: str, newRating: int) -> None:
        heapq.heappush(self.mp[self.foodCuisine[food]], (-newRating, food))
        self.foodRating[food] = newRating
    def highestRated(self, cuisine: str) -> str:
         while self.mp[cuisine]:
            rating, food = self.mp[cuisine][0]

            if -rating != self.foodRating[food]:
                heapq.heappop(self.mp[cuisine])
            else:
                return food

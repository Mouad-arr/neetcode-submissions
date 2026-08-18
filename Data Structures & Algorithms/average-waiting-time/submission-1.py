class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        time =0
        total_waiting =0
        for customer in customers :
            if time <= customer[0]:
                time = customer[1]+customer[0]
                total_waiting += customer[1]
            else :
                total_waiting += customer[1]
                total_waiting += time - customer[0]
                time += customer[1]
        return total_waiting / len(customers)
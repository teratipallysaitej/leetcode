
class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        total_satisfied = sum(customers[i] for i in range(len(customers)) if not grumpy[i])
        additional_satisfied = 0
        max_additional_satisfied = 0        
        for i in range(minutes):
            if grumpy[i]:
                additional_satisfied += customers[i]
        
        max_additional_satisfied = additional_satisfied
        
        for i in range(minutes, len(customers)):
            if grumpy[i]:
                additional_satisfied += customers[i]
            if grumpy[i - minutes]:
                additional_satisfied -= customers[i - minutes]
            max_additional_satisfied = max(max_additional_satisfied, additional_satisfied)
        
        return total_satisfied + max_additional_satisfied

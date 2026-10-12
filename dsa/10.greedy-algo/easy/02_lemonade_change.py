# You are selling lemonade at a stand where each glass costs exactly $5. Customers are standing in a queue to buy from you, and order one at a time. Each customer will only buy one lemonade and pay with either a $5, $10, or $20 bill.

# You must provide the correct change to each customer so that the net transaction is exactly $5. You start with no money in your cash register. Return true if you can provide every customer with correct change, or false if you cannot.

# Example 1
# Input: bills = [5, 5, 5, 10, 20]

# Output: true

# Explanation: Customer 1, 2, and 3 give $5. You now have three $5 bills.

# Customer 4 gives $10. You give one $5 in change. You now have two $5 bills and one $10 bill.

# Customer 5 gives $20. You give one $10 and one $5 in change. You successfully served everyone.


class Solution:
    def lemonadeChange(self, bills: list[int]) -> bool:
        fives, tens = 0,0
        n = len(bills)
        for i in range(0,n):
            if bills[i] == 5:
                fives +=1
            elif bills[i] == 10:
                if fives == 0:
                    return False
                tens += 1
                fives -=1   
            else :
                if (tens >0 and fives > 0):
                    tens -= 1
                    fives -= 1
                elif fives >= 3:
                    fives -=3
                
                else :
                    return False
        return True

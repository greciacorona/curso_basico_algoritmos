# Coin Change Problem
def coins(amount):
    result = []    
    i = len(denominations) - 1
    
    while (i >= 0):
        while (amount >= denominations[i]):
            amount = amount - denominations[i]
            result.append(denominations[i])
        i -= 1    
    
    for coin in result:
	    print(coin)



if __name__ == "__main__":
    denominations = [1, 2, 5, 10]
    amount = 44
    coins(amount)




# Recursive example of trying to get the least amount of coins to make up an amount of change.

# def recMC_greedy(coinValueList,change):
#   if change == 0:  #base case if, change is 0, then the number of coins have been finalized
#     return 0
#   else:
#     cur_max = max(coinValueList) #use the maximum in the list to see how many of these can be used to form the sum
#     count = change//cur_max #find how many of the max is needed to make the change so that the number of coins used is minimum
#     index = coinValueList.index(cur_max)
#     print(f'${coinValueList[index]} = {count} coins')
#     del coinValueList[index]   #erasing the current max so that a different max can be
#                                #used in next recursion and continue the greedy process
#     return count + recMC_greedy(coinValueList, change-cur_max * count) #returns the counts of the coins using recursion

# def main():
#   recMC_greedy([1, 2, 5, 10], 44)#using the greedy algorithm for the edge case 44 
#                                          #but greedy algorithm is not the most optimum solution
# main()

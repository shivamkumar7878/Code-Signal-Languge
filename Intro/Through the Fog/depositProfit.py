def depositProfit(deposit, rate, threshold):
    amount=deposit
    counter=0
    while amount<threshold:
        print(amount, counter)
        ir = amount*rate/100
        amount+=ir
        counter+=1
    return counter

import time


def sum_of_n_2(n):
    start = time.time()
    the_sum = 0
    for i in range(1, n +1):
        the_sum = the_sum + i
        end = time.time()


    return the_sum, end - start

def sum_of_n(n):
    n, n*(n+1)/2


def find_card(cards, number):
	current_position = 0
    
    while current_position < len(cards):
    	if cards[current_position] == number:
        	return current_position
        current_position += 1
        
        if current_position == len(cards) - 1:
        	return "Not Found"
            
cards = [24, 19, 13, 10, 7, 5, 2]
number = 10
result = find_card(cards, number)
print(result)

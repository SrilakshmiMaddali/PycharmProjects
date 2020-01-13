"""
card_deck = [4, 11, 8, 5, 13, 2, 8, 10]
hand = []

while sum(hand)<=17:
    hand.append(card_deck.pop())

print(hand)


start_num =  1#provide some start number
end_num = 15#provide some end number that you stop when you hit
count_by = 1#provide some number to count by

# write a while loop that uses break_num as the ongoing number to
#   check against end_num
break
_num=0
while break_num<=end_num:
    break_num+=start_num
    start_num+=count_by


print(break_num)

"""

num_list = [422, 136, 524, 85, 96, 719, 85, 92, 10, 17, 312, 542, 87, 23, 86, 191, 116, 35, 173, 45, 149, 59, 84, 69, 113, 166]

num_len = len(num_list)
odd_count=0
index=0
sum_odd=0
while (odd_count<5) and (index<num_len):
    if num_list[index]%2 !=0:
        sum_odd+=num_list[index]
        odd_count+=1
    index+=1

print(sum_odd)
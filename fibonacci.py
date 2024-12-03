'''Author:Thomas Cherian
   date: 3-12-24
   python program:To create a fibonacci function'''
def fibonacci(n):
    sequence =[]
    first_num, second_num = 0,1
    for i in range(n):
        sequence.append(first_num)
        first_num,second_num=second_num,first_num+second_num
    return sequence

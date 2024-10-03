"""
Программа для подсчёта хз чего, каких-то рандомных цифр
"""
def calculate_average(nums):
    '''
    Считаем копейки
    '''
    total = sum(nums)
    count = len(nums)
    average = total / count
    return average

NUMS = [10, 15, 20]
result = calculate_average(NUMS)
print("The average is:", result)

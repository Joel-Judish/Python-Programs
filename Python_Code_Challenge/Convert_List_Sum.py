def convert_add(num_list):
    list1 = []
    total_sum = 0
    
    for i in num_list:
        list1.append(int(i))
        total_sum += int(i)
    
    print("List after conversion to integer:", list1)
    print("Sum of List:", total_sum)

numbers = list(map(int, input("Enter numbers separated by space: ").split()))
convert_add(numbers)

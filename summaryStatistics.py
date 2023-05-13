def my_function():
    # Code for your function goes here
    print("Hello, world!")


def find_mean(list):
    # take an array and return the mean
    sum = 0
    for i in list:
        sum += i
    return sum / len(list)


def find_median(list):
    # take an array and return the median
    index = len(list) // 2
    sorted_list = sorted(list)
    if len(list) % 2 == 1:
        return float(sorted_list[index])
    else:
        return float(find_mean(sorted_list[index-1]+sorted_list[index]))


def find_min(list):
    # take an array and return the minimum
    minimum = list[0]
    for i in list:
        if i < minimum:
            minimum = i
    return minimum


def find_max(list):
    # take an array and return the maximum
    maximum = list[0]
    for i in list:
        if i > maximum:
            maximum = i
    return maximum


def main():
    # Code for your main function goes here
    user_input = input(
        "Enter an array of integers separated by commas and/or spaces: ")
    user_input = user_input.replace(", ", " ")
    int_array = [int(num) for num in user_input.split()]
    print(find_mean(int_array))
    print(find_median(int_array))
    print(find_min(int_array))
    print(find_max(int_array))

    # my_function()  # Call the function


if __name__ == '__main__':
    main()

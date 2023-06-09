def my_function():
    print("Hello, world!")


def find_mean(list):
    # take an array and return the mean
    sum = 0
    for i in list:
        sum += i
    return '{:.2f}'.format(sum / len(list))


def find_median(list):
    # take an array and return the median
    index = len(list) // 2
    sorted_list = sorted(list)
    if len(list) % 2 == 1:
        return '{:.2f}'.format(float(sorted_list[index]))
    else:
        return '{:.2f}'.format(float(find_mean([sorted_list[index-1], sorted_list[index]])))


def find_mode(array):
    # take an array and return the most frequently occuring element
    frequency = {}
    for i in array:
        if i in frequency:
            frequency[i] += 1
        else:
            frequency[i] = 1

    max_frequency = find_max(list(frequency.values()))
    mode = [key for key, value in frequency.items() if value == max_frequency]
    return int(mode[0])

def find_bucketed_mode(array):
    # take an array and return the most frequently occuring multiple of 10
    frequency = {}
    for i in array:
        if i // 10 * 10 in frequency:
            frequency[i // 10 * 10] += 1
        else:
            frequency[i // 10 * 10] = 1

    max_frequency = find_max(list(frequency.values()))
    mode = [key for key, value in frequency.items() if value == max_frequency]
    return int(mode[0])


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
    print("Mean\t", find_mean(int_array))
    print("Median\t", find_median(int_array))
    print("Mode\t", find_mode(int_array))
    print("Minimum\t", find_min(int_array))
    print("Maximum\t", find_max(int_array))

    # my_function()  # Call the function


if __name__ == '__main__':
    main()

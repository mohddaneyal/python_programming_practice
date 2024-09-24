def find_pairs_of_numbers(num_list, n):
    count = 0
    # Set to track the visited numbers
    visited = set()

    # Iterate through the list to find pairs
    for num in num_list:
        # Check if the complement (n - num) exists in the visited set
        complement = n - num
        if complement in visited:
            count += 1
        # Add the current number to the visited set
        visited.add(num)

    return count

# Example usage:
num_list1 = [1, 2, 7, 4, 5, 6, 0, 3]
n1 = 6
print(find_pairs_of_numbers(num_list1, n1))  # Expected output: 3

num_list2 = [3, 4, 1, 8, 5, 9, 0, 6]
n2 = 9
print(find_pairs_of_numbers(num_list2, n2))  # Expected output: 4

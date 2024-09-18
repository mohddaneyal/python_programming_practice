# def solve_puzzle(heads, legs):
#     # Check for invalid input
#     if heads <= 0 or legs <= 0:
#         print("No solution")
#         return
#
#     # Let chickens = c, rabbits = r
#     # Total heads: c + r = heads
#     # Total legs: 2c + 4r = legs
#
#     # Solve for the number of rabbits and chickens
#     for rabbits in range(heads + 1):
#         chickens = heads - rabbits
#         #print(rabbits, chickens)
#         if (2 * chickens + 4 * rabbits) == legs:
#             print(chickens, rabbits)
#             return
#
#     # If no valid solution is found
#     print("No solution")
#
#
# # Example usage with the sample input and expected output:
# solve_puzzle(150, 400)  # Expected output: 100 50
# solve_puzzle(3, 11)  # Expected output: No solution
# solve_puzzle(3, 12)  # Expected output: 0 3
# solve_puzzle(5, 10)  # Expected output: 5 0

def solve_puzzle(heads, legs):
    # Check for invalid inputs where a solution is impossible
    if legs % 2 != 0 or heads <= 0 or legs <= 0 or legs < 2 * heads or legs > 4 * heads:
        print("No solution")
        return

    # Calculate number of rabbits (R) using the derived formula
    rabbits = (legs - 2 * heads) // 2
    chickens = heads - rabbits

    # Check if the calculated numbers are valid
    if rabbits >= 0 and chickens >= 0:
        print(chickens, rabbits)
    else:
        print("No solution")


# Example usage
solve_puzzle(150, 400)  # Expected output: 100 50
solve_puzzle(3, 11)  # Expected output: No solution
solve_puzzle(3, 12)  # Expected output: 0 3
solve_puzzle(5, 10)  # Expected output: 5 0


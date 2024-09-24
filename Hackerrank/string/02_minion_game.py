# URL: https://www.hackerrank.com/challenges/the-minion-game/problem?isFullScreen=true
def minion_game(string):
    # Length of the input string
    n = len(string)

    # Scores for Kevin and Stuart
    kevin_score = 0
    stuart_score = 0

    # Iterate through each character in the string
    for i in range(n):
        # If the character is a vowel, add points to Kevin's score
        if string[i] in 'AEIOU':
            kevin_score += n - i
        else:  # Otherwise, add points to Stuart's score
            stuart_score += n - i

    # Determine the winner
    if kevin_score > stuart_score:
        print(f"Kevin {kevin_score}")
    elif stuart_score > kevin_score:
        print(f"Stuart {stuart_score}")
    else:
        print("Draw")


if __name__ == '__main__':
    minion_game("BANANA")

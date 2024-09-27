# URL : https://www.hackerrank.com/challenges/merge-the-tools/problem?isFullScreen=true
def merge_the_tools(s, k):
    # Iterate over the string in steps of k
    for i in range(0, len(s), k):
        # Get the current substring
        substring = s[i:i + k]
        #print(substring)
        #print(dict.fromkeys(substring))
        print(''.join(dict.fromkeys(substring)))

        # Join and print the result for this substring
        #print(''.join(result))


if __name__ == '__main__':
    merge_the_tools("AABCAAADA", 3)
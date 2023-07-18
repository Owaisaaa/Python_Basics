# Read n and the scores from STDIN
n = int(input())
scores = list(map(int, input().split()))

# Sort the scores in descending order
scores.sort(reverse=True)

# Find the second highest score
runner_up = -1
for score in scores:
    if score < scores[0]:
        runner_up = score
        #print(runner_up)
        break

# Print the result
print(runner_up)

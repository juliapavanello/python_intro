from collections import defaultdict

m = int(input())
user_words = defaultdict(set)
total_counts = defaultdict(int)

for _ in range(m):
    parts = input().split()
    user = parts[0]
    words = parts[1:]
    for w in words:
        total_counts[w] += 1
        user_words[user].add(w)

num_users = len(user_words)
word_user_count = defaultdict(int)
for s in user_words.values():
    for w in s:
        word_user_count[w] += 1

res = [w for w, c in word_user_count.items() if c == num_users]
if not res:
    print("ALL CLEAR")
else:
    res.sort(key=lambda w: (-total_counts[w], w))
    for w in res:
        print(w)

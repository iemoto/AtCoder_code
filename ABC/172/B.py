first_str = list(input())
anwser_str = list(input())
cnt = 0
for i in range(len(first_str)):
    if first_str[i] != anwser_str[i]:
        first_str[i] = anwser_str[i]
        cnt += 1
print(cnt)
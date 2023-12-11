text = input()
reversed_text = list(text)
reversed_text.reverse()
for i in reversed_text:
    if i != " ":
        print(i)

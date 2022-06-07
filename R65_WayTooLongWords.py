testCases = int(input());
for i in range(0, testCases):
    word = input();
    if len(word) > 10:
        print(word[0] + str(len(word[1:-1])) + word[-1]);
    else:
        print(word);
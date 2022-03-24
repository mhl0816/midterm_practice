s = "https://stackoverflow.com/questions/28522152/how-to-multiply-decimals-in-python and there could be https://towardsdatascience.com/how-to-create-user-defined-functions-in-python-e5a529386534"
start = 0
while True:
    start = s.find("h", start)
    if start == -1:
        break
    end = s.find(" ", start)
    if end == -1:
        print(s[start:])
        break
    print(s[start:end])
    start = end

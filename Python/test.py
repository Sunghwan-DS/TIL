class Test:
    def __init__(self):
        self.data = 0
        self.no = 0


test = Test()

for word in ('data', 'no'):
    if word == 'data':
        test.data += 1
    elif word == 'no':
        test.no += 1

print(test.data)
print(test.no)
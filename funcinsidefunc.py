def display(name):
    def message():
        return "hello"
    result = message()+name
    return result
b = display("kiran")
a=''.join(b)
print(a)
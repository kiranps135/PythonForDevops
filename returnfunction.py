def display(name):
    def message():
        return "hello"
    return message()+name

fun=display("kiran")
print(fun)
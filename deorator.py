from datetime import datetime
def time(func):
    def wrapper():
        start = datetime.now()
        func()
        end = datetime.now() - start
        print(end)
    return wrapper
@time
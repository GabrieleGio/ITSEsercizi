import time
def get_time(func):

    def wrapper(*args):
        start = time.time()
        func(*args)
        end = time.time()
        elapsed_time = end - start
        print(f"{elapsed_time=}")
    
    return wrapper



def say_hello(name: str) -> None:
    print(f"Hello, {name}")

say_hello = get_time(say_hello)

say_hello("Flavio")

def say_ciao(name: str) -> None:
    print(f"Ciao, {name}")

say_ciao = get_time(say_ciao)

say_ciao("Flavio")

# def saluta(func):
#     func("Flavio")

# saluta(say_hello)

# def parent():
    
#     print(f"Sono in parent")

#     def first_child():
#         print(f"Sono in first child")

#     def second_child():
#         print(f"Sono in second child")

#     first_child()
#     second_child()

#     return second_child


# out_function = parent()
# print(out_function)
# out_function()



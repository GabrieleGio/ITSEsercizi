#Apro il file e lo chiudo
# reader = open("esempiofile.txt")
# print(reader)

# try:
#     reader.readline()
#     print("Sono nella try")
#     raise Exception("Eccezione")

# except Exception:
#     print("Sono nella except")

# finally:
#     print(reader)

#     reader.close()

#     print("Sono nella finally")

#Apro di nuovo il file
# with open("esempiofile.txt") as reader:
#     line = reader.readline()
#     line_counter = 0

#     while line != '':
#         print(f"{line} - number: {line_counter}")
#         line = reader.readline()
#         line_counter += 1

with open("esempiofile.txt", "w") as reader:
    l = [f"Ciao sono Giuseppe\n", f"Ciao sono Marco\n",f"Ciao sono Luca\n"]
    reader.writelines(l)
    

# class ContextManager:
#     def __enter__(self):

#         print("Ciao sono nell'enter")

#         return self
    
#     def __exit__(self, exc_type, exc_value, traceback):

#         if exc_type is not None:

#             print("Eccezione")

#         return False
    

# try:
#     with ContextManager() as cm:

#         print("Ciao")
#         print(cm)

# except Exception:

#         print()
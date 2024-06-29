import time
import random

def chatbot1():
    print("type `exit` to exit")
    print("Chat : Hello, how can I assist you to day?")
    while True:
        i = input("You  : ")
        if i == "exit":
            print("Chat : See you later")
            time.sleep(1)
            break
        rd = random.randrange(3)
        if rd == 0:
            print("error")
        if rd == 1:
            print("umm.. IDK")
        if rd == 2:
            print("idk, I don't understand, please ask another question")
        if rd == 3:
            print("error")

chatbot1()
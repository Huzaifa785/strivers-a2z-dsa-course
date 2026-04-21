counter = 0
def func():
    global counter
    if (counter == 2):
        return
    print(counter)
    counter+=1
    func()
    
if __name__ == "__main__":
    func()
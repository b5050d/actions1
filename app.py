import time

class MyApp():
    def __init__(self):
        self.myString = "Hello"
        self.timeout = 10

    def fakeMethod(self, iter):
        return "Our current iteration = {}".format(iter)


    def mainloop(self):
        print("Initiating Mainloop")
        iter = 0
        start_time = time.time()
        timeout = start_time + self.timeout
        while time.time()<timeout:
            print(self.fakeMethod(iter))
            iter+=1
            time.sleep(.5)
        
        print("Ending Mainloop")
    
        

if __name__=="__main__":
    a = MyApp()
    a.mainloop()
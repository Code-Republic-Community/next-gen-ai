from threading import Thread
 
s = 'This is the text!'
 
first_thread_index = 0
second_thread_index = 1
 
 
class First(Thread):
 
    def __init__(self, name):
        Thread.__init__(self)
        self.name = name
 
    def run(self):
 
        global first_thread_index
 
        while first_thread_index < len(s):
            print(self.name + ' - ' + s[first_thread_index])
            first_thread_index += 2
 
 
class Second(Thread):
 
    def __init__(self, name):
        Thread.__init__(self)
        self.name = name
 
    def run(self):
        global second_thread_index
 
        while second_thread_index < len(s):
            print(self.name + ' - ' + s[second_thread_index])
            second_thread_index += 2
 
 
first = First('Thread #1')
second = Second('Thread #2')
 
first.start()
second.start()
 
first.join()
second.join()

import time

class Timer:
    def __init__(self):
        self.start_time= None
        self.end_time = None

    def start(self):
        self.start_time = time.time()
        print("Timer is started")

    def end(self):
        if self.start_time is None:
            print("Timer was not started !")
        else:    
            self.end_time = time.time()
            execute_timer = self.start_time - self.end_time
            print(f"Timer stopped! The timer is : {execute_timer:.3f} seconds ")

    def reset(self):
        self.start_time = None
        self.end_time = None
        print("Timer rest.")
    
    @staticmethod # is it a decorater 
    def time_function(func, *args, **kwargs):

        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(
            f"Function'{func.__name__}' executed in {end - start:.4f} seconds.'")
        return result

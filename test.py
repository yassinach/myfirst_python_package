from simpletimer import Timer

timer = Timer()
#Test 1
timer.start()
for i in range(10**6):
    pass
timer.stop()

#Test 2
timer.reset()

#Test 3
def sample_func(x):
    total = 0
    for i in range(x):
        total += i
    return total

Timer.time_function(sample_func,10**6)
    
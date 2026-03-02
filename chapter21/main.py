# from timer0 import timer

# time = timer(pow,2,1000)
# print(time)
# print(min(tup for tup in [(2.0, 3), (3.0, 3), (1.0, 3), (0.0, 3), (4.0, 3)]))
import timer 

reps, text = 100_000, 'hack' * 100
print(timer.once(pow,2,1000)[0])
print(timer.once(str.upper,text))
print(timer.total(reps,pow,2,1000)[0])
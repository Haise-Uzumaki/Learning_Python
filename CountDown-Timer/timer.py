import time

my_time = int(input("For How Long You Need To Set The Timer For(seconds): "))


for x in range(my_time, 0 , -1): 
    seconds = x % 60
    minutes = int(x / 60) % 60
    hours = int(x / 3600)
    print(f"{hours:02}:{minutes:02}:{seconds:02}")
    time.sleep(1)
    
#You Can Reverse The CountDown By Doing This =>
# for x in reversed(range(0,my_time))
#for normal one's
# for x in range(0, my_time)
    
print("Time's UP!!!!")
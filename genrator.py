import time
def genrator_time(in_minute):
    total_second = in_minute*60
    for second in range(total_second+1):
        min = second //60
        sec = second %60
        yield f"{min:02}:{sec:02}"
       
for i in genrator_time(3):
    print(i)
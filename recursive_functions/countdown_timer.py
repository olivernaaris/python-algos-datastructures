import time


def recur_countdown_timer(n):
    # Base case for recursive function
    if n == 0:
        return n
    else:
        print(n)
        time.sleep(1)
        return recur_countdown_timer(n-1)


z = 5
print(recur_countdown_timer(z))
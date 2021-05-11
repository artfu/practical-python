# bounce.py
#
# Exercise 1.5
height = 100
bounce_time = 0
while bounce_time < 10:
    height = round(height * 3/5, 4)
    bounce_time = bounce_time + 1
    print(bounce_time, height)

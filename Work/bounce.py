# bounce.py
#
# Exercise 1.5

height = 100 #starting height of bouncing ball = 100m
bounce = 0

while bounce < 10:
    height = (3/5)*height
    bounce = bounce + 1
    print(bounce, round(height,4))



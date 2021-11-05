#Problem Statement : You are painting a wall. The instructions on the paint can says that **1 can of paint can cover 5 square meters** of wall. Given a random height and width of wall, calculate how many cans of paint you'll need to buy?
import math
test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
def paint_calc(height, width, cover):
  #math.ceil function is used for rounding of ceiling problems. We have not used round function because if the Cans = 18.2 and since it is less than 18.5 the round function will round it to 18 cans which will result in wrong result so to round it to next integer irrespective of 0.5, we directly import math and use math.ceil(formula) to get next rounded value.
  Cans = math.ceil(height * width / cover)
  print(f"Number of Cans required are {Cans}")

paint_calc(height=test_h, width=test_w, cover=coverage)



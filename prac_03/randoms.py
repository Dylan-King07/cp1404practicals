# What did you see on line 1?
# Line 1 printed a random integer between 5 and 20.
# When the command was executed, the random integer produced was 10.


# What was the smallest number you could have seen, what was the largest?
# The range set was between 5 and 20. Therefore, the smallest possible number is 5, and the largest is 20.


# What did you see on line 2?
# Line 2 has a range of 3 to 10, counting every 2 integers.
# This produces the sequence 3, 5, 7, 9. A random integer was then printed from this sequence.
# When executed, the random value produced was 7.


# What was the smallest number you could have seen, what was the largest?
# The smallest integer possible is 3.
# As the command prints a random integer from the aforementioned sequence, the largest possible integer is 9.


# Could line 2 have produced a 4?
# No, because line 2 counts up 2 integers at a time, starting at 3. Therefore, 4 is skipped and 5 is counted.


# What did you see on line 3?
# Line 3 produced a random floating point between 2.5 and 5.5.
# When executed, the random floating point produced was 5.449997908420073.


# What was the smallest number you could have seen, what was the largest?
# The smallest possible number is 2.5. The largest possible number is 5.5.


# Write code, not a comment, to produce a random number between 1 and 100 inclusive.
import random
print(random.randint(1, 100))


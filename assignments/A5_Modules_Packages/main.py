
# ---- Task 1 Module Import ----
import task1_math_utils
from task1_math_utils import square

print("Addition:", task1_math_utils.add(10, 5))
print("Subtraction:", task1_math_utils.subtract(10, 5))
print("Square:", square(4))


# ---- Task 2 Module Import ----
import task2_string_utils

text = "python is very easy"

print("Capitalized:", task2_string_utils.capitalize_words(text))
print("Reversed:", task2_string_utils.reverse_string(text))
print("Word Count:", task2_string_utils.word_count(text))


# ---- Task 3 Package Import ----
import task3_shop_package.task3_discount as disc
from task3_shop_package.task3_billing import calculate_total
from task3_shop_package import apply_tax

print("Discounted Price:", disc.apply_discount(1000, 10))
print("Flat Discount:", disc.flat_discount(500))
print("Total Bill:", calculate_total([100, 200, 300]))
print("Bill with Tax:", apply_tax(1000))

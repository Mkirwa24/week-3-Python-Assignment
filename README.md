# week-3-Python-Assignment
Create a function named calculate_discount(price, discount_percent) that calculates the final price after applying a discount. The function should take the original price (price) and the discount percentage (discount_percent) as parameters. If the discount is 20% or higher, apply the discount; otherwise, return the original price.
Using the calculate_discount function, prompt the user to enter the original price of an item and the discount percentage. Print the final price after applying the discount, or if no discount was applied, print the original price.

## To run the python file one needs to open a new terminal, navigate to the folder where the python project file has been saved using the cd command then type:

* python discount_calculator.py


## Explanation:
1. Function Definition:

* The calculate_discount function takes two arguments: price (float) and discount_percent (float).
* If discount_percent is 20 or more, it calculates the discount amount and subtracts it from the price.
* Otherwise, it simply returns the original price.

2. User Interaction:

* The program prompts the user to input the original price and the discount percentage.
* Inputs are converted to float to handle decimal values.

3. Validation:

* A try-except block ensures that invalid inputs (e.g., strings) are caught, and an appropriate error message is displayed.

4. Output:

* Displays the final price if the discount is applied.
* If the discount is less than 20%, informs the user that no discount was applied.

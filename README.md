# Python-Lab 4

#### Try and Except

Write a program that do the following :-
1. Ask the user to enter his name.
2. Ask the user to enter his age.
3. If his age is between 0 and 6, then print "Kid"
4. Else if his age is under 0, then print "Wrong age value, you can not enter value 0 or less."
5. Else if the age is greater than 6, do the following :-
    - An empty variable called total_cost with initial value 0.
    - Ask him to enter the number of items that he wants to buy.
    - for each item, do the following :-
        - Ask him to enter the item name.
        - Ask him to enter the item price.
        - Ask him to enter the item quantity.
        - You need to calculate the item total cost by multiplying the quantity by the price and name it as item_cost.
        - Then, you need to update the total_cost variable by adding the value of item_cost.
        - Print the item_cost and the total_cost.
    - Now, if the total_cost is greater than 200, make a discount by 20% for this special customer!!
6. Do not forget to handle any unexpected inputs from the users (Just cast the input values and catch the errors!!).
7. Finally, ask the user if he want to repeat the same process from step 1 until 6 or not, Use the loops, but one of them ;)
    - Note : The ask is after catching the errors.

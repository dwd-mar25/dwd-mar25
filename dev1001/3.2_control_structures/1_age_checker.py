# --- USE: Age Checker ---

# --- MODIFY ---
# 1. Change the required_age to 21. Test with user_age as 20 and 22.
# 2. Inside the else block, add another
#       print statement: Please try again when you are older.
# 3. What if there was no else block? Comment out the else block and its contents.
#       What happens if user_age is 15 now? What about can_proceed?

user_age = 15 # Try changing this to 15, 18
required_age = 21
can_proceed = False

print(f"User's age: {user_age}, Required age: {required_age}")

# >= is a comparison operator, which evaluates to bool
# Other comparison ops: >, <, <=, == (equality), != (not equal)
# Equality has to be '==' because '=' is assignment 
# if statement - checks the boolean condition, and executes the block if true
if user_age >= required_age:
    # In Python, indenting defines where a block begins and ends
    print("Access granted. You meet the age requirement.")
    can_proceed = True
else: # else is optional
    print("Access denied. You do not meet the age requirement.")
    can_proceed = False

print(f"Can proceed with activity? {can_proceed}")

# --- USE: Ternary Operator ---

# --- MODIFY ---
# 1. Rewrite the ternary assignment for category using a traditional
#       if-else block to demonstrate equivalence.
#       Then, change the condition in the ternary operator:
#       if age < 13, category is "Child", else it's "Teen or Adult".

age = 5
# Ternary flow
# 1. Python evaluates the boolean expression between 'if' and 'else'
# 2. If true, the whole ternary expression evaluates to whatever is on the left of the 'if'
# 3. Otherwise, it evaluates to whatever is to the right of the 'else'
# 4. In this case, the result of the ternary is being stored in a variable
# The ternary is '"Adult" if age >= 18 else "Minor"'
category = "Child" if age < 13 else "Teen or Adult" # The ternary expression
# if age >= 18:
#     category = "Adult"
# else:
#     category = "Minor"

print(f"Age: {age}, Category: {category}")
# print("Adult" if age >= 18 else "Minor")

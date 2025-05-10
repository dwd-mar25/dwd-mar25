# --- USE: match-case Statement ---

# --- MODIFY ---
# 1. Add a new case for http_status_code 301 that sets status_meaning to
#       "Moved Permanently - Resource has a new URL."
# 2. How could you make case 200 and case 201 (Created) both lead to a
#       similar "Success" message, perhaps by setting a common variable or
#       using |? (e.g., case 200 | 201: status_type = "Success")

http_status_code = 201 # Try 200, 500, 999
status_meaning = ""

# if http_status_code == 200:
#   status_meaning = "OK"
# elif http_status_code == 403:
#   status_meaning = "Forbidden"
# ...
match http_status_code:
    case 200 | 201: # 200 or 201
        status_meaning = "OK - Request successful."
    case 403:
        status_meaning = "Forbidden - You don't have permission."
    case 301:
        status_meaning = "Moved Permanently - Resource has a new URL."
    case 404:
        status_meaning = "Not Found - The resource doesn't exist."
    case 500:
        status_meaning = "Internal Server Error - Something went wrong on our end."
    case _: # Default case (like an 'else' - must be last)
        status_meaning = "Unknown or unhandled status code."

print(f"Status {http_status_code}: {status_meaning}")

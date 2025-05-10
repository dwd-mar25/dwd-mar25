# match-case: Ask the user to input a command (e.g., "start", "stop", "pause").
#   Use match-case to print a different action message for each command
#   (e.g., "Process starting...", "Process stopping...").
#   Include a default for unknown commands."
command = input('Command: ')
# print(command.lower())
# command.lower - match to the method itself (i.e. the code of the method)
# command.lower() - with parentheses - calls the method and matches on the return value
match command.lower:
    case 'start':
        print('Process starting ...')
    case 'stop':
        print('Process stopping ...')
    case 'pause':
        print('Process paused.')
    case _:
        print('Unknown command.')

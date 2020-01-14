####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####

team_name = 'Team 3' # Only 10 chars displayed.
strategy_name = 'mem_bCBBC'
strategy_description = ''
    
def move(my_history, their_history, my_score, their_score):
    if len(my_history) == 0:
        return 'b'
    else:
        if my_history[len(my_history)-1] == 'c':
            if their_history[len(their_history)-1] == 'c':
                return 'c'
            else:
                return 'b'
        elif my_history[len(my_history)-1] == 'b':
            if their_history[len(their_history)-1] == 'c':
                return 'b'
            else:
                return 'c'
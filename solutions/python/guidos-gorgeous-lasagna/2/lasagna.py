EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 2
print(EXPECTED_BAKE_TIME)
def bake_time_remaining(elapsed_bake_time):
    """
    Llogarit kohen qe ka mbetur per pjekje
    """
    remaining_bake_time = EXPECTED_BAKE_TIME - elapsed_bake_time
    return remaining_bake_time

def preparation_time_in_minutes(number_of_layers):
    """
    Llogarit kohen qe merr reni i llazanjes per pregatitje
    """
    return number_of_layers*PREPARATION_TIME

def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """
    Llogarit kohen totale (pregatitje + pjekje deri aty)
    """
    total_elapsed_time = elapsed_bake_time + preparation_time_in_minutes(number_of_layers)
    return total_elapsed_time

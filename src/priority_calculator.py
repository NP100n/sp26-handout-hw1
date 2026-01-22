"""
Functions to calculate housing priority score based given user answers.
"""



def points_for_class_year(year: int) -> int:
    """
    Given an integer `year`, return points based on your scoring system.

    Here, you may assume year is an integer from 1 to 4, since we already 
    validated input in the question asker. 

    Example scoring systems:
    - Linear: Freshman=1, Sophomore=2, Junior=3, Senior=4
    - Exponential: Freshman=2, Sophomore=4, Junior=8, Senior=16
    - Custom: Design your own fair system
    
    Implement logic to calculate points based on class year
    """

    return (16 * year)


def points_for_graduation(is_graduating: bool) -> int:
    """ 
    Return points based on graduation status.

    Typical approach: graduating students get bonus points (e.g., 5),
    non-graduating students get 0. But you can design your own system.
    
    Implement logic for calculating points for a graduating student
    """

    if is_graduating == True:
        return 5
    else:
        return 0

def points_for_credits(num_credits: int) -> int:
    """
    Compute points based on credits earned.

    Example systems:
    - 1 point per credit
    - 0.5 points per credit
    - Tiered system: 0-30 credits = 1pt each, 31+ = 2pts each
    - Maximum cap: up to 50 credits count

    Here, you may assume num_credits is a non-negative integer,
    since we already validated input in the question asker.
    
    Implement points system for credits.
    """
    return num_credits

def points_for_additional_questions(responses: dict[str, bool]) -> int:
    """
    Given the dict from ask_additional_questions(), assign points.

    Example:
    - 'old23': True → 2 points, False → 0 points
    - 'honors': True → 3 points, False → 0 points
    - Total for {'old23': True, 'honors': False} = 2 + 0 = 2 points

    Design your own questions and point values!
    
    Implement scoring logic.
    """
    points = 0
    # {age: num, gpa: num, honors: num}

    if responses["any_academic_violations"] == True:
        points -=15
    if responses["attending_honors_program"] == True:
        points += 15

    return points


def calculate_total_score(
    year: int,
    is_graduating: bool,
    num_credits: int,
    additional_responses: dict[str, bool],
) -> int:
    """
    Calculate the total priority score based on all inputs.

    This method should use all your other methods:
    total = (
        points_for_class_year(year)
        + points_for_graduation(is_graduating)
        + points_for_credits(num_credits)
        + points_for_additional_questions(additional_responses)
    )

    Here, you may assume that the responses dict contains valid keys
    corresponding to the questions you designed in ask_additional_questions().
    
    Args:
        year (int): Class year (1-4)
        is_graduating (bool): Whether student is graduating this semester
        credits (int): Number of credits earned
        additional_responses (dict): Dictionary of additional question responses
    Returns:
        int: Total priority score
        
    Use the other methods you implemented to calculate total score
    """
    total = points_for_class_year(year) + points_for_graduation(is_graduating) + points_for_credits(num_credits) + points_for_additional_questions(additional_responses)
    return total



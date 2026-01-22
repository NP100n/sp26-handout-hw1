
#Main module to run the Housing Priority Calculator application.


import sys
sys.path.append(".")



from src.question_asker import (
    ask_additional_questions,
    ask_class_year,
    ask_credits_earned,
    ask_graduation_status,
)
from src.priority_calculator import (
    points_for_additional_questions,
    points_for_class_year,
    points_for_credits,
    points_for_graduation,
    calculate_total_score,
)

def main() -> None:
    # TODO: Call functions from question_asker to get user input
    # TODO: Call functions from priority_calculator to compute score
    # TODO: Calculate and print the final housing priority score
    # TODO: Add documentation to this function
    pass



grad = ask_graduation_status()
cred = ask_credits_earned()
year = ask_class_year()
add_q = ask_additional_questions()

print(calculate_total_score(year, grad, cred, add_q))




if __name__ == "__main__":
    main()

import quiz_config
import quiz_functions

print("===============================================================================================================")
# executes various functions
print(quiz_config.intro)
name = input(quiz_config.give_name)
print(quiz_config.instructions)
input(quiz_config.begin)
print("===============================================================================================================")

# runs the question and grading functions for each question number in variable question_nums
for num in range(1, 11):
    quiz_functions.question(num)
    quiz_functions.grading_system(num)

print("\n=============================================================================================================")
print(f"Congratulations on completing the quiz {name}! Type anything and hit enter to view your results! ")
print("=============================================================================================================")
input()
quiz_functions.score_results()
print("\n=============================================================================================================")
print(quiz_config.check_answers)
print("=============================================================================================================")
input()
# checks if the user didn't get a perfect score
if sum(quiz_functions.score) != 100:
    # runs the review_incorrect_answers function correcting the user on any question they got wrong
    for num in range(1, 11):
        quiz_functions.review_incorrect_answers(num)
else:
    print(quiz_config.perf_score)
input("\nEnter any key to continue: ")
print("\n=============================================================================================================")
print("\nThanks for taking time out of your day to take this quiz. Enter any key to end the quiz.")
input()

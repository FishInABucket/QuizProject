import quiz_config
import quiz_functions

print("===============================================================================================================")
print(quiz_config.intro)
name = input(quiz_config.give_name)
print(quiz_config.instructions)
input(quiz_config.begin)
print("===============================================================================================================")

# question 1
quiz_functions.question(1)
quiz_functions.grading_system(1)

# question 2
quiz_functions.question(2)
quiz_functions.grading_system(2)

# question 3
quiz_functions.question(3)
quiz_functions.grading_system(3)

# question 4
quiz_functions.question(4)
quiz_functions.grading_system(4)

# question 5
quiz_functions.question(5)
quiz_functions.grading_system(5)

# question 6
quiz_functions.question(6)
quiz_functions.grading_system(6)

# question 7
quiz_functions.question(7)
quiz_functions.grading_system(7)

# question 8
quiz_functions.question(8)
quiz_functions.grading_system(8)

# question 9
quiz_functions.question(9)
quiz_functions.grading_system(9)

# question 10
quiz_functions.question(10)
quiz_functions.grading_system(10)

print("\n=============================================================================================================")
print(f"Congratulations on completing the quiz {name}! Type anything and hit enter to view your results! ")
print("=============================================================================================================")
input()
quiz_functions.score_results()
print("\n=============================================================================================================")
print(quiz_config.check_answers)
print("=============================================================================================================")
input()
if sum(quiz_functions.score) != 100:
    quiz_functions.compare_answers(1)
    quiz_functions.compare_answers(2)
    quiz_functions.compare_answers(3)
    quiz_functions.compare_answers(4)
    quiz_functions.compare_answers(5)
    quiz_functions.compare_answers(6)
    quiz_functions.compare_answers(7)
    quiz_functions.compare_answers(8)
    quiz_functions.compare_answers(9)
    quiz_functions.compare_answers(10)
else:
    print(quiz_config.perf_score)
input("\nEnter any key to continue: ")
print("\n=============================================================================================================")
print("\nThanks for taking time out of your day to take this quiz. Enter any key to end the quiz.")
input()

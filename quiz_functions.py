import quiz_config
import keyboard

score = [0]
ans1 = [quiz_config.ans1]
ans2 = [quiz_config.ans2]
ans3 = [quiz_config.ans3]
ans4 = [quiz_config.ans4]
ans5 = [quiz_config.ans5]
ans6 = [quiz_config.ans6]
ans7 = [quiz_config.ans7]
ans8 = [quiz_config.ans8]
ans9 = [quiz_config.ans9]
ans10 = [quiz_config.ans10]
user_choices = ["null"]


def question(question_num):
    match question_num:
        case 1:
            print(quiz_config.question_list[0])
        case 2:
            print(quiz_config.question_list[1])
        case 3:
            print(quiz_config.question_list[2])
        case 4:
            print(quiz_config.question_list[3])
        case 5:
            print(quiz_config.question_list[4])
        case 6:
            print(quiz_config.question_list[5])
        case 7:
            print(quiz_config.question_list[6])
        case 8:
            print(quiz_config.question_list[7])
        case 9:
            print(quiz_config.question_list[8])
        case 10:
            print(quiz_config.question_list[9])


def check_for_mcq_options():
    while True:
        ans_choice = input()
        if ans_choice.lower() in ["a", "b", "c"]:
            print(f" You selected choice: {ans_choice.upper()}.")
            user_choices.append(ans_choice.lower())
            break
        else:
            print(f"\"{ans_choice}\" is not an answer choice, please select A, B, or C. ")


def grading_system(question_num):
    match question_num:
        case 1:
            while True:
                check_for_mcq_options()
                if user_choices[1] in ans1:
                    score.append(10)
                    break
                else:
                    score.append(0)
                    break
        case 2:
            while True:
                check_for_mcq_options()
                if user_choices[2] in ans2:
                    score.append(10)
                    break
                else:
                    score.append(0)
                    break
        case 3:
            while True:
                check_for_mcq_options()
                if user_choices[3] in ans3:
                    score.append(10)
                    break
                else:
                    score.append(0)
                    break
        case 4:
            while True:
                check_for_mcq_options()
                if user_choices[4] in ans4:
                    score.append(10)
                    break
                else:
                    score.append(0)
                    break
        case 5:
            while True:
                check_for_mcq_options()
                if user_choices[5] in ans5:
                    score.append(10)
                    break
                else:
                    score.append(0)
                    break
        case 6:
            while True:
                check_for_mcq_options()
                if user_choices[6] in ans6:
                    score.append(10)
                    break
                else:
                    score.append(0)
                    break
        case 7:
            while True:
                check_for_mcq_options()
                if user_choices[7] in ans7:
                    score.append(10)
                    break
                else:
                    score.append(0)
                    break
        case 8:
            while True:
                check_for_mcq_options()
                if user_choices[8] in ans8:
                    score.append(10)
                    break
                else:
                    score.append(0)
                    break
        case 9:
            while True:
                check_for_mcq_options()
                if user_choices[9] in ans9:
                    score.append(10)
                    break
                else:
                    score.append(0)
                    break
        case 10:
            while True:
                check_for_mcq_options()
                if user_choices[10] in ans10:
                    score.append(10)
                    break
                else:
                    score.append(0)
                    break


def score_results():
    match sum(score):
        case 100:
            print(f"You got an A and your score was: {sum(score)}%! Nice job!")
        case 90:
            print(f"You got an A and your score was: {sum(score)}%! Nice job!")
        case 80:
            print(f"You got a B and your score was: {sum(score)}%!")
        case 70:
            print(f"You got a C and your score was: {sum(score)}%.")
        case 60:
            print(f"You got a D and your score was: {sum(score)}%...")
        case _:
            print(f"You got an F and your score was: {sum(score)}%... Better luck next time...")


def compare_answers(question_num):
    match question_num:
        case 1:
            if score[1] == 0:
                print(f"For question 1 you answered \"{user_choices[1]}\", the correct answer is {quiz_config.ans1}.")
        case 2:
            if score[2] == 0:
                print(f"For question 2 you answered \"{user_choices[2]}\", the correct answer is {quiz_config.ans2}.")
        case 3:
            if score[3] == 0:
                print(f"For question 3 you answered \"{user_choices[3]}\", the correct answer is {quiz_config.ans3}.")
        case 4:
            if score[4] == 0:
                print(f"For question 4 you answered \"{user_choices[4]}\", the correct answer is {quiz_config.ans4}.")
        case 5:
            if score[5] == 0:
                print(f"For question 5 you answered \"{user_choices[5]}\", the correct answer is {quiz_config.ans5}.")
        case 6:
            if score[6] == 0:
                print(f"For question 6 you answered \"{user_choices[6]}\", the correct answer is {quiz_config.ans6}.")
        case 7:
            if score[7] == 0:
                print(f"For question 7 you answered \"{user_choices[7]}\", the correct answer is {quiz_config.ans7}.")
        case 8:
            if score[8] == 0:
                print(f"For question 8 you answered \"{user_choices[8]}\", the correct answer is {quiz_config.ans8}.")
        case 9:
            if score[9] == 0:
                print(f"For question 9 you answered \"{user_choices[9]}\", the correct answer is {quiz_config.ans9}.")
        case 10:
            if score[10] == 0:
                print(
                    f"For question 10 you answered \"{user_choices[10]}\", the correct answer is {quiz_config.ans10}.")

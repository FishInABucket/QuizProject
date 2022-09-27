#######################################################################################################################
# Place an introductory statement below:
intro = "Welcome to my quiz! This quiz will test you on basic knowledge of molecular biology, \nas I didn't know " \
        "what else to write here. \n"

# Prompt the user for their name:
give_name = "Please type out your name: "

# Write your instructions below:
instructions = "\nThere are 10 equally weighted multiple choice questions in this quiz with option choices A, B, and C." \
               "\nUpon answering a question, press enter to submit your answer. You may change your answer choice for a" \
               "\nparticular question before hitting Enter for that question. Both capital and lowercase letters are " \
               "\nacceptable responses and if you accidentally submit an invalid answer choice, the quiz will let you" \
               "\nresubmit until you pick a valid answer choice. There is no time limit on the quiz, good luck!\n"

# Prompt the user to begin:
begin = "Type anything and hit enter to begin: "

# Prompt the user to check the wrong answers:
check_answers = "If you would like to check to see which questions you got wrong and what the right answer was,\n " \
                "press any key to continue. "

# Tell the user they got a perfect score when trying to check their wrong answer
perf_score = "You answered every question correctly, there's nothing to see here! "
#######################################################################################################################
# This is the pool of questions to choose from, each one separated by a comma. Question 1 is question_list[0], question
# 2 is question_list[1], and so on.

question_list = ["\nQuestion 1: Which of the following is an example of a seedless vascular plant?\n"
                 "\nA: a fern"
                 "\nB: a sunflower"
                 "\nC: moss\n ",
                 "\nQuestion 2: What is the first known photosynthetic organism? \n"
                 "\nA: chloroplast"
                 "\nB: cyanobacteria"
                 "\nC: early lichen\n ",
                 "\nQuestion 3: What do plant cells and animal cells share in common?\n "
                 "\nA: cell walls"
                 "\nB: mitochondria"
                 "\nC: chloroplasts\n ",
                 "\nQuestion 4: What molecule is responsible for providing energy to cells?\n "
                 "\nA: deoxyribonucleic acid (DNA)"
                 "\nB: adenosine triphosphate (ATP)"
                 "\nC: oxygen gas\n ",
                 "\nQuestion 5: What class of macromolecule does keratin fall under?\n"
                 "\nA: carbohydrate"
                 "\nB: nucleic acid "
                 "\nC: polypeptide\n ",
                 "\nQuestion 6: Which atom is known as the \"building block of life\"?\n"
                 "\nA: carbon"
                 "\nB: oxygen"
                 "\nC: nitrogen\n ",
                 "\nQuestion 7: What do eukaryotic cells have that prokaryotic cells do not?\n "
                 "\nA: cytoplasm"
                 "\nB: cell membrane"
                 "\nC: nucleus\n ",
                 "\nQuestion 8: What kind of genetic material could a virus have?\n "
                 "\nA: only DNA"
                 "\nB: only RNA"
                 "\nC: either, depending on the variant\n ",
                 "\nQuestion 9: What is a cell membrane made of?\n "
                 "\nA: a lipid membrane made of triglycerides"
                 "\nB: a lipid membrane called the phospholipid bilayer "
                 "\nC: a chain link membrane mesh of polysaccharides\n ",
                 "\nQuestion 10: What is a correct characteristic of a phospholipid?\n"
                 "\nA: their \"head\" is polar while their \"tail\" is nonpolar"
                 "\nB: their \"tail\" is polar while their \"head\" is nonpolar"
                 "\nC: they are nonpolar\n "]

#######################################################################################################################
# This is the pool of answers to satisfy the questions above. Each ans# variable corresponds to that question name.

ans1 = "a"
ans2 = "b"
ans3 = "b"
ans4 = "b"
ans5 = "c"
ans6 = "a"
ans7 = "c"
ans8 = "c"
ans9 = "b"
ans10 = "a"

#######################################################################################################################

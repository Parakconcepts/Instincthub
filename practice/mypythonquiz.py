# from classes import Laptop
# from classes import Quiz

# laptop1 = Laptop("HP","15.6","Intel","4G", True)
# print(laptop1)


quiz_prompt = [
    "Who licked honey without permission? \n(a)Samson \n(b)Jonathan \n(c)Joash\n\n",
    "Who lied because of a woman? \n(a)David \n(b)Abram \n(c)Jacob\n\n",
    "Who sacrificed a child because of Ambition? \n(a)Manaseh \n(b)Jephtah \n(c)Mesha\n\n",


]

quizes = [
    Quiz(quiz_prompt[0], "b"),
    Quiz(quiz_prompt[1], "b"),
    Quiz(quiz_prompt[2], "c"),

]

def display_quiz(quizes):
    score = 0
    for questions in quizes:
        answer = raw_input(questions.prompt )
        if answer == questions.answer:
            score += 30
    print ("You Got " + str(score) + " points")

display_quiz(quizes)
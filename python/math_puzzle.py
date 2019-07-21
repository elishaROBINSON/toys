# math game is a basic math skill testing game
from random import randrange
from time import time
# from progress import bar

# difficulty level easy medium hard
difficulty = {"1":(0,9),"2":(10,99),"3":(100,999)}[raw_input(
    """
 enter the difficulty level you want 
    [1]easy
    [2]medium
    [3]hard
    """)]
# time trial 
# time_trial = if raw_input("do you want to do a time trial y/n") in ["y","Y","yes"] True else False

# score
score = 0

# rounds 
rounds = 10

start_time = time()

def gen_questions():
    a = randrange(*difficulty)
    b = randrange(*difficulty)
    operation = {0:"*",1:"/",2:"+",3:"-"}[randrange(0,4)]
    question = " "+str(a)+" "+operation+" "+str(b)
    return question, eval(question)

for rou in range(1,rounds): 
    print("starting round {}".format(rou))
    question,answer = gen_questions()
    print("what is {} ".format(question))
    u_answer = input()
    if u_answer == answer:
        print("correct")
        score+=1
    else:
        print("wrong")

print(" your score is {}".format(score))
print(" you completed all rounds in {} seconds".format(round(time()-start_time)))


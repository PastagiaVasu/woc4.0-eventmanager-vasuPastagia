from questions import questions

questions_prompts = ["What colours are apples ? \n(a) Red/Green \n(b) Purple \n(c) Orange\n\n",
                     "What colours are banana?\n(a) Teal \n(b) Green/Yellow \n(c) Magenta\n\n"]
Question = [
    questions(questions_prompts[0], "a"),
    questions(questions_prompts[1], "b"),
    ]
def run_test(question):
    score = 0
    for q in question:
        print(q.prompt);
        ans = input("Enter your choice: ")
        if(ans == q.ans):
            score+=1
    print("YOU got " + str(score) + " / " + str(len(question)) + " Correct")

run_test(Question)
score=0
print("================================")
print("WELCOME TO THE QUIZ GAME")
print("================================")
questions=[{"question":"1.What is the capital of India?","options":["A.Chennai","B.New Delhi","C.Mumbai","D.Kolkata"],"answer":"B"},
{"question":"2.Which Language is used for AI AND DS?","options":["A.Python","B.HTML","C.CSS","D.XML"],"answer":"A"},
{"question":"3.How many continents are there?","options":["A.5","B.6","C.7","D.8"],"answer":"C"},
{"question":"4.Which planet is known as the red planet?","options":["A.Earth","B.Venus","C.Mars","D.Jupiter"],"answer":"C"},
{"question":"5.Who developed python?","options":["A.Dennis Ritche","B.James Gosling","C.Guido Van Rossum","D.Bjarne Stroustrup"],"answer":"C"}]
for q in questions:
    print("\n"+q["question"])
    for option  in q["options"]:
        print(option)
    user_answer=input("Enter your answer(A/B/C/D):").upper()
    if user_answer==q["answer"]:
        print("Correct!")
        score+=1
    else:
        print("Wrong!")
print("\n===============================")
print("QUIZ COMPLETED!")
print("Your score:",score,"/",len(questions))
percentage=(score/len(questions))*100
print("Percentage:",percentage,"%")
if percentage>=80:
    print("Excellent!")
elif percentage>=60:
    print("Good Job!")
else:
    print("Keep practicing!")
print("==============================")

    
    


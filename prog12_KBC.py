ques=["q1","q2","q3","q4","q5","q6","q7","q8","q9","q10"]
Options=["a-optionq11,b-optionq12,c-optionq13,d-optionq14",
         "a-optionq21,b-optionq22,c-optionq23,d-optionq24",
         "a-optionq31,b-optionq32,c-optionq33,d-optionq34",
         "a-optionq41,b-optionq42,c-optionq43,d-optionq44",
         "a-optionq51,b-optionq52,c-optionq53,d-optionq54",
         "a-optionq61,b-optionq62,c-optionq63,d-optionq64",
         "a-optionq71,b-optionq72,c-optionq73,d-optionq74",
         "a-optionq81,b-optionq82,c-optionq83,d-optionq84",
         "a-optionq91,b-optionq92,c-optionq93,d-optionq94",
         "a-optionq101,b-optionq102,c-optionq103,d-optionq104",
         ]
solutions=["a","b","c","d","a","b","c","d","a","b"]
score=[10000,20000,30000,40000,50000,60000,70000,80000,90000,125555]
for i in range (11):
    print("Question", i+1, ":", ques[i])
    print("Options:", Options[i])
    user_answer = input("Enter your answer (a/b/c/d): ")
    if user_answer == solutions[i]:
        print("Correct answer!")
        print("You have won Rs.", score[i])
    else:
        print("Incorrect answer!")
        break
print("The final amount you have won is Rs.", score[i-1])

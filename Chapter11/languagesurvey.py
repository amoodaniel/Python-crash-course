from survery import AnonymousSurvey
#Define a question
question = 'What is the first language you learnt'
my_survey = AnonymousSurvey(question)

#Show question and store responses
my_survey.show_questions()
print("Enter 'q' to Quit")
while True:
    reponse = input('Language: ')
    if reponse == 'q':
        break
    my_survey.store_response(reponse)
    
#Show the results
my_survey.show_results()
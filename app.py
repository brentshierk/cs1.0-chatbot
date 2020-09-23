# inputs = []
# response1 = []
# def interactionStart():
    
#     user_inputs = str(input('So I herd you like programming'))
#     splitStr = user_inputs.split(' ')
#     print(splitStr)
#     inputs = splitStr

#     for word in splitStr:
#         if word == 'yes' or word == 'yeah':
#             print('thats super cool')
#         else:
#             print('i guess thats all then')
    
# interactionStart()

# def secondInteraction():

#     getLang = str(input('So whats your favorite language?'))
#     splitStr = getLang.split(' ')
#     print(splitStr)
#     inputs = splitStr

#     for word in splitStr:
#         if word == 'python':
#             print('I love python')
#         elif word == 'javascript':
#             print('I love javascript!')
#         else:
#             print('im not fimilar with that language')
            
# secondInteraction()

# def funFact():
#         user_input = str(input('Do you want to hear a fun fact about {getLang}'))
#         if user_input == 'yes':
#             print('heres your fact...')
#         else:
#             print('your missing out i got some really good facts')

user_response = str(input('hey! I herd you like programming : '))
def get_bot_response(user_response):
   #user_response = str(input('hey! I herd you like programming : '))
    botResponseQ1 = [('yes','thats really cool i was made with programming'),('no',"I guess we're done here. *frown in binary*")]
    
    if user_response == 'yes' or user_response == 'yeah':
        print(botResponseQ1[0][1])
    elif user_response == 'no'or user_response == 'nope':
        print(botResponseQ1[1][1])
    
    botResponseQ2 = [
    ('python','I was actually made with python!'),
    ('javascript','thats a great language! and I love the all of the possiblities of JS with its diverse set of librarys and frameworks '),
    ('none','well I know you will find one soon!')
    ]
    if user_response == 'yes' or user_response == 'yeah':
        q2Input = str(input('so whats your favorite coding language? '))
        print(q2Input)
    
    if q2Input == 'python':
        print(botResponseQ2[0][1])
    elif q2Input == 'javascript':
        print(botResponseQ2[1][1])
    else:
        print(botResponseQ2[2][1])

    q3Input = str(input(f'Do you want to hear a fun fact about {q2Input}? '))
    botResponseQ3 = [('pythonFact','The language’s name isn’t about snakes, but about the popular British comedy troupe Monty Python (from the 1970s). Guido himself is a big fan of Monty Python’s Flying Circus. Being in a rather irreverent mood, he named the project ‘Python’. Isn’t it an interesting Python fact?'),
    ('javascript','JavaScript was created in 10 days only and when released, it used to cover a very small portion of a proper programming language.','JavaScript was being developed under the name Mocha.')]
    if q3Input == 'yes' or q3Input == 'yeah' and q2Input == 'python':
        print(botResponseQ3[0][1])
    elif q3Input == 'yes' or q3Input =='yeah' and q2Input == 'javascript':
        print(botResponseQ3[1][1])
    elif q3Input == 'yes' or q3Input =='yeah' and q2Input == 'none':
        print('no fun facts for you!')


    

    while True:
        user_response = input('Well I had a great time talking about programming, enter done if you would like to end the conversation or anything if you would like to continue')
        if user_response == 'done':
            break
    
    
get_bot_response(user_response)





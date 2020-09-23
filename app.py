
#while


#abcd
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


    

    
    
    
get_bot_response(user_response)





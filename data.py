# -*- coding: utf-8 -*-

WELCOME_MESSAGE = ("Welcome to Learn Stem Jeopardy! I'll ask you for the topic you want and your grade level. "
                "When you answer a question, please do so in Jeopardy style by phrasing your answer as 'What is...' "
                "Now to start. For which topic would you like a question? ")

SUBJECT_SPECIFICATION = "Would you like to learn coding or math?"

ANSWER_CLARIFICATION_REQUEST = "Please make sure you answered in Jeopardy Style, for example 'What is...'"

CORRECT_ANSWER_RESPONSE = "Nice job! You answered the question correctly!"
MISSING_PHRASING_RESPONSE = "Please make sure you answered in Jeopardy Style, for example 'What is...'"
WRONG_ANSWER_RESPONSE= "Oops, that is not the correct answer. You have another chance to answer though."

HELP_MESSAGE =  ("If you haven’t been asked a question yet, state which topic and grade level for which you’d like a question. "
                "If you’re having trouble getting the right answer, make sure you’re answering with “what is” followed by your answer. "
                "If you’d like a new question, say “ask me a new question.” "
                "To stop or cancel, just say “stop learn stem” or “cancel learn stem.” You can restart after by saying “start learn stem.” "
                "How would you like to proceed? ")

STOP_CANCEL_OUTPUT = "Learn Stem has ended. If you want a new session, ask me for a new question. See you next time!"

ISSUE_MESSAGE = "Sorry, I had trouble doing what you asked. Please try again."

GLOBAL_ANSWER = "placeholder string"
GLOBAL_QUESTION = "placeholder string"
GLOBAL_QTYPE = "placeholder string"
GLOBAL_GLEVEL = "placeholder string"
GLOBAL_NULL = "null"

LAST_QUESTION_ASKED = "placeholder"

SKILL_NAME = "Learn Stem"

MATH_FIFTH_LIST = ['What is 20 divided by 4?:5', 
                  'What is 10 squared?:100', 
                  'What is three cubed?:9', 
                  'A large box contains 18 small boxes and each small box contains 25 chocolate bars. How many chocolate bars are in the large box?:450', 
                  'It takes Dalton 20 minutes to walk to the car park and 40 to drive to work. At what time should he get out of the house in order to get to work at 9 a.m.?:7', 
                  'Sam can walk 4 kilometers in one hour. How long does it take Sam to walk 16 kilometers?:4 hours', 
                  'What is 3 times 4 + 2 times 5:22', 
                  'Angles around a point add up to how many degrees?:360', 
                  'The ratio of lions to tigers in a zoo is 1 to 3. If there are 4 lions, how many tigers will there be?:12', 
                  '4 times 7 is equivalent to 30 minus...?:2', 
                  'What is 8 times 6 plus 7?:55', 
                  'What is 1000 minus 60?:940', 
                  'If 2x + 1 equals 7, then the value of x is?:3']

MATH_FOURTH_LIST = ['What is 1000 minus 550?:450', 
                   'If 6 times 4 equals 3 times y, y is?:8', 
                   'What is 0.7 + 0.8?:1.5', 
                   'What is 42 divided 6?:7', 
                   'What is 10 minus 2.7?:7.3', 
                   'What is one third of 21?:7', 
                   'If Dalton has 13 computers. How many computers does he need in order to get 100 computers?:87', 
                   'The value of 2x + 1 if x equals 6?:13', 
                   'If 12 out 20 kids in the class are boys. Then the number of girls in the class is?:8', 
                   'What is 6+7 times 3?:27']

MATH_THIRD_LIST = ['What is 4+5+6?:15', 
                  'What is 20 minus 4?:16', 
                  'What is 5 times 3?:15', 
                  'How many groups of 3 make 15?:5', 
                  'What is 40 times 2?:80', 
                  'What is half of 16?:8', 
                  'What is 10 times 7?:70', 
                  'What is 4 + 9 + 6?:19', 
                  'What is one fourth of 20 is?:5', 
                  'What is 42 divided 6?:7']

MATH_SECOND_LIST = ['What is 80 + 80?:160', 
                   'What is 9 minus 3?:6', 
                   'What is 18 minus 11?:7', 
                   'What is 7 + 1 minus 2?:6', 
                   'What is 72 minus 2?:70', 
                   'What is 2 times 5?:10', 
                   'What is 2 times 4?:8', 
                   'What is 6 times 2?:12', 
                   'Dalton has some noodles. He gives 12 noodles to Sam. Now Dalton only has 54 noodles. How many noodles did Dalton have to begin with?:66', 
                   'What is 900 minus 750?:150']

MATH_FIRST_LIST = ['What is 3+4?:7', 
                  'What is 3+3?:6', 
                  'What is 5+2?:7', 
                  'What is 7+0? :7', 
                  'What is 6 minus 5?:1', 
                  'What is 7 minus 7?:0', 
                  'What is 5 minus 3?:2', 
                  'What is 17 minus 6?:11', 
                  'What is 15 minus 13?:2', 
                  'What is 14 minus 10?:4']

#-------------------------

CODING_FIFTH_LIST = ['In computers how many bits make up a byte?:8', 
                    'Letters, numbers, or charaters with no meaning.:data', 
                    'The letters WWW stand for?:world wide web', 
                    'Web pages are made using HTML, which stands for?:hypertext markup Language', 
                    'A computer that delivers web pages when requested.:a web server', 
                    'A set of information when writing code (x, y, w, h).:parameters', 
                    'Statements that only run under certain conditions.:conditionals', 
                    'The ordered steps in a program.:a sequence', 
                    'List of steps you follow to finish a task.:an algorithm', 
                    'A block of organized, reusable code that is used to perform a certain action.:a function']

CODING_FOURTH_LIST = ['Computers store information in a special code. The smallest piece of this code is called...?:a bit', 
                     'A piece of information bigger than a bit is?:a byte', 
                     'A stranger asks Sam for his address on the internet, should Sam give his address to them?:no', 
                     'A worldwide collection of computers which are connected together.:the internet', 
                     'URL or Uniform Resource Locator.:a web address', 
                     'A program which can find specific data on the web.:a search engine', 
                     'Java, Python, Swift, C plus plus, and JavaScript are all...?:programming languages', 
                     'An algorithm is...? A. a bunch of code? B. a set of step by step instructions? C. 7?:b', 
                     'The process of designing and building an executable computer program for accomplishing a specific computing task.:a computer program', 
                     'If x is less than 10 go on to the next step, else stop. What number will stop the program? A. any number less than 10? B. any number greater than 10? C. any number greater than 9?:c']

CODING_THIRD_LIST = ['A mistake in a program.:a bug', 
                    'What happens if there is a bug in Maddies program? A. it will work? B. it wont work?:b', 
                    'The action of looking for a bug and fixing it.:debugging', 
                    'What does RAM stand for?:random access memory', 
                    'Is 1010 12 in binary?:no', 
                    'Can anyone learn how to code?:yes', 
                    'A set of detailed step-by-step instructions or formula for solving a problem.:an algorithm', 
                    'Is it okay to share personal info on the internet?:no', 
                    'Computers store this so that they can work.:information', 
                    'How many bits are there in a byte?:8']

CODING_SECOND_LIST = ['A detailed step-by-step instruction set or formula for solving a problem or completing a task.:an algorithm', 
                     'How do you write an Algorithm? A. One step at a time? B. As a story? C. In any order? D. As a poem?:a', 
                     'Is a recipe an example of an algorithm?:yes', 
                     'A world wide network of computers.:the internet', 
                     'Another name for computer programs.:software', 
                     'Everything you read on the internet is true.:false', 
                     'What does CPU stand for?:central processing unit', 
                     'What does the E in e-mail stand for?:electronic', 
                     'Is it okay to tell strangers personal information on the internet?:no', 
                     'If x is less than 10, Sam keeps running around the track, else Sam stops running. What happens when x is equal to 11? A. Sam keeps running? B. Sam stops running? C. Same runs faster?:b']

CODING_FIRST_LIST = ['Should I share personal information, like my name, online?:no', 
                    'Is everyone able to learn how to code?:yes', 
                    'You will move forward if x is less than 10. If x equals 15, will you move forward?:no', 
                    'While Maddie is holding 5 cups of coffee, she is full of energy. If Maddie is only holding 4 cups of coffee, is she full of energy?:no', 
                    'If someone on the internet asks where you live do you, do you tell them?:no', 
                    'Is coding used in almost everything in life now?:Yes', 'Is coding cool?:yes', 
                    'What is the main coding language used to make iPhone apps? A. Python, B. Java, C. Swift, D. Haskell.:c', 
                    'Code is written in short steps. A series of these steps in code is called an?:an algorithm', 
                    'Dalton is writing code to control a toy robot. What is Dalton doing to have the toy robot move around? A. Colouring, B. Shaping, C. Programming?:c']



#creating a basic multiple choice program for skills assessment
"""
name =input("Enter Your name: ")
age = input("Enter Your age: ")
email = input("Enter Your email: ")
print("[Python][Networking][Database][Business]")
speciality = input("Enter Your Speciality: ")
"""

questions = {
    #These are python questions
    "Which symbol is used for comments in Python: ": "C",
    "How do you print 'Hello,World' to the console on Python: ": "A",
    "Which of the following is a correct way to declare a variable in Python: ": "B",
    "How do you check the length of a list named 'my_list' in Python: ": "B",
    "What is the correct syntax for a multi-line comment in Python: ": "C",

    #These are networking questions
    "What does the acronym 'LAN' stand for in networking: ": "A",
    "Which protocol is commonly used for email communication in networking: ": "C",
    "What does DNS stand for in networking: ": "B",
    "In the OSI model, which layer is responsible for logical addressing, such as IP addresses: ": "A",
    "What device is used to connect multiple computers in a local network and operates at the Data Link Layer: ": "B",

    #These are database questions
    "What is the primary responsibility of a database administrator (DBA): ": "C",
    "Which of the following is NOT a type of database model: ": "D",
    "What does SQL stand for: ": "C",
    "In a relational database, what is a primary key: ": "B",
    "What is the purpose of database normalization: ": "C",

    #These are business questions
    "What is the primary goal of business analysis ": "C",
    "Which technique is commonly used for gathering requirements by observing how users perform their tasks: ": "D",
    "What does SWOT analysis stand for: ": "B",
    "Which document outlines the scope, objectives and constraints of a project and is used to gain approval from stakeholders: ": 'C',
    "In the context of business analysis, what is the purpose of a Use Case: ": "B",
}


options = (
    #These question are python mutiple choice options
    ["A. //", "B. --", "C. #", "D. /**/"],
    ["A. print('Hello,World')", "B. echo Hello,World", "C. console.log('Hello World')", "D. display('Hello,World!')"],
    ["A. variable x = 10", "B. x = 10", "C. int x = 10", "D. let x = 10"],
    ["A. size(my_list)", "B. len(my_list)", "C. length(my_list)", "D. count(my_list)"],
    ["A. /*This is a comment*/", "B. //This is a comment//", "C. 'This is a comment'", "D. #This is a comment#"],
    #These question are networking mutiple choice options
    ["A. Local Area Network", "B. Large Area Network", "C. Longitudinal Access Network", "D. Limited Access Node"],
    ["A. HTTP", "B. FTP", "C. SMTP", "D. UDP"],
    ["A. Data Naming System", "B. Domain Name System", "C. Dynamic Network Service", "D. Digital Network Security"],
    ["A. Network Layer", "B. Data-Link Layer", "C. Transport Layer", "D. Presentation Layer"],
    ["A. Router", "B. Switch", "C. Hub", "D. Moderm"],
    #These question are database administrator mutiple choice options
    ["A. Writing code for applications", "B. Designing user interfaces", "C. Managing and maintaining databases", "D. Conducting market research"],
    ["A. Relational Database Model", "B. Hierarchical Database Model", "C. Network Database Model", "D. Linear Database Model"],
    ["A. Simple Query Langauge", "B. Structured Question Langauge", "C. Standard Query Langauge", "D. Systematic Query Logic"],
    ["A. A key used for encryption", "B. A unique identifier for a record in a table", "C. A key used to access the database","D. A foreign key from another table"],
    ["A. /*This is a comment*/", "B. //This is a comment//", "C. 'This is a comment'", "D. #This is a comment#"],
    #These question are business analysis mutiple choice options
    ["A. Increase sales", "B. Maximize profit", "C. Understand business needs and find solutions", "D. Improve employee satisfaction"],
    ["A. Interviews", "B. Surveys", "C. Use Cases", "D. Observation"],
    ["A. Software Work and Operational Tasks", "B. Strengths,Weakness,Opportunities,Threats", "C. Strategic Ways of Organizing Teams","D. Systematic Workflow for Organizational Tasks"],
    ["A. Business Case", "B. Requirements Document", "C. Project Charter", "D. Risk Management Plan"],
    ["A. increasing redundancy in the database", "B. Improving performance by adding more data", "C. Reducing redundancy and dependancy in the database", "D. Adding complexity to the database schema"]
)
def new_game():

    guesses = []
    correct_guesses = 0
    questions_num = 1
    for key in questions:
        print("----------------------")
        print(key)
        for i in options[questions_num-1]:
            print(i)
        guess = input("Please select either [A, B, C or D]")
        guess = guess.upper()
        guesses.append(guess)
        correct_guesses += check_answer(questions.get(key),guess)
        display_score(correct_guesses, guesses)
        questions_num += 1


def check_answer(answer, guess):
    if answer == guess:
        print('Correct')
        return 1
    else:
        print('Incorrect')
        return 0


def display_score(correct_guesses, guesses):
    print("--------------------------")
    print("Results")
    print("--------------------------")
    print("Answers: ", end="")
    for i in questions:
        print(questions.get(i), end="")
    print()
    score = int((correct_guesses / len(questions))*100)
    print("Your score is "+str(score)+"%")


def play_again():
    response = input("Do you want to re-take the assessment? [Yes] or [No]")
    response = response.upper()

    if response == "YES":
        return True
    else:
        return False

def new_game():

    while play_again():
        new_game()
    print("GoodBye")


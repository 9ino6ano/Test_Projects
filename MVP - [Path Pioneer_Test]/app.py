from questions import question
#questions_prompt 1
question_prompts = [
#These are python questions
    "Which symbol is used for comments in Python:\n(a) //\n(b) --\n(c) #\n(d)/**/\n\n",
    "How do you print 'Hello,World' to the console on Python:\n(a) print('Hello,World')\n(b) echo 'Hello,World'\n(c) console.log('Hello,World')\n(d)display('Hello,World')\n\n",
    "Which of the following is a correct way to declare a variable in Python:\n(a) variable x = 10\n(b) x = 10\n(c) int x = 1=\n(d)let x = 10\n\n",
    "How do you check the length of a list named 'my_list' in Python: \n(a) size(my_list)\n(b) len(my_list)\n(c) length(my_list)\n(d)count(my_list)\n\n",
    "What is the correct syntax for a multi-line comment in Python:\n(a) /*This is a comment*/ \n(b) //This is a comment//\n(c) 'This is a comment'\n(c)#This is a comment#\n\n",

    #These are networking questions
    "What does the acronym 'LAN' stand for in networking: \n(a) Local Area Network\n(b) Large Area Network\n(c) Longitudinal Access Network\n(d) Limited Access Node\n\n",
    "Which protocol is commonly used for email communication in networking: \n(a) HTTP\n(b) FTP\n(c) SMTP\n(d)UDP\n\n",
    "What does DNS stand for in networking:\n(a) Data Naming System\n(b) Domain Name System\n(c) Dynamic Network Service\n(d) Digital Network Security\n\n",
    "In the OSI model, which layer is responsible for logical addressing, such as IP addresses:\n(a) Network Layer\n(b) Data-Link Layer\n(c) Transport Layer\n(d) Presentation Layer\n\n",
    "What device is used to connect multiple computers in a local network and operates at the Data Link Layer: \n(a) Router\n(b) Switch\n(c) Hub\n(d)Moderm\n\n",

    #These are database questions
    "What is the primary responsibility of a database administrator (DBA):\n(a) Writing code for apps\n(b) Designing User Interface\n(c) Managing and Maintaining Databases\n(d)Conduct market research\n\n",
    "Which of the following is NOT a type of database model:\n(a) Relational Database Model\n(b) Hierachiel Database Model\n(c) Network Database Model\n(d)Linear Database Model\n\n",
    "What does SQL stand for:\n(a) Simple Query Langauge\n(b) Structured Question Langauge\n(c) Standard Query Langauge\n(d)System Query Logic\n\n",
    "In a relational database, what is a primary key:\n(a) A key used for encryption\n(b) A unique identifier for a record in a table\n(c) A Key used to access the database\n(d)A foreign key from another table\n\n",
    "What is the purpose of database normalization:\n(a) Increasing redundancy in the database\n(b) Improving performance by adding more data\n(c) Reduce redundancy and dependency in the database\n(d)Adding complexity to the database schema\n\n",

    #These are business questions
    "What is the primary goal of business analysis:\n(a) Increase sales\n(b) Maximize Profit\n(c) Understand business needs and find solutions\n(d) Improve employee satisfaction\n\n",
    "Which technique is commonly used for gathering requirements by observing how users perform their tasks:\n(a) Interviews\n(b) Surveys\n(c) Use cases\n(d) Observation\n\n",
    "What does SWOT analysis stand for:\n(a) Software Work and Operational Tasks\n(b) Strengths,Weakness,Threats,Opportunities\n(c) Strategic Ways of Organizing Teams\n(d) Systematic workflow for organizing tasks\n\n",
    "Which document outlines the scope, objectives and constraints of a project and is used to gain approval from stakeholders:\n(a) Business Case\n(b) Requirements Document\n(c) Project Charter\n(d) Risk Management Plan\n\n",
    "In the context of business analysis, what is the purpose of a Use Case:\n(a) Increasing redundancy in a database\n(b) Improving performance by adding more data\n(c) Reducing redundancy and dependency in a database\n(d) Adding complexity to the database schema\n\n",
]

questions = [
    question(question_prompts[0],"c"),
    question(question_prompts[1],"a"),
    question(question_prompts[2],"b"),
    question(question_prompts[3],"b"),
    question(question_prompts[4],"c"),
    question(question_prompts[5],"a"),
    question(question_prompts[6],"c"),
    question(question_prompts[7],"b"),
    question(question_prompts[8],"a"),
    question(question_prompts[9],"b"),
    question(question_prompts[10],"c"),
    question(question_prompts[11],"d"),
    question(question_prompts[12],"c"),
    question(question_prompts[13],"b"),
    question(question_prompts[14],"c"),
    question(question_prompts[15],"c"),
    question(question_prompts[16],"d"),
    question(question_prompts[17],"b"),
    question(question_prompts[18],"c"),
    question(question_prompts[19],"b")
]
def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print("Hey, You Got " + str(score) + " Out Of "+str(len(questions)) + " correct.")

run_test(questions)

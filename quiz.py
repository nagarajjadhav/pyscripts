#!python3
#prepares different set of multiple choice question paper for 50 questions
import random

capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix',
            'Arkansas': 'Little Rock', 'California': 'Sacramento',
            'Colorado': 'Denver', 'Connecticut': 'Hartford', 'Delaware': 'Dover',
            'Florida': 'Tallahassee', 'Georgia': 'Atlanta', 'Hawaii': 'Honolulu',
            'Idaho': 'Boise', 'Illinois': 'Springfield', 'Indiana': 'Indianapolis',
            'Iowa': 'Des Moines', 'Kansas': 'Topeka', 'Kentucky':
            'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine': 'Augusta',
            'Maryland': 'Annapolis', 'Massachusetts': 'Boston',
            'Michigan': 'Lansing', 'Minnesota': 'Saint Paul',
            'Mississippi': 'Jackson', 'Missouri': 'Jefferson City',
            'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada': 'Carson City',
            'New Hampshire': 'Concord', 'New Jersey': 'Trenton',
            'New Mexico': 'Santa Fe', 'New York': 'Albany',
            'North Carolina': 'Raleigh', 'North Dakota': 'Bismarck',
            'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City', 'Oregon': 'Salem',
            'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence',
            'South Carolina': 'Columbia', 'South Dakota': 'Pierre',
            'Tennessee': 'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City',
            'Vermont': 'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia',
            'West Virginia': 'Charleston', 'Wisconsin': 'Madison',
            'Wyoming': 'Cheyenne'}

for quiznum in range(2):
    ques = open('quiz %s.txt'%(quiznum+1),'w')
    ans = open('quiz_ans %s.txt'%(quiznum+1),'w')
    ques.write('Name:\n\nDate:\n\nPeriod:\n\n')
    ques.write((''*20)+'State capital Quiz (form %s)'%(quiznum+1))
    ques.write('\n\n')

    states = list(capitals.keys())
    random.shuffle(states)

    for quesnum in range(50):
        correctans = capitals[states[quesnum]]
        wrongans = list(capitals.values())
        del wrongans[wrongans.index(correctans)]
        wrongans = random.sample(wrongans,3)
        ansoptions = wrongans + [correctans]
        random.shuffle(ansoptions)

        ques.write('%s. What is the capital of %s?\n'%(quesnum+1,states[quesnum]))
        for i in range(4):
            ques.write('    %s. %s\n'%('ABCD'[i],ansoptions[i]))
        ques.write('\n')

        ans.write('%s. %s\n'%(quesnum+1,'ABCD'[ansoptions.index(correctans)]))
    ques.close()
    ans.close()























    

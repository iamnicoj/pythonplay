
################################################

employees = { 'bob': 250000,
            'Richard': 350000,
            'Jennifer': 450000,
            'Petrosky': 800000,
            'Ginovesky': 850000,
            }

print(employees)

print([(name, val) for name, val in employees.items() if val > 500000])

################################################

text = '''
Suppose that communal kitchen years to come perhaps. 
All trotting down with porringers and tommycans to be filled. 
Devour contents in the street. 
John Howard Parnell example the provost of Trinity every mother’s son don’t talk of your provosts and provost of Trinity women and children cabmen priests parsons fieldmarshals archbishops. 
From Ailesbury road, Clyde road, artisans’ dwellings, north Dublin union, lord mayor in his gingerbread coach, old queen in a bathchair. 
My plate’s empty. After you with our incorporated drinkingcup. 
Like sir Philip Crampton’s fountain. Rub off the microbes with your handkerchief. 
Next chap rubs on a new batch with his. Father O’Flynn would make hares of them all. 
Have rows all the same. All for number one. Children fighting for the scrapings of the pot. 
Want a souppot as big as the Phoenix park. Harpooning flitches and hindquarters out of it. 
Hate people all round you. City Arms hotel table d’hôte she called it. Soup, joint and sweet. 
Never know whose thoughts you’re chewing. Then who’d wash up all the plates and forks? Might be all feeding on tabloids that time. 
Teeth getting worse and worse.
'''

# print([[word.upper() for word in [(line.replace('\n', "").split(" ")) for line in text.split(".")]] ])

print([[word for word in line.split() if len(word) > 3] for line in text.split(".")])


################################################

f = 'basics.py'

file = open(f)
lines = []
for line in file:
    lines.append(line.strip())
print (lines)

# Is equal to:
print([x.strip() for x in open('basics.py')])

################################################


strings = [
            "hello its me how are you",
            "it's been so many crazy years you've been calling on my door",
            "if you don't wanna see me dancing with somebody",
            ]

print([("if" in x, x) for x in strings])

# Is equal to: ATTENTION ON THE WAY IT CREATES AN AUTOMATIC LOOP AROUND THE STRINGS
theMap = map(lambda s: (True, s) if "if" in s else (False, s), strings)

print(list(theMap))

print("another option:")
secondMap = map(lambda s: s, strings)
print(list(secondMap))

################################################

text = '''
Suppose that communal kitchen years to come perhaps. 
All trotting down with porringers and tommycans to be filled. 
Devour contents in the street. 
John Howard Parnell example the provost of Trinity every mother’s son don’t talk of your provosts and provost of Trinity women and children cabmen priests parsons fieldmarshals archbishops. 
From Ailesbury road, Clyde road, artisans’ dwellings, north Dublin union, lord mayor in his gingerbread coach, old queen in a bathchair. 
My plate’s empty. After you with our incorporated drinkingcup. 
Like sir Philip Crampton’s fountain. Rub off the microbes with your handkerchief. 
Next chap rubs on a new batch with his. Father O’Flynn would make hares of them all. 
Have rows all the same. All for number one. Children fighting for the scrapings of the pot. 
Want a souppot as big as the Phoenix park. Harpooning flitches and hindquarters out of it. 
Hate people all round you. City Arms hotel table d’hôte she called it. Soup, joint and sweet. 
Never know whose thoughts you’re chewing. Then who’d wash up all the plates and forks? Might be all feeding on tabloids that time. 
Teeth getting worse and worse.
'''

print(text[text.find("Philip")-18: text.find("Philip") + 18: 1])

# Is equal to:

myfind = lambda txt, query: txt[txt.find(query)-18: txt.find(query) + 18: 1] if query in txt else -1

print(myfind(text, "Philip32"))


###################################################
# List comprenhension and slicing

stock_prices = [[9.9, 7.8, 5.9, 5.6, 8.3],
                [7.9, 9.6, 9.6, 6.7, 6.8],
                [8.9, 4.7, 8.7, 5.8, 9.7],
                [6.9, 8.4, 7.8, 8.9, 7.6],
                ]

print([stock[::2] for stock in stock_prices])

###################################################
# Slice assignment

visitors = [
    "Firefox", "Corrupted", " Chrome", "Corrupted",
    "Safari", "Corrupted", " Safari", "Corrupted",
    "Chrome", "Corrupted", "Firefox", "Corrupted",
]

visitors[1::2] = visitors[::2]

print(visitors)

###################################################
# List Concatenation

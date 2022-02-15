from collections import defaultdict

persons = [
    {"name" : "John", "age" : 15},
    {"name" : "Elton", "age" : 33},
    {"name" : "Jerry", "age" : 27},
    {"name" : "Clark", "age" : 17},
    {"name" : "Rachel", "age" : 15}
]


sort_age = defaultdict(list)
sort_name = defaultdict(list)
ages = []

for p in persons:
    name = p['name']
    age = p['age']
    sort_age[age].append(name)
    sort_name[len(name)].append(name)
    ages.append(age)

min_age = min(sort_age)
print(sort_age[min_age])
max_sort_name = max(sort_name)
print(sort_name[max_sort_name])
print(sum(ages) // len(ages))
########################################################

def in_sub(string1, string2):
    string1 = list(string1)
    string2 = list(string2)
    string3 = []
    for i in string1:
        for j in string2:
            if i == j:
                string3.append(i)
    print(string3)

print(in_sub('asftgtrgefs', 'aggregergeg'))

############################################################

def in_sub(string1, string2):
    string1 = set(list(string1))
    string2 = set(list(string2))
    string3 = []
    for i in string1:
        for j in string2:
            if i == j:
                string3.append(i)
    print(string3)

print(in_sub('asftgtrgefs', 'aggregergeg'))

########################################################
import random
import string

senames = ['smith', 'pitt', 'harris', 'backer', 'butcher']
domains = ['net', 'com', 'ua', 'ru', 'us']

def random_str(length):
    letter = string.ascii_lowercase
    rand_string = ''.join(random.choice(letter) for i in range(length))
    return(rand_string)

def create_mail(names, dom):
    names = list(names)
    dom = list(dom)
    random_names = random.choice(names)
    random_dom = random.choice(dom)
    print(str(random_names) + '.' + str(random.randint(100, 999)) + '@' + str(random_str(random.randint(5, 7))) + '.' + str(random_dom))

e_mail = create_mail(senames, domains)
print(e_mail)

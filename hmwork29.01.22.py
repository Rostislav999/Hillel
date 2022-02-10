n = 32454500
new_n = str(n)
k = 0
for i in new_n:
    if i > "0":
        None
    else:
        k += 1
print(k)


#####################################
n = 1002000
new_n = str(n)
k = 0
for i in new_n:
    if i > "0":
        k = 0
    else:
        k += 1
print(k)

######################################

my_list_1 = [1, 2, 3, 4, 5]
my_list_2 = [10, 15, 20, 25]
my_result = []
for i in range(len(my_list_1)):
    if i % 2 != 0:
        my_result.append(my_list_1[i])
for i in range(len(my_list_2)):
    if i % 2 == 0:
        my_result.append(my_list_2[i])
print(my_result)


my_list = [1, 2, 3, 4]
new_list = my_list[1:] + [my_list[0]]
print(new_list)



###############################################

my_list = [1, 2, 3, 4]
my_list.pop(0)
my_list.append(1)
print(my_list)

##############################################

my_str = '45 больше чем 34 но меньше чем 56'
int1 = []
for i in my_str.split():
    try:
        int1.append(int(i))
    except ValueError:
        None
print(sum(int1))

###############################################

my_str = "My long string"
l_limit = "o"
r_limit = "g"
sub_str = []
for i in my_str:
    if i != l_limit:
        sub_str.append(i)
    elif i == l_limit:
        sub_str.clear()
        continue
sub_str.pop()
print(''.join(sub_str))
################################################

s = 'qwert'
result_list = []
lenstr = len(s)
for i in range(0, lenstr, 2):
    if i < lenstr - 1:
        result_list.append(s[i] + s[i + 1])
    else:
        result_list.append(s[i] + '_')


#################################################

list = [int(i) for i in input().split()]
k = 0
for i in range(1, len(list) - 1):
    if list[i-1] <list[i] > list[i+1]:
        k += 1
    else:
        None
print(k)


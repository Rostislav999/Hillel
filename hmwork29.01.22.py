a = str(input())
k = 0
for i in a:
  if i == "0":
      k += 1
print(k)



#####################################
num = 1002000
count = 0
for i in str(num)[::-1]:
     if i =='0':
         count += 1
     else:
         break
print(count)

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
list_value = my_list.pop(0)
my_list.append(list_value)
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
l_limit, r_limit = "o", "g"
l_index = my_str.find(l_limit) + 1  # нам не нужен символ 'o'
r_index = my_str.rfind(r_limit)
sub_str = my_str[my_str.find(l_limit) + 1: my_str.rfind(r_limit)]

print(sub_str)
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

list = [1, 9, 1, 3, 4, 1, 9, 1]
k = 0
for i in range(0, len(list) - 1):
    if sum([i-1] + [i+1]) < list[i]:
        k += 1
    else:
        None
print(k)


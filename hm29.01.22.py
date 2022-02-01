my_list = []
i = 0
while i < 9:
    my_list.append(int(input()))
    i += 1
for i in my_list:
    if i > 100:
       print(i)

##################################################

my_list1 = [123, 43, 546, 565, 99, 322, 111]
my_results = []
for i in my_list1:
    if i > 100:
       my_results.append(i)
print(my_results)

###################################################

my_list2 = [434, 345, 322, 113, 34, 11, 555]

sum = my_list2[-1] + my_list2[-2]
if len(my_list2) < 2:
    my_list2.append(0)
    print(my_list2)
else:
    my_list2.append(my_list2[-1] + my_list2[-2])
    print(my_list2)


########################################################
my_string = '0123456789'
my_list3 = []
for i1 in (my_string):
    for i2 in (my_string):
        rez = int(i1 + i2)
        if rez < 100:
            my_list3.append(rez)
print(my_list3)
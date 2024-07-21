my_list = [1,2,3,4,5]
my_list.append(6)
my_list.remove(3)
my_list[0] = 10
print(my_list)

my_dict = {'name': 'anshika', 'age': 21, 'salary': 30000, 'city': 'Lucknow'}
my_dict['domain'] = 'Business Analyst'
del my_dict['age']
my_dict['city'] = 'lucknow'
print(my_dict)

my_set = {2,4,6,8,}
my_set.add(1)
my_set.remove(6)
my_set.discard(8)
my_set.add(12)
print(my_set)
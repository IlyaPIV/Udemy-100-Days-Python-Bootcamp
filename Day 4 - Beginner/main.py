import random

# random_integer = random.randint(1, 10)
# print(random_integer)
#
# # 0.0000000.... - 0.999999999....
# random_float = random.random()
# print(random_float)
# #
# random_number = random.random() * 5


states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia"]
print(states_of_america)

states_of_america.append("Appended") # добавляет элемент в конец

states_of_america.extend(["Extended 1", "Extended 2"])  # добавляет массив
print(states_of_america)

states_of_america.insert(2, "Inserted") # вставляет
states_of_america.insert(4, "Inserted") # вставляет
print(states_of_america)

states_of_america.pop(7)    # вытаскивает
print(states_of_america)

states_of_america.remove("Inserted")    # удаляет первый совпадающий
print(states_of_america)

states_of_america.clear()
print(states_of_america)



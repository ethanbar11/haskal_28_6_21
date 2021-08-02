# Reading Example
path = 'hello.txt'
file_object = open(path, 'r')
print(file_object.readlines())
file_object.close()

# Writing example
path_to_write = 'Bla.txt'
with open(path_to_write, 'w') as file_object_to_write:
    file_object_to_write.write('Hello mama!\n')
    file_object_to_write.write('2222222222')

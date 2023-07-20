import FileUtils as fu
import os




# print(dir(fu.file_handling))

# fu.file_operations.create_file('new.txt')
# fu.file_handling.append_to_file('new.txt','this is a new file from the package')
# print(fu.file_handling.read_file('new.txt'))

# fu.file_operations.rename_file('new.txt','new2.txt')
# fu.file_operations.delete_file('new2.txt')
# fu.file_handling.write_to_file('new.txt','this is new')
# fu.file_operations.delete_file('new.txt')

# # fu.file_operations.rename_file('name.txt','khan.txt')


# # fu.file_operations.create_file('shah.txt')

# print(fu.file_handling.read_file('shah.txt'))

# print(fu.file_statistics.get_file_size('new.txt'))
# print(fu.file_statistics.count_lines('new.txt'))
print(fu.file_statistics.calculate_word_frequency('new.txt'))
# print(fu.file_statistics.analyze_directory('.'))
# print(fu.file_statistics.count_file_extensions('.'))

# print(os.getcwd())
def write_file(file_name, file_contents):
    with open(file_name, mode='w', encoding='utf-8') as log_file:
        log_file.write(file_contents)

def append_file(file_name, file_contents):
    with open(file_name, mode='a', encoding='utf-8') as log_file:
        log_file.write(file_contents)

def read_file(file_name):
    with open(file_name, encoding='utf-8') as log_file:
        for line in log_file:
            print(line)

def clear_file(file_name):
    with open(file_name, mode='w', encoding='utf-8') as log_file:
        log_file.write('')


clear_file('lib/data/logfile.txt')
write_file('lib/data/logfile.txt', "Log 1: 5 bananas added")
append_file('lib/data/logfile.txt', "\nLog 2: 3 bananas subtracted")
read_file('lib/data/logfile.txt')
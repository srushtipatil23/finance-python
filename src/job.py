# Write a code to read the file from input folder with the file name
# and write the file into a new folder called as output in root without using pandas
def basic_word_count(path:str):
    '''
    This is a function to count words in given input file
    :param path: path of input file which is to be read as string
    :return: count of words as integer
    '''
    file = open(path, 'r')
    read_data = file.read()
    per_word = read_data.split("\n")
    return per_word

# function call to read the input file data
total_words = basic_word_count(path = "C:/Users/ASUS/PycharmProjects/finance-python/input/ledger.txt")

# Filter category
word = 'Uber'

def filter_for_category(total_words)->list:
    '''
    This is a function to filter the input file for category UBER
    :param total_words: input file data converted into a list
    :return: filtered data in form of list
    '''
    output_list = []
    for sentence in total_words:
        if word in sentence:
           output_list.append(sentence)

    return output_list

# function call for filtering the data
samp = filter_for_category(total_words)

# Adding \n to get data in separate lines
sample_list = [element + '\n' for element in samp]

# Creating new file to store filtered data
output_file = open(r"C:\Users\ASUS\PycharmProjects\finance-python\output\filtered_output.txt", "w")
output_file.writelines(sample_list)
output_file.close()

# Reading the to check the output
temp = open(r"C:\Users\ASUS\PycharmProjects\finance-python\output\filtered_output.txt", 'r')
temp_data = temp.read()
new_word = temp_data.split("\n")
print("The Filtered Output for category UBER : \n" , new_word)
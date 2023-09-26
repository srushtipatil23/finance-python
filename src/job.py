# Write a code to read the file from input folder with the file name
# and write the file into a new folder called as output in root without using pandas
#dummy

def basic_word_count(path: str):
    '''
    This is a function to count words in given input file
    :param path: path of input file which is to be read as string
    :return: count of words as integer
    '''
    with open(path, 'r') as f:
        read_data = f.read()
        per_word = read_data.split("\n")
    return per_word


def filter_for_category(total_words, filter_word) -> list:
    '''
    This is a function to filter the input file for category UBER
    :param total_words: input file data converted into a list
    :return: filtered data in form of list
    '''
    output_list = []
    for sentence in total_words:
        if filter_word in sentence:
            output_list.append(sentence)

    return output_list


def driver_test(root_path: str, filter_word):

    # Get all sentences as a list
    total_words = basic_word_count(path=root_path + "/input/ledger.txt")

    # Filter based on the criteria
    samp = filter_for_category(total_words, filter_word=filter_word)

    # Adding \n to get data in separate lines
    sample_list = [element + '\n' for element in samp]

    # Creating new file to store filtered data
    with open(root_path + "/output/filtered_output.txt", "w") as f:
        f.writelines(sample_list)


if __name__ == "__main__":
    path = "C:/Users/ASUS/PycharmProjects/finance-python"
    word = 'Uber'
    print("inside main")
    # driver_test(root_path=path, filter_word=word)

import pandas

student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

# Looping through dictionaries:
for (key, value) in student_dict.items():
    print(key)
    print(value)
    pass

student_data_frame = pandas.DataFrame(student_dict)
req_dict = {}
# Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    # Access index and row
    # Access row.student or row.score
    req_dict[row.student] = row.score
print(req_dict)

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

# TODO 1. Create a dictionary in this format:
data = pandas.read_csv('C:\\My_Folder\\Logics_in_python\\day-26-NATO\\nato_phonetic_alphabet.csv')
words_data = {row.letter: row.code for (index, row) in data.iterrows()}
print(words_data)

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.


def generate_nato():
    try:
        user_input = input("Enter a name: ").upper()
        result_dict = {}
        for letter in user_input:
            if letter in words_data.keys():
                result_dict[letter] = words_data[letter]
        output = [words_data[letter] for letter in user_input]
    except KeyError:
        print("There is only letters in alphabets.")
        generate_nato()
    else:
        print(result_dict)
        print(output)


generate_nato()

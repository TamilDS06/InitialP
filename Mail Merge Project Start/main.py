PLACE_HOLDER = "[name]"

with open('./Mail Merge Project Start/Input/Names/invited_names.txt', mode='r') as list_names:
    names = list_names.readlines()

with open('./Mail Merge Project Start/Input/Letters/starting_letter.txt', mode='r') as example_letter:
    new_letter = example_letter.read()
    for name in names:
        stripped_name = name.strip()
        new_letter = new_letter.replace(PLACE_HOLDER, stripped_name)
        with open(f'./Mail Merge Project Start/Output/ReadyToSend/Letter_to_{name.strip()}', mode='w') as file_write:
            file_write.write(new_letter)

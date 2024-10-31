
def combine_marks(names, test1_marks, test2_marks):
    student_data = []  # Initialize the student_data list
    for i in range(len(names)):
        first_name, last_name = names[i].split()  # Split full name into first and last name
        student_data.append({
            'first_name': first_name,
            'last_name': last_name,
            'test1': test1_marks[i],
            'test2': test2_marks[i]
        })
        
  # Check if the list is not empty before deleting the last item
    if student_data: 
        # Delete the last dictionary
        del student_data[-1]  
    return student_data

def get_summary(character):
    return f"{character['name']} (level {character['level']} {character['race']} {character['class']}) - HP: {character['hp']}"

def is_vowel(character):
    return character.lower() in 'aeiou'  # Check if the character is a vowel

def count_vowels_iter(sentence):
    count = 0
    for char in sentence:
        if is_vowel(char):
            count += 1
    return count

def main():
    # This main() function is here in case you want to test your functions with sample data

    # part 1
    names = ['Lucie Manette', 'Charles Darnay', 'Sydney Carton']
    test1_marks = [34.0, 75.5, 58.0]
    test2_marks = [47.5, 82.0, 63.5]

    student_data = combine_marks(names, test1_marks, test2_marks)
    print(student_data)

    # part 2
    character = {
        'name': 'Grimbor',
        'race': 'Dwarf',
        'class': 'Warrior',
        'hp': 58,
        'level': 9,
    }
    summary = get_summary(character)
    print(summary)

    # part 3
    print(f'{is_vowel("t")=}')   # prints False
    print(f'{is_vowel("o")=}')   # prints True
    print(f'{is_vowel("u")=}')   # prints True

    # part 4
    print(f'{count_vowels_iter("this is a sentence")=}')   # prints 6
    print(f'{count_vowels_iter("loud")=}')                 # prints 2
    print(f'{count_vowels_iter("rebel")=}')                # prints 2

if __name__ == "__main__":
    main()             
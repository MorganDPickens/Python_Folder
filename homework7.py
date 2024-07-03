#Morgan Pickens
#11/29/2023
#HW7: File statistics

import string

#--------------------------------------------------------------------------------
                                # Section 1
# In this section, we write the function to get the file name that you want
# to check the statistics on.

#test case issues i couldn't get the file to actually not error when getting the
#file name so i had to make some adjustments to my main function to fix it. I also
#added in this strip part to remove any possible whitespaces to remove any issues here.
#--------------------------------------------------------------------------------

# This will get your file name make sure you include the extenstion. 
def get_input_filename():
    return input("Enter the input filename: ").strip()

# This will create the output statistic file
def get_output_filename(input_filename):
    filename, extension = input_filename.split('.')
    return f"{filename}stats.txt"

#--------------------------------------------------------------------------------
                                # Section 2
#In this section of the program we create our function to count the characters
#were listed in the assignment
#--------------------------------------------------------------------------------

def count_digit(char):
    return char.isdigit()

def count_whitespace(char):
    return char.isspace()

def count_word_character(char):
    return char in '@#$%&+-=<>*/'

def count_vowel(char):
    return char.lower() in 'aeiou'

def count_consonant(char):
    return char.isalpha() and not count_vowel(char)

def count_whitespace(char):
    return char.isspace()

def count_punctuation(char):
    return char in '!~`^()_{}[]|\\;:\"\',.?'

#---------------------------------------------------------------------------------
                        # Section 3
#In this section we have to create the actual statistics counter
#and the function to write them.

# creating the statistics counter took some time to understand but after watching
# a video on using the sum function to count what we needed i was able to understand
# how this works.
                        
#----------------------------------------------------------------------------------

def statisticsCounter(contents):
    stats = {
        'characters': len(contents),
        'letters': sum(1 for char in contents if char.isalpha()),
        'consonants': sum(1 for char in contents if count_consonant(char)),
        'digits': sum(1 for char in contents if count_digit(char)),
        'spaces': sum(1 for char in contents if count_whitespace(char)),
        'word_characters': sum(1 for char in contents if count_word_character(char)),
        'punctuation': sum(1 for char in contents if count_punctuation(char))
    }
    return stats

def statisticsWriter(output_filename, input_filename, stats):
    with open(output_filename, 'w') as output_file:
        output_file.write(f"Statistics for source file: {input_filename}\n")
        for stat, value in stats.items():
            output_file.write(f"{stat}: {value}\n")


#----------------------------------------------------------------------------------
                        # Section 4
#In this section we create our main function
#In this section i ran into the issue where i couldn't get the file name to
#to register but this was fixed. 
#----------------------------------------------------------------------------------
def main():
    while True:
        input_filename = get_input_filename()

        try:
            with open(input_filename, 'r') as input_file:
                contents = input_file.read()
                stats = statisticsCounter(contents)
                output_filename = get_output_filename(input_filename)
                statisticsWriter(output_filename, input_filename, stats)
                print(f"Statistics file created{output_filename}")
        except FileNotFoundError:
            print(f"Error: File {input_filename} not found. try to reEnter.")
        except Exception as e:
            print(f"Error: {e}")

        repeat = input(" would you like to try another file? (yes/no): ").lower()
        if repeat != 'yes':
            break

if __name__ == "__main__":
    main()

#How did i go about starting this assignment? Not gonna lie to me awhile to get
#Started but i just took it step by step i got stuck trying to get the program
#To read the file

#testing i ran testing myself by making a test file and running the code to see
# if it will print another page. But my homework does me the homeword specificaitons

#I learned alot form this assignment on input and output on files. 

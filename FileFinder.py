#Morgan Pickens
#12/11/2023
#Hw8: Working with Data Files and List

#Input section
print("Welcome to the program!")

#Creating a variable for our error message
file_path_valid = False

#This is to make sure you type the correct file path
if not file_path_valid:
    data_file_path = input("Please enter the full path of the dataset file: ")

    #Attempt to open the file to check if it exists
    try:
        with open(data_file_path, 'r'):
            file_path_valid = True  # Set the flag to True if the file exists
    except FileNotFoundError:
        print("I'm sorry, that file name did not work. Please try again :(")

                     # Functions section
                     
# This function takes two lists and uses a for loop to iterate through the length
# of the lists to count the number of matches
def match_count(data, key):
    count = 0
    for i in range(len(data)):
        if data[i] == key[i]:
            count += 1
    return count

#This function will give us our results of the List/Key Pair
def process_data(file_path, key):
    results = []
    with open(file_path, 'r') as file:
        for line in file:
            dataset = line.strip().split(',')

            matches = match_count(dataset, key)

            results.append({
                "Data": dataset,
                "Matches": matches
            })
    return results

                       #File Finder
#INSTRUCTIONS FOR THE FILE FINDER
#make sure you replace this part of the code with the correct file path
#when you run the program make sure you put the complete file path as well
key_file = r"C:\Users\morga\Documents\keylist.txt.txt"
key_data = open(key_file, 'r').read().strip().split(',')

output_results = process_data(data_file_path, key_data)

#Output to print results, including the number of lists, matches, and average
total_lists = len(output_results)
total_matches = sum(result["Matches"] for result in output_results)
average_matches = total_matches / total_lists if total_lists > 0 else 0

for result in output_results:
    print("Data:", result["Data"])
    print("Matches:", result["Matches"], "\n")

#ADDED BASED OFF THE EXAMPLE GIVEN IN THE INSTRUCTIONS
print(f"Number of Lists in the File: {total_lists}")
print(f"Total Matches: {total_matches}")
print(f"Average Matches per List: {average_matches}")


# A terminal-based program for analyzing movie awards data.
# You must include the code listed below. You may add your own additional functions, variables, etc. 
# You may not import any modules.
# You may only use built-in functions that directly support strings, lists, dictionaries, sets, and tuples.
# Remember to include docstrings for your functions and comments throughout your code.
# awards_data.py
# Data is provided below to be used with awards.py. Both files must remain in the same directory.
# Do not modify the code in this section.
# You may not hardcode (manually enter in the code) any other data.


# Screen Actors Guild Awards 2022
SAG = ["Everything Everywhere All at Once", "Top Gun: Maverick"]

# Academy Awards (Oscars) 2023
oscars = ["Everything Everywhere All at Once", "All Quiet on the Western Front", "Guillermo del Toro's Pinocchio", "Navalny", "All Quiet on the Western Front", 
          "Everything Everywhere All at Once", "Women Talking", "Avatar: The Way of Water", "All Quiet on the Western Front", "Black Panther: Wakanda Forever",
          "Everything Everywhere All at Once", "The Whale", "All Quiet on the Western Front", "Top Gun: Maverick"]

# National Board of Review Awards 2022
NBR = ["Top Gun: Maverick", "The Banshees of Inisherin", "All Quiet on the Western Front", "Marcel the Shell with Shoes On", "Close", "Sr.", "Women Talking"]

# Independent Spirit Awards 2023
ISA = ["Everything Everywhere All at Once", "Aftersun", "All The Beauty And The Bloodshed", "Everything Everywhere All at Once", "Joyland", "Tár", "Everything Everywhere All at Once"]

# GLAAD (Gay & Lesbian Alliance Against Defamation) Media Awards 2023 
GLAAD = ["Bros", "The Inspection", "Fire Island", "Anything's Possible", "Framing Agnes"]

# NAACP (National Association for the Advancement of Colored People) Image Awards 2023
NAACP = ["Black Panther: Wakanda Forever", "Bantú Mama", "The Inspection", "Wendell & Wild", "Civil"]



# ******************************************************************************************************
# ******************************************************************************************************
# Data is imported from the included awards_data.py file. Both files must remain in the same directory.
# Do not modify the code in this section.
# You may not hardcode (manually enter in the code) any other data.
award_list_names = ['sag', 'oscars', 'nbr', 'isa', 'glaad', 'naacp']
award_list_options = [SAG, oscars, NBR, ISA, GLAAD, NAACP]
# ******************************************************************************************************



# ******************************************************************************************************
# DEFINE FUNCTIONS HERE

def count_awards(movie_title):
    ''''''
    count = 0
    movie_title = movie_title.strip().lower()
    for award_types in award_list_options:
        for movies in award_types:
            if movie_title == movies.lower():
                count += 1

    return count

def print_award_winners(organization):
    organization = organization.strip().lower()
    index = award_list_names.index(organization)
    for winning_movies in award_list_options[index]:
        print(winning_movies)




# ******************************************************************************************************
print("Awards Data Program")

# DEFINE MAIN CODE BELOW

# You may find the following strings helpful for the interface design:
# "\nSelect 1 to search a specific movie, 2 to print specific rewards results, 0 to end: "
# "Please enter the movie title you would like to search: "
# "\nPlease choose one of the following awards lists:\nOscars\nSAG\nNBR\nISA\nGLAAD\nNAACP\n\n"
# "Awards list not found."
# "You must select either 1, 2, or 0."
# "Thank you for using the awards data program."
# "--Number of Awards Won--"
# "--Requested Award Winners--"


num_select = 1 
while num_select != 0:
    num_select = int(input('\nSelect 1 to search a specific movie, 2 to print specific rewards results, 0 to end: '))
    if num_select == 1:
        movie = input('Please enter the movie title you would like to search: ')
        print("--Number of Awards Won--")
        print(count_awards(movie))
    elif num_select == 2:
        award_choice = input('\nPlease choose one of the following awards lists:\nOscars\nSAG\nNBR\nISA\nGLAAD\nNAACP\n\n')

        for awards in award_list_names:
            if award_choice.strip().lower() not in award_list_names:
                print('Awards list not found.')
                break
            else:
                print('--Requested Award Winners--')
                print_award_winners(award_choice)
                break
    elif num_select == 0:
        print('Thank you for using the awards data program.')
        exit()        
    else:
        print('You must select either 1, 2, or 0.')



num_select = 1 
while num_select != 0:
    num_select = int(input('\nSelect 1 to search a specific movie, 2 to print specific rewards results, 0 to end: '))
    if num_select == 1:
        movie = input('Please enter the movie title you would like to search: ')
        print("--Number of Awards Won--")
        print(count_awards(movie))
    elif num_select == 2:
        award_choice = input('\nPlease choose one of the following awards lists:\nOscars\nSAG\nNBR\nISA\nGLAAD\nNAACP\n\n')

        for awards in award_list_names:
            if award_choice.strip().lower() not in award_list_names:
                print('Awards list not found.')
                break
            else:
                print('--Requested Award Winners--')
                print_award_winners(award_choice)
                break
    elif num_select == 0:
        print('Thank you for using the awards data program.')
        exit()        
    else:
        print('You must select either 1, 2, or 0.')

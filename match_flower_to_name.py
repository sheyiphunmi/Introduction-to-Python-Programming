#create a dictionary from flowers.txt
def flower_names(filename):
    flower_dict = {}
    with open(filename, 'r') as names:
        for line in names:
            letter = line.split(": ")[0].lower()
            flower = line.split(": ")[1].lower().strip()
            flower_dict[letter] = flower                                                 
    return flower_dict
            
        


#function to ask for user's first and last name
def main():
    flower_dict1 = flower_names('flowers.txt')
    your_name = input('Enter your First [space] Last name only:')
    first_letter = your_name[0].lower()
    print("Unique flower name with the first letter: {}".format(flower_dict1[first_letter]))
    
 
        
main()


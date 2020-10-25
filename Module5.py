"""
Eugene Bellau
Agile UNO Module 5
Strings and Lists
"""

from sys import exit  # This command will import the exit command from the system

import requests # This command will import the requests library


site_data = {} # This command will store the data in the .csv file into a dictonary

with open("sites.csv", "r") as infile: # This command will open the .csv file in the context manager with read permissions
    data = infile.read() # This command will read the contents of the .csv file
    sites = data.split(",") # This command will split the data in the .csv file with the comma and create a list

for site in sites: # This command will pull each site in the sites list
    site_data[site] = requests.get(site) # This command will access each site in the dictonary

# This command will print out each site and the value of the site
for key, value in site_data.items():
    print(f"\n{key} : {value}")




# 1
# Using String Slicing print out each URL extension

for site in sites: # This command will pull each site in the sites list
    print(site[-4:]) # This command will print each item in the string starting at the fourth to last item



#2
# Print out any sites that end with .com 

for site in sites: # This command will pull each site in the sites list
    if '.com' in site: # This command will look to see if .com is apart of the site
        print(site) # This command will print the site if the if statement is true


#3 
# Convert each site name to UPPER case and print out site address

for site in sites: # This command will pull each site in the sites list
    print(site.upper()) # This command will print each site in uppercase


#4
# Add a new site to the .csv file from the user's input, reverse the order of the list and print out the list
with open("sites.csv", "r+") as infile: # This command will open the .csv file in the context manager with write permissions
    sites = data.split(",") # This command will split the data in the .csv file with the comma and create a list
    sites.append(input("Please enter a new site: ")) # This command will ask the user to enter a new site and append it to the dictonary
    sites.reverse() # This command will reverse the order of the sites
    print(sites) # This command will print the list
    

#5
# Print out the Server of the response of the URL for each item in the list
for site in sites: # This command will pull each site in the sites list
    MySiteData = requests.get(site) # This command will access each site in the dictonary
    print(f"{MySiteData.headers.get('server')} \n") # This command will print the server information that was listed in each site's header information


#6
# Exit the program using the sys module's exit function

exit() # This command will exit the program
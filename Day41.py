website_dictionary = {"name": None, "url": None, "description": None, "rating": None}

name = input("Enter the name of the website: ")
url = input("Enter the url of the website: ")
description = input("Enter the description of the website: ")
rating = input("Enter the rating of the website: ")

website_dictionary["name"] = name
website_dictionary["url"] = url
website_dictionary["description"] = description
website_dictionary["rating"] = rating

for key, value in website_dictionary.items():
    print(key + ":", value)

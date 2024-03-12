""" A Simple Python Script to generate the band name """

# Print the Greeting message to the user
print("Hiya!,Welcome to Band Name Generator")

# get the city where the user grown up
city_name = input("What's the name of the city you grew up in?\n")

# get the user's pet name
pet_name = input("What is your pet's name?\n")

# print the suggested band name city_name + pet_name to the user
print("Your band name van be something like " +
      "\"" + city_name.capitalize() + " " + pet_name.capitalize() + "\"")

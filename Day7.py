likesPizza = input("Do you like pizza?: ")
if likesPizza == "yes":
    print("Pizza is my favorite food!")
    favoriteTopping = input("What is your favorite topping?: ")
    if favoriteTopping == "pepperoni":
        print("I don't like pepperoni because I can't eat it!")
        print("I prefer green peppers.")
    else:
        print("I like " + favoriteTopping + " too!")
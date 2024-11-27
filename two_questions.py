print("Let's play 2 Questions!")
answer1 = input("Is it an animal, vegetable, or mineral? ")
answer2 = input("Is it bigger than a breadbox? ")

if answer1 == "animal" and answer2 == "yes":
print("I think you're thinking of an elephant!")
elif answer1 == "animal" and answer2 == "no":
print("I think you're thinking of a mouse!")
elif answer1 == "vegetable" and answer2 == "yes":
print("I think you're thinking of a pumpkin!")
elif answer1 == "vegetable" and answer2 == "no":
print("I think you're thinking of a pea!")
elif answer1 == "mineral" and answer2 == "yes":
print("I think you're thinking of a mountain!")
elif answer1 == "mineral" and answer2 == "no":
print("I think you're thinking of a rock!")

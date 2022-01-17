last_semester_gradebook = [["politics", 80], ["latin", 96], ["dance", 97], ["architecture", 65]]

# Your code below: 
subjects = ["physics", "calculus", "poetry", "history"]
grades = [98, 97, 85, 88]

gradebook = [["physics", 98], ["calculus", 97], ["poetry", 85], ["history", 88]]

# adding elements to item
gradebook.append(["computer science", 100])
gradebook.append(["visual arts", 93])

# increasing virtual art scores
gradebook[-1][-1] += 5

# remove scores from poetry
gradebook[2].remove(85)

# adding pass to virtual arts element
gradebook[2].append("Pass")
#print(gradebook)

# combining the past and present sems
full_gradebook = last_semester_gradebook  + gradebook
print(full_gradebook)
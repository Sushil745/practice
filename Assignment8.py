sports = {"Rahul", "Anil", "Priya", "Kiran"}

music = {"Priya", "Kiran", "Meena", "Arun"}

# 1. Students who joined either activity
either_activity = sports.union(music)
print("Students who joined either activity:")
print(either_activity)

# 2. Students who joined both activities
both_activity = sports.intersection(music)
print("\nStudents who joined both activities:")
print(both_activity)

# 3. Students who joined only sports
only_sports = sports.difference(music)
print("\nStudents who joined only sports:")
print(only_sports)

# 4. Students who joined only music
only_music = music.difference(sports)
print("\nStudents who joined only music:")
print(only_music)
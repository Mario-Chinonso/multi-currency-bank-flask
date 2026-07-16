number = 5
while number > 0:
    print(number)
    number-=1

names_of_students_who_passed=["Emeka","Jude","Obi"]


names_of_students_who_passed.append("James")
names_of_students_who_passed.insert(2,"Okonkwo")
names_of_students_who_passed.remove("Emeka")
print(names_of_students_who_passed)

goals = {
    "Carreer":"Data Scientist",
    "Works":"Ai chatbot",
    "Age":32
}

print("My future goals: ",list(goals.keys()))
print("Carreer: ",goals["Carreer"])

words = " I love my mom! "
clean_words = words.strip().upper()
word2 = " I LOVE MY MOM! "
new_words = word2.strip().lower()
print(clean_words)
print(new_words)
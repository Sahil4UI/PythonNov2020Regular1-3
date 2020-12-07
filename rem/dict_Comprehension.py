keys=["roll","name","marks","address"]
values = [101,"Ravi",90,"Delhi"]

StudentDictionary = {key:value for (key,value) in zip(keys,values) }
print(StudentDictionary)
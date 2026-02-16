# mylist = [1,2,3]

# myString = 'mustafa'

# print(len(mylist))
# print(len(myString))




class Movie():
    def __init__(self, title, director, duration):
        self.title = title
        self.director = director
        self.duration = duration
    def __str__(self):
        return f"{self.title} by {self.director}"
    
    def __len__(self):
        return self.duration

m = Movie("film adı", 'yönetmen', 120)
print(str(m))
print(len(m))
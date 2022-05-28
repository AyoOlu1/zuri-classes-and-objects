class Student:
    # [assignment] Skeleton class. Add your code here
    def __init__(self, name, age, tracks, score):
        self.name = name
        self.age = age
        self.tracks = tracks
        self.scores = score
        
    def change_name(self, new_name):
        self.name = new_name
        if type(new_name) == str:
            return new_name
        else:
            return "Enter a string!"

    def change_age(self, new_age):
        self.age = new_age
        if type(new_age) == int:
            return new_age
        else:
            return "Enter a number!"

    def add_track(self, new_track):
        track_list = self.tracks
        track_list.append(str(new_track))
        return track_list

    def get_score(self):
        return self.scores




Bob = Student(name="Bob", age=26, tracks=["FE","BE"],score=20.90)


# Expected methods
Bob.name
Bob.change_name("jsgdjshd")
Bob.add_track("UI/UX")
Bob.change_age(30)
Bob.add_track("sdsd")
Bob.get_score()

class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

        def bark(self):
            print("Woof! Woof!")

        def celebrate_Birthday(self):
            self.age += 1
            print(f"Happy birthday! {self.name} is now {self.age} years old.")

        def get_Info(self):
            return f"Dog Name: {self.name}, Age: {self.age}"


if __name__ == "__main__":
    my_dog = Dog("Max", 5)
    print(my_dog.get_Info())
    my_dog.bark()
    my_dog.celebrate_Birthday()
    print(my_dog.get_Info())
    
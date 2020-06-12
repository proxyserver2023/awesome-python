name = "Alamin"
age = 25

print(f"Hello, {name}. You are {age}")
print(f"{5*5}")


def to_lowercase(input):
    return input.lower()


name = "Alamin Mahamud"
print(f"{to_lowercase(name)} is awesome!")
print(f"{name.lower()} is F*ckin awesome!")


class Rockstar:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def __str__(self):
        return f"{self.first_name} {self.last_name} is {self.age}."

    def __repr__(self):
        return f"{self.first_name} {self.last_name} is {self.age}. Surprise!"


new_rockstar = Rockstar("Alamin", "Mahamud", 25)
print(f"{new_rockstar}")
print(f"{new_rockstar!r}")


# Multiline f-strings
name = "Alamin"
profession = "Engineer"
affiliation = "BriteCore"
message = (
    f"Hi {name}. "
    f"You are a/an {profession}. "
    f"You work in {affiliation}."
)
print(message)

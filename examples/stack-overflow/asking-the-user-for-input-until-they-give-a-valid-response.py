#!usr/bin/env python3
#https://stackoverflow.com/questions/23294658/asking-the-user-for-input-until-they-give-a-valid-response

while True:
    try:
        age = int(input("Please enter your age."))
    except ValueError:
        print("Sorry, I didn't understand that.")
        continue
    else:
        break

if age >= 18:
    print("You are able to vote in the USA.")
else:
    print("You are not eligible to vote.")



# implementing your own validation rules
while True:
    data = input("Please enter a loud message.(must be all caps)")
    if not data.isupper():
        print("Sorry, your response was not loud enough.")
        continue
    else:
        break

while True:
    data = input("Pick an answer from A to D:")
    if data.lower() not in ('a', 'b', 'c', 'd'):
        print("Not an appropriate choice.")
    else:
        break


# Combining exception handling and custom validation:
while True:
    try:
        age = int(input("Please enter your age."))
    except ValueError:
        print("Sorry, I didn't understand that.")
        continue

    if age < 0:
        print("Sorry, your response must not be negative.")
        continue
    else:
        break

if age >= 18:
    print("You are eligible to vote in USA.")
else:
    print("You are not eligible to vote in USA.")


# Encapsulating it into one-function
def get_non_negative_int(prompt):
    while True:
        try:
            value = int(input(prompt))
        except ValueError:
            print("Sorry! I didn't understand that.")

        if value < 0:
            print("Sorry! you can't enter negative number.")
            continue
        else:
            break

    return value


age = get_non_negative_int("Please enter your age.")
kids = get_non_negative_int("Please enter the number of children you have.")
salary = get_non_negative_int("Please enter your yearly earnings. in Dollars.")


# Putting it alltogether
def sanitised_input(prompt, type_=None, min_=None, max_=None, range_=None):
    if min_ is not None and max_ is not None and max_ < min_:
        raise ValueError("min_ must be less than or equal to max_")

    while True:
        ui = input(prompt)
        if type_ is not None:
            try:
                ui = type_(ui)
            except ValueError:
                print("Input type must be {0}.".format(type_.__name__))
                continue
        if max_ is not None and ui > max_:
            print("Input value must be less than or equal to {0}".fomrat(max_))
        elif min_ is not None and ui < min_:
            print("Input must be greater than or equal to {0}.".format(min_))
        elif range_ is not None and ui not in range_:
            if isinstance(range_, range):
                template = "Input must be between {0.start} and {0.stop}".format(range_)
            else:
                template = "Input must be {0}."
                if len(range_) == 1:
                    print(template.format(*range_))
                else:
                    print(template.format(
                        " or ".join(
                            ", ".join(
                                (
                                    map(str, range[:-1]),
                                    str(range_[-1])
                                )
                            )
                        )
                    ))

        else:
            return ui

age = sanitised_input("Enter you age:", int, 1, 10)
answer = sanitised_input("Enter your answer:",
                         str.lower,
                         range_=('a', 'b', 'c', 'd', 'e'))

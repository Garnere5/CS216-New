# Author - Earl Garner
# Date - 03-28-2026
#
#
# Starting character
Norm = {
    "name": "Norm the Forester",
    "health": 100,
    "attack" : 50,
}

# TODO: Add at least two more attributes to Norm
# (include "attack" for battle)
# Second character 
Earl = {
    "name": "Earl the bowler",
    "health": 100,
    "attack": 40,
}
# TODO: Create two additional characters
# Third character 
Ethan = {
    "name": "Ethan the ragebaiter",
    "health": 100,
    "attack": 30,
}

def update_health(character, amount):
    # TODO: update health
    # ensure it stays between 0 and 100
    for key in character:
        if key == "health":
            character[key] += amount
            if character[key] < 0:
                character[key] = 0
            elif character[key] > 100:
                character[key] = 100
    pass


def display_character(character):
    # TODO: print name
    # TODO: print health
    # TODO: print other attributes
    for key in character:
        print(f"{key}: {character[key]}")
    pass


def attack(attacker, defender):
    # TODO:
    # get attack value
    # reduce defender health using update_health
    # print attack message
    for key in attacker:
        if key == "attack":
            attack_value = attacker[key]
            update_health(defender, -attack_value)
            print(f"{attacker['name']} attacks {defender['name']} for {attack_value} damage!")
            

    pass


# --- User Input for New Attribute ---
def add_attribute(Norm):
    attr_name = input("Enter attribute name: ")
    attr_value = int(input("Enter value: "))
    Norm[attr_name] = attr_value
# TODO: ask user for attribute name
# TODO: ask user for value
# TODO: add to Norm dictionary


# --- Test your functions ---
print(add_attribute(Norm))
update_health(Norm, -20)

# TODO: call attack between two characters
update_health(Earl, -10)


update_health(Ethan, -15)

display_character(Norm)
print()

# TODO: display your other two characters
#Second character
display_character(Earl)
print()

#Third character
display_character(Ethan)
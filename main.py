# SCOPE IN PYTHON

# global Constants
SAMPLE_VAR = "global"
POTION_STRENGTH = 'global weak'
PLAYER_HEALTH = '100%'
GAME_LEVEL = 3
NUM_OF_ENEMIES = 1


# enclosing scope (nested scope)
def outer_function():
    outer_variable = "outer"

    def inner_function():
        # outer_variable not found in local so python searches in enclosing scope
        print(f"enclosing scope: {outer_variable}")

    inner_function()


outer_function()


# LOCAL SCOPE - 1

def local_scope_fn():
    # this is a local variable
    SAMPLE_VAR = "local"
    print(f"local scope: {SAMPLE_VAR}")


local_scope_fn()
print(f"global scope: {SAMPLE_VAR}")


# LOCAL SCOPE - 2

def drink_potion():
    POTION_STRENGTH = 'local strong'
    print(f"local potion strength: {POTION_STRENGTH}")


drink_potion()
print(f"global potion strength: {POTION_STRENGTH}")


# GLOBAL SCOPE

def game():
    def drink_potion():
        print(f"player health local: {PLAYER_HEALTH}")

    drink_potion()


game()
print(f"player health global: {PLAYER_HEALTH}")


# NOTE: there is no block scope in python

def create_enemy():
    enemies = ["Skeleton", "Zombie", "Alien"]

    # ternary block (notice new_enemy is local to function)
    new_enemy = enemies[1] if GAME_LEVEL < 5 else enemies[2]

    # alternative if-else block
    # new_enemy would be available outside the if-else block
    # also applicable if it was not in a function

    # if GAME_LEVEL < 5:
    #     new_enemy = enemies[0]
    # else:
    #     new_enemy = enemies[2]

    print(f"from block scope: {new_enemy}")


create_enemy()


# modifying global scope
# not good practise to modify global constants

def increase_enemies():
    global NUM_OF_ENEMIES

    print(f"enemies not modified global: {NUM_OF_ENEMIES}")
    NUM_OF_ENEMIES += 2

    return NUM_OF_ENEMIES


NUM_OF_ENEMIES = increase_enemies()
print(f"enemies modified global: {NUM_OF_ENEMIES}")

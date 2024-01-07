# no returns for functions print instead for ease of testing

# It should then print out each name, in number order, using print.

def roll_call_dwarves(l):
    if l :
        for i in range(len(l)):
            print(f"{i+1}. {l[i]}")
        return
    print("where are the dwarves?")


# It should then capitalize each element and add an exclamation point at the end. The return value of this function should be a list,
def summon_captain_planet(l):

    refact = [el.capitalize() + "!" for el in l]

    print(refact)

def long_planeteer_calls(l):
    for i in l:
        if(len(i) > 4 ):
            print("True")
            return
    
    print("False")


# def find_the_cheese(l): => prints true or false
#     cheeses = ["cheddar", "gouda", "camembert"]
#     ans = any(cheese in l for cheese in cheeses)
#     print(ans)


def find_the_cheese(foods):
    cheeses = ["cheddar", "gouda", "camembert"]
    for food in foods:
        if food in cheeses:
            print(food)

    return None


find_the_cheese(['carrot', 'potato', 'gouda'])
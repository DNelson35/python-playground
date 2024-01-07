katz_deli = []

# Build the line() function that shows everyone their current place in the line. If there is nobody in line, it should say "The line is currently empty.".

def line(l):
    if l :
        message = f"The line is currently: "
        for index, name in enumerate(l):
            if index != len(l) - 1:
                message += f"{index+1}. {name} "
            else: 
                message += f"{index+1}. {name}"

        print(message)
        return
    
    print("The line is currently empty.")

# Build a function that a new customer will use when entering the deli. The take_a_number() function should accept two arguments, the list for the current line of people (katz_deli), and a string containing the name of the person joining the end of the line. The function should call out (i.e., print) the person's name along with their position in line.

def take_a_number(l, name):
    l.append(name)
    print(f"Welcome, {name}. You are number {len(l)} in line.")


# Build the now_serving() function which should call out (print) the next person in line and then remove them from the front. If there is nobody in line, it should call out (print) that "There is nobody waiting to be served!".

def now_serving(l):
    if l:
        print(f"Currently serving {l[0]}")
        del l[0]
        return
    print("There is nobody waiting to be served!")
    


katz_deli = []

take_a_number(katz_deli, "Ada") #=> Welcome, Ada. You are number 1 in line.
take_a_number(katz_deli, "Grace") #=> Welcome, Grace. You are number 2 in line.
take_a_number(katz_deli, "Kent") #=> Welcome, Kent. You are number 3 in line.

line(katz_deli) #=> "The line is currently: 1. Ada 2. Grace 3. Kent"

now_serving(katz_deli) #=> "Currently serving Ada."

line(katz_deli) #=> "The line is currently: 1. Grace 2. Kent"

take_a_number(katz_deli, "Matz") #=> Welcome, Matz. You are number 3 in line.

line(katz_deli) #=> "The line is currently: 1. Grace 2. Kent 3. Matz"

now_serving(katz_deli) #=> "Currently serving Grace."

line(katz_deli) #=> "The line is currently: 1. Kent 2. Matz"

now_serving(katz_deli) #=> "Currently serving kent."
now_serving(katz_deli) #=> "Currently serving Matz."
now_serving(katz_deli) #=> "There is nobody waiting to be served!"
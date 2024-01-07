# You're hosting a conference and need to print badges for the speakers. Each badge should read: "Hello, my name is _____." Write a badge_maker() function that, when provided a person's name, will create and return the message, e.g.:

def badge_maker(name):
    return f"Hello, my name is {name}"

# Write a batch_badge_creator() function that takes a list of names as an argument and returns a list of badge messages.

def batch_badge_creator(l):
    batch = [badge_maker(name) for name in l]
    return batch

# Return a new list of strings representing room assignments in the form of: "Hello, _____! You'll be assigned to room _____!"

def assign_rooms(names):
   message = lambda name, index: f"Hello, {name}! You'll be assigned to room {index}!"

   assigned = [message(name, index+1) for index, name in enumerate(names)]

   return assigned

# Now you have to tell the printer what to print. Create a function called printer() that will output first the results of the batch_badge_creator() function, and then the output of the assign_rooms() function, to the screen.

def printer(l):
   joined = batch_badge_creator(l) + assign_rooms(l)

   for i in joined:
        print(i)

printer(["Arel", "Carol"])



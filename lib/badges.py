# You're hosting a conference and need to print badges for the speakers. Each badge should read: "Hello, my name is _____." Write a badge_maker() function that, when provided a person's name, will create and return the message, e.g.:

def badge_maker(name):
    return f"Hello, my name is {name}"

# Write a batch_badge_creator() function that takes a list of names as an argument and returns a list of badge messages.

def batch_badge_creator(l):
    batch = [badge_maker(name) for name in l]
    return batch

def assign_rooms(l):
    message = f"Hello, {name}! You'll be assigned to room {index}!"

    assigned = [message for name , index in l]

    print(assigned)

assign_rooms(["Arel", "Carol"])


class Book:

    def __init__(self, title, page_count):
        self.title = title
        self.page_count = page_count

    def get_page_count(self):
        return self._page_count
    
    def set_page_count(self, count):
        if type(count) != int:
            print("page_count must be an integer")
        else:
            self._page_count = count

    def turn_page(self):
        print("Flipping the page...wow, you read fast!")
    
    page_count = property(get_page_count, set_page_count)


Wheel = Book("Wheel of Time", 1200)

Wheel.turn_page()
Wheel.page_count = "not a number"
Wheel.page_count = 1400
print(Wheel.page_count)


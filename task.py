class Book:
    def __init__(self,name,title,author_name,price):

        name = input('Enter the book name :')
        title = input('Enter the title :')
        auther_name = input('Enter the auther_name:')
        price = input('Enter the price of the book :')

        self.name = name
        self.title = title
        self.auther_name = auther_name
        self.price = price

    def mybook(self):
        print('book name is %s title is %s auther_name is %s price %d' % (self.name, self.title, self.auther_name, self.price))

n = int(input('Enter how many books you want to add:'))
for i in range(n):
    x = Book('Annie','short story','fathima','100')
    x.mybook()



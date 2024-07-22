class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.available = True
        print(f":: Book() - title: {title} // author: {author}")

    def borrow(self):
        if self.available:
            self.available = False
            print(f"::Book.borrow - El libro {self.title} ha sido prestado")
        else:
            print(f"::Book.borrow - El libro {self.title} no está disponible")                        

    def return_book(self):
        self.available = True
        print(f"::Book.return_book - El libro {self.title} ha sido devuelto")       

#-------------------------------------------------------------

class User:
    def __init__(self, name, user_id):
        self.name = name
        self.user_id = user_id
        self.borrowed_books = []
        print(f":: User() - name: {name} // user_id: {user_id}")

    def borrow_book(self, book):
        if book.available:
            book.borrow()
            self.borrowed_books.append(book)
            print("::User.borrow_book - True")
        else:
            print(f"::User.borrow_book - El libro {book.title} no está disponible")                        

    def return_book(self,book):
        if book in self.borrowed_books:
            book.return_book()
            self.borrowed_books.remove(book)
            print("::User.return_book - True")            
        else:
            print(f"::User.return_book - El libro {book.title} no está en la lista de prestados") 

#-------------------------------------------------------------

class Library:
    def __init__(self):
        self.books = []
        self.users = []

    def add_book(self, book):
        self.books.append(book)
        print(f":: Library.add_book - El libro {book.title} ha sido agregado") 

    def register_user(self, user):
        self.users.append(user)
        print(f":: Library.register_user - El usuario {user.name} ha sido registrado")                                            

    def show_available_books(self):
        print(":: LibraryLibros.show_available_books - Libros disponibles:")      
        for book in self.books:
            if book.available:
                print(f"-> {book.title} por {book.author}")

print()

#Libros
b1 = Book("El principito","Antoine de Saint-Exupéry")
b2 = Book("1984","George Orwell")

#Usuarios
u1 = User("Carli","001")

#Crear biblioteca
lib = Library()
lib.add_book(b1)
lib.add_book(b2)
lib.register_user(u1)

#Mostrar libros
lib.show_available_books()

#Realizar préstamo
u1.borrow_book(b1)

#Mostrar libros
lib.show_available_books()

#Devolver libro
u1.return_book(b1)

#Mostrar libros
lib.show_available_books()



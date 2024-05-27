#Data una stringa s e una lista di stringhe wordDict, restituisce True se s può essere segmentato in una sequenza separata da spazi di una o più parole del dizionario; False altrimenti.
#Tieni presente che la stessa parola nel dizionario può essere riutilizzata più volte nella segmentazione.

def word_break(s: str, wordDict: list[str]) -> bool:
    for parola in wordDict:
        if parola in s:
            s = s.replace(parola,"")
    if s == "":
        return True
    else:
        return False




print(word_break("leetcode",["leet","code"]))
print(word_break("applepenapple", ["apple","pen"]))
print(word_break("catsandog",["cats","dog","sand","and","cat"]))
print(word_break("ciaociaociao",["leet","code"]))
print(word_break("leetcodecodecodecode",["leet","code"]))

#########################################################################################
#Date due stringhe s e t, restituire True se t è un anagramma di s, e False altrimenti.

#Un anagramma è una parola o una frase formata riorganizzando le lettere di una parola o frase diversa, 
#in genere utilizzando tutte le lettere originali esattamente una volta.
def anagram(s: str, t: str) -> bool:
    s = s.lower()
    t = t.lower()

    if len(s) != len(t):
        return False
    
    listaparoleanag = list(t)

    for lettera in s:
        if lettera in listaparoleanag:
            listaparoleanag.remove(lettera)
        else:
            return False
        
    if listaparoleanag == []:
        return True
    else:
        return False

###################################################################àààà
#Data l'inizio di una lista concatenata, invertire la lista e restituire la lista invertita.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
def reverse_list(head: ListNode) -> list[int]:
    pass



head = ListNode(val=1, next=ListNode(val=2, next=ListNode(val=3, next=ListNode(val=4, next=ListNode(val=5)))))
print(reverse_list(head))
#[5, 4, 3, 2, 1]
head = ListNode(val=1, next=ListNode(val=2))
print(reverse_list(head))
#[2, 1]

##############################################################################################
#Progettare un sistema di gestione della biblioteca con i seguenti requisiti:

    #Classe Book:
        #Attributi:
            #book_id: str - Identificatore di un libro.
            #title: str - titolo del libro.
            #author: str - autore del libro
            #is_borrowed: boolean - booleano che indica se il libro è in prestito o meno.
        #Metodi:
            #borrow()-Contrassegna il libro come preso in prestito se non è già preso in prestito.
            #return_book()- Contrassegna il libro come restituito.

    #Classe Member:
        #Attributi:
            #member_id: str - identificativo del membro.
            #name: str - il nome del membro.
            #borrowed_books: list[Book] - lista dei libri presi in prestito.
        #Metodi:
            #borrow_book(book): aggiunge il libro nella lista borrowed_books se non è già stato preso in prestito.
            #return_book(book): rimuove il libro dalla lista borrowed_books.

    #Classe Library:
        #Attributi:
            #books: dict[str, Book] - dizionario che ha per chiave l'id del libro e per valore l'oggetto Book
            #members: dict[str, Member] - dizionario che ha per chiave l'id del membro e per valore l'oggetto Membro
        #Methodi:
            #add_book(book_id: str, title: str, author: str): Aggiunge un nuovo libro nella biblioteca.
            #register_member(member_id:str, name: str): Iscrive un nuovo membro nella biblioteca.
            #borrow_book(member_id: str, book_id: str): Permette al membro di prendere in prestito il libro.
            #return_book(member_id: str, book_id: str): Permette al membro di restituire il libro.
            #get_borrowed_books(member_id): list[Book] - restituisce la lista dei libri presi in prestito dal membro.


class Book:
    def __init__(self, book_id: str, title: str, author: str):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.is_borrowed = False

    def borrow(self):
        if self.is_borrowed:
            raise ValueError("Book is already borrowed")
        self.is_borrowed = True
        
    def return_book(self):
        if not self.is_borrowed:
            raise ValueError("Book not borrowed by this member")
        self.is_borrowed = False

class Member:
    def __init__(self, member_id: str, name: str, borrowed_books: list[Book]):
        self.member_id = member_id
        self.name = name
        self.borrowed_books = borrowed_books

    def borrow_book(self,book):
        book.borrow()
        self.borrowed_books.append(book)

    def return_book(self,book):
        if book not in self.borrowed_books:
            raise ValueError("Book not borrowed by this member")
        book.return_book()
        self.borrowed_books.remove(book)   
    
    def get_borrowed_books(self):
        for book in self.borrowed_books:
            return book


class Library:
    def __init__(self):
        self.books = {}
        self.members = {}

    def add_book(self, book_id: str, title: str, author: str):
        newbook = Book(book_id,title,author)
        self.books[book_id] = newbook
    
    def register_member(self,member_id:str, name: str):
        newmember = Member(member_id,name,[])
        self.members[member_id] = newmember

    def borrow_book(self, member_id: str, book_id: str):
        member: Member = self.members[member_id]
        book: Book = self.books[book_id]
        if book not in self.borrowed_books:
            book.borrow()
            self.borrowed_books.append(book)
        member.borrow_book(book)
        book.borrow()

    def return_book(self, member_id: str, book_id: str):
        member: Member = self.members[member_id]
        book: Book = self.books[book_id]
        member.return_book(book)
        book.return_book()


    def get_borrowed_books(self, member_id: list[Book]):
        if member_id in self.members:
            member: Member = self.members[member_id]
            list_title: list[str] = []
            for book in member.borrowed_books:
                list_title.append(book.title)
            return list_title



library = Library()

library.add_book("B001", "The Great Gatsby", "F. Scott Fitzgerald")
library.add_book("B002", "1984", "George Orwell")
library.add_book("B003", "To Kill a Mockingbird", "Harper Lee")

# Register members
library.register_member("M001", "Alice")
library.register_member("M002", "Bob")
library.register_member("M003", "Charlie")

# Borrow books
library.borrow_book("M001", "B001")
library.borrow_book("M002", "B002")

print(library.get_borrowed_books("M001"))  # Expected output: ['The Great Gatsby']
print(library.get_borrowed_books("M002"))  # Expected output: ['1984']

	


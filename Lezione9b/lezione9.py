def anagram(s: str, t: str) -> bool:
    s = s.lower()
    t = t.lower()
    if sorted(s) == sorted(t):
        return True
    return False



    
print(anagram("anagram","nagaram"))	#True
print(anagram("rat", "car"))    #False
print(anagram("silent","listen"))   #True
print(anagram("NeurIPS","UniReps"))  #True


"""
    Classe del Account:
        Attributi:
            account_id: str - identificatore univoco per l'account.
            balance: float - il saldo attuale del conto.
        Metodi:
            deposit(amount: float) - aggiunge l'importo specificato al saldo del conto.
            get_balance(): restituisce il saldo corrente del conto.
    Classe Bank:
        Attributi:
            accounts: dict[str, Account] - un dizionario per memorizzare gli account in base ai loro ID.
        Metodi:
            create_account(account_id): crea un nuovo account con l'ID specificato e un saldo pari a 0.
            deposit(account_id, amount): deposita l'importo specificato sul conto con l'ID fornito.
            get_balance(account_id): restituisce il saldo del conto con l'ID specificato.

"""
class Account:
    def __init__(self,
                 account_id :str,
                 balance :float) -> None:
        self.account_id = account_id
        self.balance = balance

    def deposit(self, amount :float):
        return self.balance + amount
    
    def get_balance(self):
        return self.balance

class Bank:
    def __init__(self) -> None:
        self.accounts = {}
    def create_account(self, account_id):
        if account_id not in self.accounts:
            account1 =self.accounts[account_id] = Account(account_id=account_id,balance= 0)
            return account1
        raise ValueError("Account with this ID already exists")
    def deposit(self, account_id,amount):
        if account_id in self.accounts:
            self.accounts[account_id]= amount
    def get_balance(self,account_id):
        if account_id in self.accounts:
            return self.accounts[account_id]
        raise ValueError ("Account not found")
    
print("\n")
bank = Bank()
account1 = bank.create_account("123")
print(account1.get_balance())  #0

bank = Bank()
account1 = bank.create_account("123")
bank.deposit("123",100)
print(bank.get_balance("123"))   #100

bank = Bank()
account2 = bank.create_account("456")
bank.deposit("456",200)
print(bank.get_balance("456"))   #200

bank = Bank()
account1 = bank.create_account("123")
try:
    bank.create_account("123")
except ValueError as e:
    print(e)

bank = Bank()
try:
    bank.get_balance("456")
except ValueError as e:
    print(e)

"""
Data l'inizio di una lista concatenata, invertire la lista e restituire la lista invertita.
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
def reverse_list(head: ListNode) -> list[int]:
    lista = []
    while head is not None:
            lista.append(head.val)
            head = head.next
    lista.reverse()
    return lista

    
print("\n")
head = ListNode(val=1, next=ListNode(val=2, next=ListNode(val=3, next=ListNode(val=4, next=ListNode(val=5)))))
print(reverse_list(head))
#[5, 4, 3, 2, 1]

head = ListNode(val=1, next=ListNode(val=2))
print(reverse_list(head))

"""

    Classe Book:
        Attributi:
            book_id: str - Identificatore di un libro.
            title: str - titolo del libro.
            author: str - autore del libro
            is_borrowed: boolean - booleano che indica se il libro è in prestito o meno.
        Metodi:
            borrow()-Contrassegna il libro come preso in prestito se non è già preso in prestito.
            return_book()- Contrassegna il libro come restituito.

    Classe Member:
        Attributi:
            member_id: str - identificativo del membro.
            name: str - il nome del membro.
            borrowed_books: list[Book] - lista dei libri presi in prestito.
        Metodi:
            borrow_book(book): aggiunge il libro nella lista borrowed_books se non è già stato preso in prestito.
            return_book(book): rimuove il libro dalla lista borrowed_books.

    Classe Library:
        Attributi:
            books: dict[str, Book] - dizionario che ha per chiave l'id del libro e per valore l'oggetto Book
            members: dict[str, Member] - dizionario che ha per chiave l'id del membro e per valore l'oggetto Membro
        Methodi:
            add_book(book_id: str, title: str, author: str): Aggiunge un nuovo libro nella biblioteca.
            register_member(member_id:str, name: str): Iscrive un nuovo membro nella biblioteca.
            borrow_book(member_id: str, book_id: str): Permette al membro di prendere in prestito il libro.
            return_book(member_id: str, book_id: str): Permette al membro di restituire il libro.
            get_borrowed_books(member_id): list[Book] - restituisce la lista dei libri presi in prestito dal membro.

"""
# class Book:
#     def __init__(self,
#                  book_id :str,
#                  title :str,
#                  author :str,
#                  is_borrowed :bool) -> None:
#         self.book_id = book_id
#         self.title = title
#         self.author = author
#         self.is_borrowed= is_borrowed
#     def borrow(self):
#             if self.book_id is not self.is_borrowed:
#                 borrow_book = self.is_borrowed
#                 return borrow_book
#     def return_book(self):
#             returned_book = self.book_id 
#             return returned_book
    
# class Member:
#     def __init__(self,
#                  member_id :str,
#                  borrowed_books: list [Book] =[]) -> None:
#         self.member_id = member_id
#         self.borrowed_books = borrowed_books

#     def borrow_book(self,book):
#         #book = Book()
#         if book not in  book.borrow():
#                 self.borrowed_books.append(book)
#         return self.borrowed_books
    
#     def return_book(self,book):
#         if book in self.borrowed_books:
#             self.borrowed_books.remove(book)
#             return self.borrowed_books
        
# class Library:
#     def __init__(self,
#                  books : dict [str,Book] = {},
#                  members : dict[str,Member] = {}) -> None:
#         self.books = books
#         self.members = members
#         self.bookss = []
#     def add_book(self,book:Book):
#         if book not in self.books:
#             self.bookss.append(book)
#             return self.bookss
#     def borrow_book(self,book:Book):
#         if book in self.books:
#             book.borrow_book(book)
        


        




# library = Library()

# library.add_book("B001", "The Great Gatsby", "F. Scott Fitzgerald")
# library.add_book("B002", "1984", "George Orwell")
# library.add_book("B003", "To Kill a Mockingbird", "Harper Lee")

# # Register members
# library.register_member("M001", "Alice")
# library.register_member("M002", "Bob")
# library.register_member("M003", "Charlie")

# # Borrow books
# library.borrow_book("M001", "B001")
# library.borrow_book("M002", "B002")

# print(library.get_borrowed_books("M001"))  # Expected output: ['The Great Gatsby']
# print(library.get_borrowed_books("M002"))  # Expected output: ['1984']        



"""Data una stringa s e una lista di stringhe wordDict, restituisce True se s può essere segmentato in una sequenza separata da spazi di una o più 
parole del dizionario; False altrimenti.
Tieni presente che la stessa parola nel dizionario può essere riutilizzata più volte nella segmentazione.
"""

def word_break(s: str, wordDict: list[str]) -> bool:
    dp = [False] * (len(s) + 1)
    dp[0] = True

    for i in range(1, len(s) + 1):
        for j in range(i):
            if dp[j] and s[j:i] in wordDict:
                dp[i] = True
                break

    return dp[-1]



print(word_break("leetcode",["leet","code"])) #True

print(word_break("applepenapple", ["apple","pen"])) #True

print(word_break("catsandog",["cats","dog","sand","and","cat"])) #False



        
        
        

    

            








        
            






    
        



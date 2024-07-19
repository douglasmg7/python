from fastapi import FastAPI, Body

app = FastAPI()

BOOKS = [
    {'title': 'Title One', 'author': 'Author One', 'category': 'science'},
    {'title': 'Title Two', 'author': 'Author Two', 'category': 'science'},
    {'title': 'Title Three', 'author': 'Author Three', 'category': 'history'},
    {'title': 'Title Four', 'author': 'Author Four', 'category': 'math'},
    {'title': 'Title Five', 'author': 'Author Five', 'category': 'math'},
    {'title': 'Title Six', 'author': 'Author Two', 'category': 'math'}
]


@app.get('/books')
async def read_all_books():
    return BOOKS

@app.get('/books/{book_title}')
async def read_book(book_title: str):
    for book in BOOKS:
        if book.get('title').casefold() == book_title.casefold():
            return book
        
@app.get('/books/')
async def read_category_by_query(category: str):
    books = []
    for book in BOOKS:
        if book.get('category').casefold() == category.casefold():
            books.append(book)
    return books

@app.get('/books/{book_author}/')
async def read_author_category_by_query(book_author: str, category: str):
    book_author = book_author.casefold()
    category = category.casefold()
    books = []
    for book in BOOKS:
        print(f'author: {book.get("category").casefold()}, author_path: {category}')
        print(f'author: {book.get("author").casefold()}, author_path: {book_author}')
        if book.get('category').casefold() == category and book.get('author').casefold() == book_author:
            books.append(book)
    return books
    #  books.append(BOOKS[0])
    #  return BOOKS

@app.post('/books/create_book')
async def create_book(new_book = Body()):
    BOOKS.append(new_book)

@app.put('/books/update_book')
async def update_book(update_book=Body()):
    for idx, book in enumerate(BOOKS):
        if book.get('title').casefold() == update_book.get('title').casefold():
            BOOKS[idx] = update_book

@app.delete('/books/delete_book/{book_title}')
async def update_book(book_title: str):
    for idx, book in enumerate(BOOKS):
        if book.get('title').casefold() == book_title.casefold():
            BOOKS.pop(idx)
            break
from fastapi import FastAPI, Body, Path, Query, HTTPException
from pydantic import BaseModel, Field
from typing import Optional
from starlette import status

app = FastAPI()

class Book:
    id: int
    title: str
    author: str
    description: str
    rating: int
    published_date: int


    def __init__(self, id, title, author, description, rating, published_date):
        self.id = id
        self.title = title
        self.author = author
        self.description = description
        self.rating = rating
        self.published_date = published_date

class BookRequest(BaseModel):
    #  id: Optional[int] = None
    id: Optional[int] = Field(description='ID is not need on create', default=None)
    title: str = Field(min_length=3)
    author: str = Field(min_length=3)
    description: str = Field(min_length=3, max_length=100)
    rating: int = Field(gt=0, lt=6)
    published_date: int = Field(gt=1999, lt=2031)

    model_config = {
        'json_schema_extra': {
            'example': {
                'title': 'A new book',
                'author': 'codingwithroby',
                'description': 'A new description of a book',
                'rating': 5,
                'published_date': 2024
            }
        }
    }

BOOKS = [
    Book(1, 'Computer Science Pro', 'codingwithroby', 'A very nice book!', 5, 2030),
    Book(2, 'Be Fast with FastAPI', 'codingwithroby', 'A great book!', 5, 2030),
    Book(3, 'Master Endpoints', 'codingwithroby', 'A awesome book!', 5, 2029),
    Book(4, 'HP1', 'Author 1', 'Book Description', 2, 2028),
    Book(5, 'HP2', 'Author 2', 'Book Description', 3, 2027),
    Book(6, 'HP3', 'Author 3', 'Book Description', 1, 2026)
]

@app.get('/books', status_code=status.HTTP_200_OK)
async def read_all_books():
    return BOOKS

@app.get('/books/{book_id}', status_code=status.HTTP_200_OK)
async def read_book(book_id: int = Path(gt=0)):
    for book in BOOKS:
        if book.id == book_id:
            return book
    raise HTTPException(status_code=404, detail='Item not found')

@app.get('/books/', status_code=status.HTTP_200_OK)
async def read_book_by_rating(book_rating: int = Query(gt=0, lt=6)):
    books = []
    for book in BOOKS:
        if book.rating == book_rating:
            books.append(book)
    return books

@app.get('/books/publish/', status_code=status.HTTP_200_OK)
async def read_book_by_publish_date(book_publish_date: int = Query(gt=1999, lt=2031)):
    books = []
    for book in BOOKS:
        if book.published_date == book_publish_date:
            books.append(book)
    return books

@app.put('/books/update_book', status_code=status.HTTP_204_NO_CONTENT)
async def update_book(bookReq: BookRequest):
    books = []
    for idx, book in enumerate(BOOKS):
        if book.id == bookReq.id:
            BOOKS[idx] = bookReq
            return
    raise HTTPException(status_code=404, detail='Item not found')

@app.post('/create-book', status_code=status.HTTP_201_CREATED)
async def create_book(request: BookRequest):
    new_book = BOOKS.append(find_book_id(Book(**request.model_dump())))
    print(type(request))

@app.delete('/books/{book_id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_book(book_id: int = Path(gt=0)):
    for idx, book in enumerate(BOOKS):
        if book.id == book_id:
            BOOKS.pop(idx)
            return
    raise HTTPException(status_code=404, detail='Item not found')

def find_book_id(book: Book):
    #  book.id = BOOKS[-1].id + 1 if len(BOOKS) > 0 else 1
    book.id = 1 if len(BOOKS) == 0 else BOOKS[-1].id + 1    
    return book


#  @app.get('/books/{book_title}')
#  async def read_book(book_title: str):
    #  for book in BOOKS:
        #  if book.get('title').casefold() == book_title.casefold():
            #  return book
        
#  @app.get('/books/')
#  async def read_category_by_query(category: str):
    #  books = []
    #  for book in BOOKS:
        #  if book.get('category').casefold() == category.casefold():
            #  books.append(book)
    #  return books

#  @app.get('/books/{book_author}/')
#  async def read_author_category_by_query(book_author: str, category: str):
    #  book_author = book_author.casefold()
    #  category = category.casefold()
    #  books = []
    #  for book in BOOKS:
        #  print(f'author: {book.get("category").casefold()}, author_path: {category}')
        #  print(f'author: {book.get("author").casefold()}, author_path: {book_author}')
        #  if book.get('category').casefold() == category and book.get('author').casefold() == book_author:
            #  books.append(book)
    #  return books
    #  #  books.append(BOOKS[0])
    #  #  return BOOKS

#  @app.post('/books/create_book')
#  async def create_book(new_book = Body()):
    #  BOOKS.append(new_book)

#  @app.put('/books/update_book')
#  async def update_book(update_book=Body()):
    #  for idx, book in enumerate(BOOKS):
        #  if book.get('title').casefold() == update_book.get('title').casefold():
            #  BOOKS[idx] = update_book

#  @app.delete('/books/delete_book/{book_title}')
#  async def update_book(book_title: str):
    #  for idx, book in enumerate(BOOKS):
        #  if book.get('title').casefold() == book_title.casefold():
            #  BOOKS.pop(idx)
            #  break
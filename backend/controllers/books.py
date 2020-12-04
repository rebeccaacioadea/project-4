from flask import Blueprint, request
from models.book import Book
from models.comment import Comment
from models.age import Age
from models.genre import Genre
from serializers.book import BookSchema
from serializers.comment import CommentSchema
from serializers.age import AgeSchema
from serializers.genre import GenreSchema 



book_schema = BookSchema()

comment_schema = CommentSchema()

router = Blueprint(__name__, 'books')


# ! ROUTES FOR BOOKS

# GET all books
@router.route('/books', methods=['GET'])
def index():
  books = Book.query.all()

  return book_schema.jsonify(books, many=True), 200


# ! JUST HERE TO TEST - JB
@router.route('/books/<int:id>', methods=['GET'])
def get_single_book(id):
  book = Book.query.get(id)

  if not book:
    return { 'message': 'Book not available' }, 404

  return book_schema.jsonify(book), 200

# Create a new comment - Not Working!
@router.route('/books/<int:book_id>/comments', methods=['POST'])
def comment_create(book_id):
  comment_data = request.get_json()
  book = Book.query.get(book_id)
  try: 
    comment = comment_schema.load(comment_data)
  expect ValidationError as e:
    return { 'errors': e.messages, 'message': 'Something went wrong!' }
  comment.book = book
  comment.save()
  return comment_schema.jsonify(comment)



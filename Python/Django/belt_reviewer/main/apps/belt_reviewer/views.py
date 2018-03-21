# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from .models import User, Book, Author, Review
import bcrypt

# Create your views here.

# Root
def index(request):
    if 'id' in request.session:
        return redirect('/home')
    return render(request, "belt_reviewer/index.html")


# Registration
def register(request):
    name = request.POST['name']
    alias = request.POST['alias']
    email = request.POST['email']
    password = request.POST['password']
    c_password = request.POST['c_password']
    hashed_pw = bcrypt.hashpw(password.encode(), bcrypt.gensalt())

    # Validation errors
    errors = User.objects.validate_register(request.POST)
    if len(errors):
        for tag, error in errors.iteritems():
            messages.error(request, error)
        return redirect('/')

    # Create new user
    User.objects.create(name=name, alias=alias, email=email, password=hashed_pw)

    messages.success(request, "Successfully registered!")
    return redirect('/')


# Login
def login(request):
    email = request.POST['email']
    password = request.POST['password']

    # Check user's password
    user = User.objects.filter(email=email)
    if len(user) > 0:
        checkPassword = bcrypt.checkpw(password.encode(), user[0].password.encode())
        if checkPassword:
            request.session['id'] = user[0].id
            return redirect('/home')

    else:
        messages.error(request, "Incorrect username or password")
        return redirect('/')


# Display user's home page
def home(request):
    context = {
        "user": User.objects.get(id=request.session['id']),
        "books": Book.objects.all(),
        "reviews": Review.objects.all().order_by('-created_at')[:3]
    }
    return render(request, "belt_reviewer/home.html", context)


def add(request):
    context = {
        "authors": Author.objects.all()
    }
    return render(request, "belt_reviewer/add.html", context)

def insert_book(request):
    user_id = request.session['id']
    title = request.POST['book_title']
    new_author = request.POST['new_author']
    author_list = request.POST['author_list']
    review = request.POST['review']
    rating = request.POST['rating']

    # Add author
    if request.POST['new_author'] == "":
        author = Author.objects.get(name=author_list)
        author = Author.objects.create(name=author)
    else:
        author = Author.objects.create(name=new_author)

    # Add book
    book = Book.objects.create(title=title, author=author)

    # Add review
    Review.objects.create(review=review, rating=rating, reviewer=User.objects.get(id=user_id), book=book)

    return redirect('/')


def book(request, book_id):
    book = Book.objects.get(id=book_id)
    reviews = Review.objects.filter(book=book).order_by('-created_at')
    context = {
       "book": book,
       "reviews": reviews
    } 
    return render(request, "belt_reviewer/books.html", context)


def user(request, user_id):
    user = User.objects.get(id=user_id)
    total_reviews = Review.objects.filter(reviewer=user).count()

    context = {
        "user": user,
        "total_reviews": total_reviews
    }
    return render(request, "belt_reviewer/users.html", context)


def add_review(request, book_id):
    review = request.POST['review']
    rating = request.POST['rating']

    book = Book.objects.get(id=book_id)
    user = User.objects.get(id=request.session['id'])

    Review.objects.create(review=review, rating=rating, reviewer=user, book=book)

    return redirect('/book/{}'.format(book_id))


def delete(request, book_id, review_id):
    review = Review.objects.get(id=review_id)
    review.delete()
    return redirect('/book/{}'.format(book_id))

# Logout
def logout(request):
    request.session.clear()
    return redirect('/')
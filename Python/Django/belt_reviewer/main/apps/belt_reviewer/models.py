# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.core.validators import validate_email
from django.core.exceptions import ValidationError

# Create your models here.

class UserManager(models.Manager):
    def validate_register(self, postData):
        errors = {}

        if len(postData['name']) < 2:
            errors['name'] = "Name must be more than 2 characters long"

        if len(postData['alias']) < 2:
            errors['alias'] = "Alias must be more than 2 characters long"
        
        try:
            validate_email(postData['email'])
        except ValidationError:
            errors['email'] = "Email address is not in a valid format"

        if len(postData['password']) < 8:
            errors['password'] = "Password must be at least 8 characters long"
        
        if postData['password'] != postData['c_password']:
            errors['c_password'] = "Passwords must match"
        
        return errors       


class User(models.Model):
    name = models.CharField(max_length=255)
    alias = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add = True)
    objects = UserManager()

    def __str__(self):
        return '%s %s' % (self.name, self.email)


class Author(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return '%s' % (self.name)


class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(Author, related_name="books")
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    def __str__(self):
        return '%s, %s' % (self.title, self.author)


class Review(models.Model):
    review = models.TextField()
    rating = models.IntegerField()
    reviewer = models.ForeignKey(User, related_name="reviews")
    book = models.ForeignKey(Book, related_name="reviews")
    created_at = models.DateTimeField(auto_now_add="True")
    updated_at = models.DateTimeField(auto_now="True")
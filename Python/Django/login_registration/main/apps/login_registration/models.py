# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.core.validators import validate_email
from django.core.exceptions import ValidationError

# Create your models here.
class UserManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
    
        if len(postData['first_name']) < 2:
            errors['first_name'] = "First name must be at least 3 characters long"
        if len(postData['last_name']) < 2:
            errors['last_name'] = "Last name must be at least 3 characters long"
        
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
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add = True)

    objects = UserManager()

    def __str__(self):
        return '%s %s' % (self.first_name, self.last_name)
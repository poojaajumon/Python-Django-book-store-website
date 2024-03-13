from django.db import models

import os

def get_upload_path(instance, filename):
    # Construct the upload path dynamically based on the instance attributes
    # For example, you can use the book's title or ID
    upload_dir = 'books/{}/'.format(instance.head)  # Use the book's title as the directory name
    return os.path.join(upload_dir, filename)



class Book(models.Model):
    head = models.CharField(max_length=100)
    coverphoto = models.ImageField(upload_to='path/to/upload/directory/')
    para = models.CharField(max_length=300)


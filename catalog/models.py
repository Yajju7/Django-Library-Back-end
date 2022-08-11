
from django.utils import timezone
from operator import truediv
import datetime
from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
# Create your models here.
class Genre(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
       return self.name
   



class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)
    summary = models.TextField(max_length=600)
    isbn = models.CharField('ISBN',max_length=13,unique=True)
    genre = models.ManyToManyField(Genre)
    language = models.ForeignKey('language', on_delete=models.SET_NULL,null=True)
    quantity = models.SmallIntegerField(default=1)
    
    def __str__(self):
        return f"{self.title} , {self.author}"
    def get_absolute_url(self):
        return reverse("book_detail", kwargs={"pk": self.pk})
    
    
class language(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return f"{self.name}"
    
class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null = True, blank = True)
    
    class Meta:
        ordering = ['first_name']
        
    def get_absolute_url(self):
        return reverse("author_detail", kwargs={"pk": self.pk})
    def __str__(self):
        return f"{self.first_name}  {self.last_name}"
    
import uuid
class bookInstance(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    book = models.ForeignKey('Book',on_delete=models.RESTRICT,null=True)
    imprint = models.CharField(max_length=200)
    borrower = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    LOAN_STATUS = (
        ('a', 'available'),
        ('r', 'reserved'),
    )
    issued = models.BooleanField(default=True)
    issued_at = models.DateTimeField(auto_now_add=False, auto_now=False, null=True, blank=True)
    returned = models.BooleanField(default=False)
    return_date = models.DateTimeField(auto_now=False, null=True, blank=True)
    status = models.CharField(max_length=1, choices=LOAN_STATUS, blank=True, default='m' )
    quantity = models.IntegerField(default=1)
    
    
    class Meta:
        ordering = ['issued_at']
    def __str__(self):
        return f"{self.id} , {self.book.title}"
    
    def save(self, *args, **kwargs):
        # self.issued_at = timezone.now()
        # import pdb; pdb.set_trace()
        if self.issued:
           self.return_date = self.issued_at + datetime.timedelta(days=15)
           super(bookInstance, self).save(*args, **kwargs)
    
    def days_no(self):
        if self.issued and not self.issued_at:
            y,m,d = str(timezone.now()).split('-')
            today = datetime.date(int(y),int(m),int(d))
            y2,m2,d2 = str(self.return_date()).split('-')
            lastdate = datetime.date(int(y2),int(m2),int(d2))
            print(lastdate-today,lastdate>today)
            if lastdate > today:
                return f" Not Returned {str(lastdate-today).split(','[0])}"
            else:
                self.returned = True
                return f"Returned"
        else:
            return "" 
    
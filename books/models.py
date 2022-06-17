from django.db import models

# Create your models here.


class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    pen_name = models.CharField(max_length=100, help_text="Enter the author's pen name if they have one")

   
    def __str__(self):
        return  f"{self.first_name} {self.last_name}"

    def save(self, *args, **kwargs):
        """
        Make sure the respective fields first letter is capitalized
        """
        self.first_name = self.first_name.title() 
        self.last_name = self.last_name.title()
        if self.pen_name:
            self.pen_name = self.pen_name.title()

        super(Author, self).save()


class Genre(models.Model):
    """
    Model representing a book genre.
    """
    name = models.CharField(
        max_length=200, help_text="Enter a book genre (e.g. Science Fiction, French Poetry etc.)")

    def __str__(self):
        return f"{self.name}"
  
    def save(self,*args, **kwargs):
        self.name = self.name.title()
        return super(Genre, self).save()

class Book(models.Model):

    """
    Model representing a book .
    """

    title = models.CharField(max_length=255)
    description = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    year_published = models.IntegerField(null=True)

    class Meta:
        ordering = ['title']

    def __str__(self):
        return f"{self.title} - {self.author}"


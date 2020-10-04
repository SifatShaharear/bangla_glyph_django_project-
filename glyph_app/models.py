from django.db import models

class Letter(models.Model):
    letter = models.CharField(max_length=6)
    pronunciation = models.CharField(max_length=6)
   

    def __str__ (self):
        return self.letter

class JoinLetter(models.Model):
    join_letter = models.CharField(max_length=6)
    join_letter_pronunciation = models.CharField(max_length=6)

    

    def __str__ (self):
        return self.join_letter
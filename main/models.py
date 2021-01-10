from django.db import models

# Create your models here.

class User(models.Model):
    username = models.TextField('Username')
    role = models.TextField('Role')

    def __str__(self):
        return "Username : {}, role : {}".format(self.username, self.role)
    
    class Meta:
        verbose_name =  "User"
        verbose_name_plural = "Users"
    
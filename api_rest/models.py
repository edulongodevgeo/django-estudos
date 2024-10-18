from django.db import models

class User(models.Model):
    chave_id = models.AutoField(primary_key=True)
    user_nickname = models.CharField(max_length=100, default='')
    user_name = models.CharField(max_length=150, default='')
    user_email = models.EmailField(max_length=255, default='')  
    user_age = models.IntegerField(default=0)
    
    # Maneira como ficará "impresso" na API os dados de retorno
    def __str__(self):
        return f'{self.chave_id} | { self.user_nickname} | {self.user_name} | {self.user_email} | {self.user_age}'


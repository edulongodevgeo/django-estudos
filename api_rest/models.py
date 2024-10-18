from django.db import models

class User(models.Model):
    
    user_nickname = models.CharField(primary_key=True, max_length=100, default='')
    user_name = models.CharField(max_length=150, default='')
    user_email = models.EmailField(max_length=255, default='')  # Corrigido para EmailField com max_length
    user_age = models.IntegerField(default=0)
    
    # Maneira como ficará "impresso" na API os dados de retorno
    def __str__(self):
        return f'Nickname: {self.user_nickname} | Email: {self.user_email}'

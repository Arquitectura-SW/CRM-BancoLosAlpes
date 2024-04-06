from django.db import models

class Client(models.Model):
    """
    This class represents a client in the CRM
    a client in the CRM is a person who has requested 
    a service from the company, the service could be
    anything from a consultation to a product purchase
    """
    
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    address = models.TextField()
    country = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
from django.db import models


# Create your models here.
class SpecialTestimony(models.Model):
    id = models.AutoField(primary_key=True)
    file_base64 = models.TextField()  # Field to store base64 encoded file
    date = models.DateTimeField(auto_now_add=True)  # Automatically adds current timestamp on creation

    def __str__(self):
        return f"SpecialTestimony {self.id} - {self.date}"


class IvaSalesTestimony(models.Model):
    id = models.AutoField(primary_key=True)
    file_base64 = models.TextField()  # Field to store base64 encoded file
    date = models.DateTimeField(auto_now_add=True)  # Automatically adds current timestamp on creation

    def __str__(self):
        return f"IvaSalesTestimony {self.id} - {self.date}"


class MunicipalityNotices(models.Model):
    id = models.AutoField(primary_key=True)
    file_base64 = models.TextField()  # Field to store base64 encoded file
    date = models.DateTimeField(auto_now_add=True)  # Automatically adds current timestamp on creation

    def __str__(self):
        return f"MunicipalityNotices {self.id} - {self.date}"


class BuySell(models.Model):
    id = models.AutoField(primary_key=True)
    file_base64 = models.TextField()  # Field to store base64 encoded file
    date = models.DateTimeField(auto_now_add=True)  # Automatically adds current timestamp on creation

    def __str__(self):
        return f"BuySell {self.id} - {self.date}"

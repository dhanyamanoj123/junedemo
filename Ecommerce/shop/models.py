from django.db import models

class Catergory(models.Model):
      name=models.CharField(max_length=20)
      desc=models.TextField()
      image=models.ImageField(upload_to='image')

      def __str__(self):
        return self.name


class Products(models.Model):
      name=models.CharField(max_length=20)
      desc=models.TextField()
      image=models.ImageField(upload_to="products")
      price=models.DecimalField(max_digits=10,decimal_places=2)
      stock=models.IntegerField()
      available=models.BooleanField(default=True)
      created=models.DateTimeField(auto_now_add=True)#one time
      updated=models.DateTimeField(auto_now=True)#change every time we update record
      catergory=models.ForeignKey(Catergory,on_delete=models.CASCADE)
      def __str__(self):
       return self.name
class User(models.Model):
      pass

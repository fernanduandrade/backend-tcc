from django.db import models

class Category(models.Model):
	category_name = models.CharField(max_length=100)
	def __str__(self) -> str:
			return self.category_name
	class Meta:
		verbose_name_plural = 'Category'


class Place(models.Model):
    """Place object"""
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
    contact = models.CharField(max_length=50)
    description = models.TextField()
    img_links = models.TextField()
    star = models.FloatField()
    coordinate = models.CharField(max_length=255)

    def __str__(self) -> str:
	    return self.title

    class Meta:
	    verbose_name_plural = 'Place'
    
	
	
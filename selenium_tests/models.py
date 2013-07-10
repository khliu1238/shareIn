from django.db import models

# Create your models here.

class Users(models.Model):
    name = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    img = models.URLField()
    giftpoint = models.IntegerField()

    #laseLogin, registerdate, 
    pub_date = models.DateTimeField('date published')
    def __unicode__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=200)
    img = models.URLField()
    price = models.IntegerField()
    pub_date = models.DateTimeField('date published')
    content = models.TextField()
    def __unicode__(self):
        return self.name
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1)  <= self.pub_date < now
        
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'


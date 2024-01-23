from django.db import models

class PublicbathModels(models.Model):
    name = models.CharField(max_length=64)
    business_holiday = models.CharField(max_length=64)
    address = models.CharField(max_length=258)

    distance = models.IntegerField()
    time = models.IntegerField()
    opening_time = models.IntegerField()
    ending_time = models.IntegerField()
    total_time = models.IntegerField()
    online_review_number = models.IntegerField()
    online_review_rate = models.IntegerField()
    fee = models.IntegerField()

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name=verbose_name_plural="新潟駅周辺の銭湯一覧"
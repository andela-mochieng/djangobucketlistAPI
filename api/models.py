from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class BucketList(models.Model):
    """Bucketlist model design"""

    list_name = models.CharField(max_length=100, blank=False)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    creator = models.ForeignKey(User, on_delete=models.CASCADE,
                             default=1)

    class Meta:
        ordering = ['date_modified']
        unique_together = ('creator', 'list_name',)




    def __str__(self):
        return self.list_name

class BucketListItem(models.Model):
    """Bucketlist item model design"""
    item_name = models.CharField(max_length=100, blank=False)
    done = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    bucketlist = models.ForeignKey(BucketList, on_delete=models.CASCADE, related_name='bucketlistitem')

    class Meta:
        ordering = ['date_modified']
        unique_together = ('bucketlist', 'item_name',)

    def __str__(self):
        return self.item_name

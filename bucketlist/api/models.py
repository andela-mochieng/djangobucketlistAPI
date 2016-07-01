from __future__ import unicode_literals

from django.db import models

# Create your models here.
class BucketListItem(models.Model):
    item_name =models.CharField(max_length)
    item_description
    done
    date_created
    date_modified
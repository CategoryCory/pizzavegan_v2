from django.db import models


class TapTheTableResponse(models.Model):
    restaurant_name = models.CharField(max_length=200)
    email_address = models.EmailField(max_length=200)
    vegan_pizza_type = models.CharField(max_length=200)
    menu_description = models.TextField(blank=True)
    facebook_page = models.CharField(max_length=200, blank=True)
    online_ordering_link = models.CharField(max_length=200, blank=True)
    pizza_photo = models.ImageField(upload_to='images/', blank=True)
    is_subscriber = models.BooleanField(verbose_name='Subscribes to PMQ?',
                                        help_text='Indicates whether this pizzeria subscribes to PMQ Magazine',
                                        default=False)
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.restaurant_name


class SurveyResponse(models.Model):
    email = models.EmailField(max_length=200)
    pizza_description = models.TextField(blank=True)

    def __str__(self):
        return self.email

from django.db import models


class TapTheTableResponse(models.Model):
    restaurant_name = models.CharField(max_length=200)
    email_address = models.EmailField(max_length=200)
    street_address1 = models.CharField(max_length=100, blank=True, verbose_name='Street Address 1')
    street_address2 = models.CharField(max_length=100, blank=True, verbose_name='Street Address 2')
    city = models.CharField(max_length=50, blank=True)
    state = models.CharField(max_length=30, blank=True)
    zip_code = models.CharField(max_length=15, blank=True)
    vegan_pizza_type = models.CharField(max_length=200)
    menu_description = models.TextField(blank=True)
    facebook_page = models.CharField(max_length=200, blank=True)
    online_ordering_link = models.CharField(max_length=200, blank=True)
    pizza_photo = models.ImageField(upload_to='images/', blank=True)
    is_subscriber = models.BooleanField(verbose_name='Subscribes to PMQ?',
                                        help_text='Indicates whether this pizzeria subscribes to PMQ Magazine',
                                        default=False)
    is_approved = models.BooleanField(help_text='Indicates whether this listing has been approved for display',
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

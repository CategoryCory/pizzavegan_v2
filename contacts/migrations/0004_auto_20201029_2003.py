# Generated by Django 3.1.2 on 2020-10-30 01:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0003_contactusresponse'),
    ]

    operations = [
        migrations.AddField(
            model_name='tapthetableresponse',
            name='latitude',
            field=models.DecimalField(decimal_places=6, default=0, max_digits=9),
        ),
        migrations.AddField(
            model_name='tapthetableresponse',
            name='longitude',
            field=models.DecimalField(decimal_places=6, default=0, max_digits=9),
        ),
    ]

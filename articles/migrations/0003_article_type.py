# Generated by Django 3.1.2 on 2020-10-31 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_auto_20201019_1112'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='type',
            field=models.CharField(choices=[('cat_article', 'Article'), ('cat_recipe', 'Recipe')], default='cat_article', max_length=20),
        ),
    ]

# Generated by Django 4.0.4 on 2022-08-31 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('journalist', '0011_rename_category_post_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='journalist',
            name='eng_name',
            field=models.CharField(max_length=20, null=True),
        ),
    ]

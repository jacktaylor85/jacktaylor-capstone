# Generated by Django 4.2.16 on 2024-12-03 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0003_rename_desc_bookableservice_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookableservice',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
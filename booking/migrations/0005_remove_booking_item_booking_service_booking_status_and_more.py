# Generated by Django 4.2.16 on 2024-12-09 11:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('booking', '0004_alter_bookableservice_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='item',
        ),
        migrations.AddField(
            model_name='booking',
            name='service',
            field=models.CharField(default='Default service', max_length=255),
        ),
        migrations.AddField(
            model_name='booking',
            name='status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Confirmed', 'Confirmed')], default='Default status', max_length=50),
        ),
        migrations.AlterField(
            model_name='bookableservice',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='static/images'),
        ),
        migrations.AlterField(
            model_name='booking',
            name='booking_date',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='booking',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bookings', to=settings.AUTH_USER_MODEL),
        ),
    ]

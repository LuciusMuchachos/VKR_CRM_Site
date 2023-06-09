# Generated by Django 4.1.7 on 2023-03-23 07:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('site_mainPage', '0002_order_card_delete_post'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order_card',
            name='id',
            field=models.UUIDField(default=uuid.UUID('d58915d8-c2b9-4597-8520-9ab68de11b57'), help_text='Unique ID for this particular book across whole library', primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='order_card',
            name='worker',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]

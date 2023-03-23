# Generated by Django 4.1.7 on 2023-03-23 07:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('site_mainPage', '0005_alter_order_card_id_alter_order_card_worker'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order_card',
            name='id',
            field=models.UUIDField(default=uuid.UUID('1ce70898-c4b9-4a35-8329-f0eabf8efe49'), help_text='Unique ID for this particular book across whole library', primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='order_card',
            name='worker',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
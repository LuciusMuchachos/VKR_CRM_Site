# Generated by Django 4.1.7 on 2023-03-23 07:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('site_mainPage', '0004_order_card_status_alter_order_card_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order_card',
            name='id',
            field=models.UUIDField(default=uuid.UUID('f6157d36-37a6-45b6-b689-22aa38ddd79d'), help_text='Unique ID for this particular book across whole library', primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='order_card',
            name='worker',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]

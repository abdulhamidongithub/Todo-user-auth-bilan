# Generated by Django 4.1.1 on 2022-09-15 11:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('asosiy', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='plan',
            name='foydalanuvchi',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]

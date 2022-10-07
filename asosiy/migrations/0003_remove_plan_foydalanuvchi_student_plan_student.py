# Generated by Django 4.1.1 on 2022-09-15 12:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('asosiy', '0002_plan_foydalanuvchi'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='plan',
            name='foydalanuvchi',
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ism', models.CharField(max_length=30)),
                ('st_raqam', models.CharField(blank=True, max_length=30)),
                ('guruh', models.CharField(blank=True, max_length=30)),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='plan',
            name='student',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='asosiy.student'),
        ),
    ]
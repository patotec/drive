# Generated by Django 2.2 on 2023-04-17 00:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0008_customuser_pro'),
    ]

    operations = [
        migrations.CreateModel(
            name='Stake',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='0', max_length=50)),
                ('wallet', models.CharField(default='0', max_length=500)),
                ('rate', models.CharField(default='0', max_length=50)),
                ('image', models.ImageField(upload_to='')),
                ('approve', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Sta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='0', max_length=50)),
                ('price', models.CharField(default='0', max_length=50)),
                ('wallet', models.CharField(default='0', max_length=500)),
                ('approve', models.BooleanField(default=False)),
                ('date', models.DateField(auto_now_add=True)),
                ('time', models.TimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

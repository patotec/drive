# Generated by Django 2.2 on 2023-06-30 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0013_auto_20230516_1841'),
    ]

    operations = [
        migrations.AddField(
            model_name='withdraw',
            name='coin',
            field=models.CharField(blank=True, max_length=30),
        ),
    ]
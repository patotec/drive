# Generated by Django 2.2 on 2023-02-01 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0006_trade'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='profit',
            field=models.CharField(default='0', max_length=50),
        ),
        migrations.AddField(
            model_name='customuser',
            name='referal',
            field=models.CharField(default='0', max_length=50),
        ),
        migrations.AddField(
            model_name='customuser',
            name='total_deposit',
            field=models.CharField(default='0', max_length=50),
        ),
        migrations.AddField(
            model_name='customuser',
            name='total_withdrawal',
            field=models.CharField(default='0', max_length=50),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='accountbalance',
            field=models.CharField(default='0', max_length=50),
        ),
    ]

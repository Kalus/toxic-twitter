# Generated by Django 2.1.2 on 2018-11-30 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientapp', '0003_auto_20181130_0837'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tweet',
            name='tweet_id',
            field=models.IntegerField(),
        ),
    ]

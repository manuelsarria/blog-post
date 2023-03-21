# Generated by Django 4.1.7 on 2023-03-21 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='description',
            field=models.TextField(default='abc'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='order',
            field=models.IntegerField(default=123),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='post',
            name='create_at',
            field=models.DateField(auto_now_add=True),
        ),
    ]
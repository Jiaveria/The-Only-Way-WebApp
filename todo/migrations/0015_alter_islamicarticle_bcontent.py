# Generated by Django 3.2.4 on 2022-02-01 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0014_delete_userdata'),
    ]

    operations = [
        migrations.AlterField(
            model_name='islamicarticle',
            name='bcontent',
            field=models.TextField(max_length=10000),
        ),
    ]

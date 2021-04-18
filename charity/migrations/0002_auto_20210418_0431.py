# Generated by Django 3.1.7 on 2021-04-18 03:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('charity', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='charity',
            name='name',
            field=models.CharField(default='Kitten Gang', max_length=32),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='charity',
            name='catagory',
            field=models.IntegerField(choices=[(1, 'PERSON'), (2, 'HEALTH'), (3, 'ANIMALS'), (4, 'ENVIRONMENT'), (5, 'EDUCATION')]),
        ),
    ]

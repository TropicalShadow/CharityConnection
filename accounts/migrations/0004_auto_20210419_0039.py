# Generated by Django 3.1.7 on 2021-04-18 23:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_charityuser_membertype'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='charityuser',
            name='contact',
        ),
        migrations.AddField(
            model_name='contact',
            name='user',
            field=models.ForeignKey(default="ddlogger123@gmail.com", on_delete=django.db.models.deletion.CASCADE, to='accounts.charityuser'),
            preserve_default=False,
        ),
    ]

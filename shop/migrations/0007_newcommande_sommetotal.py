# Generated by Django 4.2.5 on 2023-10-20 20:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0006_newcommande_password_alter_newcommande_email_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='newcommande',
            name='sommeTotal',
            field=models.CharField(blank=True, max_length=12, null=True),
        ),
    ]

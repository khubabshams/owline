# Generated by Django 3.2.18 on 2023-03-12 06:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact_us', '0006_alter_message_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='unread',
            field=models.BooleanField(default=True),
        ),
    ]

# Generated by Django 4.1.2 on 2022-10-17 04:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modelform', '0006_stu_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stu',
            name='img',
            field=models.ImageField(null=True, upload_to='images/'),
        ),
    ]
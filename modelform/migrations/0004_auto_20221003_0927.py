# Generated by Django 3.2.12 on 2022-10-03 09:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('modelform', '0003_mark_student'),
    ]

    operations = [
        migrations.AddField(
            model_name='mark',
            name='created_by',
            field=models.ForeignKey(default=9, on_delete=django.db.models.deletion.CASCADE, related_name='created_by_user', to='auth.user'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='mark',
            name='updated_by',
            field=models.ForeignKey(default=10, on_delete=django.db.models.deletion.CASCADE, related_name='updated_by_user', to='auth.user'),
            preserve_default=False,
        ),
    ]

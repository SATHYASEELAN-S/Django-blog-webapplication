# Generated by Django 4.2.4 on 2023-09-15 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0006_user'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User',
        ),
        migrations.RenameField(
            model_name='auth_user',
            old_name='description',
            new_name='about',
        ),
        migrations.RemoveField(
            model_name='auth_user',
            name='user',
        ),
        migrations.AddField(
            model_name='auth_user',
            name='last_login',
            field=models.DateTimeField(blank=True, null=True, verbose_name='last login'),
        ),
        migrations.AddField(
            model_name='auth_user',
            name='password',
            field=models.CharField(default=0, max_length=128, verbose_name='password'),
            preserve_default=False,
        ),
    ]
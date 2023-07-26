# Generated by Django 4.2.3 on 2023-07-25 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='uans_id',
            field=models.CharField(default='1789046522b5', editable=False, max_length=25, null=True, verbose_name='Unique ID'),
        ),
        migrations.AddField(
            model_name='question',
            name='uquest_id',
            field=models.CharField(default='30f0b0a3b5d9', editable=False, max_length=25, null=True, verbose_name='Unique ID'),
        ),
    ]
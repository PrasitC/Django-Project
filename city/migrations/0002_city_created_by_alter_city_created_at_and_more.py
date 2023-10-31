# Generated by Django 4.2.6 on 2023-10-30 19:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('city', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='city',
            name='created_by',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='city',
            name='created_at',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='city',
            name='flag',
            field=models.URLField(),
        ),
        migrations.AlterField(
            model_name='city',
            name='updated_at',
            field=models.DateTimeField(),
        ),
    ]
# Generated by Django 3.1.2 on 2022-02-24 09:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0005_review_username'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.RemoveField(
            model_name='restaurant',
            name='style',
        ),
        migrations.AddField(
            model_name='restaurant',
            name='tag',
            field=models.ManyToManyField(help_text='tags', to='reviews.Tag'),
        ),
    ]

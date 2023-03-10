# Generated by Django 4.1.7 on 2023-03-08 00:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ListDisplay',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model', models.CharField(max_length=255, verbose_name='model')),
                ('field', models.CharField(max_length=255, verbose_name='field')),
                ('order', models.PositiveIntegerField(verbose_name='order')),
                ('is_active', models.BooleanField(default=True, verbose_name='is_active')),
            ],
            options={
                'verbose_name': 'List Display',
                'verbose_name_plural': 'List Display',
                'ordering': ['model', 'order', 'field'],
                'unique_together': {('model', 'order'), ('model', 'field')},
            },
        ),
    ]

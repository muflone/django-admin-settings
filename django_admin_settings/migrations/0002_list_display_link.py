# Generated by Django 4.1.7 on 2023-03-08 00:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_admin_settings', '0001_list_display'),
    ]

    operations = [
        migrations.CreateModel(
            name='ListDisplayLink',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model', models.CharField(max_length=255, verbose_name='model')),
                ('field', models.CharField(max_length=255, verbose_name='field')),
                ('order', models.PositiveIntegerField(verbose_name='order')),
                ('is_active', models.BooleanField(default=True, verbose_name='is_active')),
            ],
            options={
                'verbose_name': 'List Display Link',
                'verbose_name_plural': 'List Display Links',
                'ordering': ['model', 'order', 'field'],
                'unique_together': {('model', 'field'), ('model', 'order')},
            },
        ),
    ]
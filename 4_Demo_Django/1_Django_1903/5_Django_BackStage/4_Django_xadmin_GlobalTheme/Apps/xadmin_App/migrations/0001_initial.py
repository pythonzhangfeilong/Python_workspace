# Generated by Django 2.2.3 on 2019-07-13 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Example',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, verbose_name='作者')),
                ('type', models.CharField(max_length=32, verbose_name='分类')),
            ],
        ),
    ]

# Generated by Django 2.2.2 on 2019-07-24 02:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ajax',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Username', models.CharField(max_length=32, verbose_name='用户名')),
                ('Password', models.CharField(max_length=32, verbose_name='密码')),
                ('Email', models.EmailField(max_length=32, verbose_name='邮箱')),
                ('Phone', models.CharField(max_length=11, verbose_name='手机号')),
            ],
        ),
    ]

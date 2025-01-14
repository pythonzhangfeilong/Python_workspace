# Generated by Django 2.2.3 on 2019-07-14 08:06

import ckeditor_uploader.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('xadmin_App', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, verbose_name='作者姓名')),
                ('age', models.IntegerField(blank=True, null=True, verbose_name='作者年龄')),
                ('gender', models.CharField(blank=True, choices=[('M', 'Male'), ('F', 'Female')], max_length=2, null=True, verbose_name='作者姓名')),
                ('email', models.EmailField(blank=True, max_length=254, null=True, verbose_name='作者邮箱')),
                ('phone', models.CharField(blank=True, max_length=11, null=True, verbose_name='作者电话')),
            ],
            options={
                'verbose_name': '作者',
                'verbose_name_plural': '作者',
            },
        ),
        migrations.CreateModel(
            name='Classify',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=32, verbose_name='分类标签')),
                ('description', models.TextField(verbose_name='分类描述')),
            ],
            options={
                'verbose_name': '分类',
                'verbose_name_plural': '分类',
            },
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=32, verbose_name='文章标题')),
                ('time', models.DateField(verbose_name='文章发表日期')),
                ('description', ckeditor_uploader.fields.RichTextUploadingField(verbose_name='文章描述')),
                ('content', ckeditor_uploader.fields.RichTextUploadingField(verbose_name='文章内容')),
                ('picture', models.ImageField(default='image/default.png', upload_to='images/%Y%m', verbose_name='文章图片')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='xadmin_App.Author')),
                ('classify', models.ManyToManyField(to='xadmin_App.Classify')),
            ],
            options={
                'verbose_name': '文章',
                'verbose_name_plural': '文章',
            },
        ),
    ]

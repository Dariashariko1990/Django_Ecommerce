# Generated by Django 2.2.10 on 2020-06-24 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='price',
            field=models.FloatField(default=0, verbose_name='Цена'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(default='', max_length=150, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=50, verbose_name='Модель'),
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Категория')),
                ('products', models.ManyToManyField(blank=True, related_name='category', to='app.Product')),
            ],
        ),
    ]

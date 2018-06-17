# Generated by Django 2.0.5 on 2018-06-17 20:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='pullover',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tittle', models.CharField(blank=True, max_length=100, null=True, verbose_name='Название')),
                ('adress', models.CharField(blank=True, max_length=200, null=True, verbose_name='Ссылка')),
                ('price', models.IntegerField(default=0, verbose_name='Цена')),
                ('photo', models.ImageField(upload_to='image/', verbose_name='Изображение')),
                ('top', models.BooleanField(default=False, verbose_name='В топ?')),
            ],
            options={
                'verbose_name': 'Свитшоты',
                'verbose_name_plural': 'Свитшоты',
            },
        ),
    ]

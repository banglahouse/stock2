# Generated by Django 3.2.5 on 2021-07-28 03:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='stock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stockName', models.CharField(max_length=100)),
                ('stockPrice', models.CharField(max_length=10)),
                ('stockSl', models.CharField(max_length=10)),
                ('stockTarget', models.CharField(max_length=10)),
                ('stockAdvice', models.CharField(max_length=10)),
                ('timeStamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]

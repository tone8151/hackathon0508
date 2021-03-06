# Generated by Django 2.2.22 on 2021-05-08 10:15

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Match',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('player1', models.CharField(max_length=30)),
                ('player2', models.CharField(max_length=30)),
                ('match_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('winner', models.CharField(choices=[(models.CharField(max_length=30), models.CharField(max_length=30)), (models.CharField(max_length=30), models.CharField(max_length=30))], default='plyaer1', max_length=30)),
            ],
        ),
    ]

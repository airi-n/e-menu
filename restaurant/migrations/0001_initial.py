# Generated by Django 4.1.1 on 2022-11-04 09:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Jp_name', models.TextField()),
                ('category', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('method', models.CharField(max_length=5)),
                ('price', models.IntegerField()),
                ('num_people', models.IntegerField()),
                ('photo', models.ImageField(upload_to='')),
                ('cuisine_num', models.IntegerField(blank=True, null=True)),
                ('Restaurant_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.restaurant')),
                ('ingredient', models.ManyToManyField(to='restaurant.ingredient')),
            ],
        ),
    ]

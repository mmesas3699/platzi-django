# Generated by Django 2.0.1 on 2018-02-25 23:30

from django.db import migrations, models

def create_continent(apps, schema_editor):
    Continent = apps.get_model('continents', 'Continent')

    Continent.objects.create(name='Asia', color='red', translate='Asia')
    Continent.objects.create(name='Europa', color='blue', translate='Europa')
    Continent.objects.create(name='America', color='yellow', translate='America')
    Continent.objects.create(name='Africa', color='black', translate='Africa')
    Continent.objects.create(name='Oceania', color='grey', translate='Oceania')


class Migration(migrations.Migration):

    dependencies = [
        ('countries', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_continent),
        migrations.AlterField(
            model_name='country',
            name='code',
            field=models.CharField(choices=[('Colombia', 'CO'), ('Estados Unidos', 'USA'), ('Mexico', 'MX')], max_length=3),
        ),
    ]
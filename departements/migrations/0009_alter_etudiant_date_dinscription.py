# Generated by Django 3.2.4 on 2021-07-23 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('departements', '0008_auto_20210721_1443'),
    ]

    operations = [
        migrations.AlterField(
            model_name='etudiant',
            name='date_dinscription',
            field=models.DateField(),
        ),
    ]

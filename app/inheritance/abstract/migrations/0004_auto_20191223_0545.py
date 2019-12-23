# Generated by Django 2.2.9 on 2019-12-23 05:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('abstract', '0003_auto_20191223_0537'),
    ]

    operations = [
        migrations.AlterField(
            model_name='childa',
            name='m2m',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='abstract_childa_set', to='abstract.Student'),
        ),
        migrations.AlterField(
            model_name='childb',
            name='m2m',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='abstract_childb_set', to='abstract.Student'),
        ),
    ]

# Generated by Django 4.2.5 on 2023-10-08 05:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0002_alter_author_age'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='booktype',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='book.booktype'),
        ),
    ]
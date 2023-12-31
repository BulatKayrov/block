# Generated by Django 4.2.4 on 2023-08-09 05:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('slug', models.SlugField(unique=True)),
                ('sort_page', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Block',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('link', models.TextField()),
                ('sort_block', models.IntegerField(default=0)),
                ('count_view', models.IntegerField(default=0)),
                ('page', models.ManyToManyField(related_name='block', to='page_content.page')),
            ],
        ),
    ]

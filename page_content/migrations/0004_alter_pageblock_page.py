# Generated by Django 4.2.4 on 2023-08-09 13:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('page_content', '0003_remove_block_sort_block_pageblock_alter_block_page'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pageblock',
            name='page',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='page_block', to='page_content.page'),
        ),
    ]

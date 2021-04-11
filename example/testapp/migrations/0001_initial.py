# Generated by Django 1.9.7 on 2016-06-11 08:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True, verbose_name='Name')),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Chapter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=255, null=True, verbose_name='Title')),
                ('my_order', models.PositiveIntegerField()),
            ],
            options={
                'ordering': ['my_order'],
            },
        ),
        migrations.CreateModel(
            name='Notes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('note', models.CharField(blank=True, max_length=255, null=True, verbose_name='Note')),
            ],
        ),
        migrations.CreateModel(
            name='SortableBook',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=255, null=True, verbose_name='Title')),
                ('my_order', models.PositiveIntegerField(default=0)),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='testapp.Author')),
            ],
            options={
                'ordering': ['my_order'],
            },
        ),
        migrations.AddField(
            model_name='notes',
            name='book',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='testapp.SortableBook'),
        ),
        migrations.AddField(
            model_name='chapter',
            name='book',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='testapp.SortableBook'),
        ),
    ]

# Generated by Django 3.0.2 on 2020-02-02 18:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mac', '0002_auto_20200201_0016'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('msg_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=70)),
                ('email', models.CharField(max_length=70)),
                ('phone', models.CharField(default='', max_length=50)),
                ('desc', models.CharField(default='', max_length=500)),
            ],
        ),
        migrations.AlterField(
            model_name='product',
            name='desc',
            field=models.CharField(max_length=500),
        ),
    ]

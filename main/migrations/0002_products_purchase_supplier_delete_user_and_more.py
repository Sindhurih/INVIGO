# Generated by Django 4.2.2 on 2023-06-14 16:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('created', models.DateTimeField(auto_created=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('product_no', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('name', models.TextField(max_length=200)),
                ('quantity', models.IntegerField()),
                ('price', models.FloatField()),
                ('pescription', models.TextField(max_length=250)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Purchase',
            fields=[
                ('created', models.DateTimeField(auto_created=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('billno', models.AutoField(primary_key=True, serialize=False)),
                ('time', models.DateTimeField(auto_now=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('created', models.DateTimeField(auto_created=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=150)),
                ('phone', models.CharField(max_length=12, unique=True)),
                ('address', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('gstin', models.CharField(max_length=15, unique=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.DeleteModel(
            name='User',
        ),
        migrations.AddField(
            model_name='purchase',
            name='supplier',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='purchasesupplier', to='main.supplier'),
        ),
    ]

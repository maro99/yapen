# Generated by Django 2.1 on 2018-08-07 01:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=300, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Pension',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('pension_image_thumbnail', models.ImageField(blank=True, upload_to='pension')),
                ('lowest_price', models.IntegerField(blank=True, default=0)),
                ('ypidx', models.IntegerField(blank=True, default=0)),
                ('location', models.CharField(blank=True, max_length=100)),
                ('sub_location', models.CharField(blank=True, max_length=100)),
                ('discount_rate', models.IntegerField(blank=True, default=0)),
                ('address', models.TextField(blank=True, max_length=200)),
                ('check_in', models.CharField(blank=True, max_length=100)),
                ('check_out', models.CharField(blank=True, max_length=100)),
                ('pickup', models.CharField(blank=True, max_length=100)),
                ('room_num', models.IntegerField(blank=True, default=0)),
                ('info', models.TextField(blank=True)),
                ('theme', models.TextField(blank=True)),
                ('lat', models.FloatField(blank=True, default=0)),
                ('lng', models.FloatField(blank=True, default=0)),
                ('check_in_out_detail', models.TextField(blank=True)),
                ('pickup_detail', models.TextField(blank=True)),
                ('gretting', models.TextField(blank=True)),
                ('precautions', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='PensionImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pension_image', models.ImageField(blank=True, upload_to='pension')),
            ],
        ),
        migrations.CreateModel(
            name='PensionLike',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(blank=True)),
                ('subscriber', models.CharField(blank=True, max_length=100)),
                ('phone_number', models.CharField(blank=True, max_length=100)),
                ('birth_date', models.CharField(blank=True, max_length=100)),
                ('pickup_or_not', models.BooleanField(blank=True, default=True)),
                ('entering_time', models.CharField(blank=True, max_length=100)),
                ('requested_term', models.TextField(blank=True)),
                ('deposit_bank', models.CharField(blank=True, max_length=100)),
                ('depositor_name', models.CharField(blank=True, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('structure', models.CharField(blank=True, max_length=100)),
                ('equipments', models.TextField(blank=True)),
                ('info', models.TextField(blank=True)),
                ('size', models.CharField(blank=True, max_length=100)),
                ('normal_num_poeple', models.IntegerField(blank=True, default=0)),
                ('max_num_people', models.IntegerField(blank=True, default=0)),
                ('price', models.IntegerField(blank=True, default=0)),
                ('extra_charge_head', models.CharField(blank=True, max_length=100)),
                ('extra_charge_adult', models.IntegerField(blank=True, default=0)),
                ('extra_charge_child', models.IntegerField(blank=True, default=0)),
                ('extra_charge_baby', models.IntegerField(blank=True, default=0)),
                ('pension', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='location.Pension')),
            ],
        ),
        migrations.CreateModel(
            name='RoomImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room_image', models.ImageField(blank=True, upload_to='room')),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='location.Room')),
            ],
        ),
        migrations.AddField(
            model_name='reservation',
            name='room',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='location.Room'),
        ),
    ]

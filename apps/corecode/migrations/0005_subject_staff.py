# Generated by Django 4.2.11 on 2024-03-31 12:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('staffs', '0008_remove_staff_id_alter_staff_empid'),
        ('corecode', '0004_auto_20201124_0614'),
    ]

    operations = [
        migrations.AddField(
            model_name='subject',
            name='staff',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='staffs.staff'),
        ),
    ]

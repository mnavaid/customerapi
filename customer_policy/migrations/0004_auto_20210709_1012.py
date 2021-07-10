# Generated by Django 3.1.2 on 2021-07-09 17:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0002_auto_20210708_0559'),
        ('customer_policy', '0003_customerpolicy_policy'),
    ]

    operations = [
        migrations.RenameField(
            model_name='policy',
            old_name='type',
            new_name='ptype',
        ),
        migrations.AlterField(
            model_name='customerpolicy',
            name='customer_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='customer', to='customer.customer'),
        ),
        migrations.AlterField(
            model_name='customerpolicy',
            name='policy_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='policy', to='customer_policy.policy'),
        ),
    ]
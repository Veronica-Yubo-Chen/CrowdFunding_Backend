# Generated migration for complex logic features

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('fundraisers', '0007_fundraiser_category_fundraiser_product_link'),
    ]

    operations = [
        migrations.AddField(
            model_name='fundraiser',
            name='deadline',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='fundraiser',
            name='is_public',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='pledge',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterUniqueTogether(
            name='pledge',
            unique_together={('fundraiser', 'supporter')},
        ),
    ]

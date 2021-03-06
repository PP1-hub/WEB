from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='company',
            options={'verbose_name_plural': 'Companies'},
        ),
        migrations.AlterModelOptions(
            name='vacancy',
            options={'verbose_name_plural': 'Vacancies'},
        ),
        migrations.AddField(
            model_name='company',
            name='address',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='company',
            name='description',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='vacancy',
            name='description',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='vacancy',
            name='salary',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='company',
            name='city',
            field=models.CharField(max_length=300),
        ),
        migrations.AlterField(
            model_name='vacancy',
            name='company',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='api.Company'),
        ),
    ]
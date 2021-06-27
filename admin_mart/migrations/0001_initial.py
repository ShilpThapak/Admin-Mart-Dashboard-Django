# Generated by Django 3.2.4 on 2021-06-27 13:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Incident',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(choices=[('CH', 'Corporate Headpffice'), ('OD', 'Operations Department'), ('WS', 'Work Station'), ('MD', 'Marketing Division')], max_length=50)),
                ('department', models.TextField()),
                ('datetime', models.DateTimeField()),
                ('incident_location', models.TextField()),
                ('initial_severity', models.CharField(choices=[('Mild', 'Mild'), ('Moderate', 'Moderate'), ('Severe', 'Severe'), ('Fatal', 'Fatal')], max_length=10)),
                ('suspected_cause', models.TextField()),
                ('immediate_action_taken', models.TextField()),
                ('sub_incident_types', models.CharField(choices=[('Environmental Incident', 'Environmental Incident'), ('Injury/Illness', 'Injury/Illness'), ('Property Damage', 'Property Damage'), ('Vehicle', 'Vehicle')], max_length=100)),
                ('saved', models.BooleanField()),
                ('reported_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
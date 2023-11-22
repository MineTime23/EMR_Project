# Generated by Django 4.2.7 on 2023-11-21 13:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DiagnosticRecords',
            fields=[
                ('diagnosis_code', models.AutoField(primary_key=True, serialize=False)),
                ('diagnosis_date', models.DateField(auto_now_add=True)),
                ('symptoms', models.CharField(blank=True, max_length=55, null=True)),
                ('diagnosis', models.CharField(blank=True, max_length=55, null=True)),
                ('comments', models.CharField(blank=True, max_length=55, null=True)),
                ('prescription_code', models.CharField(blank=True, max_length=15, null=True)),
                ('patient', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='api.patient')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='api.user')),
            ],
        ),
        migrations.CreateModel(
            name='TreatmentRecords',
            fields=[
                ('treatment_code', models.AutoField(primary_key=True, serialize=False)),
                ('date', models.DateField(auto_now_add=True)),
                ('treatment_type', models.CharField(blank=True, max_length=30, null=True)),
                ('duration', models.IntegerField(blank=True, null=True)),
                ('time', models.IntegerField(blank=True, null=True)),
                ('patient', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='치료', to='api.patient')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='치료', to='api.user')),
            ],
        ),
        migrations.CreateModel(
            name='TestRecords',
            fields=[
                ('test_code', models.AutoField(primary_key=True, serialize=False)),
                ('MuscleMass', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('BodyFatMass', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('Muscular_strength', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('cardio_endurance', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('agility', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('flexibility', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('date', models.DateField()),
                ('patient', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='api.patient')),
            ],
        ),
        migrations.CreateModel(
            name='Prescription',
            fields=[
                ('prescription_code', models.AutoField(primary_key=True, serialize=False)),
                ('medication_name', models.CharField(max_length=100)),
                ('total_dosage', models.DecimalField(decimal_places=2, max_digits=10)),
                ('frequency', models.IntegerField()),
                ('duration_days', models.IntegerField()),
                ('unit', models.CharField(max_length=20)),
                ('medical_record', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.diagnosticrecords')),
            ],
        ),
        migrations.CreateModel(
            name='MediaRecords',
            fields=[
                ('data_code', models.AutoField(primary_key=True, serialize=False)),
                ('inbody_url', models.CharField(blank=True, max_length=255, null=True)),
                ('video_url', models.CharField(blank=True, max_length=255, null=True)),
                ('xray_url', models.CharField(blank=True, max_length=255, null=True)),
                ('Field4', models.CharField(blank=True, max_length=255, null=True)),
                ('patient', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='api.patient')),
            ],
        ),
        migrations.CreateModel(
            name='ExerciseRecords',
            fields=[
                ('exercise_code', models.AutoField(primary_key=True, serialize=False)),
                ('date', models.DateField(auto_now_add=True)),
                ('iteration', models.IntegerField(blank=True, null=True)),
                ('weight', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('duration', models.IntegerField(blank=True, null=True)),
                ('speed', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('distance', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('exercise_type', models.CharField(blank=True, choices=[('strength', '무산소'), ('cardio', '유산소')], max_length=10, null=True)),
                ('patient', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='운동', to='api.patient')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='운동', to='api.user')),
            ],
        ),
        migrations.CreateModel(
            name='Appointments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('appointment_date', models.DateField()),
                ('appointment_time', models.TimeField()),
                ('symptoms', models.TextField()),
                ('purpose', models.TextField()),
                ('status', models.CharField(choices=[('pending', 'Pending'), ('in_progress', 'In Progress'), ('completed', 'Completed')], default='pending', max_length=12)),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='doctor_appointments', to='api.user')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='patient_appointments', to='api.patient')),
            ],
        ),
    ]

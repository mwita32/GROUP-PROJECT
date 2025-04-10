# Generated by Django 4.2.20 on 2025-04-09 20:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='feebalance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reg_no', models.CharField(max_length=20, unique=True)),
                ('total_fees', models.DecimalField(decimal_places=2, max_digits=10)),
                ('amount_paid', models.DecimalField(decimal_places=2, max_digits=10)),
                ('balance', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField()),
                ('is_read', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='StudentApplication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('parental_status', models.CharField(choices=[('both', 'Have both parents'), ('one', 'Have one parent'), ('orphan', 'Total orphan')], max_length=10)),
                ('name', models.CharField(max_length=100)),
                ('reg_no', models.CharField(max_length=50, unique=True)),
                ('school', models.CharField(choices=[('SCI', 'SCI'), ('SEDU', 'SEDU'), ('SDHMA', 'SDHMA'), ('SOM', 'SOM'), ('SEBE', 'SEBE'), ('SASS', 'SASS'), ('SONAS', 'SONAS'), ('SONMAPS', 'SONMAPS'), ('SPB&T', 'SPB&T'), ('SOBE', 'SOBE'), ('SAVET', 'SAVET')], max_length=100)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1)),
                ('home_address', models.CharField(max_length=255)),
                ('phone_number', models.CharField(max_length=15)),
                ('county', models.CharField(choices=[('Baringo', 'Baringo'), ('Bomet', 'Bomet'), ('Bungoma', 'Bungoma'), ('Busia', 'Busia'), ('Elgeyo Marakwet', 'Elgeyo Marakwet'), ('Embu', 'Embu'), ('Garissa', 'Garissa'), ('Homa Bay', 'Homa Bay'), ('Isiolo', 'Isiolo'), ('Kajiado', 'Kajiado'), ('Kakamega', 'Kakamega'), ('Kericho', 'Kericho'), ('Kiambu', 'Kiambu'), ('Kilifi', 'Kilifi'), ('Kirinyaga', 'Kirinyaga'), ('Kisii', 'Kisii'), ('Kisumu', 'Kisumu'), ('Kitui', 'Kitui'), ('Kwale', 'Kwale'), ('Laikipia', 'Laikipia'), ('Lamu', 'Lamu'), ('Machakos', 'Machakos'), ('Makueni', 'Makueni'), ('Mandera', 'Mandera'), ('Marsabit', 'Marsabit'), ('Meru', 'Meru'), ('Migori', 'Migori'), ('Mombasa', 'Mombasa'), ("Murang'a", "Murang'a"), ('Nairobi', 'Nairobi'), ('Nakuru', 'Nakuru'), ('Nandi', 'Nandi'), ('Narok', 'Narok'), ('Nyamira', 'Nyamira'), ('Nyandarua', 'Nyandarua'), ('Nyeri', 'Nyeri'), ('Samburu', 'Samburu'), ('Siaya', 'Siaya'), ('Taita Taveta', 'Taita Taveta'), ('Tana River', 'Tana River'), ('Tharaka Nithi', 'Tharaka Nithi'), ('Trans Nzoia', 'Trans Nzoia'), ('Turkana', 'Turkana'), ('Uasin Gishu', 'Uasin Gishu'), ('Vihiga', 'Vihiga'), ('Wajir', 'Wajir'), ('West Pokot', 'West Pokot')], max_length=20)),
                ('next_of_kin', models.CharField(max_length=100)),
                ('next_of_kin_address', models.CharField(max_length=255)),
                ('next_of_kin_phone', models.CharField(max_length=15)),
                ('chief_name', models.CharField(max_length=100)),
                ('chief_address', models.CharField(max_length=255)),
                ('chief_phone', models.CharField(max_length=15)),
                ('disability', models.BooleanField(default=False)),
                ('disability_details', models.CharField(blank=True, max_length=255, null=True)),
                ('student_status', models.CharField(choices=[('KUCCPS', 'Government Sponsored (KUCCPS)'), ('PSSP', 'Self Sponsored (PSSP)')], max_length=10)),
                ('residential_status', models.CharField(choices=[('Resident', 'Resident'), ('Non Resident', 'Non Resident')], max_length=15)),
                ('death_certificate', models.FileField(blank=True, null=True, upload_to='documents/')),
                ('father_age', models.IntegerField(blank=True, null=True)),
                ('father_occupation', models.CharField(blank=True, max_length=100, null=True)),
                ('father_employer', models.CharField(choices=[('Employed', 'Employed'), ('Not employed', 'Not employed')], max_length=100)),
                ('father_health_status', models.FileField(blank=True, null=True, upload_to='documents/')),
                ('mother_age', models.IntegerField(blank=True, null=True)),
                ('mother_occupation', models.CharField(blank=True, max_length=100, null=True)),
                ('mother_employer', models.CharField(choices=[('Employed', 'Employed'), ('Not employed', 'Not employed')], max_length=100)),
                ('mother_health_status', models.FileField(blank=True, null=True, upload_to='documents/')),
                ('total_siblings', models.IntegerField()),
                ('university_siblings', models.IntegerField(blank=True, null=True)),
                ('secondary_siblings', models.IntegerField(blank=True, null=True)),
                ('out_of_school_siblings', models.IntegerField(blank=True, null=True)),
                ('out_of_school_reason', models.TextField(blank=True, null=True)),
                ('working_siblings_occupation', models.TextField(blank=True, null=True)),
                ('school_fee_payer', models.CharField(choices=[('Parent', 'Parent'), ('External Sponsor', 'External Sponsor')], max_length=255)),
                ('school_fee_evidence', models.FileField(blank=True, null=True, upload_to='documents/')),
                ('work_study', models.CharField(choices=[('yes', 'Yes'), ('no', 'No')], max_length=3)),
                ('work_study_evidence', models.FileField(blank=True, null=True, upload_to='documents/')),
                ('external_support', models.CharField(choices=[('yes', 'Yes'), ('no', 'No')], max_length=3)),
                ('sponsor_source', models.CharField(blank=True, choices=[('HELB', 'HELB'), ('NGO', 'NGO'), ('CDF', 'CDF'), ('Other', 'Other')], max_length=50, null=True)),
                ('sponsor_amount', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('tuition_fee_paid', models.CharField(choices=[('yes', 'Yes'), ('no', 'No')], max_length=3)),
                ('fee_balance', models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=10, null=True)),
                ('fee_statement', models.FileField(blank=True, null=True, upload_to='documents/')),
                ('deferred_study', models.CharField(choices=[('yes', 'Yes'), ('no', 'No')], max_length=3)),
                ('defer_reason', models.CharField(blank=True, choices=[('Medical', 'Medical'), ('Social', 'Social'), ('Financial', 'Financial'), ('Academic', 'Academic')], max_length=50, null=True)),
                ('additional_info', models.TextField(blank=True, null=True)),
                ('additional_info_evidence', models.FileField(blank=True, null=True, upload_to='documents/')),
                ('academic_year', models.CharField(default='2024/2025', max_length=9)),
                ('status', models.CharField(choices=[('Pending', 'Pending'), ('Approved', 'Approved'), ('Rejected', 'Rejected')], default='Pending', max_length=10)),
                ('submitted_at', models.DateTimeField(auto_now_add=True)),
                ('reviewed_at', models.DateTimeField(blank=True, null=True)),
                ('approved_amount', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('student', 'academic_year')},
            },
        ),
    ]

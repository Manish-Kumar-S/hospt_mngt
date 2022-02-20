
from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0015_auto_20200526_1501'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='mobile',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='mobile',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='patientdischargedetails',
            name='mobile',
            field=models.CharField(max_length=20, null=True),
        ),
    ]

# Generated by Django 2.2.5 on 2020-01-23 12:30

from django.db import migrations, models
import django.db.models.manager


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GDPTable',
            fields=[
                ('no', models.AutoField(primary_key=True, serialize=False)),
                ('CountryName', models.CharField(max_length=300)),
                ('gdp_1960', models.FloatField(default=0.0, null=True)),
                ('gdp_1961', models.FloatField(default=0.0, null=True)),
                ('gdp_1962', models.FloatField(default=0.0, null=True)),
                ('gdp_1963', models.FloatField(default=0.0, null=True)),
                ('gdp_1964', models.FloatField(default=0.0, null=True)),
                ('gdp_1965', models.FloatField(default=0.0, null=True)),
                ('gdp_1966', models.FloatField(default=0.0, null=True)),
                ('gdp_1967', models.FloatField(default=0.0, null=True)),
                ('gdp_1968', models.FloatField(default=0.0, null=True)),
                ('gdp_1969', models.FloatField(default=0.0, null=True)),
                ('gdp_1970', models.FloatField(default=0.0, null=True)),
                ('gdp_1971', models.FloatField(default=0.0, null=True)),
                ('gdp_1972', models.FloatField(default=0.0, null=True)),
                ('gdp_1973', models.FloatField(default=0.0, null=True)),
                ('gdp_1974', models.FloatField(default=0.0, null=True)),
                ('gdp_1975', models.FloatField(default=0.0, null=True)),
                ('gdp_1976', models.FloatField(default=0.0, null=True)),
                ('gdp_1977', models.FloatField(default=0.0, null=True)),
                ('gdp_1978', models.FloatField(default=0.0, null=True)),
                ('gdp_1979', models.FloatField(default=0.0, null=True)),
                ('gdp_1980', models.FloatField(default=0.0, null=True)),
                ('gdp_1981', models.FloatField(default=0.0, null=True)),
                ('gdp_1982', models.FloatField(default=0.0, null=True)),
                ('gdp_1983', models.FloatField(default=0.0, null=True)),
                ('gdp_1984', models.FloatField(default=0.0, null=True)),
                ('gdp_1985', models.FloatField(default=0.0, null=True)),
                ('gdp_1986', models.FloatField(default=0.0, null=True)),
                ('gdp_1987', models.FloatField(default=0.0, null=True)),
                ('gdp_1988', models.FloatField(default=0.0, null=True)),
                ('gdp_1989', models.FloatField(default=0.0, null=True)),
                ('gdp_1990', models.FloatField(default=0.0, null=True)),
                ('gdp_1991', models.FloatField(default=0.0, null=True)),
                ('gdp_1992', models.FloatField(default=0.0, null=True)),
                ('gdp_1993', models.FloatField(default=0.0, null=True)),
                ('gdp_1994', models.FloatField(default=0.0, null=True)),
                ('gdp_1995', models.FloatField(default=0.0, null=True)),
                ('gdp_1996', models.FloatField(default=0.0, null=True)),
                ('gdp_1997', models.FloatField(default=0.0, null=True)),
                ('gdp_1998', models.FloatField(default=0.0, null=True)),
                ('gdp_1999', models.FloatField(default=0.0, null=True)),
                ('gdp_2000', models.FloatField(default=0.0, null=True)),
                ('gdp_2001', models.FloatField(default=0.0, null=True)),
                ('gdp_2002', models.FloatField(default=0.0, null=True)),
                ('gdp_2003', models.FloatField(default=0.0, null=True)),
                ('gdp_2004', models.FloatField(default=0.0, null=True)),
                ('gdp_2005', models.FloatField(default=0.0, null=True)),
                ('gdp_2006', models.FloatField(default=0.0, null=True)),
                ('gdp_2007', models.FloatField(default=0.0, null=True)),
                ('gdp_2008', models.FloatField(default=0.0, null=True)),
                ('gdp_2009', models.FloatField(default=0.0, null=True)),
                ('gdp_2010', models.FloatField(default=0.0, null=True)),
                ('gdp_2011', models.FloatField(default=0.0, null=True)),
                ('gdp_2012', models.FloatField(default=0.0, null=True)),
                ('gdp_2013', models.FloatField(default=0.0, null=True)),
                ('gdp_2014', models.FloatField(default=0.0, null=True)),
                ('gdp_2015', models.FloatField(default=0.0, null=True)),
                ('gdp_2016', models.FloatField(default=0.0, null=True)),
                ('gdp_2017', models.FloatField(default=0.0, null=True)),
                ('gdp_2018', models.FloatField(default=0.0, null=True)),
                ('gdp_2019', models.FloatField(default=0.0, null=True)),
            ],
            managers=[
                ('object', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='PopulationTable',
            fields=[
                ('no', models.AutoField(primary_key=True, serialize=False)),
                ('CountryName', models.CharField(max_length=300)),
                ('population_1960', models.FloatField(default=0.0, null=True)),
                ('population_1961', models.FloatField(default=0.0, null=True)),
                ('population_1962', models.FloatField(default=0.0, null=True)),
                ('population_1963', models.FloatField(default=0.0, null=True)),
                ('population_1964', models.FloatField(default=0.0, null=True)),
                ('population_1965', models.FloatField(default=0.0, null=True)),
                ('population_1966', models.FloatField(default=0.0, null=True)),
                ('population_1967', models.FloatField(default=0.0, null=True)),
                ('population_1968', models.FloatField(default=0.0, null=True)),
                ('population_1969', models.FloatField(default=0.0, null=True)),
                ('population_1970', models.FloatField(default=0.0, null=True)),
                ('population_1971', models.FloatField(default=0.0, null=True)),
                ('population_1972', models.FloatField(default=0.0, null=True)),
                ('population_1973', models.FloatField(default=0.0, null=True)),
                ('population_1974', models.FloatField(default=0.0, null=True)),
                ('population_1975', models.FloatField(default=0.0, null=True)),
                ('population_1976', models.FloatField(default=0.0, null=True)),
                ('population_1977', models.FloatField(default=0.0, null=True)),
                ('population_1978', models.FloatField(default=0.0, null=True)),
                ('population_1979', models.FloatField(default=0.0, null=True)),
                ('population_1980', models.FloatField(default=0.0, null=True)),
                ('population_1981', models.FloatField(default=0.0, null=True)),
                ('population_1982', models.FloatField(default=0.0, null=True)),
                ('population_1983', models.FloatField(default=0.0, null=True)),
                ('population_1984', models.FloatField(default=0.0, null=True)),
                ('population_1985', models.FloatField(default=0.0, null=True)),
                ('population_1986', models.FloatField(default=0.0, null=True)),
                ('population_1987', models.FloatField(default=0.0, null=True)),
                ('population_1988', models.FloatField(default=0.0, null=True)),
                ('population_1989', models.FloatField(default=0.0, null=True)),
                ('population_1990', models.FloatField(default=0.0, null=True)),
                ('population_1991', models.FloatField(default=0.0, null=True)),
                ('population_1992', models.FloatField(default=0.0, null=True)),
                ('population_1993', models.FloatField(default=0.0, null=True)),
                ('population_1994', models.FloatField(default=0.0, null=True)),
                ('population_1995', models.FloatField(default=0.0, null=True)),
                ('population_1996', models.FloatField(default=0.0, null=True)),
                ('population_1997', models.FloatField(default=0.0, null=True)),
                ('population_1998', models.FloatField(default=0.0, null=True)),
                ('population_1999', models.FloatField(default=0.0, null=True)),
                ('population_2000', models.FloatField(default=0.0, null=True)),
                ('population_2001', models.FloatField(default=0.0, null=True)),
                ('population_2002', models.FloatField(default=0.0, null=True)),
                ('population_2003', models.FloatField(default=0.0, null=True)),
                ('population_2004', models.FloatField(default=0.0, null=True)),
                ('population_2005', models.FloatField(default=0.0, null=True)),
                ('population_2006', models.FloatField(default=0.0, null=True)),
                ('population_2007', models.FloatField(default=0.0, null=True)),
                ('population_2008', models.FloatField(default=0.0, null=True)),
                ('population_2009', models.FloatField(default=0.0, null=True)),
                ('population_2010', models.FloatField(default=0.0, null=True)),
                ('population_2011', models.FloatField(default=0.0, null=True)),
                ('population_2012', models.FloatField(default=0.0, null=True)),
                ('population_2013', models.FloatField(default=0.0, null=True)),
                ('population_2014', models.FloatField(default=0.0, null=True)),
                ('population_2015', models.FloatField(default=0.0, null=True)),
                ('population_2016', models.FloatField(default=0.0, null=True)),
                ('population_2017', models.FloatField(default=0.0, null=True)),
                ('population_2018', models.FloatField(default=0.0, null=True)),
                ('population_2019', models.FloatField(default=0.0, null=True)),
            ],
        ),
    ]

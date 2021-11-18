from datetime import datetime

my_datetime = datetime.utcnow()
print(my_datetime)

date_LATAM = my_datetime.strftime('%d-%m-%Y')
print(f'LATAM format: {date_LATAM}')

date_USA = my_datetime.strftime('%m-%d-%Y')
print(f'USA format: {date_USA}')

my_year = my_datetime.strftime('Estamos en el año: %Y')
print(f'My year format: {my_year}')
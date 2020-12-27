import datetime

def horaActual(zonahoraria=-3):
  formato = "%H:%M:%S"
  time_zone = datetime.timezone(datetime.timedelta(hours=zonahoraria))
  hora_actual = datetime.datetime.now(time_zone).time()
  hora_formateada = hora_actual.strftime(formato)
  print(hora_formateada)

def fechayhora(zonahoraria=-3):
  formato = "%d %B %Y - %H:%M:%S"
  time_zone = datetime.timezone(datetime.timedelta(hours=zonahoraria))
  fechahora = datetime.datetime.now(time_zone)
  fecha_hora_formateada = fechahora.strftime(formato)
  print(fecha_hora_formateada)



def limpiar():
    import os
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def menu():
  print("\n1_")
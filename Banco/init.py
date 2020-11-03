from clientepe import Persona
from classic import Classic
# import datetime
# import calendar
# today=datetime.datetime.now()
 
# dateMonthStart="%s-%s-01" % (today.year, today.month)
# dateMonthEnd="%s-%s-%s" % (today.year, today.month, calendar.monthrange(today.year, today.month)[1])

# print("primer dia del mes: %s" % dateMonthStart)
# print("Ultimo dia del mes: %s" % dateMonthEnd)


cuenta=Classic(123141412)
cliente1 = Persona("Andres","K",12313,"asdasd",5234234,cuenta)

print(cliente1.get_cuenta().get_cbu())



from datetime import datetime
from tabulate import tabulate

fechaReporte = "2020-11-30"
fechaReporte = datetime.strptime(fechaReporte, '%Y-%m-%d') 




file = open("file_amortizacion.txt", "r")
file_valores = open("val_reporte_auto.txt", "r")
val_line = file_valores.readline()
arrLine_val = val_line.split()

##Valores obtenidos del reporte
moi_repo = float(arrLine_val[0])
ej_mensual_repo = float(arrLine_val[1])
ej_acumulado_repo = float(arrLine_val[2])
vu_exigido_repo = float(arrLine_val[3])
vu_porexigir_repo = float(arrLine_val[4])


##Resultados obtenidos de sumas
moi_res = 0
ej_mensual_res = 0
ej_acumulado_res = 0
vu_exigido_res = 0
vu_porexigir_res = 0

enganche = 0
residual = 0
capitalTotal = 0

fechaFiltro = []
arrCapital = []

for line in file:
    arrLine = line.split(",")
    
    enganche = float(arrLine[1])
    residual = float(arrLine[2])

    capitalTotal = capitalTotal +  float(arrLine[3])

    arrCapital.append(arrLine[3])
    fechaFiltro.append(arrLine[5])


for i, fecha in enumerate(fechaFiltro):
    fecha = datetime.strptime(fecha, '%Y-%m-%d')
    mes = fecha.month
    year = fecha.year
    if mes == fechaReporte.month and year == fechaReporte.year:
        ej_mensual_res = ej_mensual_res + float(arrCapital[i])

for i, fecha in enumerate(fechaFiltro):
    fecha = datetime.strptime(fecha, '%Y-%m-%d')
    mes = fecha.month
    year = fecha.year
    if year == fechaReporte.year:
        ej_acumulado_res = ej_acumulado_res + float(arrCapital[i])

for i, fecha in enumerate(fechaFiltro):
    fecha = datetime.strptime(fecha, '%Y-%m-%d')    
    if fecha < fechaReporte:
        vu_exigido_res = vu_exigido_res + float(arrCapital[i])


for i, fecha in enumerate(fechaFiltro):
    fecha = datetime.strptime(fecha, '%Y-%m-%d')    
    if fecha > fechaReporte:
        vu_porexigir_res = vu_porexigir_res + float(arrCapital[i])

data = []
moi = capitalTotal + float(enganche) + float(residual)

if moi_repo == round(moi,2):
    data.append([moi, moi_repo, 'true'])
else:
    data.append([moi, moi_repo, 'false'])

if ej_mensual_repo == round(ej_mensual_res, 2):
    data.append([ej_mensual_res, ej_mensual_repo, 'true'])
else:
    data.append([ej_mensual_res, ej_mensual_repo, 'false'])

if ej_acumulado_repo == round(ej_acumulado_res, 2):
    data.append([ej_acumulado_res, ej_acumulado_repo, 'true'])    
else:
    data.append([ej_acumulado_res, ej_acumulado_repo, 'false']) 

vu_exigido_res = vu_exigido_res + float(enganche)
if vu_exigido_repo == round(vu_exigido_res, 2):
    data.append([vu_exigido_res, vu_exigido_repo, 'true']) 
else:
    data.append([vu_exigido_res, vu_exigido_repo, 'false']) 

if vu_porexigir_repo == round(vu_porexigir_res, 2):
    data.append([vu_porexigir_res, vu_porexigir_repo, 'true'])
else:
    data.append([vu_porexigir_res, vu_porexigir_repo, 'false'])


print (tabulate(data, headers=["Pos", "Team", "Win", "Lose"]))
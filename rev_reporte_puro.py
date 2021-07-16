
from datetime import datetime
from tabulate import tabulate

fechaReporte = "2020-11-30"
fechaReporte = datetime.strptime(fechaReporte, '%Y-%m-%d') 




file = open("archivos/file_amortizacion.txt", "r")
file_valores = open("archivos/val_reporte_auto.txt", "r")
val_line = file_valores.readline()
arrLine_val = val_line.split()

##Valores obtenidos del reporte
moi_repo = float(arrLine_val[0].replace(",", ""))
ej_mensual_repo = float(arrLine_val[1].replace(",", ""))
ej_acumulado_repo = float(arrLine_val[2].replace(",", ""))
vu_exigido_repo = float(arrLine_val[3].replace(",", ""))
vu_porexigir_repo = float(arrLine_val[4].replace(",", ""))


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
moi = round(moi, 2)
if moi_repo == moi:
    data.append(["MOI", moi, moi_repo, 'true'])
else:
    data.append(["MOI", moi, moi_repo, 'false'])

ej_mensual_res = round(ej_mensual_res, 2)
if ej_mensual_repo == ej_mensual_res:
    data.append(["EJ MENSUAL", ej_mensual_res, ej_mensual_repo, 'true'])
else:
    data.append(["EJ MENSUAL", ej_mensual_res, ej_mensual_repo, 'false'])

ej_acumulado_res = round(ej_acumulado_res, 2)
if ej_acumulado_repo == ej_acumulado_res:
    data.append(["EJ ACUMULADO", ej_acumulado_res, ej_acumulado_repo, 'true'])    
else:
    data.append(["EJ ACUMULADO", ej_acumulado_res, ej_acumulado_repo, 'false']) 

vu_exigido_res = round(vu_exigido_res, 2) + float(enganche)
if vu_exigido_repo == vu_exigido_res:
    data.append(["VU EXIGIDO", vu_exigido_res, vu_exigido_repo, 'true']) 
else:
    data.append(["VU EXIGIDO", vu_exigido_res, vu_exigido_repo, 'false']) 

vu_porexigir_res = round(vu_porexigir_res, 2)
if vu_porexigir_repo == vu_porexigir_res:
    data.append(["VU POR EXIGIR", vu_porexigir_res, vu_porexigir_repo, 'true'])
else:
    data.append(["VU POR EXIGIR", vu_porexigir_res, vu_porexigir_repo, 'false'])


print (tabulate(data, headers=["Concepto", "Resultado", "Reporte", "Igual?"], floatfmt=".2f"))
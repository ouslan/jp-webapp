from django.shortcuts import render
import plotly.graph_objects as go
import polars as pl

def salary_and_employee(request):
    # Leer el archivo parquet usando Polars
    df = pl.read_parquet('data/processed/naics4_df.parquet')

    # Filtrar el DataFrame para incluir solo años hasta 2023
    df = df.filter(pl.col('year') <= 2023)

    # Obtener los códigos NAICS únicos (limitados a 4 dígitos) y convertir a una lista
    naics_list = df.select(pl.col('first_4_naics_code').cast(pl.Int32)).unique().to_series().to_list()

    # Obtener las selecciones del usuario
    if request.method == "POST":
        x_axis = request.POST.get('x_axis', 'year')  # Eje X (por defecto es year)
        naics_code = request.POST.get('first_4_naics_code', None)  # NAICS seleccionado
        selected_year = request.POST.get('year', None)  # Año seleccionado (solo cuando el eje X es qtr)
        selected_qtr = request.POST.get('qtr', None)  # Trimestre seleccionado (solo cuando el eje X es qtr)
    else:
        x_axis = 'year'
        naics_code = None
        selected_year = None
        selected_qtr = None

    # Filtrar por NAICS seleccionado si se seleccionó uno
    if naics_code:
        naics_code = int(naics_code)  # Convertir el NAICS seleccionado a entero
        df = df.filter(pl.col('first_4_naics_code') == naics_code)

    # Asegurar que los valores en el eje X sean únicos y calcular según la selección
    if x_axis == 'year':
        # Agrupar por año y sumar los valores de los trimestres para cada año
        df_grouped = df.group_by('year').agg(pl.col('total_wages_sum').sum())
        x_column = df_grouped['year'].sort()
        y_column = df_grouped['total_wages_sum']

    elif x_axis == 'qtr':
        # Filtrar por año y trimestre específico
        if selected_year and selected_qtr:
            df_filtered = df.filter((pl.col('year') == int(selected_year)) & (pl.col('qtr') == int(selected_qtr)))
            x_column = df_filtered['qtr'].sort()
            y_column = df_filtered['total_wages_sum']
        else:
            x_column = []
            y_column = []

    # Crear el gráfico usando Plotly
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=x_column, y=y_column, mode='lines', name=f'Total Wages (NAICS {naics_code})'))

    # Actualizar el diseño del gráfico
    fig.update_layout(
        title=f"Salario y Empleo para NAICS {naics_code}",
        xaxis_title=x_axis.capitalize(),
        yaxis_title="Total Wages",
        width=1400,
        height=750
    )

    # Convertir el gráfico a HTML
    graph_html = fig.to_html(full_html=False)

    # Pasar el gráfico, la lista de NAICS, y el valor de 'x_axis' al contexto
    context = {
        'graph': graph_html,
        'x_axis': x_axis,
        'naics_list': naics_list,  # Pasamos la lista de NAICS al contexto
        'naics_code': naics_code,
        'selected_year': selected_year,
        'selected_qtr': selected_qtr
    }

    return render(request, "salario_y_empleo.html", context)
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
from django.shortcuts import render

def web_app_indicadores(request):
    df = pd.read_csv("data/processed/master.csv")
    df = df.sort_values(by="date")

    x_axis = df["date"]
    x_title = "Time"

    y_axis_options = [
        "Movimiento de pasajeros en el aeropuerto José Aponte de la Torre (NRR)",
        "Movimiento de pasajeros en barcos cruceros (Puerto de San Juan)",
        "Movimiento de pasajeros en el aeropuerto Mercedita (PSE)",
        "Movimiento de pasajeros en el aeropuerto Rafael Hernández (BQN)",
        "Movimiento de pasajeros en el aeropuerto de Humacao (HUC)",
        "Número de barcos cruceros (Puerto de San Juan)",
        "Movimiento de pasajeros en el aeropuerto Fernando Luis Ribas Dominicci (SIG)",
        "Movimiento de pasajeros en el aeropuerto Benjamín Rivera Noriega (CPX)",
        "Movimiento de pasajeros en el aeropuerto Antonio Nery Juarbe Pol (ARE)",
        "Movimiento de pasajeros en el aeropuerto Eugenio María de Hostos (MAZ)",
        "Movimiento de pasajeros en el aeropuerto Luis Muñoz Marín (SJU)",
        "Movimiento de carga- Puerto de San Juan (Toneladas)",
        "Índice de Actividad Económica del Banco de Desarrollo Económico",
        "Información",
        "Manufactura",
        "Gobierno",
        "Otros Servicios",
        # "Minería Tala de Árboles y Construcción",
        "Gobierno Estatal",
        "Recreación y Alojamiento",
        "Gobierno Federal",
        # "Empleo No Agrícola- Todas las Industrias",
        "Servicios Profesionales y Comerciales",
        # "Comercio Transportación y Utilidades",
        "Actividades Financieras",
        "Gobierno Municipal",
        # "Servicios Educativos y de Salud",
        "Índice de Precios al Consumidor - Ropa",
        "Índice de Precios al Consumidor - Educación y Comunicación",
        "Índice de Precios al Consumidor - Todos los Grupos",
        "Índice de Precios al Consumidor - Cuidado Médico",
        "Índice de Precios al Consumidor - Alojamiento",
        "Índice de Precios al Consumidor - Transportación",
        "Índice de Precios al Consumidor - Entretenimiento",
        "Índice de Precios al Consumidor - Alimentos y Bebidas",
        "Índice de Precios al Consumidor - Otros Artículos y Servicios",
        "Balance Comercial - Miles de Dólares",
        "Total de Importaciones - Miles de Dólares",
        "Total de Exportaciones - Miles de Dólares",
        "Commercial Electric Power Consumption (Millions of Kilowatts : Hour)",
        "Consumo de Energía Eléctrica en la Agricultura (Millones de Kilovatios : Horas)",
        "Consumo de Energía Eléctrica Total (Millones de Kilovatios : Hora)",
        "Consumo de Energía Eléctrica Residencial (Millones de Kilovatios : Hora)",
        "Consumo de Energía Eléctrica Industrial (Millones de Kilovatios : Horas)",
        "Generación de Energía Eléctrica (Millones de Kilovatios : Hora)",
        "Grupo Trabajador",
        "Empleo Total",
        "Desempleo",
        "Tasa de Desempleo",
        "Diesel (centavos por litro)",
        "Diesel (centavos por litro)",
        "Diesel (centavos por litro)",
        "Quiebras en Puerto Rico - Capítulo 12",
        "Quiebras en Puerto Rico - Capítulo 13",
        "Quiebras en Puerto Rico - Capítulo 13",
        "Empleo No Agrícola- Manufactura",
        # "Empleo No Agrícola-  Minería Tala y Construcción",
        "Empleo en Gobierno",
        "Empleo en Gobierno Federal",
        "Empleo en Recreación y Alojamiento",
        "Empleo en Comercio al Por Mayor",
        "Empleo en Comercio al Detalle",
        # "Empleo en Otros Servicios",
        "Empleo en Servicios Profesionales y Comerciales",
        # "Empleo en Finanzas y Seguros",
        # "Empleo en Gobierno Municipal",
        # "Empleo en Comercio Transportación y Utilidades",
        "Empleo No Agrícola- Todas las Industrias_right",
        # "Empleo en Bienes Raíces Alquiler y Arrendamiento",
        "Empleo en Actividades Financieras",
        "Empleo en Servicios Educativos y de Salud",
        "Empleo en Información",
        "Empleo en Hospederías y Restaurantes",
        "Índice de Actividad Económica en la  Construcción",
        "Índice Coincidente de Actividad Económica de la Junta de Planificación",
        "Índice de Actividad Económica en el Turismo",
        "Índice Coincidente de Actividad Económica en la Manufactura",
        "Empleo- Manufactura de Bebidas y Tabaco (Miles de Personas)",
        "Empleo- Manufactura de Ropa (Miles de Personas)",
        "Empleo- Manufactura de Bienes Duraderos (Miles de Personas)",
        "Empleo- Manufactura de Computadoras y  Productos Electrónicos (Miles de Personas)",
        "Horas - Hombre Mensuales Trabajadas en la Manufactura (miles)",
        "Empleo- Manufactura de Minerales No - Metálicos (Miles de Personas)",
        "Empleo Manufactura de Productos de Metales (Miles de Personas)",
        # "Empleo- Manufactura de Equipos Aparatos y Accesorios Eléctrónicos (Miles de Personas)",
        "Empleo- Manufactura de Alimentos (Miles de Personas)",
        "Empleo- Manufactura de Químicos (Miles de Personas)",
        "Nómina de los Trabajadores de Producción (miles de dólares)",
        "Manufactura (miles de Personas)",
        "Empleo- Manufactura de Bienes No - Duraderos (Miles de Personas)",
        "Empleo-  Manufactura De Bienes Duraderos Misceláneos (Miles de Personas)",
        "Diesel (centavos por litro)_right",
        "Sin Plomo Regular (centavos por litro)",
        "Promedio General (centavos por litro)",
        "Sin Plomo Super (centavos por litro)",
        "De otras Fuentes - Miles de Dólares",
        "Contribución sobre Ingresos - Miles de Dólares",
        "Recaudos por concepto del Impuesto sobre Ventas y Usos (IVU) Tasa del 11.5%",
        # "Arbitrios Gran Total - Miles de Dólares",
        "Contribución sobre Ingresos Retenida a No Residentes - Miles de Dólares",
        "Contribución sobre Ingresos Retenida a Sociedades - Miles de Dólares",
        "Contribución sobre Ingresos Retenida a Individuos - Miles de Dólares",
        "Licencias - Miles de Dólares",
        "Arbitrios - Bebidas Alcohólicas",
        "Recaudos por concepto del Impuesto sobre Ventas y Usos (IVU) Tasa del 7.0%",
        "Arbitrios - Vehículos de Motor",
        "No Contributivos - Miles de Dólares",
        "Contribución sobre Ingreso Retenida a Corporaciones - Miles de Dólares",
        "INDICADORES DE INGRESOS NETOS",
        "De Fuentes Estatales - Miles de Dólares",
        "Empleo en Construcción",
        "Empleo en Manufactura",
        "Tasa de Participación",
        "Grupo Trabajador_right",
        "Empleo Total_right",
        "Empleo en Administración Pública",
        "Población Civil No-Institucional",
        # "Empleo en Finanzas Seguros y Bienes Raíces",
        "Empleo por Cuenta Propia",
        "Empleo en Comercio",
        "Empleo en Servicios",
        # "Empleo en Transportación Comunicaciones y Utilidades Públicas",
        "Desempleo_right",
        "Tasa de Desempleo_right",
        "Empleo Agricola",
        "Mueblerías - A precios corrientes",
        "Restaurantes y Lugares de Bebidas Alcohólicas - A precios corrientes",
        "Tiendas de Piezas  para Autos - A precios corrientes",
        "Tiendas de Artículos Electrónicos - A precios corrientes",
        "Total de Ventas al Detalle - A precios corrientes",
        "Ferreterías y Materiales para el Hogar - A precios corrientes",
        "Tiendas de Ropa - A precios corrientes",
        "Distribuidores de Combustible - A precios corrientes",
        "Gasolineras y Tiendas de Conveniencia - A precios corrientes",
        "Supermercados y Tiendas de Bebidas Alcohólicas - A precios corrientes",
        "Tiendas de Calzado - A precios corrientes",
        "Equipo de Patio y Jardinería - A precios corrientes",
        "Tiendas de Alimentos Especiales - A precios corrientes",
        # "Tiendas de Joyería Equipaje y Artículos de Cuero - A precios corrientes",
        "Tiendas de Cosméticos, Productos de Belleza y Perfumes - A precios corrientes",
        # "Tiendas de Deporte Instrumentos Musicales y de Entretenimiento - A precios corrientes",
        "Ventas al Detalle Vehículos de Motor Nuevos y Usados - A precios corrientes",
        "Farmacias y Droguerías - A precios corrientes",
        "Tiendas por Departamento y otros Artículos Misceláneos - A precios corrientes",
        "Total de Registros de RESIDENTES en Hoteles",
        "Tasa de Ocupación en Hoteles y Paradores",
        "Habitaciones Ocupadas en Hoteles y Paradores - Promedio Diario",
        "Habitaciones Ocupadas en Paradores - Promedio Diario",
        "Tasa de Ocupación en Paradores",
        "Total de Registros de NO RESIDENTES en Paradores",
        "Habitaciones Disponibles en Hoteles y Paradores - Promedio Diario",
        "Total de Registros en Paradores",
        "Total de Registros de RESIDENTES en Hoteles y Paradores",
        "Total de Registros de NO RESIDENTES en Hoteles",
        "Habitaciones Disponibles en Hoteles - Promedio Diario",
        "Habitaciones Ocupadas en Hoteles - Promedio Diario",
        "Total de Registros de NO RESIDENTES en Hoteles y Paradores",
        "Total de Registros en Hoteles",
        "Tasa de Ocupación en Hoteles",
        "Habitaciones Disponibles en Paradores - Promedio Diario",
        "Total de Registros en Hoteles y Paradores",
        "Total de Registros de RESIDENTES en Paradores",
        "Producción de Cemento (Miles de Sacos de 94 libras)",
        "Número de Unidades de Vivienda Vendidas en Puerto Rico - Existentes",
        "Valor Total de Permisos de Construcción Públicos - Miles de Dólares",
        "Permisos de Construcción Privados en Puerto Rico",
        "Valor de las Unidades de Vivienda Vendidas en Puerto Rico (dólares)",
        "Permisos de Construcción APP en Puerto Rico",
        "Permisos de Construcción Privados en Unidades de Vivienda en Puerto Rico",
        "Número de Unidades de Vivienda Vendidas en Puerto Rico - Nueva Construcción",
        "Número de Unidades Residenciales Reposeídas",
        "Permisos de Construcción Públicos en Puerto Rico",
        "Número Total de Permisos de Construcción Privados",
        "Número Total de Permisos de Construcción",
        "Valor de las Unidades de Vivienda Vendidas en Puerto Rico - Nueva Construcción (dólares)",
        "Total de Permisos de Construcción en Unidades de Vivienda en Puerto Rico",
        "Permisos de Construcción APP en Unidades de Vivienda en Puerto Rico",
        "Valor Total de Permisos de Construcción - Miles de Dólares",
        "Valor Total de Permisos de Construcción Privados - Miles de Dólares",
        "Valor de Permisos de Construcción Privados en Puerto Rico - Miles de Dólares",
        "Número de Unidades de Vivienda Privadas",
        "Número de Unidades de Vivienda Públicas",
        "Valor Total de Permisos de Construcción en Puerto Rico - Miles de Dólares",
        "Valor de las Unidades de Vivienda Vendidas en Puerto Rico - Existentes (dólares)",
        "Número Total de Permisos de Construcción Públicos",
        "Número de Unidades de Vivienda",
        "Ventas de Cemento (Miles de Sacos de 94 libras)",
        "Valor de Permisos de Construcción APP en Puerto Rico - Miles de Dólares",
        "Número de Unidades de Vivienda Vendidas en Puerto Rico",
        "Permisos de Construcción Públicos en Unidades de Vivienda en Puerto Rico",
        "Valor de Permisos de Construcción Públicos en Puerto Rico - Miles de Dólares",
        "Total de Permisos de Construcción en Puerto Rico"
    ]

    y_axis = df[y_axis_options[0]]
    y_title = y_axis_options[0]

    fig = px.scatter(
        x=x_axis,
        y=y_axis,
    )
    fig.add_trace(go.Scatter(
        x=x_axis,
        y=y_axis,
        mode='lines+markers',
        line=dict(color='#FF2525', width=3),
        marker=dict(size=4, color='#00CDFF'),
        hoverinfo='text',
    ))
    fig.update_layout(
        margin=dict(l=30, r=30, t=25, b=25),
        plot_bgcolor='#F7F7F7',
        hovermode='x',
        showlegend=False,
        xaxis=dict(
            title="",
            color='black',
            showgrid=True,
            showticklabels=True,
            linecolor='black',
            linewidth=2,
            ticks='outside',
            tickfont=dict(
                family='Arial',
                size=12,
                color='black'
            ),
        ),
        yaxis=dict(
            title="",
            color='black',
            showline=True,
            showgrid=True,
            showticklabels=True,
            linecolor='black',
            linewidth=2,
            ticks='outside',
            tickfont=dict(
                family='Arial',
                size=12,
                color='black'
            ),
        ),
        width=1100, 
        height=600  
    )

    fig.update_layout(
        annotations=[
            dict(
                x=0.02,
                y=1.11,
                xref='paper',
                yref='paper',
                text='Y:',
                showarrow=False,
                font=dict(
                    family='Arial',
                    size=18,
                    color='black'
                ),
                xanchor='left',
                yanchor='top'
            ),
            dict(
                x=0.77,
                y=1.11,
                xref='paper',
                yref='paper',
                text='X:',
                showarrow=False,
                font=dict(
                    family='Arial',
                    size=18,
                    color='black'
                ),
                xanchor='left',
                yanchor='top'
            )
        ],
        updatemenus=[
            dict(
                buttons=[
                    dict(
                        args=[{"y": [df[col]]}],
                        label=col,
                        method="update"
                    ) for col in y_axis_options
                ],
                direction="down",
                pad={"r": 10, "t": 10},
                showactive=True,
                x=0.05,
                xanchor="left",
                y=1.14,
                yanchor="top"
            ),
            dict(
                buttons=[
                    dict(
                        args=[{"yaxis.type": "linear"}],
                        label="Anual",
                        method="relayout"
                    ),
                    dict(
                        args=[{"yaxis.type": "log"}],
                        label="Trimestral",
                        method="relayout"
                    ),
                    dict(
                        args=[{"yaxis.range": [0, max(y_axis)]}],
                        label="Mensual",
                        method="relayout"
                    ),
                ],
                direction="down",
                pad={"r": 10, "t": 10},
                showactive=True,
                x=0.8,
                xanchor="left",
                y=1.14,
                yanchor="top"
            )
        ]
    )
    indicadores_html = fig.to_html()
    
    context = {
        "indicadores": indicadores_html,
    }
    return render(request, "indicadores.html", context)
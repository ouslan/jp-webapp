import polars as pl
import plotly.express as px
from ..jp_imports.src.jp_imports.data_process import DataProcess
from django.shortcuts import render

def web_app_imports_exports(request):
    df1 = DataProcess(saving_dir="data/", instance="jp_instetute", debug=True).process_int_jp(time="yearly", types="country")
    df2 = DataProcess(saving_dir="data/", instance="jp_instetute", debug=True).process_int_jp(time="monthly", types="country")
    df3 = DataProcess(saving_dir="data/", instance="jp_instetute", debug=True).process_int_jp(time="qrt", types="country")

    fig = px.pie(df1, values='imports', names='country')
    fig.update_traces(textposition='inside', textinfo='percent+label')
    
    if request.method == "POST":
        frequency = request.POST.get("frequency")
        second_dropdown = request.POST.get("second_dropdown")
        
        if frequency == "Yearly":
            df1 = df1.with_columns(imports=pl.col("imports")) # type: ignore
            df1 = df1.filter(pl.col("year") == int(second_dropdown))
            fig = px.pie(df1, values='imports', names='country')
        elif frequency == "Monthly":
            df2 = df2.with_columns(imports=pl.col("imports")) # type: ignore
            df2 = df2.filter(pl.col("month") == int(second_dropdown))
            fig = px.pie(df2, values='imports', names='country')
        elif frequency == "Quarterly":
            df3 = df3.with_columns(imports=pl.col("imports")) # type: ignore
            df3 = df3.filter(pl.col("qrt") == int(second_dropdown))
            fig = px.pie(df3, values='imports', names='country')
        
        fig.update_layout(
            title=f"Gráfica de Importaciones: {frequency} / {second_dropdown}",
        )
    
    fig.update_traces(textposition='inside', textinfo='percent+label')

    
    imports_and_exports = fig.to_html(full_html=False, default_height=500, default_width=700)

    context = {
        "imports_and_exports": imports_and_exports
    }

    return render(request, "imports_exports.html", context)




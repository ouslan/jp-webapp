import polars as pl
import plotly.express as px
from ..jp_imports.src.jp_imports.data_process import DataProcess
from django.shortcuts import render

def web_app_imports_exports(request):
    df1_imports = DataProcess(saving_dir="data/", instance="jp_instetute", debug=True).process_int_jp(time="yearly", types="country").collect() # type: ignore
    df2_imports = DataProcess(saving_dir="data/", instance="jp_instetute", debug=True).process_int_jp(time="monthly", types="country").collect() # type: ignore
    df3_imports = DataProcess(saving_dir="data/", instance="jp_instetute", debug=True).process_int_jp(time="qrt", types="country").collect() # type: ignore

    df1_exports = df1_imports.clone()
    df2_exports = df2_imports.clone()
    df3_exports = df3_imports.clone()
    
    # IMPORTS GRAPH 
    fig = px.pie(df1_imports, values='imports', names='country')
    fig.update_traces(textposition='inside', textinfo='percent+label')
    
    if request.method == "POST":
        frequency = request.POST.get("frequency")
        second_dropdown = request.POST.get("second_dropdown")
        
        if frequency == "Yearly":
            df1_imports = df1_imports.with_columns(imports=pl.col("imports")) # type: ignore
            df1_imports = df1_imports.filter(pl.col("year") == int(second_dropdown))
            fig = px.pie(df1_imports, values='imports', names='country')
        elif frequency == "Monthly":
            df2_imports = df2_imports.with_columns(imports=pl.col("imports")) # type: ignore
            df2_imports = df2_imports.filter(pl.col("month") == int(second_dropdown))
            fig = px.pie(df2_imports, values='imports', names='country')
        elif frequency == "Quarterly":
            df3_imports = df3_imports.with_columns(imports=pl.col("imports")) # type: ignore
            df3_imports = df3_imports.filter(pl.col("qrt") == int(second_dropdown))
            fig = px.pie(df3_imports, values='imports', names='country')
        
        if frequency == None and second_dropdown == None:
            frequency = "Yearly"
            second_dropdown = 2009
            
        fig.update_layout(
            title={
                'text': f"Gráfica de Importaciones: {frequency} / {second_dropdown}",
                'x': 0.5,
                'font': {'color': 'black'}
            },
        )
    
    fig.update_traces(textposition='inside', textinfo='percent+label')

    imports = fig.to_html(full_html=False, default_height=500, default_width=700)

    # ------------------------------------------------------------------------------------------------------------------------------------------------------------
    
    # EXPORTS GRAPH
    
    fig1 = px.pie(df1_exports, values='exports', names='country')
    fig1.update_traces(textposition='inside', textinfo='percent+label')
    
    if request.method == "POST":
        frequency_2 = request.POST.get("frequency_2")
        second_dropdown_2 = request.POST.get("second_dropdown_2")
        
        if frequency_2 == "Yearly":
            df1_exports = df1_exports.with_columns(exports=pl.col("exports")) # type: ignore
            df1_exports = df1_exports.filter(pl.col("year") == int(second_dropdown_2))
            fig1 = px.pie(df1_exports, values='exports', names='country')
        elif frequency_2 == "Monthly":
            df2_exports = df2_exports.with_columns(exports=pl.col("exports")) # type: ignore
            df2_exports = df2_exports.filter(pl.col("month") == int(second_dropdown_2))
            fig1 = px.pie(df2_exports, values='exports', names='country')
        elif frequency_2 == "Quarterly":
            df3_exports = df3_exports.with_columns(exports=pl.col("exports")) # type: ignore
            df3_exports = df3_exports.filter(pl.col("qrt") == int(second_dropdown_2))
            fig1 = px.pie(df3_exports, values='exports', names='country')
            
        if frequency_2 == None and second_dropdown_2 == None:
            frequency_2 = "Yearly"
            second_dropdown_2 = 2009
            
        fig1.update_layout(
            title={
                'text': f"Gráfica de Exportaciones: {frequency_2} / {second_dropdown_2}",
                'x': 0.5,
                'font': {'color': 'black'}
            },
        )
    
    fig1.update_traces(textposition='inside', textinfo='percent+label')

    exports = fig1.to_html(full_html=False, default_height=500, default_width=700)

    # ------------------------------------------------------------------------------------------------------------------------------------------------------------
    
    context = {
        "imports": imports,
        "exports": exports
    }

    return render(request, "imports_exports.html", context)

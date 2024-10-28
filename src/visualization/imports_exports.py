import polars as pl
import plotly.express as px
from ..jp_imports.src.jp_imports.data_process import DataTrade
from django.shortcuts import render
from dotenv import load_dotenv
import os

load_dotenv()

def web_app_imports_exports(request):
    dp = DataTrade(str(os.environ.get("DATABASE_URL")), debug=True)
    df1_imports = pl.from_pandas(dp.process_int_jp(time="yearly", types="country").to_pandas())
    df2_imports = pl.from_pandas(dp.process_int_jp(time="monthly", types="country").to_pandas())
    df3_imports = pl.from_pandas(dp.process_int_jp(time="qrt", types="country").to_pandas())

    df1_exports = df1_imports.clone()
    df2_exports = df2_imports.clone()
    df3_exports = df3_imports.clone()

    # IMPORTS GRAPH 
    fig = px.pie(df1_imports, values='imports', names='country_name')
    fig.update_traces(textposition='inside', textinfo='percent+label')

    if request.method == "POST":
        frequency = request.POST.get("frequency")
        second_dropdown = request.POST.get("second_dropdown")
        third_dropdown = request.POST.get("third_dropdown")

        if frequency == "Yearly":
            df1_imports = df1_imports.with_columns(imports=pl.col("imports")) # type: ignore
            df1_imports = df1_imports.filter(pl.col("year") == int(second_dropdown))
            fig = px.pie(df1_imports, values='imports', names='country_name')
        elif frequency == "Monthly":
            df2_imports = df2_imports.with_columns(imports=pl.col("imports")) # type: ignore
            df2_imports = df2_imports.filter((pl.col("month") == int(second_dropdown)) & (pl.col("year") == int(third_dropdown)))
            fig = px.pie(df2_imports, values='imports', names='country_name')
        elif frequency == "Quarterly":
            df3_imports = df3_imports.with_columns(imports=pl.col("imports")) # type: ignore
            df3_imports = df3_imports.filter((pl.col("qrt") == int(second_dropdown)) & (pl.col("year") == int(third_dropdown)))
            fig = px.pie(df3_imports, values='imports', names='country_name')

        if frequency is None and second_dropdown is None:
            frequency = "Yearly"
            second_dropdown = 2009

        if third_dropdown is None:
            fig.update_layout(
                title={
                    'text': f"Time: {frequency} / {second_dropdown}",
                    'x': 0.5,
                    'font': {'color': 'black'}
                },
            )
        else:
            fig.update_layout(
                title={
                    'text': f"Time: {frequency} / {second_dropdown} / {third_dropdown}",
                    'x': 0.5,
                    'font': {'color': 'black'}
                },
            )

    fig.update_traces(textposition='inside', textinfo='percent+label')

    imports = fig.to_html(full_html=False, default_height=500, default_width=700)

    # ------------------------------------------------------------------------------------------------------------------------------------------------------------

    # EXPORTS GRAPH
 
    fig1 = px.pie(df1_exports, values='exports', names='country_name')
    fig1.update_traces(textposition='inside', textinfo='percent+label')

    if request.method == "POST":
        frequency_2 = request.POST.get("frequency_2")
        second_dropdown_2 = request.POST.get("second_dropdown_2")
        third_dropdown_2 = request.POST.get("third_dropdown_2")

        if frequency_2 == "Yearly":
            df1_exports = df1_exports.with_columns(exports=pl.col("exports")) # type: ignore
            df1_exports = df1_exports.filter(pl.col("year") == int(second_dropdown_2))
            fig1 = px.pie(df1_exports, values='exports', names='country_name')
        elif frequency_2 == "Monthly":
            df2_exports = df2_exports.with_columns(exports=pl.col("exports")) # type: ignore
            df2_exports = df2_exports.filter((pl.col("month") == int(second_dropdown_2)) & (pl.col("year") == int(third_dropdown_2)))
            fig1 = px.pie(df2_exports, values='exports', names='country_name')
        elif frequency_2 == "Quarterly":
            df3_exports = df3_exports.with_columns(exports=pl.col("exports")) # type: ignore
            df3_exports = df3_exports.filter((pl.col("qrt") == int(second_dropdown_2)) & (pl.col("year") == int(third_dropdown_2)))
            fig1 = px.pie(df3_exports, values='exports', names='country_name')

        if frequency_2 is None and second_dropdown_2 is None:
            frequency_2 = "Yearly"
            second_dropdown_2 = 2009

        if third_dropdown_2 is None:
            fig1.update_layout(
                title={
                    'text': f"Time: {frequency_2} / {second_dropdown_2}",
                    'x': 0.5,
                    'font': {'color': 'black'}
                },
            )
        else:
            fig1.update_layout(
                title={
                    'text': f"Time: {frequency_2} / {second_dropdown_2} / {third_dropdown_2}",
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

import polars as pl
import plotly.express as px
from django.shortcuts import render

def web_app_imports_exports(request):
    df = pl.read_parquet("data/external/temporero.parquet")
    data = dict(
        names=df["country"].to_list() + df["year"].unique().cast(str).to_list(),
        parents=df["year"].cast(str).to_list() + [""] * df["year"].n_unique(),
        values=df["data"].to_list() + [df.filter(pl.col("year") == y).select(pl.col("data")).sum().item() for y in df["year"].unique()]
    )
    fig = px.sunburst(
        data,
        names='names',
        parents='parents',
        values='values',
    )
    imports_and_exports = fig.to_html(full_html=False, default_height=500, default_width=700)
    context = {
        "imports_and_exports": imports_and_exports
    }
    return render(request, "imports_exports.html", context)

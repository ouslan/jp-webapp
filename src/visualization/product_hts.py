import plotly.graph_objects as go
import pandas as pd
import requests
from django.shortcuts import render

API_URL = "http://localhost:8057/"

def fetch_trade_data(agg, hts_code):
    url = f"{API_URL}data/trade/jp/?&time&types=hts&agr=false&group=false&data_filter={hts_code}&agg={agg}&update=false"
    response = requests.get(url).json()
    return pd.DataFrame(response)

def sort_data(data, frequency, trade_type):
    data = data.sort_values(by='year', ascending=True)
        
    data['hts_code_first2'] = data['hts_code'].str[:2]
    data = data.sort_values(by=['year', 'hts_code_first2'], ascending=[True, True])
    data = data.groupby(['year', 'hts_code_first2']).agg({trade_type: 'sum'}).reset_index()
    
    data = data[['year', 'hts_code_first2', trade_type]]
    
    return data

def refactor_frequency(frequency):
    if frequency == 'yearly':
        return 'year'
    elif frequency == 'monthly':
        return 'month'
    elif frequency == 'quarterly':
        return 'qrt'
    elif frequency == 'fiscal':
        return 'fiscal'

def products_hts(request):
    frequency = "yearly"
    hts_code = "01"
    trade_type = "imports"
    
    data = fetch_trade_data(frequency, hts_code)
    data = sort_data(data, frequency, trade_type)
    
    x_axis = data['year']
    y_axis = data[trade_type]
    context = {
        'frequency': frequency,
        'hts_code': hts_code,
        'trade_type': trade_type
    }

    if request.method == 'POST':
        frequency = request.POST.get('frequency')
        hts_code = request.POST.get('hts_code')
        trade_type = request.POST.get('trade_type')
        
        data = fetch_trade_data(frequency, hts_code)
        new_frequency = refactor_frequency(frequency)
        data = sort_data(data, new_frequency)
        
        x_axis = data[new_frequency]
        y_axis = data[trade_type]
        
        context = {
            'frequency': frequency,
            'hts_code': hts_code,
            'trade_type': trade_type
        }
            
    # Add title to the graph
    title = f"Frequency: {frequency}    HTS Code: {hts_code}    Trade Type: {trade_type}"

    # Create the graph with the x and y axis
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=x_axis, y=y_axis, mode='lines+markers'))

    fig.update_layout(title=title)

    # Render the template with the graph
    return render(request, 'product_hts.html', {'graph': fig.to_html(), 'context': context})
    
#This file was temporarily created too try to render the Altair viz graph. To do this however, I think I
need the path to the file.


from django.http import JsonResponse
import json
import os

def get_static_chart(request):
    """ Serve the static JSON file for the graph. """
    json_path = os.path.join(os.path.dirname(__file__), "chart.json")  # Correct file path

    try:
        with open(json_path, "r") as f:
            chart_data = json.load(f)
        return JsonResponse(chart_data)
    except FileNotFoundError:
        return JsonResponse({"error": "Chart JSON file not found"}, status=404)

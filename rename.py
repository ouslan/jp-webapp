import os

for directory in os.listdir("data/indicadores_economicos"):
    for file in os.listdir(f"data/indicadores_economicos/{directory}"):
        os.rename(f"data/indicadores_economicos/{directory}/{file}", f"data/indicadores_economicos/{directory}/{file.lower().replace(" ", "_")}")


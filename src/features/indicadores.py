import pandas as pd

def indicadores_df():
    df = pd.read_csv('src/data/indicadores.csv')
    df_x = df.melt(var_name='Year')
    df_y = df.melt(id_vars=['Meses'], value_name='Value')
    return df_x, df_y

if __name__ == '__main__':
    print(indicadores_df())
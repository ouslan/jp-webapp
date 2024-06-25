from django import forms

class IP_110(forms.Form):
    company_name = forms.CharField(label='Nombre compañía / Company Name', max_length=100)
    address = forms.CharField(label='Dirección / Address', max_length=200)
    email = forms.EmailField(label='Correo electrónico / Email')
    liaison_officer = forms.CharField(label='Persona contacto / Liaison officer', max_length=100)
    ssn = forms.CharField(label='Numero de Seguro Social / Social Security Number', max_length=11)
    tel = forms.CharField(label='Tel', max_length=20)
    fax = forms.CharField(label='Fax', max_length=20)
    legal_form = forms.ChoiceField(
        label='Forma legal de organización / Legal form of organization', 
        choices=[('Corporación', 'Corporación'), ('Sociedad', 'Sociedad'), ('Cooperativa', 'Cooperativa'), ('Empresa Individual', 'Empresa Individual'), ('Empresa sin fines pecuniarios', 'Empresa sin fines pecuniarios')]
    )
    cfc = forms.ChoiceField(label='CEC', choices=[('Si', 'Si'), ('No', 'No')])
    business_type = forms.CharField(label='Clase de negocio / Type of business', max_length=200)
    business_function = forms.CharField(
        label='Describa brevemente la función principal del negocio / Explain briefly the main function of the business activity', 
        widget=forms.Textarea
    )
    branches = forms.ChoiceField(label='¿Opera sucursuales esta firma? / Do you have branch operations?', choices=[('Si', 'Si'), ('No', 'No')])
    closing_date = forms.DateField(label='Fecha de cierre de sus libros / Your accounting period closing date', widget=forms.SelectDateWidget)
    services_revenues_12 = forms.CharField(label='Ingresos por servicios - Services rendered'),
    services_revenues_13 = forms.CharField(label='Ingresos por servicios - Services rendered'),
    industries_businesses_12 = forms.CharField(label='Ingresos por industrias y negocios - From industries and businesses'),
    industries_businesses_13 = forms.CharField(label='Ingresos por industrias y negocios - From industries and businesses'),
    people_12 = forms.CharField(label='Ingresos por personas - From people'),
    people_13 = forms.CharField(label='Ingresos por personas - From people'),
    sales_12 = forms.CharField(label='2. Ventas - From sale of merchandise'),
    sales_13 = forms.CharField(label='2. Ventas - From sale of merchandise'),
    incomes_rents_12 = forms.CharField(label='3. Alquileres - From rents'),
    incomes_rents_13 = forms.CharField(label='3. Alquileres - From rents'),
    incomes_interests_12 = forms.CharField(label='4. Intereses - Interests'),
    incomes_interests_13 = forms.CharField(label='4. Intereses - Interests'),
    dividends_12 = forms.CharField(label='5. Ganancia o pérdida de capital - Capital gain or loss'),
    dividends_13 = forms.CharField(label='5. Ganancia o pérdida de capital - Capital gain or loss'),
    others_incomes_12 = forms.CharField(label='6. Otros ingresos de operación - Other operating income'),
    others_incomes_13 = forms.CharField(label='6. Otros ingresos de operación - Other operating income'),
    total_income_12 = forms.CharField(label='7. Total de ingresos - Total income'),
    total_income_13 = forms.CharField(label='7. Total de ingresos - Total income'),
    expenses_2012 = forms.CharField(label='B. Gastos - Expenses'),
    expenses_2012 = forms.CharField(label='B. Gastos - Expenses'),
    salaries_2012 = forms.CharField(label='1. Salarios, jornales, bono de Navidad y comisiones - Salaries, wages, Christmas bonus, and commissions'),
    salaries_2013 = forms.CharField(label='1. Salarios, jornales, bono de Navidad y comisiones - Salaries, wages, Christmas bonus, and commissions'),
    expenses_interests_12 = forms.CharField(label='2. Intereses - Interests'),
    expenses_interests_13 = forms.CharField(label='2. Intereses - Interests'),
    expenses_rents_12 = forms.CharField(label='3. Renta de terreno y edificio - Rent of land and building'),
    expenses_rents_13 = forms.CharField(label='3. Renta de terreno y edificio - Rent of land and building'),
    depreciation_12 = forms.CharField(label='4. Depreciación - Depreciation'),
    depreciation_13 = forms.CharField(label='4. Depreciación - Depreciation'),
    bad_debts_12 = forms.CharField(label='5. Cuentas incobrables - Bad debts'),
    bad_debts_13 = forms.CharField(label='5. Cuentas incobrables - Bad debts'),
    donations_12 = forms.CharField(label='6. Donativos - Donations'),
    donations_13 = forms.CharField(label='6. Donativos - Donations'),
    sales_tax_12 = forms.CharField(label='7. Impuesto sobre la venta y uso - sales and use tax'),
    sales_tax_13 = forms.CharField(label='7. Impuesto sobre la venta y uso - sales and use tax'),
    machinery_12 = forms.CharField(label='a. Por Compra de maquinaria y equipo - On purchases of machinery and equipment'),
    machinery_13 = forms.CharField(label='a. Por Compra de maquinaria y equipo - On purchases of machinery and equipment'),
    other_purchases_12 = forms.CharField(label='b. Por otras compras - On other purchases'),
    other_purchases_13 = forms.CharField(label='b. Por otras compras - On other purchases'),
    licenses_12 = forms.CharField(label='8. Licencias y patentes - Licenses and patents'),
    licenses_13 = forms.CharField(label='8. Licencias y patentes - Licenses and patents'),
    other_expenses_12 = forms.CharField(label='9. Otros gastos de operación - Other operating expenses'),
    other_expenses_13 = forms.CharField(label='9. Otros gastos de operación - Other operating expenses'),
    total_expenses_12 = forms.CharField(label='10. Total de gastos - Total expenses'),
    total_expenses_13 = forms.CharField(label='10. Total de gastos - Total expenses'),
    net_profit_12 = forms.CharField(label='C. Ganancia o pérdida neta ( + ó - ) - Net profit or loss ( + or - )'),
    net_profit_13 = forms.CharField(label='C. Ganancia o pérdida neta ( + ó - ) - Net profit or loss ( + or - )'),
    income_tax_12 = forms.CharField(label='1. Contribución sobre ingresos - Income tax'),
    income_tax_13 = forms.CharField(label='1. Contribución sobre ingresos - Income tax'),
    profit_after_tax_12 = forms.CharField(label='2. Ganancia después de contribución sobre ingresos - Profit after income tax'),
    profit_after_tax_13 = forms.CharField(label='2. Ganancia después de contribución sobre ingresos - Profit after income tax'),
    withheld_tax_12 = forms.CharField(label='D. Impuesto sobre ventas y uso retenido - Sales and use tax Withheld'),
    withheld_tax_13 = forms.CharField(label='D. Impuesto sobre ventas y uso retenido - Sales and use tax Withheld'),
    signature = forms.CharField(label='Nombre de persona que suministra la información - Name of person furnishing information', max_length=100)
    rank = forms.CharField(label='Rango - Title')
    

class JP_304(forms.Form):
    MONTH_CHOICES = [
        ('mes', 'mes'),
        ('enero', 'enero'),
        ('febrero', 'febrero'),
        ('marzo', 'marzo'),
        ('abril', 'abril'),
        ('mayo', 'mayo'),
        ('junio', 'junio'),
        ('julio', 'julio'),
        ('agosto', 'agosto'),
        ('septiembre', 'septiembre'),
        ('octubre', 'octubre'),
        ('noviembre', 'noviembre'),
        ('diciembre', 'diciembre'),
    ]

    start_month = forms.ChoiceField(choices=MONTH_CHOICES, required=True)
    end_month = forms.ChoiceField(choices=MONTH_CHOICES, required=True)
    year = forms.IntegerField(required=True)
    name = forms.CharField(label='Nombre / Name', max_length=100)
    direction = forms.CharField(label='Dirección / Address', max_length=200)
    liaison_officer = forms.CharField(label='Persona contacto / Liaison officer', max_length=100)
    title = forms.CharField(label='Título / Title', max_length=100)
    tel = forms.CharField(label='Tel', max_length=20)
    nombre_agencia_federal = forms.CharField(label='Nombre de la agencia federal / Name of federal agency', max_length=100)
    catalogo_federal = forms.CharField(label='Número de catálogo federal / Federal catalog number', max_length=100)
    sai_federal = forms.CharField(label='Número de SAI federal / Federal SAI number', max_length=100)
    titulo_federal = forms.CharField(label='Título federal / Federal title', max_length=100)
    aportacion_aprobada_federal = forms.CharField(label='Aportación aprobada federal / Federal approved contribution', max_length=100)
    fecha_aprobacion_federal = forms.DateField(label='Fecha de aprobación federal / Federal approval date', widget=forms.SelectDateWidget)
    aportacion_recibida_federal = forms.CharField(label='Aportación recibida federal / Federal contribution received', max_length=100)
    fecha_recibo_federal = forms.DateField(label='Fecha de recibo federal / Federal receipt date', widget=forms.SelectDateWidget)
    aportacion_gastada_federal = forms.CharField(label='Aportación gastada federal / Federal contribution spent', max_length=100)
    fecha_gasto_federal = forms.DateField(label='Fecha de gasto federal / Federal spending date', widget=forms.SelectDateWidget)
    agencia_local_table_box = forms.CharField(label='Agencia local / Local agency', max_length=100)
    catalogo_local = forms.CharField(label='Número de catálogo local / Local catalog number', max_length=100)
    programa_local = forms.CharField(label='Programa local / Local program', max_length=100)
    aportacion_federal_aprobada_local = forms.CharField(label='Aportación aprobada federal local / Local federal approved contribution', max_length=100)
    fecha_aprobacion_local = forms.DateField(label='Fecha de aprobación local / Local approval date', widget=forms.SelectDateWidget)
    aportacion_federal_recibida_local = forms.CharField(label='Aportación recibida federal local / Local federal contribution received', max_length=100)
    fecha_recibo_local = forms.DateField(label='Fecha de recibo federal local / Local federal receipt date', widget=forms.SelectDateWidget)
    aportacion_federal_gastada_local = forms.CharField(label='Aportación gastada federal local / Local federal contribution spent', max_length=100)
    fecha_gasto_local = forms.DateField(label='Fecha de gasto federal local / Local federal spending date', widget=forms.SelectDateWidget)
    numero_cuenta_local = forms.CharField(label='Número de cuenta local / Local account number', max_length=100)


class JP_541(forms.Form):
    COMPANT_TYPE_CHOICES = [
        ('Corporación', 'Corporación'),
        ('Administración', 'Administración'),
    ]
    
    #TABLE 1
    form_1 = forms.CharField(label='Encuesta :', max_length=100)
    fiscal_year_1 = forms.CharField(label='Año Fiscal :', max_length=100)
    company_name_1 = forms.CharField(label='Nombre de la Empresa:', max_length=100)
    liaison_officer_1 = forms.CharField(label='Persona de Contacto:', max_length=100)
    tel_1 = forms.CharField(label='Teléfono::', max_length=100)
    project_1 = forms.CharField(label='Proyecto por::', max_length=100)
    branches_1 = forms.CharField(choice=COMPANT_TYPE_CHOICES, max_length=100)
    
    project_name_1_1 = forms.CharField(label='', max_length=100)
    city_1_1 = forms.CharField(label='', max_length=100)
    total_number_project_1_1 = forms.CharField(label='', max_length=100)
    total_cost_1_1 = forms.CharField(label='', max_length=100)
    start_date_1_1 = forms.DateField(label='', widget=forms.SelectDateWidget)
    end_date_1_1 = forms.DateField(label='', widget=forms.SelectDateWidget)
    value_first_trimester_1_1 = forms.CharField(label='', max_length=100)
    value_second_trimester_1_1 = forms.CharField(label='', max_length=100)
    value_third_trimester_1_1 = forms.CharField(label='', max_length=100)
    value_fourth_trimester_1_1 = forms.CharField(label='', max_length=100)
    
    project_name_1_2 = forms.CharField(label='', max_length=100)
    city_1_2 = forms.CharField(label='', max_length=100)
    total_number_project_1_2 = forms.CharField(label='', max_length=100)
    total_cost_1_2 = forms.CharField(label='', max_length=100)
    start_date_1_2 = forms.DateField(label='', widget=forms.SelectDateWidget)
    end_date_1_2 = forms.DateField(label='', widget=forms.SelectDateWidget)
    value_first_trimester_1_2 = forms.CharField(label='', max_length=100)
    value_second_trimester_1_2 = forms.CharField(label='', max_length=100)
    value_third_trimester_1_2 = forms.CharField(label='', max_length=100)
    value_fourth_trimester_1_2 = forms.CharField(label='', max_length=100)
    
    project_name_1_3 = forms.CharField(label='', max_length=100)
    city_1_3 = forms.CharField(label='', max_length=100)
    total_number_project_1_3 = forms.CharField(label='', max_length=100)
    total_cost_1_3 = forms.CharField(label='', max_length=100)
    start_date_1_3 = forms.DateField(label='', widget=forms.SelectDateWidget)
    end_date_1_3 =  forms.DateField(label='', widget=forms.SelectDateWidget)
    value_first_trimester_1_3 = forms.CharField(label='', max_length=100)
    value_second_trimester_1_3 = forms.CharField(label='', max_length=100)
    value_third_trimester_1_3 = forms.CharField(label='', max_length=100)
    value_fourth_trimester_1_3 = forms.CharField(label='', max_length=100)
    
    project_name_1_4 = forms.CharField(label='', max_length=100)
    city_1_4 = forms.CharField(label='', max_length=100)
    total_number_project_1_4 = forms.CharField(label='', max_length=100)
    total_cost_1_4 = forms.CharField(label='', max_length=100)
    start_date_1_4 = forms.DateField(label='', widget=forms.SelectDateWidget)
    end_date_1_4 = forms.DateField(label='', widget=forms.SelectDateWidget)
    value_first_trimester_1_4 = forms.CharField(label='', max_length=100)
    value_second_trimester_1_4 = forms.CharField(label='', max_length=100)
    value_third_trimester_1_4 = forms.CharField(label='', max_length=100)
    value_fourth_trimester_1_4 = forms.CharField(label='', max_length=100)
    
    project_name_1_5 = forms.CharField(label='', max_length=100)
    city_1_5 = forms.CharField(label='', max_length=100)
    total_number_project_1_5 = forms.CharField(label='', max_length=100)
    total_cost_1_5 = forms.CharField(label='', max_length=100)
    start_date_1_5 = forms.DateField(label='', widget=forms.SelectDateWidget)
    end_date_1_5 = forms.DateField(label='', widget=forms.SelectDateWidget)
    value_first_trimester_1_5 = forms.CharField(label='', max_length=100)
    value_second_trimester_1_5 = forms.CharField(label='', max_length=100)
    value_third_trimester_1_5 =  forms.CharField(label='', max_length=100)
    value_fourth_trimester_1_5 = forms.CharField(label='', max_length=100)
    
    
    #TABLE 2
    form_2 = forms.CharField(label='Encuesta :', max_length=100)
    fiscal_year_2 = forms.CharField(label='Año Fiscal :', max_length=100)
    company_name_2 = forms.CharField(label='Nombre de la Empresa:', max_length=100)
    liaison_officer_2 = forms.CharField(label='Persona de Contacto:', max_length=100)
    tel_2 = forms.CharField(label='Teléfono::', max_length=100)
    project_2 = forms.CharField(label='Proyecto por::', max_length=100)
    branches_2 = forms.CharField(choice=COMPANT_TYPE_CHOICES, max_length=100)
    
    project_name_2_1 = forms.CharField(label='', max_length=100)
    city_2_1 = forms.CharField(label='', max_length=100)
    total_number_project_2_1 = forms.CharField(label='', max_length=100)
    total_cost_2_1 = forms.CharField(label='', max_length=100)
    start_date_2_1 = forms.DateField(label='', widget=forms.SelectDateWidget)
    end_date_2_1 = forms.DateField(label='', widget=forms.SelectDateWidget)
    value_first_trimester_2_1 = forms.CharField(label='', max_length=100)
    value_second_trimester_2_1 = forms.CharField(label='', max_length=100)
    value_third_trimester_2_1 = forms.CharField(label='', max_length=100)
    value_fourth_trimester_2_1 = forms.CharField(label='', max_length=100)
    
    project_name_2_2 = forms.CharField(label='', max_length=100)
    city_2_2 = forms.CharField(label='', max_length=100)
    total_number_project_2_2 = forms.CharField(label='', max_length=100)
    total_cost_2_2 = forms.CharField(label='', max_length=100)
    start_date_2_2 = forms.DateField(label='', widget=forms.SelectDateWidget)
    end_date_2_2 = forms.DateField(label='', widget=forms.SelectDateWidget)
    value_first_trimester_2_2 = forms.CharField(label='', max_length=100)
    value_second_trimester_2_2 = forms.CharField(label='', max_length=100)
    value_third_trimester_2_2 = forms.CharField(label='', max_length=100)
    value_fourth_trimester_2_2 = forms.CharField(label='', max_length=100)
    
    project_name_2_3 = forms.CharField(label='', max_length=100)
    city_2_3 = forms.CharField(label='', max_length=100)
    total_number_project_2_3 = forms.CharField(label='', max_length=100)
    total_cost_2_3 = forms.CharField(label='', max_length=100)
    start_date_2_3 = forms.DateField(label='', widget=forms.SelectDateWidget)
    end_date_2_3 =  forms.DateField(label='', widget=forms.SelectDateWidget)
    value_first_trimester_2_3 = forms.CharField(label='', max_length=100)
    value_second_trimester_2_3 = forms.CharField(label='', max_length=100)
    value_third_trimester_2_3 = forms.CharField(label='', max_length=100)
    value_fourth_trimester_2_3 = forms.CharField(label='', max_length=100)
    
    project_name_2_4 = forms.CharField(label='', max_length=100)
    city_2_4 = forms.CharField(label='', max_length=100)
    total_number_project_2_4 = forms.CharField(label='', max_length=100)
    total_cost_2_4 = forms.CharField(label='', max_length=100)
    start_date_2_4 = forms.DateField(label='', widget=forms.SelectDateWidget)
    end_date_2_4 = forms.DateField(label='', widget=forms.SelectDateWidget)
    value_first_trimester_2_4 = forms.CharField(label='', max_length=100)
    value_second_trimester_2_4 = forms.CharField(label='', max_length=100)
    value_third_trimester_2_4 = forms.CharField(label='', max_length=100)
    value_fourth_trimester_2_4 = forms.CharField(label='', max_length=100)
    
    project_name_2_5 = forms.CharField(label='', max_length=100)
    city_2_5 = forms.CharField(label='', max_length=100)
    total_number_project_2_5 = forms.CharField(label='', max_length=100)
    total_cost_2_5 = forms.CharField(label='', max_length=100)
    start_date_2_5 = forms.DateField(label='', widget=forms.SelectDateWidget)
    end_date_2_5 = forms.DateField(label='', widget=forms.SelectDateWidget)
    value_first_trimester_2_5 = forms.CharField(label='', max_length=100)
    value_second_trimester_2_5 = forms.CharField(label='', max_length=100)
    value_third_trimester_2_5 =  forms.CharField(label='', max_length=100)
    value_fourth_trimester_2_5 = forms.CharField(label='', max_length=100)
    
    
    #TABLE 3
    form_3 = forms.CharField(label='Encuesta :', max_length=100)
    fiscal_year_3 = forms.CharField(label='Año Fiscal :', max_length=100)
    company_name_3 = forms.CharField(label='Nombre de la Empresa:', max_length=100)
    liaison_officer_3 = forms.CharField(label='Persona de Contacto:', max_length=100)
    tel_3 = forms.CharField(label='Teléfono::', max_length=100)
    project_3 = forms.CharField(label='Proyecto por::', max_length=100)
    branches_3 = forms.CharField(choice=COMPANT_TYPE_CHOICES, max_length=100)
    
    project_name_3_1 = forms.CharField(label='', max_length=100)
    city_3_1 = forms.CharField(label='', max_length=100)
    total_number_project_3_1 = forms.CharField(label='', max_length=100)
    total_cost_3_1 = forms.CharField(label='', max_length=100)
    start_date_3_1 = forms.DateField(label='', widget=forms.SelectDateWidget)
    end_date_3_1 = forms.DateField(label='', widget=forms.SelectDateWidget)
    value_first_trimester_3_1 = forms.CharField(label='', max_length=100)
    value_second_trimester_3_1 = forms.CharField(label='', max_length=100)
    value_third_trimester_3_1 = forms.CharField(label='', max_length=100)
    value_fourth_trimester_3_1 = forms.CharField(label='', max_length=100)
    
    project_name_3_2 = forms.CharField(label='', max_length=100)
    city_3_2 = forms.CharField(label='', max_length=100)
    total_number_project_3_2 = forms.CharField(label='', max_length=100)
    total_cost_3_2 = forms.CharField(label='', max_length=100)
    start_date_3_2 = forms.DateField(label='', widget=forms.SelectDateWidget)
    end_date_3_2 = forms.DateField(label='', widget=forms.SelectDateWidget)
    value_first_trimester_3_2 = forms.CharField(label='', max_length=100)
    value_second_trimester_3_2 = forms.CharField(label='', max_length=100)
    value_third_trimester_3_2 = forms.CharField(label='', max_length=100)
    value_fourth_trimester_3_2 = forms.CharField(label='', max_length=100)
    
    project_name_3_3 = forms.CharField(label='', max_length=100)
    city_3_3 = forms.CharField(label='', max_length=100)
    total_number_project_3_3 = forms.CharField(label='', max_length=100)
    total_cost_3_3 = forms.CharField(label='', max_length=100)
    start_date_3_3 = forms.DateField(label='', widget=forms.SelectDateWidget)
    end_date_3_3 =  forms.DateField(label='', widget=forms.SelectDateWidget)
    value_first_trimester_3_3 = forms.CharField(label='', max_length=100)
    value_second_trimester_3_3 = forms.CharField(label='', max_length=100)
    value_third_trimester_3_3 = forms.CharField(label='', max_length=100)
    value_fourth_trimester_3_3 = forms.CharField(label='', max_length=100)
    
    project_name_3_4 = forms.CharField(label='', max_length=100)
    city_3_4 = forms.CharField(label='', max_length=100)
    total_number_project_3_4 = forms.CharField(label='', max_length=100)
    total_cost_3_4 = forms.CharField(label='', max_length=100)
    start_date_3_4 = forms.DateField(label='', widget=forms.SelectDateWidget)
    end_date_3_4 = forms.DateField(label='', widget=forms.SelectDateWidget)
    value_first_trimester_3_4 = forms.CharField(label='', max_length=100)
    value_second_trimester_3_4 = forms.CharField(label='', max_length=100)
    value_third_trimester_3_4 = forms.CharField(label='', max_length=100)
    value_fourth_trimester_3_4 = forms.CharField(label='', max_length=100)
    
    project_name_3_5 = forms.CharField(label='', max_length=100)
    city_3_5 = forms.CharField(label='', max_length=100)
    total_number_project_3_5 = forms.CharField(label='', max_length=100)
    total_cost_3_5 = forms.CharField(label='', max_length=100)
    start_date_3_5 = forms.DateField(label='', widget=forms.SelectDateWidget)
    end_date_3_5 = forms.DateField(label='', widget=forms.SelectDateWidget)
    value_first_trimester_3_5 = forms.CharField(label='', max_length=100)
    value_second_trimester_3_5 = forms.CharField(label='', max_length=100)
    value_third_trimester_3_5 =  forms.CharField(label='', max_length=100)
    value_fourth_trimester_3_5 = forms.CharField(label='', max_length=100)
    
    
    #TABLE 4
    form_4 = forms.CharField(label='Encuesta :', max_length=100)
    fiscal_year_4 = forms.CharField(label='Año Fiscal :', max_length=100)
    company_name_4 = forms.CharField(label='Nombre de la Empresa:', max_length=100)
    liaison_officer_4 = forms.CharField(label='Persona de Contacto:', max_length=100)
    tel_4 = forms.CharField(label='Teléfono::', max_length=100)
    project_4 = forms.CharField(label='Proyecto por::', max_length=100)
    branches_4 = forms.CharField(choice=COMPANT_TYPE_CHOICES, max_length=100)
    
    project_name_4_1 = forms.CharField(label='', max_length=100)
    city_4_1 = forms.CharField(label='', max_length=100)
    total_number_project_4_1 = forms.CharField(label='', max_length=100)
    total_cost_4_1 = forms.CharField(label='', max_length=100)
    start_date_4_1 = forms.DateField(label='', widget=forms.SelectDateWidget)
    end_date_4_1 = forms.DateField(label='', widget=forms.SelectDateWidget)
    value_first_trimester_4_1 = forms.CharField(label='', max_length=100)
    value_second_trimester_4_1 = forms.CharField(label='', max_length=100)
    value_third_trimester_4_1 = forms.CharField(label='', max_length=100)
    value_fourth_trimester_4_1 = forms.CharField(label='', max_length=100)
    
    project_name_4_2 = forms.CharField(label='', max_length=100)
    city_4_2 = forms.CharField(label='', max_length=100)
    total_number_project_4_2 = forms.CharField(label='', max_length=100)
    total_cost_4_2 = forms.CharField(label='', max_length=100)
    start_date_4_2 = forms.DateField(label='', widget=forms.SelectDateWidget)
    end_date_4_2 = forms.DateField(label='', widget=forms.SelectDateWidget)
    value_first_trimester_4_2 = forms.CharField(label='', max_length=100)
    value_second_trimester_4_2 = forms.CharField(label='', max_length=100)
    value_third_trimester_4_2 = forms.CharField(label='', max_length=100)
    value_fourth_trimester_4_2 = forms.CharField(label='', max_length=100)
    
    project_name_4_3 = forms.CharField(label='', max_length=100)
    city_4_3 = forms.CharField(label='', max_length=100)
    total_number_project_4_3 = forms.CharField(label='', max_length=100)
    total_cost_4_3 = forms.CharField(label='', max_length=100)
    start_date_4_3 = forms.DateField(label='', widget=forms.SelectDateWidget)
    end_date_4_3 =  forms.DateField(label='', widget=forms.SelectDateWidget)
    value_first_trimester_4_3 = forms.CharField(label='', max_length=100)
    value_second_trimester_4_3 = forms.CharField(label='', max_length=100)
    value_third_trimester_4_3 = forms.CharField(label='', max_length=100)
    value_fourth_trimester_4_3 = forms.CharField(label='', max_length=100)
    
    project_name_4_4 = forms.CharField(label='', max_length=100)
    city_4_4 = forms.CharField(label='', max_length=100)
    total_number_project_4_4 = forms.CharField(label='', max_length=100)
    total_cost_4_4 = forms.CharField(label='', max_length=100)
    start_date_4_4 = forms.DateField(label='', widget=forms.SelectDateWidget)
    end_date_4_4 = forms.DateField(label='', widget=forms.SelectDateWidget)
    value_first_trimester_4_4 = forms.CharField(label='', max_length=100)
    value_second_trimester_4_4 = forms.CharField(label='', max_length=100)
    value_third_trimester_4_4 = forms.CharField(label='', max_length=100)
    value_fourth_trimester_4_4 = forms.CharField(label='', max_length=100)
    
    project_name_4_5 = forms.CharField(label='', max_length=100)
    city_4_5 = forms.CharField(label='', max_length=100)
    total_number_project_4_5 = forms.CharField(label='', max_length=100)
    total_cost_4_5 = forms.CharField(label='', max_length=100)
    start_date_4_5 = forms.DateField(label='', widget=forms.SelectDateWidget)
    end_date_4_5 = forms.DateField(label='', widget=forms.SelectDateWidget)
    value_first_trimester_4_5 = forms.CharField(label='', max_length=100)
    value_second_trimester_4_5 = forms.CharField(label='', max_length=100)
    value_third_trimester_4_5 =  forms.CharField(label='', max_length=100)
    value_fourth_trimester_4_5 = forms.CharField(label='', max_length=100)
    

class JP_361(forms.Form):
    income_expenses_year_1 = forms.CharField(label='Year', max_length=4)
    income_expenses_year_2 = forms.CharField(label='Year', max_length=4)
    income_life_1 = forms.CharField(label='a) Life', max_length=100)
    income_life_2 = forms.CharField(label='a) Life', max_length=100)
    income_disability_1 = forms.CharField(label='b) Disability', max_length=100)
    income_disability_2 = forms.CharField(label='b) Disability', max_length=100)
    income_auto_1 = forms.CharField(label='c) Auto', max_length=100)
    income_auto_2 = forms.CharField(label='c) Auto', max_length=100)
    income_other_1 = forms.CharField(label='d) Other', max_length=100)
    income_other_2 = forms.CharField(label='d) Other', max_length=100)
    income_interest_1 = forms.CharField(label='2. Interest', max_length=100)
    income_interest_2 = forms.CharField(label='2. Interest', max_length=100)
    income_rent_1 = forms.CharField(label='3. Rent of land and building', max_length=100)
    income_rent_2 = forms.CharField(label='3. Rent of land and building', max_length=100)
    income_other_2_1 = forms.CharField(label='4. Other', max_length=100)
    income_other_2_2 = forms.CharField(label='4. Other', max_length=100)
    total_income_1 = forms.CharField(label='Total Income', max_length=100)
    total_income_2 = forms.CharField(label='Total Income', max_length=100)
    expenses_life_1 = forms.CharField(label='a) Life', max_length=100)
    expenses_life_2 = forms.CharField(label='a) Life', max_length=100)
    expenses_disability_1 = forms.CharField(label='b) Disability', max_length=100)
    expenses_disability_2 = forms.CharField(label='b) Disability', max_length=100)
    expenses_auto_1 = forms.CharField(label='c) Auto', max_length=100)
    expenses_auto_2 = forms.CharField(label='c) Auto', max_length=100)
    expenses_other_1 = forms.CharField(label='d) Other', max_length=100)
    expenses_other_2 = forms.CharField(label='d) Other', max_length=100)
    expenses_salaries_1 = forms.CharField(label='2. Salaries', max_length=100)
    expenses_salaries_2 = forms.CharField(label='2. Salaries', max_length=100)
    expenses_interes_1 = forms.CharField(label='3. Interest', max_length=100)
    expenses_interes_2 = forms.CharField(label='3. Interest', max_length=100)
    expenses_rent_1 = forms.CharField(label='4. Rent of land and building', max_length=100)
    expenses_rent_2 = forms.CharField(label='4. Rent of land and building', max_length=100)
    expenses_depreciation_1 = forms.CharField(label='5. Depreciation', max_length=100)
    expenses_depreciation_2 = forms.CharField(label='5. Depreciation', max_length=100)
    expenses_donations_1 = forms.CharField(label='6. Donations', max_length=100)
    expenses_donations_2 = forms.CharField(label='6. Donations', max_length=100)
    expenses_commissions_1 = forms.CharField(label='7. Commissions', max_length=100)
    expenses_commissions_2 = forms.CharField(label='7. Commissions', max_length=100)
    expenses_employees_1 = forms.CharField(label='a) To employees', max_length=100)
    expenses_employees_2 = forms.CharField(label='a) To employees', max_length=100)
    expenses_brokers_1 = forms.CharField(label='b) To local brokers', max_length=100)
    expenses_brokers_2 = forms.CharField(label='b) To local brokers', max_length=100)
    expenses_other_operational_1 = forms.CharField(label='8. Other operational expenses', max_length=100)
    expenses_other_operational_2 = forms.CharField(label='8. Other operational expenses', max_length=100)
    total_expenses_1 = forms.CharField(label='Total Expenses', max_length=100)
    total_expenses_2 = forms.CharField(label='Total Expenses', max_length=100)
    net_profit_1 = forms.CharField(label='Net profit or loss', max_length=100)
    net_profit_2 = forms.CharField(label='Net profit or loss', max_length=100)
    balance_year_1 = forms.CharField(label='As of 6/30/', max_length=4)
    balance_year_2 = forms.CharField(label='Estimated as of 6/30/', max_length=4)
    guaranteed_1 = forms.CharField(label='1. F.H.A. guaranteed', max_length=100)
    guaranteed_2 = forms.CharField(label='1. F.H.A. guaranteed', max_length=100)
    guaranteed_3 = forms.CharField(label='1. F.H.A. guaranteed', max_length=100)
    guaranteed_4 = forms.CharField(label='1. F.H.A. guaranteed', max_length=100)
    veterans_1 = forms.CharField(label='2. Veterans Administration', max_length=100)
    veterans_2 = forms.CharField(label='2. Veterans Administration', max_length=100)
    veterans_3 = forms.CharField(label='2. Veterans Administration', max_length=100)
    veterans_4 = forms.CharField(label='2. Veterans Administration', max_length=100)
    conventional_1 = forms.CharField(label='3. Conventional', max_length=100)
    conventional_2 = forms.CharField(label='3. Conventional', max_length=100)
    conventional_3 = forms.CharField(label='3. Conventional', max_length=100)
    conventional_4 = forms.CharField(label='3. Conventional', max_length=100)
    other_1 = forms.CharField(label='4. Other', max_length=100)
    other_2 = forms.CharField(label='4. Other', max_length=100)
    other_3 = forms.CharField(label='4. Other', max_length=100)
    other_4 = forms.CharField(label='4. Other', max_length=100)
    policy_loans_1 = forms.CharField(label='1. Policy loans', max_length=100)
    policy_loans_2 = forms.CharField(label='1. Policy loans', max_length=100)
    policy_loans_3 = forms.CharField(label='1. Policy loans', max_length=100)
    policy_loans_4 = forms.CharField(label='1. Policy loans', max_length=100)
    other_specify_1 = forms.CharField(label='5. Other (Specify)', max_length=100)
    other_specify_2 = forms.CharField(label='5. Other (Specify)', max_length=100)
    other_specify_3 = forms.CharField(label='5. Other (Specify)', max_length=100)
    other_specify_4 = forms.CharField(label='5. Other (Specify)', max_length=100)
    policy_reserves_1 = forms.CharField(label='1. Policy reserves of Puerto Rican residents', max_length=100)
    policy_reserves_2 = forms.CharField(label='1. Policy reserves of Puerto Rican residents', max_length=100)
    accrued_dividends_1 = forms.CharField(label='2. Accrued dividends on life insurance policies held by Puerto Rican residents', max_length=100)
    accrued_dividends_2 = forms.CharField(label='2. Accrued dividends on life insurance policies held by Puerto Rican residents', max_length=100)
    signature = forms.CharField(label='Name of person filling the questionnaire', max_length=100)
    date = forms.CharField(label='Date', max_length=100)
    phone = forms.CharField(label='Phone Number', max_length=100)
    position = forms.CharField(label='Position', max_length=100)
    
class JP_363(forms.Form):
    bonds_year_left = forms.CharField(label='Año', max_length=4)
    bonds_year_right = forms.CharField(label='Año', max_length=4)
    notes_year_left = forms.CharField(label='Año', max_length=4)
    notes_year_right = forms.CharField(label='Año', max_length=4)

    town_bonds_left = forms.CharField(label='Bonos Municipales', max_length=100)
    town_bonds_right = forms.CharField(label='Bonos Municipales', max_length=100)
    town_notes_left = forms.CharField(label='Notas Municipales', max_length=100)
    town_notes_right = forms.CharField(label='Notas Municipales', max_length=100)
    town_name_service = forms.CharField(label='Nombre del Servicio', max_length=100)

    PC_bonds_left = forms.CharField(label='Bonos Corporativos', max_length=100)
    PC_bonds_right = forms.CharField(label='Bonos Corporativos', max_length=100)
    PC_notes_left  = forms.CharField(label='Notas Corporativas', max_length=100)
    PC_notes_right = forms.CharField(label='Notas Corporativas', max_length=100)
    PC_name_service = forms.CharField(label='Nombre del Servicio', max_length=100)

    EPA_bonds_left = forms.CharField(label='Bonos de la EPA', max_length=100)
    EPA_bonds_right = forms.CharField(label='Bonos de la EPA', max_length=100)
    EPA_notes_left = forms.CharField(label='Notas de la EPA', max_length=100)
    EPA_notes_right = forms.CharField(label='Notas de la EPA', max_length=100)
    EPA_name_service = forms.CharField(label='Nombre del Servicio', max_length=100)

    HA_bonds_left = forms.CharField(label='Bonos de la HA', max_length=100)
    HA_bonds_right = forms.CharField(label='Bonos de la HA', max_length=100)
    HA_notes_left = forms.CharField(label='Notas de la HA', max_length=100)
    HA_notes_right = forms.CharField(label='Notas de la HA', max_length=100)
    HA_name_service = forms.CharField(label='Nombre del Servicio', max_length=100)

    ASA_bonds_left = forms.CharField(label='Bonos de la ASA', max_length=100)
    ASA_bonds_right = forms.CharField(label='Bonos de la ASA', max_length=100)
    ASA_notes_left = forms.CharField(label='Notas de la ASA', max_length=100)
    ASA_notes_right = forms.CharField(label='Notas de la ASA', max_length=100)
    ASA_name_service = forms.CharField(label='Nombre del Servicio', max_length=100)

    PBA_bonds_left = forms.CharField(label='Bonos de la PBA', max_length=100)
    PBA_bonds_right = forms.CharField(label='Bonos de la PBA', max_length=100)
    PBA_notes_left = forms.CharField(label='Notas de la PBA', max_length=100)
    PBA_notes_right = forms.CharField(label='Notas de la PBA', max_length=100)
    PBA_name_service = forms.CharField(label='Nombre del Servicio', max_length=100)

    PA_bonds_left = forms.CharField(label='Bonos de la PA', max_length=100)
    PA_bonds_right = forms.CharField(label='Bonos de la PA', max_length=100)
    PA_notes_left = forms.CharField(label='Notas de la PA', max_length=100)
    PA_notes_right = forms.CharField(label='Notas de la PA', max_length=100)
    PA_name_service = forms.CharField(label='Nombre del Servicio', max_length=100)

    IDC_bonds_left = forms.CharField(label='Bonos de la IDC', max_length=100)
    IDC_bonds_right = forms.CharField(label='Bonos de la IDC', max_length=100)
    IDC_notes_left = forms.CharField(label='Notas de la IDC', max_length=100)
    IDC_notes_right = forms.CharField(label='Notas de la IDC', max_length=100)
    IDC_name_service = forms.CharField(label='Nombre del Servicio', max_length=100)

    GDB_bonds_left = forms.CharField(label='Bonos del GDB', max_length=100)
    GDB_bonds_right = forms.CharField(label='Bonos del GDB', max_length=100)
    GDB_notes_left = forms.CharField(label='Notas del GDB', max_length=100)
    GDB_notes_right = forms.CharField(label='Notas del GDB', max_length=100)
    GDB_name_service = forms.CharField(label='Nombre del Servicio', max_length=100)

    HFC_bonds_left = forms.CharField(label='Bonos de la HFC', max_length=100)
    HFC_bonds_right = forms.CharField(label='Bonos de la HFC', max_length=100)
    HFC_notes_left = forms.CharField(label='Notas de la HFC', max_length=100)
    HFC_notes_right = forms.CharField(label='Notas de la HFC', max_length=100)
    HFC_name_service = forms.CharField(label='Nombre del Servicio', max_length=100)

    other = forms.CharField(label='Otros', max_length=100)
    other_bonds_left = forms.CharField(label='Otros Bonos', max_length=100)
    other_bonds_right = forms.CharField(label='Otros Bonos', max_length=100)
    other_notes_left = forms.CharField(label='Otras Notas', max_length=100)
    other_notes_right = forms.CharField(label='Otras Notas', max_length=100)
    other_name_service = forms.CharField(label='Nombre del Servicio', max_length=100)

    other_PC_1 = forms.CharField(label='Otros Corporativos', max_length=100)
    other_PC_1_bonds_left = forms.CharField(label='Bonos', max_length=100)
    other_PC_1_bonds_right = forms.CharField(label='Bonos', max_length=100)
    other_PC_1_notes_left = forms.CharField(label='Notas', max_length=100)
    other_PC_1_notes_right = forms.CharField(label='Notas', max_length=100)
    other_PC_1_name_service = forms.CharField(label='Nombre del Servicio', max_length=100)

    other_PC_2 = forms.CharField(label='Otros Corporativos', max_length=100)
    other_PC_2_bonds_left = forms.CharField(label='Bonos', max_length=100)
    other_PC_2_bonds_right = forms.CharField(label='Bonos', max_length=100)
    other_PC_2_notes_left = forms.CharField(label='Notas', max_length=100)
    other_PC_2_notes_right = forms.CharField(label='Notas', max_length=100)
    other_PC_2_name_service = forms.CharField(label='Nombre del Servicio', max_length=100)

    GNMA_bonds_left = forms.CharField(label='Bonos de la GNMA', max_length=100)
    GNMA_bonds_right = forms.CharField(label='Bonos de la GNMA', max_length=100)
    GNMA_notes_left = forms.CharField(label='Notas de la GNMA', max_length=100)
    GNMA_notes_right = forms.CharField(label='Notas de la GNMA', max_length=100)
    GNMA_name_service = forms.CharField(label='Nombre del Servicio', max_length=100)

    other5 = forms.CharField(label='Otros', max_length=100)
    other5_bonds_left = forms.CharField(label='Otros', max_length=100)
    other5_bonds_right = forms.CharField(label='Otros', max_length=100)
    other5_notes_left = forms.CharField(label='Otros', max_length=100)
    other5_notes_right = forms.CharField(label='Otros', max_length=100)
    other5_name_service = forms.CharField(label='Nombre del Servicio', max_length=100)
    
    signature = forms.CharField(label='Name of person filling the questionnaire', max_length=100)
    position = forms.CharField(label='Position', max_length=100)
    date = forms.CharField(label='Date', max_length=100)
    phone = forms.CharField(label='Phone Number', max_length=100)
    
class JP_560(forms.Forms):
    ssn = forms.CharField(label='Social Security Number', max_length=100)
    tel = forms.CharField(label='Telephone Number', max_length=100)
    fax = forms.CharField(label='Fax Number', max_length=100)
    sales_1 = forms.CharField(label='Sales', max_length=100)
    sales_2 = forms.CharField(label='Sales', max_length=100)
    disability_1 = forms.CharField(label='Disability', max_length=100)
    disability_2 = forms.CharField(label='Disability', max_length=100)
    life_1 = forms.CharField(label='Life', max_length=100)
    life_2 = forms.CharField(label='Life', max_length=100)
    interest_1 = forms.CharField(label='Interest', max_length=100)
    interest_2 = forms.CharField(label='Interest', max_length=100)
    other_income_1 = forms.CharField(label='Other Income', max_length=100)
    other_income_2 = forms.CharField(label='Other Income', max_length=100)
    total_income_1 = forms.CharField(label='Total Income', max_length=100)
    total_income_2 = forms.CharField(label='Total Income', max_length=100)
    interest_paid_1 = forms.CharField(label='Interest Paid', max_length=100)
    interest_paid_2 = forms.CharField(label='Interest Paid', max_length=100)
    disability_paid_1 = forms.CharField(label='Disability Paid', max_length=100)
    disability_paid_2 = forms.CharField(label='Disability Paid', max_length=100)
    life_paid_1 = forms.CharField(label='Life Paid', max_length=100)
    life_paid_2 = forms.CharField(label='Life Paid', max_length=100)
    other_expenditures_1 = forms.CharField(label='Other Expenditures', max_length=100)
    other_expenditures_2 = forms.CharField(label='Other Expenditures', max_length=100)
    total_expenditures_1 = forms.CharField(label='Total Expenditures', max_length=100)
    total_expenditures_2 = forms.CharField(label='Total Expenditures', max_length=100)
    net_profit_1 = forms.CharField(label='Net Profit', max_length=100)
    net_profit_2 = forms.CharField(label='Net Profit', max_length=100)
    initial_inventory_1 = forms.CharField(label='Initial Inventory', max_length=100)
    initial_inventory_2 = forms.CharField(label='Initial Inventory', max_length=100)
    final_inventory_1 = forms.CharField(label='Final Inventory', max_length=100)
    final_inventory_2 = forms.CharField(label='Final Inventory', max_length=100)
    signature = forms.CharField(label='Name of person filling the questionnaire', max_length=100)
    rank = forms.CharField(label='Rank', max_length=100)

class IP_220(forms.Form):
    company_name = forms.CharField(label='Nombre compañía / Company Name', max_length=100)
    address = forms.CharField(label='Dirección / Address', max_length=200)
    email = forms.EmailField(label='Correo electrónico / Email')
    liaison_officer = forms.CharField(label='Persona contacto / Liaison officer', max_length=100)
    ssn = forms.CharField(label='Numero de Seguro Social / Social Security Number', max_length=11)
    tel = forms.CharField(label='Tel', max_length=20)
    fax = forms.CharField(label='Fax', max_length=20)
    legal_form = forms.ChoiceField(
        label='Forma legal de organización / Legal form of organization', 
        choices=[('Corporación', 'Corporación'), ('Sociedad', 'Sociedad'), ('Cooperativa', 'Cooperativa'), ('Empresa Individual', 'Empresa Individual'), ('Empresa sin fines pecuniarios', 'Empresa sin fines pecuniarios')]
    )
    cfc = forms.ChoiceField(label='CEC', choices=[('Si', 'Si'), ('No', 'No')])
    business_type = forms.CharField(label='Clase de negocio / Type of business', max_length=200)
    business_function = forms.CharField(
        label='Describa brevemente la función principal del negocio / Explain briefly the main function of the business activity', 
        widget=forms.Textarea
    )
    branches = forms.ChoiceField(label='¿Opera sucursuales esta firma? / Do you have branch operations?', choices=[('Si', 'Si'), ('No', 'No')])
    branches_yes = forms.ChoiceField(label='afirmativo a branches', choices=[('todas las sucursales', 'todas las sucursales'), ('este establecimiento', 'este establecimiento')])
    closing_date = forms.DateField(label='Fecha de cierre de sus libros / Your accounting period closing date', widget=forms.SelectDateWidget)
    services_revenues_12 = forms.CharField(label='Ingresos por servicios - Services rendered'),
    services_revenues_13 = forms.CharField(label='Ingresos por servicios - Services rendered'),
    residential_consumers_12 = forms.CharField(label='a. Abonados residenciales - Residential consumers'),
    residential_consumers_13 = forms.CharField(label='a. A industrias y negocios - To industries and businesses'),
    other_consumers_12 = forms.CharField(label='b. Otros abonados - Other consumers'),
    other_consumers_13 = forms.CharField(label='b. A personas - To persons'),
    sales_12 = forms.CharField(label='2. Ventas - From sale of merchandise'),
    sales_13 = forms.CharField(label='2. Ventas - From sale of merchandise'),
    incomes_rents_12 = forms.CharField(label='3. Alquileres - From rents'),
    incomes_rents_13 = forms.CharField(label='3. Alquileres - From rents'),
    incomes_interests_12 = forms.CharField(label='4. Intereses - Interests'),
    incomes_interests_13 = forms.CharField(label='4. Intereses - Interests'),
    dividends_12 = forms.CharField(label='5. Ganancia o pérdida de capital - Capital gain or loss'),
    dividends_13 = forms.CharField(label='5. Ganancia o pérdida de capital - Capital gain or loss'),
    others_incomes_12 = forms.CharField(label='6. Otros ingresos de operación - Other operating income'),
    others_incomes_13 = forms.CharField(label='6. Otros ingresos de operación - Other operating income'),
    total_income_12 = forms.CharField(label='7. Total de ingresos - Total income'),
    total_income_13 = forms.CharField(label='7. Total de ingresos - Total income'),
    salaries_2012 = forms.CharField(label='1. Salarios, jornales, bono de Navidad y comisiones - Salaries, wages, Christmas bonus, and commissions'),
    salaries_2013 = forms.CharField(label='1. Salarios, jornales, bono de Navidad y comisiones - Salaries, wages, Christmas bonus, and commissions'),
    expenses_interests_12 = forms.CharField(label='2. Intereses - Interests'),
    expenses_interests_13 = forms.CharField(label='2. Intereses - Interests'),
    expenses_rents_12 = forms.CharField(label='3. Renta de terreno y edificio - Rent of land and building'),
    expenses_rents_13 = forms.CharField(label='3. Renta de terreno y edificio - Rent of land and building'),
    depreciation_12 = forms.CharField(label='4. Depreciación - Depreciation'),
    depreciation_13 = forms.CharField(label='4. Depreciación - Depreciation'),
    bad_debts_12 = forms.CharField(label='5. Cuentas incobrables - Bad debts'),
    bad_debts_13 = forms.CharField(label='5. Cuentas incobrables - Bad debts'),
    donations_12 = forms.CharField(label='6. Donativos - Donations'),
    donations_13 = forms.CharField(label='6. Donativos - Donations'),
    sales_tax_12 = forms.CharField(label='7. Impuesto sobre la venta y uso - sales and use tax'),
    sales_tax_13 = forms.CharField(label='7. Impuesto sobre la venta y uso - sales and use tax'),
    machinery_12 = forms.CharField(label='a. Por Compra de maquinaria y equipo - On purchases of machinery and equipment'),
    machinery_13 = forms.CharField(label='a. Por Compra de maquinaria y equipo - On purchases of machinery and equipment'),
    other_purchases_12 = forms.CharField(label='b. Por otras compras - On other purchases'),
    other_purchases_13 = forms.CharField(label='b. Por otras compras - On other purchases'),
    licenses_12 = forms.CharField(label='8. Licencias y patentes - Licenses and patents'),
    licenses_13 = forms.CharField(label='8. Licencias y patentes - Licenses and patents'),
    other_expenses_12 = forms.CharField(label='9. Otros gastos de operación - Other operating expenses'),
    other_expenses_13 = forms.CharField(label='9. Otros gastos de operación - Other operating expenses'),
    total_expenses_12 = forms.CharField(label='10. Total de gastos - Total expenses'),
    total_expenses_13 = forms.CharField(label='10. Total de gastos - Total expenses'),
    net_profit_12 = forms.CharField(label='C. Ganancia o pérdida neta ( + ó - ) - Net profit or loss ( + or - )'),
    net_profit_13 = forms.CharField(label='C. Ganancia o pérdida neta ( + ó - ) - Net profit or loss ( + or - )'),
    income_tax_12 = forms.CharField(label='1. Contribución sobre ingresos - Income tax'),
    income_tax_13 = forms.CharField(label='1. Contribución sobre ingresos - Income tax'),
    profit_after_tax_12 = forms.CharField(label='2. Ganancia después de contribución sobre ingresos - Profit after income tax'),
    profit_after_tax_13 = forms.CharField(label='2. Ganancia después de contribución sobre ingresos - Profit after income tax'),
    withheld_tax_12 = forms.CharField(label='D. Impuesto sobre ventas y uso retenido - Sales and use tax Withheld'),
    withheld_tax_13 = forms.CharField(label='D. Impuesto sobre ventas y uso retenido - Sales and use tax Withheld'),
    signature = forms.CharField(label='Nombre de persona que suministra la información - Name of person furnishing information', max_length=100)
    rank = forms.CharField(label='Rango - Title')

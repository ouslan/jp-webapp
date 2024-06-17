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
    industries_businesses_12 = forms.CharField(label='a. A industrias y negocios - To industries and businesses'),
    industries_businesses_13 = forms.CharField(label='a. A industrias y negocios - To industries and businesses'),
    people_12 = forms.CharField(label='b. A personas - To persons'),
    people_13 = forms.CharField(label='b. A personas - To persons'),
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
    
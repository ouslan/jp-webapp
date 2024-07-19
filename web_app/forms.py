from django import forms
from config_ui.settings import TEMPLATES


class IP_110(forms.Form):
    company_name = forms.CharField(
        label="Nombre compañía / Company Name", max_length=100
    )
    address = forms.CharField(label="Dirección / Address", max_length=200)
    email = forms.EmailField(label="Correo electrónico / Email")
    liaison_officer = forms.CharField(
        label="Persona contacto / Liaison officer", max_length=100
    )
    ssn = forms.CharField(
        label="Numero de Seguro Social / Social Security Number", max_length=11
    )
    tel = forms.CharField(label="Tel", max_length=20)
    fax = forms.CharField(label="Fax", max_length=20)
    legal_form = forms.ChoiceField(
        label="Forma legal de organización / Legal form of organization",
        choices=[
            ("Corporación", "Corporación"),
            ("Sociedad", "Sociedad"),
            ("Cooperativa", "Cooperativa"),
            ("Empresa Individual", "Empresa Individual"),
            ("Empresa sin fines pecuniarios", "Empresa sin fines pecuniarios"),
        ],
    )
    cfc = forms.ChoiceField(label="CEC", choices=[("Si", "Si"), ("No", "No")])
    business_type = forms.CharField(
        label="Clase de negocio / Type of business", max_length=200
    )
    business_function = forms.CharField(
        label="Describa brevemente la función principal del negocio / Explain briefly the main function of the business activity",
        widget=forms.Textarea,
    )
    branches = forms.ChoiceField(
        label="¿Opera sucursuales esta firma? / Do you have branch operations?",
        choices=[("Si", "Si"), ("No", "No")],
    )
    closing_date = (
        forms.DateField(
            label="Fecha de cierre de sus libros / Your accounting period closing date",
            widget=forms.SelectDateWidget,
        ),
    )
    start_year = forms.CharField(
        label="Año de inicio de operaciones / Year of start of operations",
        max_length=100,
    )
    end_year = forms.CharField(
        label="Año de cierre de operaciones / Year of end of operations", max_length=100
    )
    services_revenues_12 = (
        forms.CharField(label="Ingresos por servicios - Services rendered"),
    )
    services_revenues_13 = (
        forms.CharField(label="Ingresos por servicios - Services rendered"),
    )
    industries_businesses_12 = (
        forms.CharField(
            label="Ingresos por industrias y negocios - From industries and businesses"
        ),
    )
    industries_businesses_13 = (
        forms.CharField(
            label="Ingresos por industrias y negocios - From industries and businesses"
        ),
    )
    people_12 = (forms.CharField(label="Ingresos por personas - From people"),)
    people_13 = (forms.CharField(label="Ingresos por personas - From people"),)
    sales_12 = (forms.CharField(label="2. Ventas - From sale of merchandise"),)
    sales_13 = (forms.CharField(label="2. Ventas - From sale of merchandise"),)
    incomes_rents_12 = (forms.CharField(label="3. Alquileres - From rents"),)
    incomes_rents_13 = (forms.CharField(label="3. Alquileres - From rents"),)
    incomes_interests_12 = (forms.CharField(label="4. Intereses - Interests"),)
    incomes_interests_13 = (forms.CharField(label="4. Intereses - Interests"),)
    dividends_12 = (
        forms.CharField(
            label="5. Ganancia o pérdida de capital - Capital gain or loss"
        ),
    )
    dividends_13 = (
        forms.CharField(
            label="5. Ganancia o pérdida de capital - Capital gain or loss"
        ),
    )
    others_incomes_12 = (
        forms.CharField(
            label="6. Otros ingresos de operación - Other operating income"
        ),
    )
    others_incomes_13 = (
        forms.CharField(
            label="6. Otros ingresos de operación - Other operating income"
        ),
    )
    total_income_12 = (forms.CharField(label="7. Total de ingresos - Total income"),)
    total_income_13 = (forms.CharField(label="7. Total de ingresos - Total income"),)
    expenses_2012 = (forms.CharField(label="B. Gastos - Expenses"),)
    expenses_2012 = (forms.CharField(label="B. Gastos - Expenses"),)
    salaries_2012 = (
        forms.CharField(
            label="1. Salarios, jornales, bono de Navidad y comisiones - Salaries, wages, Christmas bonus, and commissions"
        ),
    )
    salaries_2013 = (
        forms.CharField(
            label="1. Salarios, jornales, bono de Navidad y comisiones - Salaries, wages, Christmas bonus, and commissions"
        ),
    )
    expenses_interests_12 = (forms.CharField(label="2. Intereses - Interests"),)
    expenses_interests_13 = (forms.CharField(label="2. Intereses - Interests"),)
    expenses_rents_12 = (
        forms.CharField(
            label="3. Renta de terreno y edificio - Rent of land and building"
        ),
    )
    expenses_rents_13 = (
        forms.CharField(
            label="3. Renta de terreno y edificio - Rent of land and building"
        ),
    )
    depreciation_12 = (forms.CharField(label="4. Depreciación - Depreciation"),)
    depreciation_13 = (forms.CharField(label="4. Depreciación - Depreciation"),)
    bad_debts_12 = (forms.CharField(label="5. Cuentas incobrables - Bad debts"),)
    bad_debts_13 = (forms.CharField(label="5. Cuentas incobrables - Bad debts"),)
    donations_12 = (forms.CharField(label="6. Donativos - Donations"),)
    donations_13 = (forms.CharField(label="6. Donativos - Donations"),)
    sales_tax_12 = (
        forms.CharField(label="7. Impuesto sobre la venta y uso - sales and use tax"),
    )
    sales_tax_13 = (
        forms.CharField(label="7. Impuesto sobre la venta y uso - sales and use tax"),
    )
    machinery_12 = (
        forms.CharField(
            label="a. Por Compra de maquinaria y equipo - On purchases of machinery and equipment"
        ),
    )
    machinery_13 = (
        forms.CharField(
            label="a. Por Compra de maquinaria y equipo - On purchases of machinery and equipment"
        ),
    )
    other_purchases_12 = (
        forms.CharField(label="b. Por otras compras - On other purchases"),
    )
    other_purchases_13 = (
        forms.CharField(label="b. Por otras compras - On other purchases"),
    )
    licenses_12 = (
        forms.CharField(label="8. Licencias y patentes - Licenses and patents"),
    )
    licenses_13 = (
        forms.CharField(label="8. Licencias y patentes - Licenses and patents"),
    )
    other_expenses_12 = (
        forms.CharField(
            label="9. Otros gastos de operación - Other operating expenses"
        ),
    )
    other_expenses_13 = (
        forms.CharField(
            label="9. Otros gastos de operación - Other operating expenses"
        ),
    )
    total_expenses_12 = (forms.CharField(label="10. Total de gastos - Total expenses"),)
    total_expenses_13 = (forms.CharField(label="10. Total de gastos - Total expenses"),)
    net_profit_12 = (
        forms.CharField(
            label="C. Ganancia o pérdida neta ( + ó - ) - Net profit or loss ( + or - )"
        ),
    )
    net_profit_13 = (
        forms.CharField(
            label="C. Ganancia o pérdida neta ( + ó - ) - Net profit or loss ( + or - )"
        ),
    )
    income_tax_12 = (
        forms.CharField(label="1. Contribución sobre ingresos - Income tax"),
    )
    income_tax_13 = (
        forms.CharField(label="1. Contribución sobre ingresos - Income tax"),
    )
    profit_after_tax_12 = (
        forms.CharField(
            label="2. Ganancia después de contribución sobre ingresos - Profit after income tax"
        ),
    )
    profit_after_tax_13 = (
        forms.CharField(
            label="2. Ganancia después de contribución sobre ingresos - Profit after income tax"
        ),
    )
    withheld_tax_12 = (
        forms.CharField(
            label="D. Impuesto sobre ventas y uso retenido - Sales and use tax Withheld"
        ),
    )
    withheld_tax_13 = (
        forms.CharField(
            label="D. Impuesto sobre ventas y uso retenido - Sales and use tax Withheld"
        ),
    )
    signature = forms.CharField(
        label="Nombre de persona que suministra la información - Name of person furnishing information",
        max_length=100,
    )
    rank = forms.CharField(label="Rango - Title")


class JP_304(forms.Form):
    MONTH_CHOICES = [
        ("mes", "mes"),
        ("enero", "enero"),
        ("febrero", "febrero"),
        ("marzo", "marzo"),
        ("abril", "abril"),
        ("mayo", "mayo"),
        ("junio", "junio"),
        ("julio", "julio"),
        ("agosto", "agosto"),
        ("septiembre", "septiembre"),
        ("octubre", "octubre"),
        ("noviembre", "noviembre"),
        ("diciembre", "diciembre"),
    ]

    start_month = forms.ChoiceField(choices=MONTH_CHOICES, required=True)
    end_month = forms.ChoiceField(choices=MONTH_CHOICES, required=True)
    year = forms.IntegerField(required=True)
    name = forms.CharField(label="Nombre / Name", max_length=100)
    direction = forms.CharField(label="Dirección / Address", max_length=200)
    liaison_officer = forms.CharField(
        label="Persona contacto / Liaison officer", max_length=100
    )
    title = forms.CharField(label="Título / Title", max_length=100)
    tel = forms.CharField(label="Tel", max_length=20)
    nombre_agencia_federal = forms.CharField(
        label="Nombre de la agencia federal / Name of federal agency", max_length=100
    )
    catalogo_federal = forms.CharField(
        label="Número de catálogo federal / Federal catalog number", max_length=100
    )
    sai_federal = forms.CharField(
        label="Número de SAI federal / Federal SAI number", max_length=100
    )
    titulo_federal = forms.CharField(
        label="Título federal / Federal title", max_length=100
    )
    aportacion_aprobada_federal = forms.CharField(
        label="Aportación aprobada federal / Federal approved contribution",
        max_length=100,
    )
    fecha_aprobacion_federal = forms.DateField(
        label="Fecha de aprobación federal / Federal approval date",
        widget=forms.SelectDateWidget,
    )
    aportacion_recibida_federal = forms.CharField(
        label="Aportación recibida federal / Federal contribution received",
        max_length=100,
    )
    fecha_recibo_federal = forms.DateField(
        label="Fecha de recibo federal / Federal receipt date",
        widget=forms.SelectDateWidget,
    )
    aportacion_gastada_federal = forms.CharField(
        label="Aportación gastada federal / Federal contribution spent", max_length=100
    )
    fecha_gasto_federal = forms.DateField(
        label="Fecha de gasto federal / Federal spending date",
        widget=forms.SelectDateWidget,
    )
    agencia_local_table_box = forms.CharField(
        label="Agencia local / Local agency", max_length=100
    )
    catalogo_local = forms.CharField(
        label="Número de catálogo local / Local catalog number", max_length=100
    )
    programa_local = forms.CharField(
        label="Programa local / Local program", max_length=100
    )
    aportacion_federal_aprobada_local = forms.CharField(
        label="Aportación aprobada federal local / Local federal approved contribution",
        max_length=100,
    )
    fecha_aprobacion_local = forms.DateField(
        label="Fecha de aprobación local / Local approval date",
        widget=forms.SelectDateWidget,
    )
    aportacion_federal_recibida_local = forms.CharField(
        label="Aportación recibida federal local / Local federal contribution received",
        max_length=100,
    )
    fecha_recibo_local = forms.DateField(
        label="Fecha de recibo federal local / Local federal receipt date",
        widget=forms.SelectDateWidget,
    )
    aportacion_federal_gastada_local = forms.CharField(
        label="Aportación gastada federal local / Local federal contribution spent",
        max_length=100,
    )
    fecha_gasto_local = forms.DateField(
        label="Fecha de gasto federal local / Local federal spending date",
        widget=forms.SelectDateWidget,
    )
    numero_cuenta_local = forms.CharField(
        label="Número de cuenta local / Local account number", max_length=100
    )


class JP_541(forms.Form):
    COMPANT_TYPE_CHOICES = [
        ("Corporación", "Corporación"),
        ("Administración", "Administración"),
    ]

    # TABLE 1
    form_1 = forms.CharField(label="Encuesta :", max_length=100)
    fiscal_year_1 = forms.CharField(label="Año Fiscal :", max_length=100)
    company_name_1 = forms.CharField(label="Nombre de la Empresa:", max_length=100)
    liaison_officer_1 = forms.CharField(label="Persona de Contacto:", max_length=100)
    tel_1 = forms.CharField(label="Teléfono::", max_length=100)
    project_1 = forms.CharField(label="Proyecto por::", max_length=100)
    branches_1 = forms.CharField(choice=COMPANT_TYPE_CHOICES, max_length=100)

    project_name_1_1 = forms.CharField(label="", max_length=100)
    city_1_1 = forms.CharField(label="", max_length=100)
    total_number_project_1_1 = forms.CharField(label="", max_length=100)
    total_cost_1_1 = forms.CharField(label="", max_length=100)
    start_date_1_1 = forms.DateField(label="", widget=forms.SelectDateWidget)
    end_date_1_1 = forms.DateField(label="", widget=forms.SelectDateWidget)
    value_first_trimester_1_1 = forms.CharField(label="", max_length=100)
    value_second_trimester_1_1 = forms.CharField(label="", max_length=100)
    value_third_trimester_1_1 = forms.CharField(label="", max_length=100)
    value_fourth_trimester_1_1 = forms.CharField(label="", max_length=100)

    project_name_1_2 = forms.CharField(label="", max_length=100)
    city_1_2 = forms.CharField(label="", max_length=100)
    total_number_project_1_2 = forms.CharField(label="", max_length=100)
    total_cost_1_2 = forms.CharField(label="", max_length=100)
    start_date_1_2 = forms.DateField(label="", widget=forms.SelectDateWidget)
    end_date_1_2 = forms.DateField(label="", widget=forms.SelectDateWidget)
    value_first_trimester_1_2 = forms.CharField(label="", max_length=100)
    value_second_trimester_1_2 = forms.CharField(label="", max_length=100)
    value_third_trimester_1_2 = forms.CharField(label="", max_length=100)
    value_fourth_trimester_1_2 = forms.CharField(label="", max_length=100)

    project_name_1_3 = forms.CharField(label="", max_length=100)
    city_1_3 = forms.CharField(label="", max_length=100)
    total_number_project_1_3 = forms.CharField(label="", max_length=100)
    total_cost_1_3 = forms.CharField(label="", max_length=100)
    start_date_1_3 = forms.DateField(label="", widget=forms.SelectDateWidget)
    end_date_1_3 = forms.DateField(label="", widget=forms.SelectDateWidget)
    value_first_trimester_1_3 = forms.CharField(label="", max_length=100)
    value_second_trimester_1_3 = forms.CharField(label="", max_length=100)
    value_third_trimester_1_3 = forms.CharField(label="", max_length=100)
    value_fourth_trimester_1_3 = forms.CharField(label="", max_length=100)

    project_name_1_4 = forms.CharField(label="", max_length=100)
    city_1_4 = forms.CharField(label="", max_length=100)
    total_number_project_1_4 = forms.CharField(label="", max_length=100)
    total_cost_1_4 = forms.CharField(label="", max_length=100)
    start_date_1_4 = forms.DateField(label="", widget=forms.SelectDateWidget)
    end_date_1_4 = forms.DateField(label="", widget=forms.SelectDateWidget)
    value_first_trimester_1_4 = forms.CharField(label="", max_length=100)
    value_second_trimester_1_4 = forms.CharField(label="", max_length=100)
    value_third_trimester_1_4 = forms.CharField(label="", max_length=100)
    value_fourth_trimester_1_4 = forms.CharField(label="", max_length=100)

    project_name_1_5 = forms.CharField(label="", max_length=100)
    city_1_5 = forms.CharField(label="", max_length=100)
    total_number_project_1_5 = forms.CharField(label="", max_length=100)
    total_cost_1_5 = forms.CharField(label="", max_length=100)
    start_date_1_5 = forms.DateField(label="", widget=forms.SelectDateWidget)
    end_date_1_5 = forms.DateField(label="", widget=forms.SelectDateWidget)
    value_first_trimester_1_5 = forms.CharField(label="", max_length=100)
    value_second_trimester_1_5 = forms.CharField(label="", max_length=100)
    value_third_trimester_1_5 = forms.CharField(label="", max_length=100)
    value_fourth_trimester_1_5 = forms.CharField(label="", max_length=100)

    # TABLE 2
    form_2 = forms.CharField(label="Encuesta :", max_length=100)
    fiscal_year_2 = forms.CharField(label="Año Fiscal :", max_length=100)
    company_name_2 = forms.CharField(label="Nombre de la Empresa:", max_length=100)
    liaison_officer_2 = forms.CharField(label="Persona de Contacto:", max_length=100)
    tel_2 = forms.CharField(label="Teléfono::", max_length=100)
    project_2 = forms.CharField(label="Proyecto por::", max_length=100)
    branches_2 = forms.CharField(choice=COMPANT_TYPE_CHOICES, max_length=100)

    project_name_2_1 = forms.CharField(label="", max_length=100)
    city_2_1 = forms.CharField(label="", max_length=100)
    total_number_project_2_1 = forms.CharField(label="", max_length=100)
    total_cost_2_1 = forms.CharField(label="", max_length=100)
    start_date_2_1 = forms.DateField(label="", widget=forms.SelectDateWidget)
    end_date_2_1 = forms.DateField(label="", widget=forms.SelectDateWidget)
    value_first_trimester_2_1 = forms.CharField(label="", max_length=100)
    value_second_trimester_2_1 = forms.CharField(label="", max_length=100)
    value_third_trimester_2_1 = forms.CharField(label="", max_length=100)
    value_fourth_trimester_2_1 = forms.CharField(label="", max_length=100)

    project_name_2_2 = forms.CharField(label="", max_length=100)
    city_2_2 = forms.CharField(label="", max_length=100)
    total_number_project_2_2 = forms.CharField(label="", max_length=100)
    total_cost_2_2 = forms.CharField(label="", max_length=100)
    start_date_2_2 = forms.DateField(label="", widget=forms.SelectDateWidget)
    end_date_2_2 = forms.DateField(label="", widget=forms.SelectDateWidget)
    value_first_trimester_2_2 = forms.CharField(label="", max_length=100)
    value_second_trimester_2_2 = forms.CharField(label="", max_length=100)
    value_third_trimester_2_2 = forms.CharField(label="", max_length=100)
    value_fourth_trimester_2_2 = forms.CharField(label="", max_length=100)

    project_name_2_3 = forms.CharField(label="", max_length=100)
    city_2_3 = forms.CharField(label="", max_length=100)
    total_number_project_2_3 = forms.CharField(label="", max_length=100)
    total_cost_2_3 = forms.CharField(label="", max_length=100)
    start_date_2_3 = forms.DateField(label="", widget=forms.SelectDateWidget)
    end_date_2_3 = forms.DateField(label="", widget=forms.SelectDateWidget)
    value_first_trimester_2_3 = forms.CharField(label="", max_length=100)
    value_second_trimester_2_3 = forms.CharField(label="", max_length=100)
    value_third_trimester_2_3 = forms.CharField(label="", max_length=100)
    value_fourth_trimester_2_3 = forms.CharField(label="", max_length=100)

    project_name_2_4 = forms.CharField(label="", max_length=100)
    city_2_4 = forms.CharField(label="", max_length=100)
    total_number_project_2_4 = forms.CharField(label="", max_length=100)
    total_cost_2_4 = forms.CharField(label="", max_length=100)
    start_date_2_4 = forms.DateField(label="", widget=forms.SelectDateWidget)
    end_date_2_4 = forms.DateField(label="", widget=forms.SelectDateWidget)
    value_first_trimester_2_4 = forms.CharField(label="", max_length=100)
    value_second_trimester_2_4 = forms.CharField(label="", max_length=100)
    value_third_trimester_2_4 = forms.CharField(label="", max_length=100)
    value_fourth_trimester_2_4 = forms.CharField(label="", max_length=100)

    project_name_2_5 = forms.CharField(label="", max_length=100)
    city_2_5 = forms.CharField(label="", max_length=100)
    total_number_project_2_5 = forms.CharField(label="", max_length=100)
    total_cost_2_5 = forms.CharField(label="", max_length=100)
    start_date_2_5 = forms.DateField(label="", widget=forms.SelectDateWidget)
    end_date_2_5 = forms.DateField(label="", widget=forms.SelectDateWidget)
    value_first_trimester_2_5 = forms.CharField(label="", max_length=100)
    value_second_trimester_2_5 = forms.CharField(label="", max_length=100)
    value_third_trimester_2_5 = forms.CharField(label="", max_length=100)
    value_fourth_trimester_2_5 = forms.CharField(label="", max_length=100)

    # TABLE 3
    form_3 = forms.CharField(label="Encuesta :", max_length=100)
    fiscal_year_3 = forms.CharField(label="Año Fiscal :", max_length=100)
    company_name_3 = forms.CharField(label="Nombre de la Empresa:", max_length=100)
    liaison_officer_3 = forms.CharField(label="Persona de Contacto:", max_length=100)
    tel_3 = forms.CharField(label="Teléfono::", max_length=100)
    project_3 = forms.CharField(label="Proyecto por::", max_length=100)
    branches_3 = forms.CharField(choice=COMPANT_TYPE_CHOICES, max_length=100)

    project_name_3_1 = forms.CharField(label="", max_length=100)
    city_3_1 = forms.CharField(label="", max_length=100)
    total_number_project_3_1 = forms.CharField(label="", max_length=100)
    total_cost_3_1 = forms.CharField(label="", max_length=100)
    start_date_3_1 = forms.DateField(label="", widget=forms.SelectDateWidget)
    end_date_3_1 = forms.DateField(label="", widget=forms.SelectDateWidget)
    value_first_trimester_3_1 = forms.CharField(label="", max_length=100)
    value_second_trimester_3_1 = forms.CharField(label="", max_length=100)
    value_third_trimester_3_1 = forms.CharField(label="", max_length=100)
    value_fourth_trimester_3_1 = forms.CharField(label="", max_length=100)

    project_name_3_2 = forms.CharField(label="", max_length=100)
    city_3_2 = forms.CharField(label="", max_length=100)
    total_number_project_3_2 = forms.CharField(label="", max_length=100)
    total_cost_3_2 = forms.CharField(label="", max_length=100)
    start_date_3_2 = forms.DateField(label="", widget=forms.SelectDateWidget)
    end_date_3_2 = forms.DateField(label="", widget=forms.SelectDateWidget)
    value_first_trimester_3_2 = forms.CharField(label="", max_length=100)
    value_second_trimester_3_2 = forms.CharField(label="", max_length=100)
    value_third_trimester_3_2 = forms.CharField(label="", max_length=100)
    value_fourth_trimester_3_2 = forms.CharField(label="", max_length=100)

    project_name_3_3 = forms.CharField(label="", max_length=100)
    city_3_3 = forms.CharField(label="", max_length=100)
    total_number_project_3_3 = forms.CharField(label="", max_length=100)
    total_cost_3_3 = forms.CharField(label="", max_length=100)
    start_date_3_3 = forms.DateField(label="", widget=forms.SelectDateWidget)
    end_date_3_3 = forms.DateField(label="", widget=forms.SelectDateWidget)
    value_first_trimester_3_3 = forms.CharField(label="", max_length=100)
    value_second_trimester_3_3 = forms.CharField(label="", max_length=100)
    value_third_trimester_3_3 = forms.CharField(label="", max_length=100)
    value_fourth_trimester_3_3 = forms.CharField(label="", max_length=100)

    project_name_3_4 = forms.CharField(label="", max_length=100)
    city_3_4 = forms.CharField(label="", max_length=100)
    total_number_project_3_4 = forms.CharField(label="", max_length=100)
    total_cost_3_4 = forms.CharField(label="", max_length=100)
    start_date_3_4 = forms.DateField(label="", widget=forms.SelectDateWidget)
    end_date_3_4 = forms.DateField(label="", widget=forms.SelectDateWidget)
    value_first_trimester_3_4 = forms.CharField(label="", max_length=100)
    value_second_trimester_3_4 = forms.CharField(label="", max_length=100)
    value_third_trimester_3_4 = forms.CharField(label="", max_length=100)
    value_fourth_trimester_3_4 = forms.CharField(label="", max_length=100)

    project_name_3_5 = forms.CharField(label="", max_length=100)
    city_3_5 = forms.CharField(label="", max_length=100)
    total_number_project_3_5 = forms.CharField(label="", max_length=100)
    total_cost_3_5 = forms.CharField(label="", max_length=100)
    start_date_3_5 = forms.DateField(label="", widget=forms.SelectDateWidget)
    end_date_3_5 = forms.DateField(label="", widget=forms.SelectDateWidget)
    value_first_trimester_3_5 = forms.CharField(label="", max_length=100)
    value_second_trimester_3_5 = forms.CharField(label="", max_length=100)
    value_third_trimester_3_5 = forms.CharField(label="", max_length=100)
    value_fourth_trimester_3_5 = forms.CharField(label="", max_length=100)

    # TABLE 4
    form_4 = forms.CharField(label="Encuesta :", max_length=100)
    fiscal_year_4 = forms.CharField(label="Año Fiscal :", max_length=100)
    company_name_4 = forms.CharField(label="Nombre de la Empresa:", max_length=100)
    liaison_officer_4 = forms.CharField(label="Persona de Contacto:", max_length=100)
    tel_4 = forms.CharField(label="Teléfono::", max_length=100)
    project_4 = forms.CharField(label="Proyecto por::", max_length=100)
    branches_4 = forms.CharField(choice=COMPANT_TYPE_CHOICES, max_length=100)

    project_name_4_1 = forms.CharField(label="", max_length=100)
    city_4_1 = forms.CharField(label="", max_length=100)
    total_number_project_4_1 = forms.CharField(label="", max_length=100)
    total_cost_4_1 = forms.CharField(label="", max_length=100)
    start_date_4_1 = forms.DateField(label="", widget=forms.SelectDateWidget)
    end_date_4_1 = forms.DateField(label="", widget=forms.SelectDateWidget)
    value_first_trimester_4_1 = forms.CharField(label="", max_length=100)
    value_second_trimester_4_1 = forms.CharField(label="", max_length=100)
    value_third_trimester_4_1 = forms.CharField(label="", max_length=100)
    value_fourth_trimester_4_1 = forms.CharField(label="", max_length=100)

    project_name_4_2 = forms.CharField(label="", max_length=100)
    city_4_2 = forms.CharField(label="", max_length=100)
    total_number_project_4_2 = forms.CharField(label="", max_length=100)
    total_cost_4_2 = forms.CharField(label="", max_length=100)
    start_date_4_2 = forms.DateField(label="", widget=forms.SelectDateWidget)
    end_date_4_2 = forms.DateField(label="", widget=forms.SelectDateWidget)
    value_first_trimester_4_2 = forms.CharField(label="", max_length=100)
    value_second_trimester_4_2 = forms.CharField(label="", max_length=100)
    value_third_trimester_4_2 = forms.CharField(label="", max_length=100)
    value_fourth_trimester_4_2 = forms.CharField(label="", max_length=100)

    project_name_4_3 = forms.CharField(label="", max_length=100)
    city_4_3 = forms.CharField(label="", max_length=100)
    total_number_project_4_3 = forms.CharField(label="", max_length=100)
    total_cost_4_3 = forms.CharField(label="", max_length=100)
    start_date_4_3 = forms.DateField(label="", widget=forms.SelectDateWidget)
    end_date_4_3 = forms.DateField(label="", widget=forms.SelectDateWidget)
    value_first_trimester_4_3 = forms.CharField(label="", max_length=100)
    value_second_trimester_4_3 = forms.CharField(label="", max_length=100)
    value_third_trimester_4_3 = forms.CharField(label="", max_length=100)
    value_fourth_trimester_4_3 = forms.CharField(label="", max_length=100)

    project_name_4_4 = forms.CharField(label="", max_length=100)
    city_4_4 = forms.CharField(label="", max_length=100)
    total_number_project_4_4 = forms.CharField(label="", max_length=100)
    total_cost_4_4 = forms.CharField(label="", max_length=100)
    start_date_4_4 = forms.DateField(label="", widget=forms.SelectDateWidget)
    end_date_4_4 = forms.DateField(label="", widget=forms.SelectDateWidget)
    value_first_trimester_4_4 = forms.CharField(label="", max_length=100)
    value_second_trimester_4_4 = forms.CharField(label="", max_length=100)
    value_third_trimester_4_4 = forms.CharField(label="", max_length=100)
    value_fourth_trimester_4_4 = forms.CharField(label="", max_length=100)

    project_name_4_5 = forms.CharField(label="", max_length=100)
    city_4_5 = forms.CharField(label="", max_length=100)
    total_number_project_4_5 = forms.CharField(label="", max_length=100)
    total_cost_4_5 = forms.CharField(label="", max_length=100)
    start_date_4_5 = forms.DateField(label="", widget=forms.SelectDateWidget)
    end_date_4_5 = forms.DateField(label="", widget=forms.SelectDateWidget)
    value_first_trimester_4_5 = forms.CharField(label="", max_length=100)
    value_second_trimester_4_5 = forms.CharField(label="", max_length=100)
    value_third_trimester_4_5 = forms.CharField(label="", max_length=100)
    value_fourth_trimester_4_5 = forms.CharField(label="", max_length=100)


class JP_361(forms.Form):
    income_expenses_year_1 = forms.CharField(label="Year", max_length=4)
    income_expenses_year_2 = forms.CharField(label="Year", max_length=4)
    income_life_1 = forms.CharField(label="a) Life", max_length=100)
    income_life_2 = forms.CharField(label="a) Life", max_length=100)
    income_disability_1 = forms.CharField(label="b) Disability", max_length=100)
    income_disability_2 = forms.CharField(label="b) Disability", max_length=100)
    income_auto_1 = forms.CharField(label="c) Auto", max_length=100)
    income_auto_2 = forms.CharField(label="c) Auto", max_length=100)
    income_other_1 = forms.CharField(label="d) Other", max_length=100)
    income_other_2 = forms.CharField(label="d) Other", max_length=100)
    income_interest_1 = forms.CharField(label="2. Interest", max_length=100)
    income_interest_2 = forms.CharField(label="2. Interest", max_length=100)
    income_rent_1 = forms.CharField(
        label="3. Rent of land and building", max_length=100
    )
    income_rent_2 = forms.CharField(
        label="3. Rent of land and building", max_length=100
    )
    income_other_2_1 = forms.CharField(label="4. Other", max_length=100)
    income_other_2_2 = forms.CharField(label="4. Other", max_length=100)
    total_income_1 = forms.CharField(label="Total Income", max_length=100)
    total_income_2 = forms.CharField(label="Total Income", max_length=100)
    expenses_life_1 = forms.CharField(label="a) Life", max_length=100)
    expenses_life_2 = forms.CharField(label="a) Life", max_length=100)
    expenses_disability_1 = forms.CharField(label="b) Disability", max_length=100)
    expenses_disability_2 = forms.CharField(label="b) Disability", max_length=100)
    expenses_auto_1 = forms.CharField(label="c) Auto", max_length=100)
    expenses_auto_2 = forms.CharField(label="c) Auto", max_length=100)
    expenses_other_1 = forms.CharField(label="d) Other", max_length=100)
    expenses_other_2 = forms.CharField(label="d) Other", max_length=100)
    expenses_salaries_1 = forms.CharField(label="2. Salaries", max_length=100)
    expenses_salaries_2 = forms.CharField(label="2. Salaries", max_length=100)
    expenses_interes_1 = forms.CharField(label="3. Interest", max_length=100)
    expenses_interes_2 = forms.CharField(label="3. Interest", max_length=100)
    expenses_rent_1 = forms.CharField(
        label="4. Rent of land and building", max_length=100
    )
    expenses_rent_2 = forms.CharField(
        label="4. Rent of land and building", max_length=100
    )
    expenses_depreciation_1 = forms.CharField(label="5. Depreciation", max_length=100)
    expenses_depreciation_2 = forms.CharField(label="5. Depreciation", max_length=100)
    expenses_donations_1 = forms.CharField(label="6. Donations", max_length=100)
    expenses_donations_2 = forms.CharField(label="6. Donations", max_length=100)
    expenses_commissions_1 = forms.CharField(label="7. Commissions", max_length=100)
    expenses_commissions_2 = forms.CharField(label="7. Commissions", max_length=100)
    expenses_employees_1 = forms.CharField(label="a) To employees", max_length=100)
    expenses_employees_2 = forms.CharField(label="a) To employees", max_length=100)
    expenses_brokers_1 = forms.CharField(label="b) To local brokers", max_length=100)
    expenses_brokers_2 = forms.CharField(label="b) To local brokers", max_length=100)
    expenses_other_operational_1 = forms.CharField(
        label="8. Other operational expenses", max_length=100
    )
    expenses_other_operational_2 = forms.CharField(
        label="8. Other operational expenses", max_length=100
    )
    total_expenses_1 = forms.CharField(label="Total Expenses", max_length=100)
    total_expenses_2 = forms.CharField(label="Total Expenses", max_length=100)
    net_profit_1 = forms.CharField(label="Net profit or loss", max_length=100)
    net_profit_2 = forms.CharField(label="Net profit or loss", max_length=100)
    balance_year_1 = forms.CharField(label="As of 6/30/", max_length=4)
    balance_year_2 = forms.CharField(label="Estimated as of 6/30/", max_length=4)
    guaranteed_1 = forms.CharField(label="1. F.H.A. guaranteed", max_length=100)
    guaranteed_2 = forms.CharField(label="1. F.H.A. guaranteed", max_length=100)
    guaranteed_3 = forms.CharField(label="1. F.H.A. guaranteed", max_length=100)
    guaranteed_4 = forms.CharField(label="1. F.H.A. guaranteed", max_length=100)
    veterans_1 = forms.CharField(label="2. Veterans Administration", max_length=100)
    veterans_2 = forms.CharField(label="2. Veterans Administration", max_length=100)
    veterans_3 = forms.CharField(label="2. Veterans Administration", max_length=100)
    veterans_4 = forms.CharField(label="2. Veterans Administration", max_length=100)
    conventional_1 = forms.CharField(label="3. Conventional", max_length=100)
    conventional_2 = forms.CharField(label="3. Conventional", max_length=100)
    conventional_3 = forms.CharField(label="3. Conventional", max_length=100)
    conventional_4 = forms.CharField(label="3. Conventional", max_length=100)
    other_1 = forms.CharField(label="4. Other", max_length=100)
    other_2 = forms.CharField(label="4. Other", max_length=100)
    other_3 = forms.CharField(label="4. Other", max_length=100)
    other_4 = forms.CharField(label="4. Other", max_length=100)
    policy_loans_1 = forms.CharField(label="1. Policy loans", max_length=100)
    policy_loans_2 = forms.CharField(label="1. Policy loans", max_length=100)
    policy_loans_3 = forms.CharField(label="1. Policy loans", max_length=100)
    policy_loans_4 = forms.CharField(label="1. Policy loans", max_length=100)
    other_specify_1 = forms.CharField(label="5. Other (Specify)", max_length=100)
    other_specify_2 = forms.CharField(label="5. Other (Specify)", max_length=100)
    other_specify_3 = forms.CharField(label="5. Other (Specify)", max_length=100)
    other_specify_4 = forms.CharField(label="5. Other (Specify)", max_length=100)
    policy_reserves_1 = forms.CharField(
        label="1. Policy reserves of Puerto Rican residents", max_length=100
    )
    policy_reserves_2 = forms.CharField(
        label="1. Policy reserves of Puerto Rican residents", max_length=100
    )
    accrued_dividends_1 = forms.CharField(
        label="2. Accrued dividends on life insurance policies held by Puerto Rican residents",
        max_length=100,
    )
    accrued_dividends_2 = forms.CharField(
        label="2. Accrued dividends on life insurance policies held by Puerto Rican residents",
        max_length=100,
    )
    signature = forms.CharField(
        label="Name of person filling the questionnaire", max_length=100
    )
    date = forms.CharField(label="Date", max_length=100)
    phone = forms.CharField(label="Phone Number", max_length=100)
    position = forms.CharField(label="Position", max_length=100)


class JP_363(forms.Form):
    bonds_year_left = forms.CharField(label="Año", max_length=4)
    bonds_year_right = forms.CharField(label="Año", max_length=4)
    notes_year_left = forms.CharField(label="Año", max_length=4)
    notes_year_right = forms.CharField(label="Año", max_length=4)

    town_bonds_left = forms.CharField(label="Bonos Municipales", max_length=100)
    town_bonds_right = forms.CharField(label="Bonos Municipales", max_length=100)
    town_notes_left = forms.CharField(label="Notas Municipales", max_length=100)
    town_notes_right = forms.CharField(label="Notas Municipales", max_length=100)
    town_name_service = forms.CharField(label="Nombre del Servicio", max_length=100)

    PC_bonds_left = forms.CharField(label="Bonos Corporativos", max_length=100)
    PC_bonds_right = forms.CharField(label="Bonos Corporativos", max_length=100)
    PC_notes_left = forms.CharField(label="Notas Corporativas", max_length=100)
    PC_notes_right = forms.CharField(label="Notas Corporativas", max_length=100)
    PC_name_service = forms.CharField(label="Nombre del Servicio", max_length=100)

    EPA_bonds_left = forms.CharField(label="Bonos de la EPA", max_length=100)
    EPA_bonds_right = forms.CharField(label="Bonos de la EPA", max_length=100)
    EPA_notes_left = forms.CharField(label="Notas de la EPA", max_length=100)
    EPA_notes_right = forms.CharField(label="Notas de la EPA", max_length=100)
    EPA_name_service = forms.CharField(label="Nombre del Servicio", max_length=100)

    HA_bonds_left = forms.CharField(label="Bonos de la HA", max_length=100)
    HA_bonds_right = forms.CharField(label="Bonos de la HA", max_length=100)
    HA_notes_left = forms.CharField(label="Notas de la HA", max_length=100)
    HA_notes_right = forms.CharField(label="Notas de la HA", max_length=100)
    HA_name_service = forms.CharField(label="Nombre del Servicio", max_length=100)

    ASA_bonds_left = forms.CharField(label="Bonos de la ASA", max_length=100)
    ASA_bonds_right = forms.CharField(label="Bonos de la ASA", max_length=100)
    ASA_notes_left = forms.CharField(label="Notas de la ASA", max_length=100)
    ASA_notes_right = forms.CharField(label="Notas de la ASA", max_length=100)
    ASA_name_service = forms.CharField(label="Nombre del Servicio", max_length=100)

    PBA_bonds_left = forms.CharField(label="Bonos de la PBA", max_length=100)
    PBA_bonds_right = forms.CharField(label="Bonos de la PBA", max_length=100)
    PBA_notes_left = forms.CharField(label="Notas de la PBA", max_length=100)
    PBA_notes_right = forms.CharField(label="Notas de la PBA", max_length=100)
    PBA_name_service = forms.CharField(label="Nombre del Servicio", max_length=100)

    PA_bonds_left = forms.CharField(label="Bonos de la PA", max_length=100)
    PA_bonds_right = forms.CharField(label="Bonos de la PA", max_length=100)
    PA_notes_left = forms.CharField(label="Notas de la PA", max_length=100)
    PA_notes_right = forms.CharField(label="Notas de la PA", max_length=100)
    PA_name_service = forms.CharField(label="Nombre del Servicio", max_length=100)

    IDC_bonds_left = forms.CharField(label="Bonos de la IDC", max_length=100)
    IDC_bonds_right = forms.CharField(label="Bonos de la IDC", max_length=100)
    IDC_notes_left = forms.CharField(label="Notas de la IDC", max_length=100)
    IDC_notes_right = forms.CharField(label="Notas de la IDC", max_length=100)
    IDC_name_service = forms.CharField(label="Nombre del Servicio", max_length=100)

    GDB_bonds_left = forms.CharField(label="Bonos del GDB", max_length=100)
    GDB_bonds_right = forms.CharField(label="Bonos del GDB", max_length=100)
    GDB_notes_left = forms.CharField(label="Notas del GDB", max_length=100)
    GDB_notes_right = forms.CharField(label="Notas del GDB", max_length=100)
    GDB_name_service = forms.CharField(label="Nombre del Servicio", max_length=100)

    HFC_bonds_left = forms.CharField(label="Bonos de la HFC", max_length=100)
    HFC_bonds_right = forms.CharField(label="Bonos de la HFC", max_length=100)
    HFC_notes_left = forms.CharField(label="Notas de la HFC", max_length=100)
    HFC_notes_right = forms.CharField(label="Notas de la HFC", max_length=100)
    HFC_name_service = forms.CharField(label="Nombre del Servicio", max_length=100)

    other = forms.CharField(label="Otros", max_length=100)
    other_bonds_left = forms.CharField(label="Otros Bonos", max_length=100)
    other_bonds_right = forms.CharField(label="Otros Bonos", max_length=100)
    other_notes_left = forms.CharField(label="Otras Notas", max_length=100)
    other_notes_right = forms.CharField(label="Otras Notas", max_length=100)
    other_name_service = forms.CharField(label="Nombre del Servicio", max_length=100)

    other_PC_1 = forms.CharField(label="Otros Corporativos", max_length=100)
    other_PC_1_bonds_left = forms.CharField(label="Bonos", max_length=100)
    other_PC_1_bonds_right = forms.CharField(label="Bonos", max_length=100)
    other_PC_1_notes_left = forms.CharField(label="Notas", max_length=100)
    other_PC_1_notes_right = forms.CharField(label="Notas", max_length=100)
    other_PC_1_name_service = forms.CharField(
        label="Nombre del Servicio", max_length=100
    )

    other_PC_2 = forms.CharField(label="Otros Corporativos", max_length=100)
    other_PC_2_bonds_left = forms.CharField(label="Bonos", max_length=100)
    other_PC_2_bonds_right = forms.CharField(label="Bonos", max_length=100)
    other_PC_2_notes_left = forms.CharField(label="Notas", max_length=100)
    other_PC_2_notes_right = forms.CharField(label="Notas", max_length=100)
    other_PC_2_name_service = forms.CharField(
        label="Nombre del Servicio", max_length=100
    )

    GNMA_bonds_left = forms.CharField(label="Bonos de la GNMA", max_length=100)
    GNMA_bonds_right = forms.CharField(label="Bonos de la GNMA", max_length=100)
    GNMA_notes_left = forms.CharField(label="Notas de la GNMA", max_length=100)
    GNMA_notes_right = forms.CharField(label="Notas de la GNMA", max_length=100)
    GNMA_name_service = forms.CharField(label="Nombre del Servicio", max_length=100)

    other5 = forms.CharField(label="Otros", max_length=100)
    other5_bonds_left = forms.CharField(label="Otros", max_length=100)
    other5_bonds_right = forms.CharField(label="Otros", max_length=100)
    other5_notes_left = forms.CharField(label="Otros", max_length=100)
    other5_notes_right = forms.CharField(label="Otros", max_length=100)
    other5_name_service = forms.CharField(label="Nombre del Servicio", max_length=100)

    signature = forms.CharField(
        label="Name of person filling the questionnaire", max_length=100
    )
    position = forms.CharField(label="Position", max_length=100)
    date = forms.CharField(label="Date", max_length=100)
    phone = forms.CharField(label="Phone Number", max_length=100)


class JP_560_63110(forms.Forms):
    ssn = forms.CharField(label="Social Security Number", max_length=100)
    tel = forms.CharField(label="Telephone Number", max_length=100)
    fax = forms.CharField(label="Fax Number", max_length=100)
    sales_1 = forms.CharField(label="Sales", max_length=100)
    sales_2 = forms.CharField(label="Sales", max_length=100)
    disability_1 = forms.CharField(label="Disability", max_length=100)
    disability_2 = forms.CharField(label="Disability", max_length=100)
    life_1 = forms.CharField(label="Life", max_length=100)
    life_2 = forms.CharField(label="Life", max_length=100)
    interest_1 = forms.CharField(label="Interest", max_length=100)
    interest_2 = forms.CharField(label="Interest", max_length=100)
    other_income_1 = forms.CharField(label="Other Income", max_length=100)
    other_income_2 = forms.CharField(label="Other Income", max_length=100)
    total_income_1 = forms.CharField(label="Total Income", max_length=100)
    total_income_2 = forms.CharField(label="Total Income", max_length=100)
    interest_paid_1 = forms.CharField(label="Interest Paid", max_length=100)
    interest_paid_2 = forms.CharField(label="Interest Paid", max_length=100)
    disability_paid_1 = forms.CharField(label="Disability Paid", max_length=100)
    disability_paid_2 = forms.CharField(label="Disability Paid", max_length=100)
    life_paid_1 = forms.CharField(label="Life Paid", max_length=100)
    life_paid_2 = forms.CharField(label="Life Paid", max_length=100)
    other_expenditures_1 = forms.CharField(label="Other Expenditures", max_length=100)
    other_expenditures_2 = forms.CharField(label="Other Expenditures", max_length=100)
    total_expenditures_1 = forms.CharField(label="Total Expenditures", max_length=100)
    total_expenditures_2 = forms.CharField(label="Total Expenditures", max_length=100)
    net_profit_1 = forms.CharField(label="Net Profit", max_length=100)
    net_profit_2 = forms.CharField(label="Net Profit", max_length=100)
    initial_inventory_1 = forms.CharField(label="Initial Inventory", max_length=100)
    initial_inventory_2 = forms.CharField(label="Initial Inventory", max_length=100)
    final_inventory_1 = forms.CharField(label="Final Inventory", max_length=100)
    final_inventory_2 = forms.CharField(label="Final Inventory", max_length=100)
    signature = forms.CharField(
        label="Name of person filling the questionnaire", max_length=100
    )
    rank = forms.CharField(label="Rank", max_length=100)


class IP_210(forms.Form):
    company_name = forms.CharField(
        label="Nombre compañía / Company Name", max_length=100
    )
    address = forms.CharField(label="Dirección / Address", max_length=200)
    email = forms.EmailField(label="Correo electrónico / Email")
    liaison_officer = forms.CharField(
        label="Persona contacto / Liaison officer", max_length=100
    )
    ssn = forms.CharField(
        label="Numero de Seguro Social / Social Security Number", max_length=11
    )
    tel = forms.CharField(label="Tel", max_length=20)
    fax = forms.CharField(label="Fax", max_length=20)
    legal_form = forms.ChoiceField(
        label="Forma legal de organización / Legal form of organization",
        choices=[
            ("Corporación", "Corporación"),
            ("Sociedad", "Sociedad"),
            ("Cooperativa", "Cooperativa"),
            ("Empresa Individual", "Empresa Individual"),
            ("Empresa sin fines pecuniarios", "Empresa sin fines pecuniarios"),
        ],
    )
    cfc = forms.ChoiceField(label="CEC", choices=[("Si", "Si"), ("No", "No")])
    business_type = forms.CharField(
        label="Clase de negocio / Type of business", max_length=200
    )
    business_function = forms.CharField(
        label="Describa brevemente la función principal del negocio / Explain briefly the main function of the business activity",
        widget=forms.Textarea,
    )
    branches = forms.ChoiceField(
        label="¿Opera sucursuales esta firma? / Do you have branch operations?",
        choices=[("Si", "Si"), ("No", "No")],
    )
    closing_date = forms.DateField(
        label="Fecha de cierre de sus libros / Your accounting period closing date",
        widget=forms.SelectDateWidget,
    )
    start_year = forms.CharField(
        label="Año de inicio de operaciones / Year of start of operations",
        max_length=100,
    )
    end_year = forms.CharField(
        label="Año de cierre de operaciones / Year of end of operations", max_length=100
    )
    income_operations_12 = (
        forms.CharField(label="1. Ingresos por operaciones - Income from operations"),
    )
    income_operations_13 = (
        forms.CharField(label="1. Ingresos por operaciones - Income from operations"),
    )
    income_interests_12 = (forms.CharField(label="2. Interese - Interests"),)
    income_interests_13 = (forms.CharField(label="2. Interese - Interests"),)
    incomes_rents_12 = (forms.CharField(label="3. Alquileres - From rents"),)
    incomes_rents_13 = (forms.CharField(label="3. Alquileres - From rents"),)
    income_rent_land_12 = (
        forms.CharField(
            label="4. Ganancia o pérdida de capital - Rent of land and building"
        ),
    )
    income_rent_land_13 = (
        forms.CharField(
            label="4. Ganancia o pérdida de capital - Rent of land and building"
        ),
    )
    other_income_12 = (forms.CharField(label="5. Otros ingresos - Other income"),)
    other_income_13 = (forms.CharField(label="5. Otros ingresos - Other income"),)
    total_incomes_12 = (forms.CharField(label="6. Total de ingresos - Other income"),)
    total_incomes_13 = (forms.CharField(label="6. Total de ingresos - Other income"),)
    total_income_12 = (forms.CharField(label="7. Total de ingresos - Total income"),)
    total_income_13 = (forms.CharField(label="7. Total de ingresos - Total income"),)
    expenses_2012 = (forms.CharField(label="B. Gastos - Expenses"),)
    expenses_2012 = (forms.CharField(label="B. Gastos - Expenses"),)
    salaries_2012 = (
        forms.CharField(
            label="1. Salarios, jornales, bono de Navidad y comisiones - Salaries, wages, Christmas bonus, and commissions"
        ),
    )
    salaries_2013 = (
        forms.CharField(
            label="1. Salarios, jornales, bono de Navidad y comisiones - Salaries, wages, Christmas bonus, and commissions"
        ),
    )
    expenses_interests_12 = (forms.CharField(label="2. Intereses - Interests"),)
    expenses_interests_13 = (forms.CharField(label="2. Intereses - Interests"),)
    depreciation_12 = (forms.CharField(label="3. Depreciación - Depreciation"),)
    depreciation_13 = (forms.CharField(label="3. Depreciación - Depreciation"),)
    expenses_rent_12 = (
        forms.CharField(
            label="4. Renta de terreno y edificio - Rent of land and building"
        ),
    )
    expenses_rent_13 = (
        forms.CharField(
            label="4. Renta de terreno y edificio - Rent of land and building"
        ),
    )
    bad_debts_12 = (forms.CharField(label="5. Cuentas incobrables - Bad debts"),)
    bad_debts_13 = (forms.CharField(label="5. Cuentas incobrables - Bad debts"),)
    donations_12 = (forms.CharField(label="6. Donativos - Donations"),)
    donations_13 = (forms.CharField(label="6. Donativos - Donations"),)
    sales_tax_12 = (
        forms.CharField(label="7. Impuesto sobre la venta y uso - sales and use tax"),
    )
    sales_tax_13 = (
        forms.CharField(label="7. Impuesto sobre la venta y uso - sales and use tax"),
    )
    machinery_12 = (
        forms.CharField(
            label="a. Por Compra de maquinaria y equipo - On purchases of machinery and equipment"
        ),
    )
    machinery_13 = (
        forms.CharField(
            label="a. Por Compra de maquinaria y equipo - On purchases of machinery and equipment"
        ),
    )
    other_purchases_12 = (
        forms.CharField(label="b. Por otras compras - On other purchases"),
    )
    other_purchases_13 = (
        forms.CharField(label="b. Por otras compras - On other purchases"),
    )
    licenses_12 = (
        forms.CharField(label="8. Licencias y patentes - Licenses and patents"),
    )
    licenses_13 = (
        forms.CharField(label="8. Licencias y patentes - Licenses and patents"),
    )
    other_expenses_12 = (
        forms.CharField(
            label="9. Otros gastos de operación - Other operating expenses"
        ),
    )
    other_expenses_13 = (
        forms.CharField(
            label="9. Otros gastos de operación - Other operating expenses"
        ),
    )
    total_expenses_12 = (forms.CharField(label="10. Total de gastos - Total expenses"),)
    total_expenses_13 = (forms.CharField(label="10. Total de gastos - Total expenses"),)
    net_profit_12 = (
        forms.CharField(
            label="C. Ganancia o pérdida neta ( + ó - ) - Net profit or loss ( + or - )"
        ),
    )
    net_profit_13 = (
        forms.CharField(
            label="C. Ganancia o pérdida neta ( + ó - ) - Net profit or loss ( + or - )"
        ),
    )
    income_tax_12 = (
        forms.CharField(label="1. Contribución sobre ingresos - Income tax"),
    )
    income_tax_13 = (
        forms.CharField(label="1. Contribución sobre ingresos - Income tax"),
    )
    profit_after_tax_12 = (
        forms.CharField(
            label="2. Ganancia después de contribución sobre ingresos - Profit after income tax"
        ),
    )
    profit_after_tax_13 = (
        forms.CharField(
            label="2. Ganancia después de contribución sobre ingresos - Profit after income tax"
        ),
    )
    withheld_tax_12 = (
        forms.CharField(
            label="D. Impuesto sobre ventas y uso retenido - Sales and use tax Withheld"
        ),
    )
    withheld_tax_13 = (
        forms.CharField(
            label="D. Impuesto sobre ventas y uso retenido - Sales and use tax Withheld"
        ),
    )
    signature = forms.CharField(
        label="Nombre de persona que suministra la información - Name of person furnishing information",
        max_length=100,
    )
    rank = forms.CharField(label="Rango - Title")


class IP_220(forms.Form):
    company_name = forms.CharField(
        label="Nombre compañía / Company Name", max_length=100
    )
    address = forms.CharField(label="Dirección / Address", max_length=200)
    email = forms.EmailField(label="Correo electrónico / Email")
    liaison_officer = forms.CharField(
        label="Persona contacto / Liaison officer", max_length=100
    )
    ssn = forms.CharField(
        label="Numero de Seguro Social / Social Security Number", max_length=11
    )
    tel = forms.CharField(label="Tel", max_length=20)
    fax = forms.CharField(label="Fax", max_length=20)
    legal_form = forms.ChoiceField(
        label="Forma legal de organización / Legal form of organization",
        choices=[
            ("Corporación", "Corporación"),
            ("Sociedad", "Sociedad"),
            ("Cooperativa", "Cooperativa"),
            ("Empresa Individual", "Empresa Individual"),
            ("Empresa sin fines pecuniarios", "Empresa sin fines pecuniarios"),
        ],
    )
    cfc = forms.ChoiceField(label="CEC", choices=[("Si", "Si"), ("No", "No")])
    business_type = forms.CharField(
        label="Clase de negocio / Type of business", max_length=200
    )
    business_function = forms.CharField(
        label="Describa brevemente la función principal del negocio / Explain briefly the main function of the business activity",
        widget=forms.Textarea,
    )
    branches = forms.ChoiceField(
        label="¿Opera sucursuales esta firma? / Do you have branch operations?",
        choices=[("Si", "Si"), ("No", "No")],
    )
    branches_yes = forms.ChoiceField(
        label="afirmativo a branches",
        choices=[
            ("todas las sucursales", "todas las sucursales"),
            ("este establecimiento", "este establecimiento"),
        ],
    )
    closing_date = forms.DateField(
        label="Fecha de cierre de sus libros / Your accounting period closing date",
        widget=forms.SelectDateWidget,
    )
    start_year = forms.CharField(
        label="Año de inicio de operaciones / Year of start of operations",
        max_length=100,
    )
    end_year = forms.CharField(
        label="Año de cierre de operaciones / Year of end of operations", max_length=100
    )
    services_revenues_12 = (
        forms.CharField(label="Ingresos por servicios - Services rendered"),
    )
    services_revenues_13 = (
        forms.CharField(label="Ingresos por servicios - Services rendered"),
    )
    residential_consumers_12 = (
        forms.CharField(label="a. Abonados residenciales - Residential consumers"),
    )
    residential_consumers_13 = (
        forms.CharField(
            label="a. A industrias y negocios - To industries and businesses"
        ),
    )
    other_consumers_12 = (forms.CharField(label="b. Otros abonados - Other consumers"),)
    other_consumers_13 = (forms.CharField(label="b. A personas - To persons"),)
    sales_12 = (forms.CharField(label="2. Ventas - From sale of merchandise"),)
    sales_13 = (forms.CharField(label="2. Ventas - From sale of merchandise"),)
    incomes_rents_12 = (forms.CharField(label="3. Alquileres - From rents"),)
    incomes_rents_13 = (forms.CharField(label="3. Alquileres - From rents"),)
    incomes_interests_12 = (forms.CharField(label="4. Intereses - Interests"),)
    incomes_interests_13 = (forms.CharField(label="4. Intereses - Interests"),)
    dividends_12 = (
        forms.CharField(
            label="5. Ganancia o pérdida de capital - Capital gain or loss"
        ),
    )
    dividends_13 = (
        forms.CharField(
            label="5. Ganancia o pérdida de capital - Capital gain or loss"
        ),
    )
    others_incomes_12 = (
        forms.CharField(
            label="6. Otros ingresos de operación - Other operating income"
        ),
    )
    others_incomes_13 = (
        forms.CharField(
            label="6. Otros ingresos de operación - Other operating income"
        ),
    )
    total_income_12 = (forms.CharField(label="7. Total de ingresos - Total income"),)
    total_income_13 = (forms.CharField(label="7. Total de ingresos - Total income"),)
    salaries_2012 = (
        forms.CharField(
            label="1. Salarios, jornales, bono de Navidad y comisiones - Salaries, wages, Christmas bonus, and commissions"
        ),
    )
    salaries_2013 = (
        forms.CharField(
            label="1. Salarios, jornales, bono de Navidad y comisiones - Salaries, wages, Christmas bonus, and commissions"
        ),
    )
    expenses_interests_12 = (forms.CharField(label="2. Intereses - Interests"),)
    expenses_interests_13 = (forms.CharField(label="2. Intereses - Interests"),)
    expenses_rents_12 = (
        forms.CharField(
            label="3. Renta de terreno y edificio - Rent of land and building"
        ),
    )
    expenses_rents_13 = (
        forms.CharField(
            label="3. Renta de terreno y edificio - Rent of land and building"
        ),
    )
    depreciation_12 = (forms.CharField(label="4. Depreciación - Depreciation"),)
    depreciation_13 = (forms.CharField(label="4. Depreciación - Depreciation"),)
    bad_debts_12 = (forms.CharField(label="5. Cuentas incobrables - Bad debts"),)
    bad_debts_13 = (forms.CharField(label="5. Cuentas incobrables - Bad debts"),)
    donations_12 = (forms.CharField(label="6. Donativos - Donations"),)
    donations_13 = (forms.CharField(label="6. Donativos - Donations"),)
    sales_tax_12 = (
        forms.CharField(label="7. Impuesto sobre la venta y uso - sales and use tax"),
    )
    sales_tax_13 = (
        forms.CharField(label="7. Impuesto sobre la venta y uso - sales and use tax"),
    )
    machinery_12 = (
        forms.CharField(
            label="a. Por Compra de maquinaria y equipo - On purchases of machinery and equipment"
        ),
    )
    machinery_13 = (
        forms.CharField(
            label="a. Por Compra de maquinaria y equipo - On purchases of machinery and equipment"
        ),
    )
    other_purchases_12 = (
        forms.CharField(label="b. Por otras compras - On other purchases"),
    )
    other_purchases_13 = (
        forms.CharField(label="b. Por otras compras - On other purchases"),
    )
    licenses_12 = (
        forms.CharField(label="8. Licencias y patentes - Licenses and patents"),
    )
    licenses_13 = (
        forms.CharField(label="8. Licencias y patentes - Licenses and patents"),
    )
    other_expenses_12 = (
        forms.CharField(
            label="9. Otros gastos de operación - Other operating expenses"
        ),
    )
    other_expenses_13 = (
        forms.CharField(
            label="9. Otros gastos de operación - Other operating expenses"
        ),
    )
    total_expenses_12 = (forms.CharField(label="10. Total de gastos - Total expenses"),)
    total_expenses_13 = (forms.CharField(label="10. Total de gastos - Total expenses"),)
    net_profit_12 = (
        forms.CharField(
            label="C. Ganancia o pérdida neta ( + ó - ) - Net profit or loss ( + or - )"
        ),
    )
    net_profit_13 = (
        forms.CharField(
            label="C. Ganancia o pérdida neta ( + ó - ) - Net profit or loss ( + or - )"
        ),
    )
    income_tax_12 = (
        forms.CharField(label="1. Contribución sobre ingresos - Income tax"),
    )
    income_tax_13 = (
        forms.CharField(label="1. Contribución sobre ingresos - Income tax"),
    )
    profit_after_tax_12 = (
        forms.CharField(
            label="2. Ganancia después de contribución sobre ingresos - Profit after income tax"
        ),
    )
    profit_after_tax_13 = (
        forms.CharField(
            label="2. Ganancia después de contribución sobre ingresos - Profit after income tax"
        ),
    )
    withheld_tax_12 = (
        forms.CharField(
            label="D. Impuesto sobre ventas y uso retenido - Sales and use tax Withheld"
        ),
    )
    withheld_tax_13 = (
        forms.CharField(
            label="D. Impuesto sobre ventas y uso retenido - Sales and use tax Withheld"
        ),
    )
    signature = forms.CharField(
        label="Nombre de persona que suministra la información - Name of person furnishing information",
        max_length=100,
    )
    rank = forms.CharField(label="Rango - Title")


class JP_560_63111(forms.Form):
    ssn = forms.CharField(label="Social Security Number", max_length=100)
    tel = forms.CharField(label="Telephone Number", max_length=100)
    fax = forms.CharField(label="Fax Number", max_length=100)
    sales_1 = forms.CharField(label="Sales", max_length=100)
    sales_2 = forms.CharField(label="Sales", max_length=100)
    premiums_1 = forms.CharField(label="Premiums", max_length=100)
    premiums_2 = forms.CharField(label="Premiums", max_length=100)
    interest_received_1 = forms.CharField(label="Interest Received", max_length=100)
    interest_received_2 = forms.CharField(label="Interest Received", max_length=100)
    other_income_1 = forms.CharField(label="Other Income", max_length=100)
    other_income_2 = forms.CharField(label="Other Income", max_length=100)
    total_income_1 = forms.CharField(label="Total Income", max_length=100)
    total_income_2 = forms.CharField(label="Total Income", max_length=100)
    interest_paid_1 = forms.CharField(label="Interest Paid", max_length=100)
    interest_paid_2 = forms.CharField(label="Interest Paid", max_length=100)
    claims_paid_1 = forms.CharField(label="Claims Paid", max_length=100)
    claims_paid_2 = forms.CharField(label="Claims Paid", max_length=100)
    other_expenditures_1 = forms.CharField(label="Other Expenditures", max_length=100)
    other_expenditures_2 = forms.CharField(label="Other Expenditures", max_length=100)
    total_expenditures_1 = forms.CharField(label="Total Expenditures", max_length=100)
    total_expenditures_2 = forms.CharField(label="Total Expenditures", max_length=100)
    net_profit_loss_1 = forms.CharField(label="Net Profit/Loss", max_length=100)
    net_profit_loss_2 = forms.CharField(label="Net Profit/Loss", max_length=100)
    initial_inventory_1 = forms.CharField(label="Initial Inventory", max_length=100)
    initial_inventory_2 = forms.CharField(label="Initial Inventory", max_length=100)
    final_inventory_1 = forms.CharField(label="Final Inventory", max_length=100)
    final_inventory_2 = forms.CharField(label="Final Inventory", max_length=100)
    signature = forms.CharField(
        label="Name of person filling the questionnaire", max_length=100
    )


class IP_230(forms.Form):
    company_name = forms.CharField(
        label="Nombre compañía / Company Name", max_length=100
    )
    address = forms.CharField(label="Dirección / Address", max_length=200)
    email = forms.EmailField(label="Correo electrónico / Email")
    liaison_officer = forms.CharField(
        label="Persona contacto / Liaison officer", max_length=100
    )
    ssn = forms.CharField(
        label="Numero de Seguro Social / Social Security Number", max_length=11
    )
    tel = forms.CharField(label="Tel", max_length=20)
    fax = forms.CharField(label="Fax", max_length=20)
    legal_form = forms.ChoiceField(
        label="Forma legal de organización / Legal form of organization",
        choices=[
            ("Corporación", "Corporación"),
            ("Sociedad", "Sociedad"),
            ("Cooperativa", "Cooperativa"),
            ("Empresa Individual", "Empresa Individual"),
            ("Empresa sin fines pecuniarios", "Empresa sin fines pecuniarios"),
        ],
    )
    cfc = forms.ChoiceField(label="CEC", choices=[("Si", "Si"), ("No", "No")])
    business_function = forms.CharField(
        label="Describa brevemente la función principal del negocio / Explain briefly the main function of the business activity",
        widget=forms.Textarea,
    )
    closing_date = forms.DateField(
        label="Fecha de cierre de sus libros / Your accounting period closing date",
        widget=forms.SelectDateWidget,
    )
    start_year = forms.CharField(
        label="Año de inicio de operaciones / Year of start of operations",
        max_length=100,
    )
    end_year = forms.CharField(
        label="Año de cierre de operaciones / Year of end of operations", max_length=100
    )
    income_project_A_12 = (
        forms.CharField(label="1. Ingresos por proyecto - Income from project"),
    )
    income_project_A_13 = (
        forms.CharField(label="1. Ingresos por proyecto - Income from project"),
    )
    people_A_12 = (forms.CharField(label="2. A personas - To persons"),)
    people_A_13 = (forms.CharField(label="2. A personas - To persons"),)
    industries_businesses_A_12 = (
        forms.CharField(
            label="3. A industrias y negocios - To industries and businesses"
        ),
    )
    industries_businesses_A_13 = (
        forms.CharField(
            label="3. A industrias y negocios - To industries and businesses"
        ),
    )
    direct_indirect_B_12 = (
        forms.CharField(
            label="4. Costos directos e indirectos - Direct and indirect costs"
        ),
    )
    direct_indirect_B_13 = (
        forms.CharField(
            label="4. Costos directos e indirectos - Direct and indirect costs"
        ),
    )
    direct_christmas_vacation_B_12 = (
        forms.CharField(
            label="a. Por bono de Navidad y vacaciones - On Christmas bonus and vacation"
        ),
    )
    direct_christmas_vacation_B_13 = (
        forms.CharField(
            label="a. Por bono de Navidad y vacaciones - On Christmas bonus and vacation"
        ),
    )
    rent_land_building_B_12 = (
        forms.CharField(
            label="b. Por renta de terreno y edificio - On rent of land and building"
        ),
    )
    rent_land_building_B_13 = (
        forms.CharField(
            label="b. Por renta de terreno y edificio - On rent of land and building"
        ),
    )
    rent_equipment_B_12 = (
        forms.CharField(label="c. Por renta de equipo - On rent of equipment"),
    )
    rent_equipment_B_13 = (
        forms.CharField(label="c. Por renta de equipo - On rent of equipment"),
    )
    depreciation_B_12 = (
        forms.CharField(label="d. Por depreciación - On depreciation"),
    )
    depreciation_B_13 = (
        forms.CharField(label="d. Por depreciación - On depreciation"),
    )
    sales_tax_B_12 = (
        forms.CharField(
            label="e. Por impuesto sobre la venta y uso - On sales and use tax"
        ),
    )
    sales_tax_B_13 = (
        forms.CharField(
            label="e. Por impuesto sobre la venta y uso - On sales and use tax"
        ),
    )
    purchases_machinery_equipment_B_12 = (
        forms.CharField(
            label="f. Por compra de maquinaria y equipo - On purchases of machinery and equipment"
        ),
    )
    purchases_machinery_equipment_B_13 = (
        forms.CharField(
            label="f. Por compra de maquinaria y equipo - On purchases of machinery and equipment"
        ),
    )
    other_purchases_B_12 = (
        forms.CharField(label="g. Por otras compras - On other purchases"),
    )
    other_purchases_B_13 = (
        forms.CharField(label="g. Por otras compras - On other purchases"),
    )
    licenses_patent_B_12 = (
        forms.CharField(label="h. Por licencias y patentes - On licenses and patents"),
    )
    licenses_patent_B_13 = (
        forms.CharField(label="h. Por licencias y patentes - On licenses and patents"),
    )
    other_costs_direct_indirect_B_12 = (
        forms.CharField(
            label="i. Otros costos directos e indirectos - Other direct and indirect costs"
        ),
    )
    other_costs_direct_indirect_B_13 = (
        forms.CharField(
            label="i. Otros costos directos e indirectos - Other direct and indirect costs"
        ),
    )
    gross_profit_C_12 = (forms.CharField(label="5. Utilidad bruta - Gross profit"),)
    gross_profit_C_13 = (forms.CharField(label="5. Utilidad bruta - Gross profit"),)
    other_income_D_12 = (forms.CharField(label="6. Otros ingresos - Other income"),)
    other_income_D_13 = (forms.CharField(label="6. Otros ingresos - Other income"),)
    interest_D_12 = (forms.CharField(label="7. Intereses - Interests"),)
    interest_D_13 = (forms.CharField(label="7. Intereses - Interests"),)
    rent_land_building_D_12 = (
        forms.CharField(
            label="8. Renta de terreno y edificio - Rent of land and building"
        ),
    )
    rent_land_building_D_13 = (
        forms.CharField(
            label="8. Renta de terreno y edificio - Rent of land and building"
        ),
    )
    gain_loss_D_12 = (
        forms.CharField(
            label="9. Ganancia o pérdida de capital - Capital gain or loss"
        ),
    )
    gain_loss_D_13 = (
        forms.CharField(
            label="9. Ganancia o pérdida de capital - Capital gain or loss"
        ),
    )
    other_D_12 = (forms.CharField(label="10. Otros - Other"),)
    other_D_13 = (forms.CharField(label="10. Otros - Other"),)
    gross_profit_E_12 = (forms.CharField(label="11. Utilidad bruta - Gross profit"),)
    gross_profit_E_13 = (forms.CharField(label="11. Utilidad bruta - Gross profit"),)
    administrative_F_12 = (
        forms.CharField(label="1. Gastos administrativos - Administrative expenses"),
    )
    administrative_F_13 = (
        forms.CharField(label="1. Gastos administrativos - Administrative expenses"),
    )
    salaries_wages_bonus_commissions_F_12 = (
        forms.CharField(
            label="2. Salarios, jornales, bono de Navidad y comisiones - Salaries, wages, Christmas bonus, and commissions"
        ),
    )
    salaries_wages_bonus_commissions_F_13 = (
        forms.CharField(
            label="2. Salarios, jornales, bono de Navidad y comisiones - Salaries, wages, Christmas bonus, and commissions"
        ),
    )
    interest_F_12 = (forms.CharField(label="3. Intereses - Interests"),)
    interest_F_13 = (forms.CharField(label="3. Intereses - Interests"),)
    rent_land_building_F_12 = (
        forms.CharField(
            label="4. Renta de terreno y edificio - Rent of land and building"
        ),
    )
    rent_land_building_F_13 = (
        forms.CharField(
            label="4. Renta de terreno y edificio - Rent of land and building"
        ),
    )
    depreciation_F_12 = (forms.CharField(label="5. Depreciación - Depreciation"),)
    depreciation_F_13 = (forms.CharField(label="5. Depreciación - Depreciation"),)
    bad_depts_F_12 = (forms.CharField(label="6. Cuentas incobrables - Bad debts"),)
    bad_depts_F_13 = (forms.CharField(label="6. Cuentas incobrables - Bad debts"),)
    donation_F_12 = (forms.CharField(label="7. Donativos - Donations"),)
    donation_F_13 = (forms.CharField(label="7. Donativos - Donations"),)
    other_expenses_F_12 = (forms.CharField(label="8. Otros gastos - Other expenses"),)
    other_expenses_F_13 = (forms.CharField(label="8. Otros gastos - Other expenses"),)
    net_profit_G_12 = (
        forms.CharField(
            label="9. Ganancia o pérdida neta ( + ó - ) - Net profit or loss ( + or - )"
        ),
    )
    net_profit_G_13 = (
        forms.CharField(
            label="9. Ganancia o pérdida neta ( + ó - ) - Net profit or loss ( + or - )"
        ),
    )
    income_tax_G_12 = (
        forms.CharField(label="1. Contribución sobre ingresos - Income tax"),
    )
    income_tax_G_13 = (
        forms.CharField(label="1. Contribución sobre ingresos - Income tax"),
    )
    profit_after_tax_G_12 = (
        forms.CharField(
            label="2. Ganancia después de contribución sobre ingresos - Profit after income tax"
        ),
    )
    profit_after_tax_G_13 = (
        forms.CharField(
            label="2. Ganancia después de contribución sobre ingresos - Profit after income tax"
        ),
    )
    sales_tax_H_12 = (
        forms.CharField(label="3. Impuesto sobre la venta y uso - sales and use tax"),
    )
    sales_tax_H_13 = (
        forms.CharField(label="3. Impuesto sobre la venta y uso - sales and use tax"),
    )
    biginning_year_HA = forms.CharField(label="Año Inicial", max_length=100)
    end_year_HB = forms.CharField(label="Año Final", max_length=100)
    biginning_year_HC = forms.CharField(label="Año Inicial", max_length=100)
    end_year_HD = forms.CharField(label="Año Final", max_length=100)
    signature = forms.CharField(
        label="Name of person filling the questionnaire", max_length=100
    )
    rank = forms.CharField(label="Rank", max_length=100)


class JP_560_63210(forms.Form):
    ssn = forms.CharField(label="Social Security Number", max_length=100)
    tel = forms.CharField(label="Telephone Number", max_length=100)
    fax = forms.CharField(label="Fax Number", max_length=100)
    sales_1 = forms.CharField(label="Sales", max_length=100)
    sales_2 = forms.CharField(label="Sales", max_length=100)
    premiums_1 = forms.CharField(label="Premiums", max_length=100)
    premiums_2 = forms.CharField(label="Premiums", max_length=100)
    disability_A_1 = forms.CharField(label="Disability", max_length=100)
    disability_A_2 = forms.CharField(label="Disability", max_length=100)
    cars_A_1 = forms.CharField(label="Cars", max_length=100)
    cars_A_2 = forms.CharField(label="Cars", max_length=100)
    other_A_1 = forms.CharField(label="Other", max_length=100)
    other_A_2 = forms.CharField(label="Other", max_length=100)
    interest_received_1 = forms.CharField(label="Interest Received", max_length=100)
    interest_received_2 = forms.CharField(label="Interest Received", max_length=100)
    other_income_1 = forms.CharField(label="Other Income", max_length=100)
    other_income_2 = forms.CharField(label="Other Income", max_length=100)
    total_income_1 = forms.CharField(label="Total Income", max_length=100)
    total_income_2 = forms.CharField(label="Total Income", max_length=100)
    interest_paid_1 = forms.CharField(label="Interest Paid", max_length=100)
    interest_paid_2 = forms.CharField(label="Interest Paid", max_length=100)
    claims_paid_1 = forms.CharField(label="Claims Paid", max_length=100)
    claims_paid_2 = forms.CharField(label="Claims Paid", max_length=100)
    disability_B_1 = forms.CharField(label="Disability", max_length=100)
    disability_B_2 = forms.CharField(label="Disability", max_length=100)
    cars_B_1 = forms.CharField(label="Cars", max_length=100)
    cars_B_2 = forms.CharField(label="Cars", max_length=100)
    other_B_1 = forms.CharField(label="Other", max_length=100)
    other_B_2 = forms.CharField(label="Other", max_length=100)
    other_expenditures_1 = forms.CharField(label="Other Expenditures", max_length=100)
    other_expenditures_2 = forms.CharField(label="Other Expenditures", max_length=100)
    total_expenditures_1 = forms.CharField(label="Total Expenditures", max_length=100)
    total_expenditures_2 = forms.CharField(label="Total Expenditures", max_length=100)
    net_profit_loss_1 = forms.CharField(label="Net Profit/Loss", max_length=100)
    net_profit_loss_2 = forms.CharField(label="Net Profit/Loss", max_length=100)
    initial_inventory_1 = forms.CharField(label="Initial Inventory", max_length=100)
    initial_inventory_2 = forms.CharField(label="Initial Inventory", max_length=100)
    final_inventory_1 = forms.CharField(label="Final Inventory", max_length=100)
    final_inventory_2 = forms.CharField(label="Final Inventory", max_length=100)
    signature = forms.CharField(
        label="Name of person filling the questionnaire", max_length=100
    )
    rank = forms.CharField(label="Rank", max_length=100)


class JP_362(forms.Form):
    year_1 = forms.CharField(label="Año / Year", max_length=100)
    year_2 = forms.CharField(label="Año / Year", max_length=100)

    company_name = forms.CharField(label="Nombre de Empresa Pública", max_length=100)

    debts_balance = forms.CharField(
        label="1. Deudas en el Exterios De Largo Plazo, Total", max_length=100
    )
    debts_emision = forms.CharField(
        label="1. Deudas en el Exterios De Largo Plazo, Emisión", max_length=100
    )
    debts_amortizacion = forms.CharField(
        label="1. Deudas en el Exterios De Largo Plazo, Amortización", max_length=100
    )
    debts_final = forms.CharField(
        label="1. Deudas en el Exterios De Largo Plazo, Final", max_length=100
    )
    debts_interes = forms.CharField(
        label="1. Deudas en el Exterios De Largo Plazo, Interés", max_length=100
    )
    debts_acreedor = forms.CharField(
        label="1. Deudas en el Exterios De Largo Plazo, Acreedor", max_length=100
    )

    debts_bond_balance = forms.CharField(label="Bonos, Valor Par", max_length=100)
    debts_bond_emision = forms.CharField(label="Bonos, Valor Par", max_length=100)
    debts_bond_amortizacion = forms.CharField(label="Bonos, Valor Par", max_length=100)
    debts_bond_final = forms.CharField(label="Bonos, Valor Par", max_length=100)
    debts_bond_interes = forms.CharField(label="Bonos, Valor Par", max_length=100)
    debts_bond_acreedor = forms.CharField(label="Bonos, Valor Par", max_length=100)

    debts_promossory_notes_balance = forms.CharField(
        label="Pagarés, Valor Par", max_length=100
    )
    debts_promossory_notes_emision = forms.CharField(
        label="Pagarés, Valor Par", max_length=100
    )
    debts_promossory_notes_amortizacion = forms.CharField(
        label="Pagarés, Valor Par", max_length=100
    )
    debts_promossory_notes_final = forms.CharField(
        label="Pagarés, Valor Par", max_length=100
    )
    debts_promossory_notes_interes = forms.CharField(
        label="Pagarés, Valor Par", max_length=100
    )
    debts_promossory_notes_acreedor = forms.CharField(
        label="Pagarés, Valor Par", max_length=100
    )

    debts_others_balance = forms.CharField(label="Otras (especifique)", max_length=100)
    debts_others_emision = forms.CharField(label="Otras (especifique)", max_length=100)
    debts_others_amortizacion = forms.CharField(
        label="Otras (especifique)", max_length=100
    )
    debts_others_final = forms.CharField(label="Otras (especifique)", max_length=100)
    debts_others_interes = forms.CharField(label="Otras (especifique)", max_length=100)
    debts_others_acreedor = forms.CharField(label="Otras (especifique)", max_length=100)

    short_promossory_balance = forms.CharField(
        label="Pagarés, Valor Par", max_length=100
    )
    short_promossory_emision = forms.CharField(
        label="Pagarés, Valor Par", max_length=100
    )
    short_promossory_amortizacion = forms.CharField(
        label="Pagarés, Valor Par", max_length=100
    )
    short_promossory_final = forms.CharField(label="Pagarés, Valor Par", max_length=100)
    short_promossory_interes = forms.CharField(
        label="Pagarés, Valor Par", max_length=100
    )
    short_promossory_acreedor = forms.CharField(
        label="Pagarés, Valor Par", max_length=100
    )

    short_account_balance = forms.CharField(label="Cuentas por pagar", max_length=100)
    short_account_emision = forms.CharField(label="Cuentas por pagar", max_length=100)
    short_account_amortizacion = forms.CharField(
        label="Cuentas por pagar", max_length=100
    )
    short_account_final = forms.CharField(label="Cuentas por pagar", max_length=100)
    short_account_interes = forms.CharField(label="Cuentas por pagar", max_length=100)
    short_account_acreedor = forms.CharField(label="Cuentas por pagar", max_length=100)

    short_others_balance = forms.CharField(label="Otras (especifique)", max_length=100)
    short_others_emision = forms.CharField(label="Otras (especifique)", max_length=100)
    short_others_amortizacion = forms.CharField(
        label="Otras (especifique)", max_length=100
    )
    short_others_final = forms.CharField(label="Otras (especifique)", max_length=100)
    short_others_interes = forms.CharField(label="Otras (especifique)", max_length=100)
    short_others_acreedor = forms.CharField(label="Otras (especifique)", max_length=100)

    short_term_balance = forms.CharField(label="De Corto Plazo, Total", max_length=100)
    short_term_emision = forms.CharField(label="De Corto Plazo, Total", max_length=100)
    short_term_amortizacion = forms.CharField(
        label="De Corto Plazo, Total", max_length=100
    )
    short_term_final = forms.CharField(label="De Corto Plazo, Total", max_length=100)
    short_term_interes = forms.CharField(label="De Corto Plazo, Total", max_length=100)
    short_term_acreedor = forms.CharField(label="De Corto Plazo, Total", max_length=100)

    assets_balance = forms.CharField(
        label="2. Activos en el Exterior De Largo Plazo, Total", max_length=100
    )
    assets_emision = forms.CharField(
        label="2. Activos en el Exterior De Largo Plazo, Total", max_length=100
    )
    assets_amortizacion = forms.CharField(
        label="2. Activos en el Exterior De Largo Plazo, Total", max_length=100
    )
    assets_final = forms.CharField(
        label="2. Activos en el Exterior De Largo Plazo, Total", max_length=100
    )
    assets_interes = forms.CharField(
        label="2. Activos en el Exterior De Largo Plazo, Total", max_length=100
    )

    assets_values_balance = forms.CharField(
        label="Valores del Gobierno de E.E.U.U., Valor Par", max_length=100
    )
    assets_values_emision = forms.CharField(
        label="Valores del Gobierno de E.E.U.U., Valor Par", max_length=100
    )
    assets_values_amortizacion = forms.CharField(
        label="Valores del Gobierno de E.E.U.U., Valor Par", max_length=100
    )
    assets_values_final = forms.CharField(
        label="Valores del Gobierno de E.E.U.U., Valor Par", max_length=100
    )
    assets_values_interes = forms.CharField(
        label="Valores del Gobierno de E.E.U.U., Valor Par", max_length=100
    )

    assets_others_balance = forms.CharField(
        label="Otros, Valor Par (especifique)", max_length=100
    )
    assets_others_emision = forms.CharField(
        label="Otros, Valor Par (especifique)", max_length=100
    )
    assets_others_amortizacion = forms.CharField(
        label="Otros, Valor Par (especifique)", max_length=100
    )
    assets_others_final = forms.CharField(
        label="Otros, Valor Par (especifique)", max_length=100
    )
    assets_others_interes = forms.CharField(
        label="Otros, Valor Par (especifique)", max_length=100
    )

    short_balance = forms.CharField(label="De Corto Plazo, Total", max_length=100)
    short_emision = forms.CharField(label="De Corto Plazo, Total", max_length=100)
    short_amortizacion = forms.CharField(label="De Corto Plazo, Total", max_length=100)
    short_final = forms.CharField(label="De Corto Plazo, Total", max_length=100)
    short_interes = forms.CharField(label="De Corto Plazo, Total", max_length=100)

    short_balance_balance = forms.CharField(label="Balances Bancarios", max_length=100)
    short_balance_emision = forms.CharField(label="Balances Bancarios", max_length=100)
    short_balance_amortizacion = forms.CharField(
        label="Balances Bancarios", max_length=100
    )
    short_balance_final = forms.CharField(label="Balances Bancariosl", max_length=100)
    short_balance_interes = forms.CharField(label="Balances Bancarios", max_length=100)

    short_accouts_balance = forms.CharField(label="Cuentas por Cobrar", max_length=100)
    short_accouts_emision = forms.CharField(label="Cuentas por Cobrar", max_length=100)
    short_accouts_amortizacion = forms.CharField(
        label="Cuentas por Cobrar", max_length=100
    )
    short_accouts_final = forms.CharField(label="Cuentas por Cobrar", max_length=100)
    short_accouts_interes = forms.CharField(label="Cuentas por Cobrar", max_length=100)

    short_others_balance_2 = forms.CharField(
        label="Otros (especifique)", max_length=100
    )
    short_others_emision_2 = forms.CharField(
        label="Otros (especifique)", max_length=100
    )
    short_others_amortizacion_2 = forms.CharField(
        label="Otros (especifique)", max_length=100
    )
    short_others_final_2 = forms.CharField(label="Otros (especifique)", max_length=100)
    short_others_interes_2 = forms.CharField(
        label="Otros (especifique)", max_length=100
    )

    signature = forms.CharField(label="Name", max_length=100)
    position = forms.CharField(label="Position", max_length=100)
    date = forms.CharField(label="Date", max_length=100)
    phone = forms.CharField(label="Phone Number", max_length=100)


class JP_560_2(forms.Form):
    company_name = forms.CharField(
        label="Nombre compañía / Company Name", max_length=100
    )
    address = forms.CharField(label="Dirección / Address", max_length=200)
    email = forms.EmailField(label="Correo electrónico / Email")
    liaison_officer = forms.CharField(
        label="Persona contacto / Liaison officer", max_length=100
    )
    ssn = forms.CharField(
        label="Numero de Seguro Social / Social Security Number", max_length=11
    )
    tel = forms.CharField(label="Tel", max_length=20)
    fax = forms.CharField(label="Fax", max_length=20)
    sales_1 = forms.CharField(label="Sales", max_length=100)
    sales_2 = forms.CharField(label="Sales", max_length=100)
    interest_received_1 = forms.CharField(label="Interest Received", max_length=100)
    interest_received_2 = forms.CharField(label="Interest Received", max_length=100)
    other_income_1 = forms.CharField(label="Other Income", max_length=100)
    other_income_2 = forms.CharField(label="Other Income", max_length=100)
    total_income_1 = forms.CharField(label="Total Income", max_length=100)
    total_income_2 = forms.CharField(label="Total Income", max_length=100)
    interest_paid_1 = forms.CharField(label="Interest Paid", max_length=100)
    interest_paid_2 = forms.CharField(label="Interest Paid", max_length=100)
    other_expenditures_1_1 = forms.CharField(label="Other Expenditures", max_length=100)
    other_expenditures_2_1 = forms.CharField(label="Other Expenditures", max_length=100)
    other_expenditures_1_2 = forms.CharField(label="Other Expenditures", max_length=100)
    other_expenditures_2_2 = forms.CharField(label="Other Expenditures", max_length=100)
    net_profit_loss_1 = forms.CharField(label="Net Profit/Loss", max_length=100)
    net_profit_loss_2 = forms.CharField(label="Net Profit/Loss", max_length=100)
    initial_inventory_1 = forms.CharField(label="Initial Inventory", max_length=100)
    initial_inventory_2 = forms.CharField(label="Initial Inventory", max_length=100)
    final_inventory_1 = forms.CharField(label="Final Inventory", max_length=100)
    final_inventory_2 = forms.CharField(label="Final Inventory", max_length=100)
    signature = forms.CharField(
        label="Name of person filling the questionnaire", max_length=100
    )
    rank = forms.CharField(label="Rank", max_length=100)


class JP_364(forms.Form):
    year_bono1 = forms.CharField(label="Año / Year", max_length=100)
    year_bono2 = forms.CharField(label="Año / Year", max_length=100)
    year_paga1 = forms.CharField(label="Año / Year", max_length=100)
    year_paga2 = forms.CharField(label="Año / Year", max_length=100)
    ELA_bono1 = forms.CharField(label="ELA", max_length=100)
    ELA_bono2 = forms.CharField(label="ELA", max_length=100)
    ELA_paga1 = forms.CharField(label="ELA", max_length=100)
    ELA_paga2 = forms.CharField(label="ELA", max_length=100)
    ELA_agente = forms.CharField(label="ELA", max_length=100)
    municipio_bono1 = forms.CharField(label="Municipio", max_length=100)
    municipio_bono2 = forms.CharField(label="Municipio", max_length=100)
    municipio_paga1 = forms.CharField(label="Municipio", max_length=100)
    municipio_paga2 = forms.CharField(label="Municipio", max_length=100)
    municipio_agente = forms.CharField(label="Municipio", max_length=100)
    corp_publicas_bono1 = forms.CharField(
        label="Corporaciones Públicas", max_length=100
    )
    corp_publicas_bono2 = forms.CharField(
        label="Corporaciones Públicas", max_length=100
    )
    corp_publicas_paga1 = forms.CharField(
        label="Corporaciones Públicas", max_length=100
    )
    corp_publicas_paga2 = forms.CharField(
        label="Corporaciones Públicas", max_length=100
    )
    corp_publicas_agente = forms.CharField(
        label="Corporaciones Públicas", max_length=100
    )
    AEE_bono1 = forms.CharField(label="AEE", max_length=100)
    AEE_bono2 = forms.CharField(label="AEE", max_length=100)
    AEE_paga1 = forms.CharField(label="AEE", max_length=100)
    AEE_paga2 = forms.CharField(label="AEE", max_length=100)
    AEE_agente = forms.CharField(label="AEE", max_length=100)
    Acarreteras_bono1 = forms.CharField(label="Acarreteras", max_length=100)
    Acarreteras_bono2 = forms.CharField(label="Acarreteras", max_length=100)
    Acarreteras_paga1 = forms.CharField(label="Acarreteras", max_length=100)
    Acarreteras_paga2 = forms.CharField(label="Acarreteras", max_length=100)
    Acarreteras_agente = forms.CharField(label="Acarreteras", max_length=100)
    AAA_bono1 = forms.CharField(label="AAA", max_length=100)
    AAA_bono2 = forms.CharField(label="AAA", max_length=100)
    AAA_paga1 = forms.CharField(label="AAA", max_length=100)
    AAA_paga2 = forms.CharField(label="AAA", max_length=100)
    AAA_agente = forms.CharField(label="AAA", max_length=100)
    AEP_bono1 = forms.CharField(label="AFA", max_length=100)
    AEP_bono2 = forms.CharField(label="AFA", max_length=100)
    AEP_paga1 = forms.CharField(label="AFA", max_length=100)
    AEP_paga2 = forms.CharField(label="AFA", max_length=100)
    AEP_agente = forms.CharField(label="AFA", max_length=100)
    AP_bono1 = forms.CharField(label="AP", max_length=100)
    AP_bono2 = forms.CharField(label="AP", max_length=100)
    AP_paga1 = forms.CharField(label="AP", max_length=100)
    AP_paga2 = forms.CharField(label="AP", max_length=100)
    AP_agente = forms.CharField(label="AP", max_length=100)
    AT_bono1 = forms.CharField(label="AT", max_length=100)
    AT_bono2 = forms.CharField(label="AT", max_length=100)
    AT_paga1 = forms.CharField(label="AT", max_length=100)
    AT_paga2 = forms.CharField(label="AT", max_length=100)
    AT_agente = forms.CharField(label="AT", max_length=100)
    CFI_bono1 = forms.CharField(label="CFI", max_length=100)
    CFI_bono2 = forms.CharField(label="CFI", max_length=100)
    CFI_paga1 = forms.CharField(label="CFI", max_length=100)
    CFI_paga2 = forms.CharField(label="CFI", max_length=100)
    CFI_agente = forms.CharField(label="CFI", max_length=100)
    BGF_bono1 = forms.CharField(label="BGF", max_length=100)
    BGF_bono2 = forms.CharField(label="BGF", max_length=100)
    BGF_paga1 = forms.CharField(label="BGF", max_length=100)
    BGF_paga2 = forms.CharField(label="BGF", max_length=100)
    BGF_agente = forms.CharField(label="BGF", max_length=100)
    CFV_bono1 = forms.CharField(label="CFV", max_length=100)
    CFV_bono2 = forms.CharField(label="CFV", max_length=100)
    CFV_paga1 = forms.CharField(label="CFV", max_length=100)
    CFV_paga2 = forms.CharField(label="CFV", max_length=100)
    CFV_agente = forms.CharField(label="CFV", max_length=100)
    otherk_title = forms.CharField(label="Otros", max_length=100)
    otherk_bono1 = forms.CharField(label="Otros", max_length=100)
    otherk_bono2 = forms.CharField(label="Otros", max_length=100)
    otherk_paga1 = forms.CharField(label="Otros", max_length=100)
    otherk_paga2 = forms.CharField(label="Otros", max_length=100)
    otherk_agente = forms.CharField(label="Otros", max_length=100)
    otherl_title = forms.CharField(label="Otros", max_length=100)
    otherl_bono1 = forms.CharField(label="Otros", max_length=100)
    otherl_bono2 = forms.CharField(label="Otros", max_length=100)
    otherl_paga1 = forms.CharField(label="Otros", max_length=100)
    otherl_paga2 = forms.CharField(label="Otros", max_length=100)
    otherl_agente = forms.CharField(label="Otros", max_length=100)
    otherm_title = forms.CharField(label="Otros", max_length=100)
    otherm_bono1 = forms.CharField(label="Otros", max_length=100)
    otherm_bono2 = forms.CharField(label="Otros", max_length=100)
    otherm_paga1 = forms.CharField(label="Otros", max_length=100)
    otherm_paga2 = forms.CharField(label="Otros", max_length=100)
    otherm_agente = forms.CharField(label="Otros", max_length=100)

    year_balance1 = forms.CharField(label="Año / Year", max_length=100)
    year_balance2 = forms.CharField(label="Año / Year", max_length=100)
    FHA_balance1 = forms.CharField(label="FHA", max_length=100)
    FHA_balance2 = forms.CharField(label="FHA", max_length=100)
    FHA_agente = forms.CharField(label="FHA", max_length=100)
    GAV_balance1 = forms.CharField(label="GAV", max_length=100)
    GAV_balance2 = forms.CharField(label="GAV", max_length=100)
    GAV_agente = forms.CharField(label="GAV", max_length=100)
    convencionales_balance1 = forms.CharField(label="Convencionales", max_length=100)
    convencionales_balance2 = forms.CharField(label="Convencionales", max_length=100)
    convencionales_agente = forms.CharField(label="Convencionales", max_length=100)
    otras_instituciones_balance1 = forms.CharField(
        label="Otras Instituciones", max_length=100
    )
    otras_instituciones_balance2 = forms.CharField(
        label="Otras Instituciones", max_length=100
    )
    otras_instituciones_agente = forms.CharField(
        label="Otras Instituciones", max_length=100
    )
    prestamos_hipo_balance1 = forms.CharField(
        label="Préstamos Hipotecarios", max_length=100
    )
    prestamos_hipo_balance2 = forms.CharField(
        label="Préstamos Hipotecarios", max_length=100
    )
    prestamos_hipo_agente = forms.CharField(
        label="Préstamos Hipotecarios", max_length=100
    )
    prestamos_comerciales_industriales_balance1 = forms.CharField(
        label="Préstamos Comerciales e Industriales", max_length=100
    )
    prestamos_comerciales_industriales_balance2 = forms.CharField(
        label="Préstamos Comerciales e Industriales", max_length=100
    )
    prestamos_comerciales_industriales_agente = forms.CharField(
        label="Préstamos Comerciales e Industriales", max_length=100
    )
    prestamos_poliza_balance1 = forms.CharField(
        label="Préstamos con Póliza", max_length=100
    )
    prestamos_poliza_balance2 = forms.CharField(
        label="Préstamos con Póliza", max_length=100
    )
    prestamos_poliza_agente = forms.CharField(
        label="Préstamos con Póliza", max_length=100
    )
    reservas_poliza_balance1 = forms.CharField(
        label="Reservas con Póliza", max_length=100
    )
    reservas_poliza_balance2 = forms.CharField(
        label="Reservas con Póliza", max_length=100
    )
    reservas_poliza_agente = forms.CharField(
        label="Reservas con Póliza", max_length=100
    )
    dividendos_poliza_balance1 = forms.CharField(
        label="Dividendos con Póliza", max_length=100
    )
    dividendos_poliza_balance2 = forms.CharField(
        label="Dividendos con Póliza", max_length=100
    )
    dividendos_poliza_agente = forms.CharField(
        label="Dividendos con Póliza", max_length=100
    )
    nombre_firma = forms.CharField(label="Nombre", max_length=100)
    phone = forms.CharField(label="Teléfono", max_length=100)
    nombre_persona = forms.CharField(
        label="Nombre de la persona que llena el cuestionario", max_length=100
    )


class JP_375(forms.Form):
    year_1 = forms.CharField(label="Año / Year", max_length=100)
    year_2 = forms.CharField(label="Año / Year", max_length=100)
    year_3 = forms.CharField(label="Año / Year", max_length=100)

    FHA_1 = forms.CharField(label="1. F.H.A.", max_length=100)
    FHA_2 = forms.CharField(label="1. F.H.A.", max_length=100)
    FHA_3 = forms.CharField(label="1. F.H.A.", max_length=100)

    veteran_1 = forms.CharField(label="2. Adm. de Veteranos", max_length=100)
    veteran_2 = forms.CharField(label="2. Adm. de Veteranos", max_length=100)
    veteran_3 = forms.CharField(label="2. Adm. de Veteranos", max_length=100)

    bank_1 = forms.CharField(label="3. Banco de la Vivienda", max_length=100)
    bank_2 = forms.CharField(label="3. Banco de la Vivienda", max_length=100)
    bank_3 = forms.CharField(label="3. Banco de la Vivienda", max_length=100)

    conventional_1 = forms.CharField(label="4. Convencionales", max_length=100)
    conventional_2 = forms.CharField(label="4. Convencionales", max_length=100)
    conventional_3 = forms.CharField(label="4. Convencionales", max_length=100)

    other_1 = forms.CharField(label="5. Otras", max_length=100)
    other_2 = forms.CharField(label="5. Otras", max_length=100)
    other_3 = forms.CharField(label="5. Otras", max_length=100)

    FHA_2_1 = forms.CharField(label="1) F.H.A.", max_length=100)
    FHA_2_2 = forms.CharField(label="1) F.H.A.", max_length=100)
    FHA_2_3 = forms.CharField(label="1) F.H.A.", max_length=100)

    veteran_2_1 = forms.CharField(label="2) Adm. de Veteranos", max_length=100)
    veteran_2_2 = forms.CharField(label="2) Adm. de Veteranos", max_length=100)
    veteran_2_3 = forms.CharField(label="2) Adm. de Veteranos", max_length=100)

    conventional_2_1 = forms.CharField(label="3) Convencionales", max_length=100)
    conventional_2_2 = forms.CharField(label="3) Convencionales", max_length=100)
    conventional_2_3 = forms.CharField(label="3) Convencionales", max_length=100)

    others_2_1 = forms.CharField(label="4) Otras", max_length=100)
    others_2_2 = forms.CharField(label="4) Otras", max_length=100)
    others_2_3 = forms.CharField(label="4) Otras", max_length=100)

    FHA_3_1 = forms.CharField(label="1) F.H.A.", max_length=100)
    FHA_3_2 = forms.CharField(label="1) F.H.A.", max_length=100)
    FHA_3_3 = forms.CharField(label="1) F.H.A.", max_length=100)

    veteran_3_1 = forms.CharField(label="2) Adm. de Veteranos", max_length=100)
    veteran_3_2 = forms.CharField(label="2) Adm. de Veteranos", max_length=100)
    veteran_3_3 = forms.CharField(label="2) Adm. de Veteranos", max_length=100)

    bank_2_1 = forms.CharField(label="3) Banco de la Vivienda", max_length=100)
    bank_2_2 = forms.CharField(label="3) Banco de la Vivienda", max_length=100)
    bank_2_3 = forms.CharField(label="3) Banco de la Vivienda", max_length=100)

    conventional_3_1 = forms.CharField(label="4) Convencionales", max_length=100)
    conventional_3_2 = forms.CharField(label="4) Convencionales", max_length=100)
    conventional_3_3 = forms.CharField(label="4) Convencionales", max_length=100)

    others_3_1 = forms.CharField(label="5) Otras", max_length=100)
    others_3_2 = forms.CharField(label="5) Otras", max_length=100)
    others_3_3 = forms.CharField(label="5) Otras", max_length=100)

    FHA_4_1 = forms.CharField(label="1) F.H.A.", max_length=100)
    FHA_4_2 = forms.CharField(label="1) F.H.A.", max_length=100)
    FHA_4_3 = forms.CharField(label="1) F.H.A.", max_length=100)

    veteran_4_1 = forms.CharField(label="2) Adm. de Veteranos", max_length=100)
    veteran_4_2 = forms.CharField(label="2) Adm. de Veteranos", max_length=100)
    veteran_4_3 = forms.CharField(label="2) Adm. de Veteranos", max_length=100)

    conventional_4_1 = forms.CharField(label="3) Convencionales", max_length=100)
    conventional_4_2 = forms.CharField(label="3) Convencionales", max_length=100)
    conventional_4_3 = forms.CharField(label="3) Convencionales", max_length=100)

    others_4_1 = forms.CharField(label="4) Otras", max_length=100)
    others_4_2 = forms.CharField(label="4) Otras", max_length=100)
    others_4_3 = forms.CharField(label="4) Otras", max_length=100)

    commissions_1 = forms.CharField(
        label="b) Comisiones Recibidas de No-Residentes 3/", max_length=100
    )
    commissions_2 = forms.CharField(
        label="b) Comisiones Recibidas de No-Residentes 3/", max_length=100
    )
    commissions_3 = forms.CharField(
        label="b) Comisiones Recibidas de No-Residentes 3/", max_length=100
    )

    phone = forms.CharField(label="Phone Number", max_length=100)
    signature = forms.CharField(
        label="Name of person filling the questionnaire", max_length=100
    )
    position = forms.CharField(label="Position", max_length=100)


class IP_480(forms.Form):
    company_name = forms.CharField(
        label="Nombre compañía / Company Name", max_length=100
    )
    address = forms.CharField(label="Dirección / Address", max_length=200)
    email = forms.EmailField(label="Correo electrónico / Email")
    liaison_officer = forms.CharField(
        label="Persona contacto / Liaison officer", max_length=100
    )
    ssn = forms.CharField(
        label="Numero de Seguro Social / Social Security Number", max_length=11
    )
    tel = forms.CharField(label="Tel", max_length=20)
    fax = forms.CharField(label="Fax", max_length=20)
    legal_form = forms.ChoiceField(
        label="Forma legal de organización / Legal form of organization",
        choices=[
            ("Corporación", "Corporación"),
            ("Sociedad", "Sociedad"),
            ("Cooperativa", "Cooperativa"),
            ("Empresa Individual", "Empresa Individual"),
            ("Empresa sin fines pecuniarios", "Empresa sin fines pecuniarios"),
        ],
    )
    cfc = forms.ChoiceField(label="CEC", choices=[("Si", "Si"), ("No", "No")])
    business_function = forms.CharField(
        label="Describa brevemente la función principal del negocio / Explain briefly the main function of the business activity",
        widget=forms.Textarea,
    )
    closing_date = forms.DateField(
        label="Fecha de cierre de sus libros / Your accounting period closing date",
        widget=forms.SelectDateWidget,
    )
    start_year = forms.CharField(
        label="Año de inicio de operaciones / Year of start of operations",
        max_length=100,
    )
    end_year = forms.CharField(
        label="Año de cierre de operaciones / Year of end of operations", max_length=100
    )
    operation_incomes_1 = (
        forms.CharField(label="1. Ingresos por proyecto - Income from project"),
    )
    operation_incomes_2 = (
        forms.CharField(label="1. Ingresos por proyecto - Income from project"),
    )
    people_A_1 = (forms.CharField(label="2. A personas - To persons"),)
    people_A_2 = (forms.CharField(label="2. A personas - To persons"),)
    industries_businesses_A_1 = (
        forms.CharField(
            label="3. A industrias y negocios - To industries and businesses"
        ),
    )
    industries_businesses_A_2 = (
        forms.CharField(
            label="3. A industrias y negocios - To industries and businesses"
        ),
    )
    incomes_interests_1 = (
        forms.CharField(label="4. Ingresos por intereses - Income from interests"),
    )
    incomes_interests_2 = (
        forms.CharField(label="4. Ingresos por intereses - Income from interests"),
    )
    incomes_rents_1 = (
        forms.CharField(label="5. Ingresos por alquileres - Income from rents"),
    )
    incomes_rents_2 = (
        forms.CharField(label="5. Ingresos por alquileres - Income from rents"),
    )
    dividends_1 = (forms.CharField(label="6. Dividendos - Dividends"),)
    dividends_2 = (forms.CharField(label="6. Dividendos - Dividends"),)
    others_incomes_1 = (forms.CharField(label="7. Otros ingresos - Other incomes"),)
    others_incomes_2 = (forms.CharField(label="7. Otros ingresos - Other incomes"),)
    total_incomes_1 = (forms.CharField(label="Total de ingresos - Total incomes"),)
    total_incomes_2 = (forms.CharField(label="Total de ingresos - Total incomes"),)
    expenses_1 = (forms.CharField(label="1. Gastos - Expenses"),)
    expenses_2 = (forms.CharField(label="1. Gastos - Expenses"),)
    salaries_1 = (forms.CharField(label="2. Salarios - Salaries"),)
    salaries_2 = (forms.CharField(label="2. Salarios - Salaries"),)
    expenses_interests_1 = (
        forms.CharField(label="3. Gastos por intereses - Expenses from interests"),
    )
    expenses_interests_2 = (
        forms.CharField(label="3. Gastos por intereses - Expenses from interests"),
    )
    expenses_rents_1 = (
        forms.CharField(label="4. Gastos por alquileres - Expenses from rents"),
    )
    expenses_rents_2 = (
        forms.CharField(label="4. Gastos por alquileres - Expenses from rents"),
    )
    depreciation_1 = (forms.CharField(label="5. Depreciación - Depreciation"),)
    depreciation_2 = (forms.CharField(label="5. Depreciación - Depreciation"),)
    donations_1 = (forms.CharField(label="6. Donaciones - Donations"),)
    donations_2 = (forms.CharField(label="6. Donaciones - Donations"),)
    sales_tax_1 = (forms.CharField(label="7. Impuesto sobre ventas - Sales tax"),)
    sales_tax_2 = (forms.CharField(label="7. Impuesto sobre ventas - Sales tax"),)
    machinery_1 = (forms.CharField(label="8. Maquinaria - Machinery"),)
    machinery_2 = (forms.CharField(label="8. Maquinaria - Machinery"),)
    other_purchases_1 = (forms.CharField(label="9. Otras compras - Other purchases"),)
    other_purchases_2 = (forms.CharField(label="9. Otras compras - Other purchases"),)
    licenses_1 = (forms.CharField(label="10. Licencias - Licenses"),)
    licenses_2 = (forms.CharField(label="10. Licencias - Licenses"),)
    other_expenses_1 = (forms.CharField(label="11. Otros gastos - Other expenses"),)
    other_expenses_2 = (forms.CharField(label="11. Otros gastos - Other expenses"),)
    total_expenses_1 = (forms.CharField(label="Total de gastos - Total expenses"),)
    total_expenses_2 = (forms.CharField(label="Total de gastos - Total expenses"),)
    net_profit_1 = (forms.CharField(label="Utilidad neta - Net profit"),)
    net_profit_2 = (forms.CharField(label="Utilidad neta - Net profit"),)
    income_tax_1 = (forms.CharField(label="Impuesto sobre la renta - Income tax"),)
    income_tax_2 = (forms.CharField(label="Impuesto sobre la renta - Income tax"),)
    profit_after_tax_1 = (
        forms.CharField(label="Utilidad después de impuestos - Profit after tax"),
    )
    profit_after_tax_2 = (
        forms.CharField(label="Utilidad después de impuestos - Profit after tax"),
    )
    withheld_tax_1 = (forms.CharField(label="Impuesto retenido - Withheld tax"),)
    withheld_tax_2 = (forms.CharField(label="Impuesto retenido - Withheld tax"),)
    signature = forms.CharField(
        label="Name of person filling the questionnaire", max_length=100
    )
    rank = forms.CharField(label="Rank", max_length=100)


class IP_420(forms.Form):
    company_name = forms.CharField(
        label="Nombre compañía / Company Name", max_length=100
    )
    address = forms.CharField(label="Dirección / Address", max_length=200)
    email = forms.EmailField(label="Correo electrónico / Email")
    liaison_officer = forms.CharField(
        label="Persona contacto / Liaison officer", max_length=100
    )
    ssn = forms.CharField(
        label="Numero de Seguro Social / Social Security Number", max_length=11
    )
    tel = forms.CharField(label="Tel", max_length=20)
    fax = forms.CharField(label="Fax", max_length=20)
    legal_form = forms.ChoiceField(
        label="Forma legal de organización / Legal form of organization",
        choices=[
            ("Corporación", "Corporación"),
            ("Sociedad", "Sociedad"),
            ("Cooperativa", "Cooperativa"),
            ("Empresa Individual", "Empresa Individual"),
            ("Empresa sin fines pecuniarios", "Empresa sin fines pecuniarios"),
        ],
    )
    cfc = forms.ChoiceField(label="CEC", choices=[("Si", "Si"), ("No", "No")])
    main_line = forms.CharField(
        label="4. Línea principal de mercancía vendida por esta firma / Main line of merchandise sold by the firm:",
        max_length=200,
    )
    business_type = forms.ChoiceField(
        label="5. Clase de negocio / Type of business:",
        choices=[
            ("Distribuidor", "Distribuidor"),
            ("Representante", "Representative"),
            ("Mayorista", "Wholesaler"),
            ("Supermercado", "Supermarket"),
        ],
    )
    other_business_type = forms.CharField(
        label="6. Otros negocios / Other businesses:", max_length=200
    )
    accounting_period = forms.CharField(
        label="6. Fecha de detallar la siguiente informacion / Your accounting period closing date:",
        max_length=100,
    )
    start_year = forms.CharField(
        label="Año de inicio de operaciones / Year of start of operations",
        max_length=100,
    )
    end_year = forms.CharField(
        label="Año de cierre de operaciones / Year of end of operations", max_length=100
    )
    incomes_sales_1 = forms.CharField(label="Ventas - Sales", max_length=100)
    incomes_sales_2 = forms.CharField(label="Ventas - Sales", max_length=100)
    incomes_from_people_1 = forms.CharField(
        label="Ingresos de personas - Incomes from people", max_length=100
    )
    incomes_from_people_2 = forms.CharField(
        label="Ingresos de personas - Incomes from people", max_length=100
    )
    incomes_industries_businesses_1 = forms.CharField(
        label="Ingresos de industrias y negocios - Incomes from industries and businesses",
        max_length=100,
    )
    incomes_industries_businesses_2 = forms.CharField(
        label="Ingresos de industrias y negocios - Incomes from industries and businesses",
        max_length=100,
    )
    incomes_less_cost_1 = forms.CharField(
        label="Ingresos menos costo - Incomes less cost", max_length=100
    )
    incomes_less_cost_2 = forms.CharField(
        label="Ingresos menos costo - Incomes less cost", max_length=100
    )
    incomes_inventory_beginning_1 = forms.CharField(
        label="Inventario inicial - Inventory beginning", max_length=100
    )
    incomes_inventory_beginning_2 = forms.CharField(
        label="Inventario inicial - Inventory beginning", max_length=100
    )
    incomes_purchases_1 = forms.CharField(label="Compras - Purchases", max_length=100)
    incomes_purchases_2 = forms.CharField(label="Compras - Purchases", max_length=100)
    incomes_inventory_end_1 = forms.CharField(
        label="Inventario final - Inventory end", max_length=100
    )
    incomes_inventory_end_2 = forms.CharField(
        label="Inventario final - Inventory end", max_length=100
    )
    incomes_gross_profit_1 = forms.CharField(
        label="Utilidad bruta - Gross profit", max_length=100
    )
    incomes_gross_profit_2 = forms.CharField(
        label="Utilidad bruta - Gross profit", max_length=100
    )
    other_operation_incomes_1 = forms.CharField(
        label="Otros ingresos de operación - Other operation incomes", max_length=100
    )
    other_operation_incomes_2 = forms.CharField(
        label="Otros ingresos de operación - Other operation incomes", max_length=100
    )
    incomes_interests_1 = forms.CharField(
        label="Ingresos por intereses - Incomes from interests", max_length=100
    )
    incomes_interests_2 = forms.CharField(
        label="Ingresos por intereses - Incomes from interests", max_length=100
    )
    incomes_rent_1 = forms.CharField(
        label="Ingresos por alquileres - Incomes from rents", max_length=100
    )
    incomes_rent_2 = forms.CharField(
        label="Ingresos por alquileres - Incomes from rents", max_length=100
    )
    incomes_gain_loss_1 = forms.CharField(
        label="Ingresos por ganancias o pérdidas - Incomes from gains or losses",
        max_length=100,
    )
    incomes_gain_loss_2 = forms.CharField(
        label="Ingresos por ganancias o pérdidas - Incomes from gains or losses",
        max_length=100,
    )
    incomes_dividends_1 = forms.CharField(
        label="Ingresos por dividendos - Incomes from dividends", max_length=100
    )
    incomes_dividends_2 = forms.CharField(
        label="Ingresos por dividendos - Incomes from dividends", max_length=100
    )
    other_incomes_1 = forms.CharField(
        label="Otros ingresos - Other incomes", max_length=100
    )
    other_incomes_2 = forms.CharField(
        label="Otros ingresos - Other incomes", max_length=100
    )
    incomes_total_gross_1 = forms.CharField(
        label="Ingresos totales brutos - Total gross incomes", max_length=100
    )
    incomes_total_gross_2 = forms.CharField(
        label="Ingresos totales brutos - Total gross incomes", max_length=100
    )
    expenses_1 = forms.CharField(label="Gastos - Expenses", max_length=100)
    expenses_2 = forms.CharField(label="Gastos - Expenses", max_length=100)
    expenses_salaries_wages_bonus_1 = forms.CharField(
        label="Salarios, sueldos y bonificaciones - Salaries, wages and bonuses",
        max_length=100,
    )
    expenses_salaries_wages_bonus_2 = forms.CharField(
        label="Salarios, sueldos y bonificaciones - Salaries, wages and bonuses",
        max_length=100,
    )
    expenses_interests_1 = forms.CharField(
        label="Gastos por intereses - Expenses from interests", max_length=100
    )
    expenses_interests_2 = forms.CharField(
        label="Gastos por intereses - Expenses from interests", max_length=100
    )
    expenses_depreciation_1 = forms.CharField(
        label="Depreciación - Depreciation", max_length=100
    )
    expenses_depreciation_2 = forms.CharField(
        label="Depreciación - Depreciation", max_length=100
    )
    expenses_rent_1 = forms.CharField(label="Alquileres - Rents", max_length=100)
    expenses_rent_2 = forms.CharField(label="Alquileres - Rents", max_length=100)
    expenses_bad_debts_1 = forms.CharField(
        label="Deudas incobrables - Bad debts", max_length=100
    )
    expenses_bad_debts_2 = forms.CharField(
        label="Deudas incobrables - Bad debts", max_length=100
    )
    expenses_donations_1 = forms.CharField(
        label="Donaciones - Donations", max_length=100
    )
    expenses_donations_2 = forms.CharField(
        label="Donaciones - Donations", max_length=100
    )
    expenses_sales_taxes_1 = forms.CharField(
        label="Impuesto sobre ventas - Sales taxes", max_length=100
    )
    expenses_sales_taxes_2 = forms.CharField(
        label="Impuesto sobre ventas - Sales taxes", max_length=100
    )
    expenses_machinary_1 = forms.CharField(
        label="Maquinaria - Machinary", max_length=100
    )
    expenses_machinary_2 = forms.CharField(
        label="Maquinaria - Machinary", max_length=100
    )
    expenses_other_purchases_1 = forms.CharField(
        label="Otras compras - Other purchases", max_length=100
    )
    expenses_other_purchases_2 = forms.CharField(
        label="Otras compras - Other purchases", max_length=100
    )
    expenses_licenses_1 = forms.CharField(label="Licencias - Licenses", max_length=100)
    expenses_licenses_2 = forms.CharField(label="Licencias - Licenses", max_length=100)
    expenses_other_operations_1 = forms.CharField(
        label="Otras operaciones - Other operations", max_length=100
    )
    expenses_other_operations_2 = forms.CharField(
        label="Otras operaciones - Other operations", max_length=100
    )
    expenses_total_operations_1 = forms.CharField(
        label="Total de gastos de operación - Total operation expenses", max_length=100
    )
    expenses_total_operations_2 = forms.CharField(
        label="Total de gastos de operación - Total operation expenses", max_length=100
    )
    gross_profit_1 = forms.CharField(
        label="Utilidad bruta - Gross profit", max_length=100
    )
    gross_profit_2 = forms.CharField(
        label="Utilidad bruta - Gross profit", max_length=100
    )
    profit_income_tax_1 = forms.CharField(
        label="Utilidad antes de impuesto sobre la renta - Profit before income tax",
        max_length=100,
    )
    profit_income_tax_2 = forms.CharField(
        label="Utilidad antes de impuesto sobre la renta - Profit before income tax",
        max_length=100,
    )
    profit_after_income_tax_1 = forms.CharField(
        label="Utilidad después de impuesto sobre la renta - Profit after income tax",
        max_length=100,
    )
    profit_after_income_tax_2 = forms.CharField(
        label="Utilidad después de impuesto sobre la renta - Profit after income tax",
        max_length=100,
    )
    sales_tax_1 = forms.CharField(
        label="Impuesto sobre ventas - Sales tax", max_length=100
    )
    sales_tax_2 = forms.CharField(
        label="Impuesto sobre ventas - Sales tax", max_length=100
    )
    name = forms.CharField(
        label="Nombre de persona que suministra la información Name of person furnishing information",
        max_length=100,
    )
    rank = forms.CharField(
        label="Rango o posición que ocupa en la empresa Rank or position",
        max_length=100,
    )


class IP_310(forms.Form):
    company_name = forms.CharField(
        label="Nombre compañía / Company Name", max_length=100
    )
    address = forms.CharField(label="Dirección / Address", max_length=200)
    email = forms.EmailField(label="Correo electrónico / Email")
    liaison_officer = forms.CharField(
        label="Persona contacto / Liaison officer", max_length=100
    )
    ssn = forms.CharField(
        label="Numero de Seguro Social / Social Security Number", max_length=11
    )
    tel = forms.CharField(label="Tel", max_length=20)
    fax = forms.CharField(label="Fax", max_length=20)
    legal_form = forms.ChoiceField(
        label="Forma legal de organización / Legal form of organization",
        choices=[
            ("Corporación", "Corporación"),
            ("Sociedad", "Sociedad"),
            ("Cooperativa", "Cooperativa"),
            ("Empresa Individual", "Empresa Individual"),
            ("Empresa sin fines pecuniarios", "Empresa sin fines pecuniarios"),
        ],
    )
    cfc = forms.ChoiceField(label="CEC", choices=[("Si", "Si"), ("No", "No")])
    end_month = forms.ChoiceField(
        label="Mes de cierre de sus libros / Your accounting period closing month",
        choices=[
            ("Enero", "Enero"),
            ("Febrero", "Febrero"),
            ("Marzo", "Marzo"),
            ("Abril", "Abril"),
            ("Mayo", "Mayo"),
            ("Junio", "Junio"),
            ("Julio", "Julio"),
            ("Agosto", "Agosto"),
            ("Septiembre", "Septiembre"),
            ("Octubre", "Octubre"),
            ("Noviembre", "Noviembre"),
            ("Diciembre", "Diciembre"),
        ],
    )
    main_product_1 = forms.CharField(
        label="1. Producto principal - Main product", max_length=100
    )
    other_product_1 = forms.CharField(
        label="2. Otros productos - Other products", max_length=100
    )
    raw_material_used = forms.CharField(
        label="3. Materia prima utilizada - Raw material used", max_length=100
    )
    closing_date = forms.DateField(
        label="Fecha de cierre de sus libros / Your accounting period closing date",
        widget=forms.SelectDateWidget,
    )
    start_year = forms.CharField(
        label="Año de inicio de operaciones / Year of start of operations",
        max_length=100,
    )
    end_year = forms.CharField(
        label="Año de cierre de operaciones / Year of end of operations", max_length=100
    )
    total_sales_1 = forms.CharField(label="1. Ventas totales - Total sales", max_length=100)
    total_sales_2 = forms.CharField(label="1. Ventas totales - Total sales", max_length=100)
    from_persons_1 = forms.CharField(label="a. A personas - To persons", max_length=100)
    from_persons_2 = forms.CharField(label="a. A personas - To persons", max_length=100)
    industries_businesses_1 = forms.CharField(
        label="b. A industrias y negocios - To industries and businesses",
        max_length=100,
    )
    industries_businesses_2 = forms.CharField(
        label="b. A industrias y negocios - To industries and businesses",
        max_length=100,
    )
    goods_manufactured_1 = forms.CharField(
        label="4. Bienes manufacturados - Manufactured goods", max_length=100
    )
    goods_manufactured_2 = forms.CharField(
        label="4. Bienes manufacturados - Manufactured goods", max_length=100
    )
    exports_val_1 = forms.CharField(label="5. Exportaciones - Exports", max_length=100)
    exports_val_2 = forms.CharField(label="5. Exportaciones - Exports", max_length=100)
    gross_profit_1_1 = forms.CharField(
        label="16. Utilidad bruta - Gross profit", max_length=100
    )
    gross_profit_2_2 = forms.CharField(label="16. Utilidad bruta - Gross profit", max_length=100)
    exports_val_1_1 = forms.CharField(label="5. Exportaciones - Exports", max_length=100)
    exports_val_2_2 = forms.CharField(label="5. Exportaciones - Exports", max_length=100)
    manufacturing_cost_1 = forms.CharField(
        label="6. Costo de manufactura - Manufacturing cost", max_length=100
    )
    manufacturing_cost_2 = forms.CharField(
        label="6. Costo de manufactura - Manufacturing cost", max_length=100
    )
    inventories_begginning_1 = forms.CharField(
        label="7. Inventario al principio - Inventory at the beginning", max_length=100
    )
    inventories_begginning_2 = forms.CharField(
        label="7. Inventario al principio - Inventory at the beginning", max_length=100
    )
    purchases_1 = forms.CharField(label="8. Compras - Purchases", max_length=100)
    purchases_2 = forms.CharField(label="8. Compras - Purchases", max_length=100)
    total_raw_1 = forms.CharField(
        label="9. Total de materia prima - Total raw material", max_length=100
    )
    total_raw_2 = forms.CharField(
        label="9. Total de materia prima - Total raw material", max_length=100
    )
    imported_1 = forms.CharField(label="a. Importada - Imported", max_length=100)
    imported_2 = forms.CharField(label="a. Importada - Imported", max_length=100)
    others_1 = forms.CharField(label="b. Otras - Other", max_length=100)
    others_2 = forms.CharField(label="b. Otras - Other", max_length=100)
    direct_wages_1 = forms.CharField(
        label="10. Salarios directos - Direct wages", max_length=100
    )
    direct_wages_2 = forms.CharField(
        label="10. Salarios directos - Direct wages", max_length=100
    )
    depreciation_1 = forms.CharField(
        label="11. Depreciación - Depreciation", max_length=100
    )
    depreciation_2 = forms.CharField(
        label="11. Depreciación - Depreciation", max_length=100
    )
    rent_land_1 = forms.CharField(
        label="12. Renta de terreno - Rent of land", max_length=100
    )
    rent_land_2 = forms.CharField(
        label="12. Renta de terreno - Rent of land", max_length=100
    )
    other_direct_1 = forms.CharField(
        label="13. Otros costos directos - Other direct costs", max_length=100
    )
    other_direct_2 = forms.CharField(
        label="13. Otros costos directos - Other direct costs", max_length=100
    )
    indirect_cost_1 = forms.CharField(
        label="14. Costos indirectos - Indirect costs", max_length=100
    )
    indirect_cost_2 = forms.CharField(
        label="14. Costos indirectos - Indirect costs", max_length=100
    )
    inventories_end_1 = forms.CharField(
        label="15. Inventario al final - Inventory at the end", max_length=100
    )
    inventories_end_2 = forms.CharField(
        label="15. Inventario al final - Inventory at the end", max_length=100
    )
    gross_profit_1 = forms.CharField(
        label="16. Utilidad bruta - Gross profit", max_length=100
    )
    gross_profit_2 = forms.CharField(
        label="16. Utilidad bruta - Gross profit", max_length=100
    )
    other_operating_1 = forms.CharField(
        label="17. Otros ingresos - Other income", max_length=100
    )
    other_operating_2 = forms.CharField(
        label="17. Otros ingresos - Other income", max_length=100
    )
    interest_1 = forms.CharField(label="18. Intereses - Interests", max_length=100)
    interest_2 = forms.CharField(label="18. Intereses - Interests", max_length=100)
    rent_land_3 = forms.CharField(
        label="19. Renta de terreno - Rent of land", max_length=100
    )
    rent_land_4 = forms.CharField(
        label="19. Renta de terreno - Rent of land", max_length=100
    )
    capital_gain_1 = forms.CharField(
        label="20. Ganancia de capital - Capital gain", max_length=100
    )
    capital_gain_2 = forms.CharField(
        label="20. Ganancia de capital - Capital gain", max_length=100
    )
    other_1 = forms.CharField(label="21. Otros - Other", max_length=100)
    other_2 = forms.CharField(label="21. Otros - Other", max_length=100)
    total_gross_1 = forms.CharField(
        label="22. Total de utilidad bruta - Total gross profit", max_length=100
    )
    total_gross_2 = forms.CharField(
        label="22. Total de utilidad bruta - Total gross profit", max_length=100
    )
    expenses_not_1 = forms.CharField(
        label="23. Gastos no operacionales - Non-operating expenses", max_length=100
    )
    expenses_not_2 = forms.CharField(
        label="23. Gastos no operacionales - Non-operating expenses", max_length=100
    )
    salaries_1 = forms.CharField(label="24. Salarios - Salaries", max_length=100)
    salaries_2 = forms.CharField(label="24. Salarios - Salaries", max_length=100)
    interest_3 = forms.CharField(label="25. Intereses - Interests", max_length=100)
    interest_4 = forms.CharField(label="25. Intereses - Interests", max_length=100)
    depreciation_3 = forms.CharField(
        label="26. Depreciación - Depreciation", max_length=100
    )
    depreciation_4 = forms.CharField(
        label="26. Depreciación - Depreciation", max_length=100
    )
    donations_1 = forms.CharField(label="27. Donativos - Donations", max_length=100)
    donations_2 = forms.CharField(label="27. Donativos - Donations", max_length=100)
    rent_land_5 = forms.CharField(
        label="28. Renta de terreno - Rent of land", max_length=100
    )
    rent_land_6 = forms.CharField(
        label="28. Renta de terreno - Rent of land", max_length=100
    )
    other_operating_3 = forms.CharField(
        label="29. Otros gastos operacionales - Other operating expenses",
        max_length=100,
    )
    other_operating_4 = forms.CharField(
        label="29. Otros gastos operacionales - Other operating expenses",
        max_length=100,
    )
    sales_tax_1 = forms.CharField(
        label="30. Impuesto sobre la venta y uso - Sales and use tax", max_length=100
    )
    sales_tax_2 = forms.CharField(
        label="30. Impuesto sobre la venta y uso - Sales and use tax", max_length=100
    )
    machinery_1 = forms.CharField(
        label="31. Compra de maquinaria - Purchase of machinery", max_length=100
    )
    machinery_2 = forms.CharField(
        label="31. Compra de maquinaria - Purchase of machinery", max_length=100
    )
    on_other_1 = forms.CharField(label="32. Otras - Other", max_length=100)
    on_other_2 = forms.CharField(label="32. Otras - Other", max_length=100)
    licenses_1 = forms.CharField(label="33. Licencias - Licenses", max_length=100)
    licenses_2 = forms.CharField(label="33. Licencias - Licenses", max_length=100)
    net_loss_1 = forms.CharField(label="34. Pérdida neta - Net loss", max_length=100)
    net_loss_2 = forms.CharField(label="34. Pérdida neta - Net loss", max_length=100)
    income_tax_1 = forms.CharField(
        label="35. Contribución sobre ingresos - Income tax", max_length=100
    )
    income_tax_2 = forms.CharField(
        label="35. Contribución sobre ingresos - Income tax", max_length=100
    )
    profit_after_tax_1 = forms.CharField(
        label="36. Ganancia después de contribución sobre ingresos - Profit after income tax",
        max_length=100,
    )
    profit_after_tax_2 = forms.CharField(
        label="36. Ganancia después de contribución sobre ingresos - Profit after income tax",
        max_length=100,
    )
    sales_and_use_withheld_1 = forms.CharField(
        label="37. Impuesto sobre la venta y uso retenido - Sales and use tax withheld",
        max_length=100,
    )
    sales_and_use_withheld_2 = forms.CharField(
        label="37. Impuesto sobre la venta y uso retenido - Sales and use tax withheld",
        max_length=100,
    )
    branches = forms.ChoiceField(label="CEC", choices=[("Si", "Si"), ("No", "No")])
    branches_if_yes = forms.ChoiceField(
        label="En caso afirmativo indique si:",
        choices=[
            (
                "La información suministrada cubre todas las sucursales./The information provided includes all branches.",
                "La información suministrada cubre todas las sucursales./The information provided includes all branches.",
            ),
            (
                "La información suministrada cubre este establecimiento solamente./The information provided covers only the firm responding to this questionnaire.",
                "La información suministrada cubre este establecimiento solamente./The information provided covers only the firm responding to this questionnaire.",
            ),
        ],
    )
    signature = forms.CharField(
        label="Name of person filling the questionnaire", max_length=100
    )
    rank = forms.CharField(label="Rank", max_length=100)


class JP_383(forms.Form):
    other_section = forms.CharField(label="Otra sección", max_length=100)
    año = forms.CharField(label="Año", max_length=100)
    julio_1 = forms.CharField(label="Julio", max_length=100)
    julio_2 = forms.CharField(label="Julio", max_length=100)
    julio_3 = forms.CharField(label="Julio", max_length=100)
    julio_4 = forms.CharField(label="Julio", max_length=100)
    julio_5 = forms.CharField(label="Julio", max_length=100)
    julio_6 = forms.CharField(label="Julio", max_length=100)
    agosto_1 = forms.CharField(label="Agosto", max_length=100)
    agosto_2 = forms.CharField(label="Agosto", max_length=100)
    agosto_3 = forms.CharField(label="Agosto", max_length=100)
    agosto_4 = forms.CharField(label="Agosto", max_length=100)
    agosto_5 = forms.CharField(label="Agosto", max_length=100)
    agosto_6 = forms.CharField(label="Agosto", max_length=100)
    septiembre_1 = forms.CharField(label="Septiembre", max_length=100)
    septiembre_2 = forms.CharField(label="Septiembre", max_length=100)
    septiembre_3 = forms.CharField(label="Septiembre", max_length=100)
    septiembre_4 = forms.CharField(label="Septiembre", max_length=100)
    septiembre_5 = forms.CharField(label="Septiembre", max_length=100)
    septiembre_6 = forms.CharField(label="Septiembre", max_length=100)
    subtotal_1 = forms.CharField(label="Subtotal", max_length=100)
    subtotal_2 = forms.CharField(label="Subtotal", max_length=100)
    subtotal_3 = forms.CharField(label="Subtotal", max_length=100)
    subtotal_4 = forms.CharField(label="Subtotal", max_length=100)
    subtotal_5 = forms.CharField(label="Subtotal", max_length=100)
    subtotal_6 = forms.CharField(label="Subtotal", max_length=100)
    octubre_1 = forms.CharField(label="Octubre", max_length=100)
    octubre_2 = forms.CharField(label="Octubre", max_length=100)
    octubre_3 = forms.CharField(label="Octubre", max_length=100)
    octubre_4 = forms.CharField(label="Octubre", max_length=100)
    octubre_5 = forms.CharField(label="Octubre", max_length=100)
    octubre_6 = forms.CharField(label="Octubre", max_length=100)
    noviembre_1 = forms.CharField(label="Noviembre", max_length=100)
    noviembre_2 = forms.CharField(label="Noviembre", max_length=100)
    noviembre_3 = forms.CharField(label="Noviembre", max_length=100)
    noviembre_4 = forms.CharField(label="Noviembre", max_length=100)
    noviembre_5 = forms.CharField(label="Noviembre", max_length=100)
    noviembre_6 = forms.CharField(label="Noviembre", max_length=100)
    diciembre_1 = forms.CharField(label="Diciembre", max_length=100)
    diciembre_2 = forms.CharField(label="Diciembre", max_length=100)
    diciembre_3 = forms.CharField(label="Diciembre", max_length=100)
    diciembre_4 = forms.CharField(label="Diciembre", max_length=100)
    diciembre_5 = forms.CharField(label="Diciembre", max_length=100)
    diciembre_6 = forms.CharField(label="Diciembre", max_length=100)
    subtotal_11 = forms.CharField(label="Subtotal", max_length=100)
    subtotal_12 = forms.CharField(label="Subtotal", max_length=100)
    subtotal_13 = forms.CharField(label="Subtotal", max_length=100)
    subtotal_14 = forms.CharField(label="Subtotal", max_length=100)
    subtotal_15 = forms.CharField(label="Subtotal", max_length=100)
    subtotal_16 = forms.CharField(label="Subtotal", max_length=100)
    año_1 = forms.CharField(label="Año", max_length=100)
    enero_1 = forms.CharField(label="Enero", max_length=100)
    enero_2 = forms.CharField(label="Enero", max_length=100)
    enero_3 = forms.CharField(label="Enero", max_length=100)
    enero_4 = forms.CharField(label="Enero", max_length=100)
    enero_5 = forms.CharField(label="Enero", max_length=100)
    enero_6 = forms.CharField(label="Enero", max_length=100)
    febrero_1 = forms.CharField(label="Febrero", max_length=100)
    febrero_2 = forms.CharField(label="Febrero", max_length=100)
    febrero_3 = forms.CharField(label="Febrero", max_length=100)
    febrero_4 = forms.CharField(label="Febrero", max_length=100)
    febrero_5 = forms.CharField(label="Febrero", max_length=100)
    febrero_6 = forms.CharField(label="Febrero", max_length=100)
    marzo_1 = forms.CharField(label="Marzo", max_length=100)
    marzo_2 = forms.CharField(label="Marzo", max_length=100)
    marzo_3 = forms.CharField(label="Marzo", max_length=100)
    marzo_4 = forms.CharField(label="Marzo", max_length=100)
    marzo_5 = forms.CharField(label="Marzo", max_length=100)
    marzo_6 = forms.CharField(label="Marzo", max_length=100)
    subtotal_21 = forms.CharField(label="Subtotal", max_length=100)
    subtotal_22 = forms.CharField(label="Subtotal", max_length=100)
    subtotal_23 = forms.CharField(label="Subtotal", max_length=100)
    subtotal_24 = forms.CharField(label="Subtotal", max_length=100)
    subtotal_25 = forms.CharField(label="Subtotal", max_length=100)
    subtotal_26 = forms.CharField(label="Subtotal", max_length=100)
    abril_1 = forms.CharField(label="Abril", max_length=100)
    abril_2 = forms.CharField(label="Abril", max_length=100)
    abril_3 = forms.CharField(label="Abril", max_length=100)
    abril_4 = forms.CharField(label="Abril", max_length=100)
    abril_5 = forms.CharField(label="Abril", max_length=100)
    abril_6 = forms.CharField(label="Abril", max_length=100)
    mayo_1 = forms.CharField(label="Mayo", max_length=100)
    mayo_2 = forms.CharField(label="Mayo", max_length=100)
    mayo_3 = forms.CharField(label="Mayo", max_length=100)
    mayo_4 = forms.CharField(label="Mayo", max_length=100)
    mayo_5 = forms.CharField(label="Mayo", max_length=100)
    mayo_6 = forms.CharField(label="Mayo", max_length=100)
    junio_1 = forms.CharField(label="Junio", max_length=100)
    junio_2 = forms.CharField(label="Junio", max_length=100)
    junio_3 = forms.CharField(label="Junio", max_length=100)
    junio_4 = forms.CharField(label="Junio", max_length=100)
    junio_5 = forms.CharField(label="Junio", max_length=100)
    junio_6 = forms.CharField(label="Junio", max_length=100)
    subtotal_31 = forms.CharField(label="Subtotal", max_length=100)
    subtotal_32 = forms.CharField(label="Subtotal", max_length=100)
    subtotal_33 = forms.CharField(label="Subtotal", max_length=100)
    subtotal_34 = forms.CharField(label="Subtotal", max_length=100)
    subtotal_35 = forms.CharField(label="Subtotal", max_length=100)
    subtotal_36 = forms.CharField(label="Subtotal", max_length=100)
    total_1 = forms.CharField(label="Total", max_length=100)
    total_2 = forms.CharField(label="Total", max_length=100)
    total_3 = forms.CharField(label="Total", max_length=100)
    total_4 = forms.CharField(label="Total", max_length=100)
    total_5 = forms.CharField(label="Total", max_length=100)
    total_6 = forms.CharField(label="Total", max_length=100)
    signature = forms.CharField(
        label="Name of person filling the questionnaire", max_length=100
    )
    name = forms.CharField(
        label="Nombre de la persona que suministra la información", max_length=100
    )
    title = forms.CharField(
        label="Título o posición que ocupa en la empresa", max_length=100
    )
    phone = forms.CharField(label="Teléfono", max_length=100)


class IP_440(forms.Form):
    company_name = forms.CharField(
        label="Nombre de la empresa / Company Name", max_length=100
    )
    address = forms.CharField(label="Dirección / Address", max_length=200)
    email = forms.EmailField(label="Correo electrónico / Email")
    liaison_officer = forms.CharField(
        label="Persona contacto / Liaison officer", max_length=100
    )
    ssn = forms.CharField(
        label="Numero de Seguro Social / Social Security Number", max_length=11
    )
    tel = forms.CharField(label="Tel", max_length=20)
    fax = forms.CharField(label="Fax", max_length=20)
    legal_form = forms.ChoiceField(
        label="Forma legal de organización / Legal form of organization",
        choices=[
            ("Corporación", "Corporación"),
            ("Sociedad", "Sociedad"),
            ("Cooperativa", "Cooperativa"),
            ("Empresa Individual", "Empresa Individual"),
            ("Empresa sin fines pecuniarios", "Empresa sin fines pecuniarios"),
        ],
    )
    cfc = forms.ChoiceField(label="CEC", choices=[("Si", "Si"), ("No", "No")])
    main_line = forms.CharField(
        label="Línea principal de negocio / Main line of business", max_length=100
    )
    business_type = forms.ChoiceField(
        label="5. Clase de negocio / Type of business:",
        choices=[
            ("Distribuidor", "Distribuidor"),
            ("Representante", "Representative"),
            ("Mayorista", "Wholesaler"),
            ("Supermercado", "Supermarket"),
        ],
    )
    other_business_type = forms.CharField(
        label="Otra clase de negocio / Other type of business", max_length=100
    )
    closing_date = forms.DateField(
        label="Fecha de cierre de sus libros / Your accounting period closing date",
        widget=forms.SelectDateWidget,
    )
    start_year = forms.CharField(
        label="Año de inicio de operaciones / Year of start of operations",
        max_length=100,
    )
    end_year = forms.CharField(
        label="Año de cierre de operaciones / Year of end of operations", max_length=100
    )
    sales_A_1 = forms.CharField(label="a. Ventas - Sales", max_length=100)
    sales_A_2 = forms.CharField(label="a. Ventas - Sales", max_length=100)
    people_A_1 = forms.CharField(label="b. A personas - To persons", max_length=100)
    people_A_2 = forms.CharField(label="b. A personas - To persons", max_length=100)
    industries_businesses_A_1 = forms.CharField(
        label="c. A industrias y negocios - To industries and businesses",
        max_length=100,
    )
    industries_businesses_A_2 = forms.CharField(
        label="c. A industrias y negocios - To industries and businesses",
        max_length=100,
    )
    less_cost_A_1 = forms.CharField(label="d. Menos costos - Less cost", max_length=100)
    less_cost_A_2 = forms.CharField(label="d. Menos costos - Less cost", max_length=100)
    inventory_beginning_1 = forms.CharField(
        label="Inventario al principio - Inventory at the beginning", max_length=100
    )
    inventory_beginning_2 = forms.CharField(
        label="Inventario al principio - Inventory at the beginning", max_length=100
    )
    purchases_A_1 = forms.CharField(
        label="a. Por Compra de maquinaria y equipo / On purchases of machinery and equipment",
        max_length=100,
    )
    purchases_A_2 = forms.CharField(
        label="a. Por Compra de maquinaria y equipo / On purchases of machinery and equipment",
        max_length=100,
    )
    inventory_end_1 = forms.CharField(
        label="Inventario al final - Inventory at the end", max_length=100
    )
    inventory_end_2 = forms.CharField(
        label="Inventario al final - Inventory at the end", max_length=100
    )
    gross_profit_A_1 = forms.CharField(
        label="3.Beneficio bruto (1 - 2) / Gross profit (1 - 2)", max_length=100
    )
    gross_profit_A_2 = forms.CharField(
        label="3.Beneficio bruto (1 - 2) / Gross profit (1 - 2)", max_length=100
    )
    other_income_A_1 = forms.CharField(
        label="4. Otros ingresos de operación / Other operationg income", max_length=100
    )
    other_income_A_2 = forms.CharField(
        label="4. Otros ingresos de operación / Other operationg income", max_length=100
    )
    interests_A_1 = forms.CharField(label="a. Intereses - Interests", max_length=100)
    interests_A_2 = forms.CharField(label="a. Intereses - Interests", max_length=100)
    rent_A_1 = forms.CharField(
        label="b. Renta de terreno y edificio / Rent of land and building",
        max_length=100,
    )
    rent_A_2 = forms.CharField(
        label="b. Renta de terreno y edificio / Rent of land and building",
        max_length=100,
    )
    capital_gain_A_1 = forms.CharField(
        label="c. Ganancia o pérdida de capital / Capital gain or loss", max_length=100
    )
    capital_gain_A_2 = forms.CharField(
        label="c. Ganancia o pérdida de capital / Capital gain or loss", max_length=100
    )
    dividends_A_1 = forms.CharField(label="d. Dividendos - Dividends", max_length=100)
    dividends_A_2 = forms.CharField(label="d. Dividendos - Dividends", max_length=100)
    other_A_1 = forms.CharField(label="e. Otros - Other", max_length=100)
    other_A_2 = forms.CharField(label="e. Otros - Other", max_length=100)
    total_gross_A_1 = forms.CharField(
        label="5. Total de ingresos brutos (3 + 4) / Total gross income (3 + 4)",
        max_length=100,
    )
    total_gross_A_2 = forms.CharField(
        label="5. Total de ingresos brutos (3 + 4) / Total gross income (3 + 4)",
        max_length=100,
    )
    expenses_1 = forms.CharField(
        label="B. total costos directos e indirectos - Direct and indirect costs",
        max_length=100,
    )
    expenses_2 = forms.CharField(
        label="B. total costos directos e indirectos - Direct and indirect costs",
        max_length=100,
    )
    salaries_1 = forms.CharField(
        label="1. Salario, jornales, bono de Navidad y comiciones / Salaries, wages, Christmas bonus and comissions",
        max_length=100,
    )
    salaries_2 = forms.CharField(
        label="1. Salario, jornales, bono de Navidad y comiciones / Salaries, wages, Christmas bonus and comissions",
        max_length=100,
    )
    expenses_interests_1 = forms.CharField(
        label="2. Intereses - Interests", max_length=100
    )
    expenses_interests_2 = forms.CharField(
        label="2. Intereses - Interests", max_length=100
    )
    expenses_rents_1 = forms.CharField(
        label="3. Renta de terreno y edificio - Rent of land and building",
        max_length=100,
    )
    expenses_rents_2 = forms.CharField(
        label="3. Renta de terreno y edificio - Rent of land and building",
        max_length=100,
    )
    depreciation_1 = forms.CharField(
        label="4. Depreciación - Depreciation", max_length=100
    )
    depreciation_2 = forms.CharField(
        label="4. Depreciación - Depreciation", max_length=100
    )
    bad_debts_1 = forms.CharField(
        label="5. Cuenta incobrables / bad debts", max_length=100
    )
    bad_debts_2 = forms.CharField(
        label="5. Cuenta incobrables / bad debts", max_length=100
    )
    donations_1 = forms.CharField(label="6. Donaciones - Donations", max_length=100)
    donations_2 = forms.CharField(label="6. Donaciones - Donations", max_length=100)
    sales_tax_1 = forms.CharField(
        label="7. Impuesto sobre la venta y uso / Sales and use tax", max_length=100
    )
    sales_tax_2 = forms.CharField(
        label="7. Impuesto sobre la venta y uso / Sales and use tax", max_length=100
    )
    machinery_1 = forms.CharField(
        label="a. Por Compra de maquinaria y equipo / On purchases of machinery and equipment",
        max_length=100,
    )
    machinery_2 = forms.CharField(
        label="a. Por Compra de maquinaria y equipo / On purchases of machinery and equipment",
        max_length=100,
    )
    other_purchases_1 = forms.CharField(
        label="b. Por otras compras / On other purchases", max_length=100
    )
    other_purchases_2 = forms.CharField(
        label="b. Por otras compras / On other purchases", max_length=100
    )
    licenses_1 = forms.CharField(
        label="8. Licencias y patentes - Licenses and patents", max_length=100
    )
    licenses_2 = forms.CharField(
        label="8. Licencias y patentes - Licenses and patents", max_length=100
    )
    other_expenses_1 = forms.CharField(
        label="9. Otras operaciones - Other operations", max_length=100
    )
    other_expenses_2 = forms.CharField(
        label="9. Otras operaciones - Other operations", max_length=100
    )
    total_expenses_1 = forms.CharField(
        label="10. Total de gastos (1-9) - Total expenses (1-9)", max_length=100
    )
    total_expenses_2 = forms.CharField(
        label="10. Total de gastos (1-9) - Total expenses (1-9)", max_length=100
    )
    net_profit_1 = forms.CharField(
        label="C. Beneficio neto (5 - 10) - Net profit (5 - 10)", max_length=100
    )
    net_profit_2 = forms.CharField(
        label="C. Beneficio neto (5 - 10) - Net profit (5 - 10)", max_length=100
    )
    income_tax_1 = forms.CharField(
        label="1. Contribución sobre ingresos / Income tax", max_length=100
    )
    income_tax_2 = forms.CharField(
        label="1. Contribución sobre ingresos / Income tax", max_length=100
    )
    profit_after_tax_1 = forms.CharField(
        label="2. Ganacia después de contribución sobre ingresos / Profit after income tax",
        max_length=100,
    )
    profit_after_tax_2 = forms.CharField(
        label="2. Ganacia después de contribución sobre ingresos / Profit after income tax",
        max_length=100,
    )
    sales_D_1 = forms.CharField(
        label="D. Impuesto sobre ventas y uso retenido / Sales and use tax Withheld",
        max_length=100,
    )
    sales_D_2 = forms.CharField(
        label="D. Impuesto sobre ventas y uso retenido / Sales and use tax Withheld",
        max_length=100,
    )
    name = forms.CharField(
        label="Nombre de persona que suministra la información Name of person furnishing information",
        max_length=100,
    )
    rank = forms.CharField(
        label="Nombre de persona que suministra la información Name of person furnishing information",
        max_length=100,
    )


class IP_440g(forms.Form):
    company_name = forms.CharField(
        label="Nombre compañía / Company Name", max_length=100
    )
    address = forms.CharField(label="Dirección / Address", max_length=200)
    email = forms.EmailField(label="Correo electrónico / Email")
    liaison_officer = forms.CharField(
        label="Persona contacto / Liaison officer", max_length=100
    )
    ssn = forms.CharField(
        label="Numero de Seguro Social / Social Security Number", max_length=11
    )
    tel = forms.CharField(label="Tel", max_length=20)
    fax = forms.CharField(label="Fax", max_length=20)
    legal_form = forms.ChoiceField(
        label="Forma legal de organización / Legal form of organization",
        choices=[
            ("Corporación", "Corporación"),
            ("Sociedad", "Sociedad"),
            ("Cooperativa", "Cooperativa"),
            ("Empresa Individual", "Empresa Individual"),
            ("Empresa sin fines pecuniarios", "Empresa sin fines pecuniarios"),
        ],
    )
    cfc = forms.ChoiceField(label="CEC", choices=[("Si", "Si"), ("No", "No")])
    end_month = forms.ChoiceField(
        label="Mes de cierre de sus libros / Your accounting period closing month",
        choices=[
            ("Enero", "Enero"),
            ("Febrero", "Febrero"),
            ("Marzo", "Marzo"),
            ("Abril", "Abril"),
            ("Mayo", "Mayo"),
            ("Junio", "Junio"),
            ("Julio", "Julio"),
            ("Agosto", "Agosto"),
            ("Septiembre", "Septiembre"),
            ("Octubre", "Octubre"),
            ("Noviembre", "Noviembre"),
            ("Diciembre", "Diciembre"),
        ],
    )

    sales_A_1 = forms.CharField(label="1. Ventas - Sales", max_length=100)
    sales_A_2 = forms.CharField(label="1. Ventas - Sales", max_length=100)

    fuel_A_1 = forms.CharField(label="a. Combustible / Fuel", max_length=100)
    fuel_A_2 = forms.CharField(label="a. Combustible / Fuel", max_length=100)

    other_products_A_1 = forms.CharField(
        label="b. Otros productos / Other products", max_length=100
    )
    other_products_A_2 = forms.CharField(
        label="b. Otros productos / Other products", max_length=100
    )

    less_cost_A_1 = forms.CharField(
        label="2. Menos costo de ventas - Less cost of sales", max_length=100
    )
    less_cost_A_2 = forms.CharField(
        label="2. Menos costo de ventas - Less cost of sales", max_length=100
    )

    inventory_beginning_1 = forms.CharField(
        label="a. Inventario al principio de año- Inventory at beginning of the year",
        max_length=100,
    )
    inventory_beginning_2 = forms.CharField(
        label="a. Inventario al principio de año- Inventory at beginning of the year",
        max_length=100,
    )

    purchases_A_1 = forms.CharField(label="b. Compras - Purchases", max_length=100)
    purchases_A_2 = forms.CharField(label="b. Compras - Purchases", max_length=100)

    inventory_end_1 = forms.CharField(
        label="c. Inventario al final año- Inventory at end of the year", max_length=100
    )
    inventory_end_2 = forms.CharField(
        label="c. Inventario al final año- Inventory at end of the year", max_length=100
    )

    gross_profit_A_1 = forms.CharField(
        label="3.Beneficio bruto (1 - 2) / Gross profit (1 - 2)", max_length=100
    )
    gross_profit_A_2 = forms.CharField(
        label="3.Beneficio bruto (1 - 2) / Gross profit (1 - 2)", max_length=100
    )

    other_income_A_1 = forms.CharField(
        label="4. Otros ingresos de operación / Other operationg income", max_length=100
    )
    other_income_A_2 = forms.CharField(
        label="4. Otros ingresos de operación / Other operationg income", max_length=100
    )

    interests_A_1 = forms.CharField(label="a. Intereses - Interests", max_length=100)
    interests_A_2 = forms.CharField(label="a. Intereses - Interests", max_length=100)

    rent_A_1 = forms.CharField(
        label="b. Renta de terreno y edificio / Rent of land and building",
        max_length=100,
    )
    rent_A_2 = forms.CharField(
        label="b. Renta de terreno y edificio / Rent of land and building",
        max_length=100,
    )

    capital_gain_A_1 = forms.CharField(
        label="c. Ganancia o pérdida de capital / Capital gain or loss", max_length=100
    )
    capital_gain_A_2 = forms.CharField(
        label="c. Ganancia o pérdida de capital / Capital gain or loss", max_length=100
    )

    dividends_A_1 = forms.CharField(label="d. Dividendos - Dividends", max_length=100)
    dividends_A_2 = forms.CharField(label="d. Dividendos - Dividends", max_length=100)
    
    others_A_1 = forms.CharField(label="e. Otros - Other", max_length=100)
    others_A_2 = forms.CharField(label="e. Otros - Other", max_length=100)

    total_gross_A_1 = forms.CharField(
        label="5. Total de ingresos brutos (3 + 4) / Total gross income (3 + 4)",
        max_length=100,
    )
    total_gross_A_2 = forms.CharField(
        label="5. Total de ingresos brutos (3 + 4) / Total gross income (3 + 4)",
        max_length=100,
    )

    cost_B_1 = forms.CharField(
        label="B. total costos directos e indirectos - Direct and indirect costs",
        max_length=100,
    )
    cost_B_2 = forms.CharField(
        label="B. total costos directos e indirectos - Direct and indirect costs",
        max_length=100,
    )

    salaries_B_1 = forms.CharField(
        label="1. Salario, jornales, bono de Navidad y comiciones / Salaries, wages, Christmas bonus and comissions",
        max_length=100,
    )
    salaries_B_2 = forms.CharField(
        label="1. Salario, jornales, bono de Navidad y comiciones / Salaries, wages, Christmas bonus and comissions",
        max_length=100,
    )

    interests_B_1 = forms.CharField(label="2. Intereses - Interests", max_length=100)
    interests_B_2 = forms.CharField(label="2. Intereses - Interests", max_length=100)

    depreciation_B_1 = forms.CharField(
        label="3. Depreciación - Depreciation", max_length=100
    )
    depreciation_B_2 = forms.CharField(
        label="3. Depreciación - Depreciation", max_length=100
    )

    rent_B_1 = forms.CharField(
        label="4. Renta de terreno y edificio - Rent of land and building",
        max_length=100,
    )
    rent_B_2 = forms.CharField(
        label="4. Renta de terreno y edificio - Rent of land and building",
        max_length=100,
    )

    bad_debts_B_1 = forms.CharField(
        label="5. Cuenta incobrables / bad debts", max_length=100
    )
    bad_debts_B_2 = forms.CharField(
        label="5. Cuenta incobrables / bad debts", max_length=100
    )

    donations_B_1 = forms.CharField(label="6. Donaciones - Donations", max_length=100)
    donations_B_2 = forms.CharField(label="6. Donaciones - Donations", max_length=100)

    sales_B_1 = forms.CharField(
        label="7. Impuesto sobre la venta y uso / Sales and use tax", max_length=100
    )
    sales_B_2 = forms.CharField(
        label="7. Impuesto sobre la venta y uso / Sales and use tax", max_length=100
    )

    purchases_B_1 = forms.CharField(
        label="a. Por Compra de maquinaria y equipo / On purchases of machinery and equipment",
        max_length=100,
    )
    purchases_B_2 = forms.CharField(
        label="a. Por Compra de maquinaria y equipo / On purchases of machinery and equipment",
        max_length=100,
    )

    other_purchases_B_1 = forms.CharField(
        label="b. Por otras compras / On other purchases", max_length=100
    )
    other_purchases_B_2 = forms.CharField(
        label="b. Por otras compras / On other purchases", max_length=100
    )

    licenses_B_1 = forms.CharField(
        label="8. Licencias y patentes - Licenses and patents", max_length=100
    )
    licenses_B_2 = forms.CharField(
        label="8. Licencias y patentes - Licenses and patents", max_length=100
    )

    other_operations_B_1 = forms.CharField(
        label="9. Otras operaciones - Other operations", max_length=100
    )
    other_operations_B_2 = forms.CharField(
        label="9. Otras operaciones - Other operations", max_length=100
    )

    total_operations_B_1 = forms.CharField(
        label="10. Total de gastos de operación", max_length=100
    )
    total_operations_B_2 = forms.CharField(
        label="10. Total de gastos de operación", max_length=100
    )

    net_profit_C_1 = forms.CharField(
        label="C. Ganacia o pérdida neta (+ ó -) / Net profit or loss (+ ó -)",
        max_length=100,
    )
    net_profit_C_2 = forms.CharField(
        label="C. Ganacia o pérdida neta (+ ó -) / Net profit or loss (+ ó -)",
        max_length=100,
    )

    income_C_1 = forms.CharField(
        label="1. Contribución sobre ingresos / Income tax", max_length=100
    )
    income_C_2 = forms.CharField(
        label="1. Contribución sobre ingresos / Income tax", max_length=100
    )

    profit_C_after_1 = forms.CharField(
        label="2. Ganacia después de contribución sobre ingresos / Profit after income tax",
        max_length=100,
    )
    profit_C_after_2 = forms.CharField(
        label="2. Ganacia después de contribución sobre ingresos / Profit after income tax",
        max_length=100,
    )

    sales_D_1 = forms.CharField(
        label="D. Impuesto sobre ventas y uso retenido / Sales and use tax Withheld",
        max_length=100,
    )
    sales_D_2 = forms.CharField(
        label="D. Impuesto sobre ventas y uso retenido / Sales and use tax Withheld",
        max_length=100,
    )

    name = forms.CharField(
        label="Nombre de persona que suministra la información Name of person furnishing information",
        max_length=100,
    )
    rank = forms.CharField(
        label="Rango o posición que ocupa en la empresa Rank or position",
        max_length=100,
    )


class IP_310b(forms.Form):
    MONTH_CHOICES = [
        ("mes", "mes"),
        ("enero", "enero"),
        ("febrero", "febrero"),
        ("marzo", "marzo"),
        ("abril", "abril"),
        ("mayo", "mayo"),
        ("junio", "junio"),
        ("julio", "julio"),
        ("agosto", "agosto"),
        ("septiembre", "septiembre"),
        ("octubre", "octubre"),
        ("noviembre", "noviembre"),
        ("diciembre", "diciembre"),
    ]

    company_name = forms.CharField(
        label="Nombre compañía / Company Name", max_length=100
    )
    address = forms.CharField(label="Dirección / Address", max_length=200)
    email = forms.EmailField(label="Correo electrónico / Email")
    liaison_officer = forms.CharField(
        label="Persona contacto / Liaison officer", max_length=100
    )
    ssn = forms.CharField(
        label="Numero de Seguro Social / Social Security Number", max_length=11
    )
    tel = forms.CharField(label="Tel", max_length=20)
    fax = forms.CharField(label="Fax", max_length=20)
    legal_form = forms.ChoiceField(
        label="Forma legal de organización / Legal form of organization",
        choices=[
            ("Corporación", "Corporación"),
            ("Sociedad", "Sociedad"),
            ("Cooperativa", "Cooperativa"),
            ("Empresa Individual", "Empresa Individual"),
            ("Empresa sin fines pecuniarios", "Empresa sin fines pecuniarios"),
        ],
    )
    cfc = forms.ChoiceField(label="CEC", choices=[("Si", "Si"), ("No", "No")])
    end_month = forms.ChoiceField(choices=MONTH_CHOICES, required=True)
    main_product_1 = forms.CharField(
        label="1. Producto principal - Main product", max_length=100
    )
    main_product_2 = forms.CharField(
        label="1. Producto principal - Main product", max_length=100
    )
    raw_material_used = forms.CharField(
        label="2. Materia prima utilizada - Raw material used", max_length=100
    )
    closing_date = forms.DateField(
        label="Fecha de cierre de sus libros / Your accounting period closing date",
        widget=forms.SelectDateWidget,
    )
    start_year = forms.CharField(
        label="Año de inicio de operaciones / Year of start of operations",
        max_length=100,
    )
    end_year = forms.CharField(
        label="Año de cierre de operaciones / Year of end of operations", max_length=100
    )
    products_manufactured_1 = forms.CharField(
        label="3. Productos manufacturados - Manufactured products", max_length=100
    )
    products_manufactured_2 = forms.CharField(
        label="3. Productos manufacturados - Manufactured products", max_length=100
    )
    rum_1 = forms.CharField(label="4. Ron - Rum", max_length=100)
    rum_2 = forms.CharField(label="4. Ron - Rum", max_length=100)
    beer_1 = forms.CharField(label="5. Cerveza - Beer", max_length=100)
    beer_2 = forms.CharField(label="5. Cerveza - Beer", max_length=100)
    malt_1 = forms.CharField(label="6. Malta - Malt", max_length=100)
    malt_2 = forms.CharField(label="6. Malta - Malt", max_length=100)
    soft_drinks_1 = forms.CharField(label="7. Refrescos - Soft drinks", max_length=100)
    soft_drinks_2 = forms.CharField(label="7. Refrescos - Soft drinks", max_length=100)
    others_1 = forms.CharField(label="8. Otros - Others", max_length=100)
    others_2 = forms.CharField(label="8. Otros - Others", max_length=100)
    goods_acquired_1 = forms.CharField(
        label="9. Bienes adquiridos - Goods acquired", max_length=100
    )
    goods_acquired_2 = forms.CharField(
        label="9. Bienes adquiridos - Goods acquired", max_length=100
    )
    wines_1 = forms.CharField(label="10. Vinos - Wines", max_length=100)
    wines_2 = forms.CharField(label="10. Vinos - Wines", max_length=100)
    soft_drinks_3 = forms.CharField(label="11. Refrescos - Soft drinks", max_length=100)
    soft_drinks_4 = forms.CharField(label="11. Refrescos - Soft drinks", max_length=100)
    whiskey_1 = forms.CharField(label="12. Whiskey - Whiskey", max_length=100)
    whiskey_2 = forms.CharField(label="12. Whiskey - Whiskey", max_length=100)
    brandy_1 = forms.CharField(label="13. Brandy - Brandy", max_length=100)
    brandy_2 = forms.CharField(label="13. Brandy - Brandy", max_length=100)
    other_3 = forms.CharField(label="14. Otros - Others", max_length=100)
    other_4 = forms.CharField(label="14. Otros - Others", max_length=100)
    manufacturing_cost_1 = forms.CharField(
        label="15. Costo de manufactura - Manufacturing cost", max_length=100
    )
    manufacturing_cost_2 = forms.CharField(
        label="15. Costo de manufactura - Manufacturing cost", max_length=100
    )
    inventories_begginning_1 = forms.CharField(
        label="16. Inventario al principio - Inventory at the beginning", max_length=100
    )
    inventories_begginning_2 = forms.CharField(
        label="16. Inventario al principio - Inventory at the beginning", max_length=100
    )
    purchases_1 = forms.CharField(label="17. Compras - Purchases", max_length=100)
    purchases_2 = forms.CharField(label="17. Compras - Purchases", max_length=100)
    total_raw_1 = forms.CharField(
        label="18. Total de materia prima - Total raw material", max_length=100
    )
    total_raw_2 = forms.CharField(
        label="18. Total de materia prima - Total raw material", max_length=100
    )
    imported_1 = forms.CharField(label="a. Importada - Imported", max_length=100)
    imported_2 = forms.CharField(label="a. Importada - Imported", max_length=100)
    others_5 = forms.CharField(label="b. Otras - Other", max_length=100)
    others_6 = forms.CharField(label="b. Otras - Other", max_length=100)
    direct_wages_1 = forms.CharField(
        label="19. Salarios directos - Direct wages", max_length=100
    )
    direct_wages_2 = forms.CharField(
        label="19. Salarios directos - Direct wages", max_length=100
    )
    depreciation_1 = forms.CharField(
        label="20. Depreciación - Depreciation", max_length=100
    )
    depreciation_2 = forms.CharField(
        label="20. Depreciación - Depreciation", max_length=100
    )
    rent_land_1 = forms.CharField(
        label="21. Renta de terreno - Rent of land", max_length=100
    )
    rent_land_2 = forms.CharField(
        label="21. Renta de terreno - Rent of land", max_length=100
    )
    other_direct_1 = forms.CharField(
        label="22. Otros costos directos - Other direct costs", max_length=100
    )
    other_direct_2 = forms.CharField(
        label="22. Otros costos directos - Other direct costs", max_length=100
    )
    indirect_cost_1 = forms.CharField(
        label="23. Costos indirectos - Indirect costs", max_length=100
    )
    indirect_cost_2 = forms.CharField(
        label="23. Costos indirectos - Indirect costs", max_length=100
    )
    inventories_end_1 = forms.CharField(
        label="24. Inventario al final - Inventory at the end", max_length=100
    )
    inventories_end_2 = forms.CharField(
        label="24. Inventario al final - Inventory at the end", max_length=100
    )
    gross_profit_1 = forms.CharField(
        label="25. Utilidad bruta - Gross profit", max_length=100
    )
    gross_profit_2 = forms.CharField(
        label="25. Utilidad bruta - Gross profit", max_length=100
    )
    other_operating_1 = forms.CharField(
        label="26. Otros ingresos - Other income", max_length=100
    )
    other_operating_2 = forms.CharField(
        label="26. Otros ingresos - Other income", max_length=100
    )
    interest_1 = forms.CharField(label="27. Intereses - Interests", max_length=100)
    interest_2 = forms.CharField(label="27. Intereses - Interests", max_length=100)
    rent_land_3 = forms.CharField(
        label="28. Renta de terreno - Rent of land", max_length=100
    )
    rent_land_4 = forms.CharField(
        label="28. Renta de terreno - Rent of land", max_length=100
    )
    capital_gain_1 = forms.CharField(
        label="29. Ganancia de capital - Capital gain", max_length=100
    )
    capital_gain_2 = forms.CharField(
        label="29. Ganancia de capital - Capital gain", max_length=100
    )
    other_1 = forms.CharField(label="30. Otros - Other", max_length=100)
    other_2 = forms.CharField(label="30. Otros - Other", max_length=100)
    total_gross_1 = forms.CharField(
        label="31. Total de utilidad bruta - Total gross profit", max_length=100
    )
    total_gross_2 = forms.CharField(
        label="31. Total de utilidad bruta - Total gross profit", max_length=100
    )
    expenses_not_1 = forms.CharField(
        label="32. Gastos no operacionales - Non-operating expenses", max_length=100
    )
    expenses_not_2 = forms.CharField(
        label="32. Gastos no operacionales - Non-operating expenses", max_length=100
    )
    salaries_1 = forms.CharField(label="33. Salarios - Salaries", max_length=100)
    salaries_2 = forms.CharField(label="33. Salarios - Salaries", max_length=100)
    interest_3 = forms.CharField(label="34. Intereses - Interests", max_length=100)
    interest_4 = forms.CharField(label="34. Intereses - Interests", max_length=100)
    depreciation_3 = forms.CharField(
        label="35. Depreciación - Depreciation", max_length=100
    )
    depreciation_4 = forms.CharField(
        label="35. Depreciación - Depreciation", max_length=100
    )
    donations_1 = forms.CharField(label="36. Donativos - Donations", max_length=100)
    donations_2 = forms.CharField(label="36. Donativos - Donations", max_length=100)
    rent_land_5 = forms.CharField(
        label="37. Renta de terreno - Rent of land", max_length=100
    )
    rent_land_6 = forms.CharField(
        label="37. Renta de terreno - Rent of land", max_length=100
    )
    excise_taxes_1 = forms.CharField(
        label="38. Impuestos de consumo - Excise taxes", max_length=100
    )
    excise_taxes_2 = forms.CharField(
        label="38. Impuestos de consumo - Excise taxes", max_length=100
    )
    other_operating_3 = forms.CharField(
        label="39. Otros gastos operacionales - Other operating expenses",
        max_length=100,
    )
    other_operating_4 = forms.CharField(
        label="39. Otros gastos operacionales - Other operating expenses",
        max_length=100,
    )
    sales_tax_1 = forms.CharField(
        label="40. Impuesto sobre la venta y uso - Sales and use tax", max_length=100
    )
    sales_tax_2 = forms.CharField(
        label="40. Impuesto sobre la venta y uso - Sales and use tax", max_length=100
    )
    machinery_1 = forms.CharField(
        label="41. Compra de maquinaria - Purchase of machinery", max_length=100
    )
    machinery_2 = forms.CharField(
        label="41. Compra de maquinaria - Purchase of machinery", max_length=100
    )
    on_other_1 = forms.CharField(label="42. Otras - Other", max_length=100)
    on_other_2 = forms.CharField(label="42. Otras - Other", max_length=100)
    licenses_1 = forms.CharField(label="43. Licencias - Licenses", max_length=100)
    licenses_2 = forms.CharField(label="43. Licencias - Licenses", max_length=100)
    net_loss_1 = forms.CharField(label="44. Pérdida neta - Net loss", max_length=100)
    net_loss_2 = forms.CharField(label="44. Pérdida neta - Net loss", max_length=100)
    income_tax_1 = forms.CharField(
        label="45. Contribución sobre ingresos - Income tax", max_length=100
    )
    income_tax_2 = forms.CharField(
        label="45. Contribución sobre ingresos - Income tax", max_length=100
    )
    profit_after_tax_1 = forms.CharField(
        label="46. Ganancia después de contribución sobre ingresos - Profit after income tax",
        max_length=100,
    )
    profit_after_tax_2 = forms.CharField(
        label="46. Ganancia después de contribución sobre ingresos - Profit after income tax",
        max_length=100,
    )
    sales_and_use_withheld_1 = forms.CharField(
        label="47. Impuesto sobre la venta y uso retenido - Sales and use tax withheld",
        max_length=100,
    )
    sales_and_use_withheld_2 = forms.CharField(
        label="47. Impuesto sobre la venta y uso retenido - Sales and use tax withheld",
        max_length=100,
    )
    branches = forms.ChoiceField(label="CEC", choices=[("Si", "Si"), ("No", "No")])
    branches_if_yes = forms.ChoiceField(
        label="En caso afirmativo indique si:",
        choices=[
            (
                "La información suministrada cubre todas las sucursales./The information provided includes all branches.",
                "La información suministrada cubre todas las sucursales./The information provided includes all branches.",
            ),
            (
                "La información suministrada cubre este establecimiento solamente./The information provided covers only the firm responding to this questionnaire.",
                "La información suministrada cubre este establecimiento solamente./The information provided covers only the firm responding to this questionnaire.",
            ),
        ],
    )
    signature = forms.CharField(
        label="Name of person filling the questionnaire", max_length=100
    )
    rank = forms.CharField(label="Rank", max_length=100)


class IP_480a(forms.Form):
    company_name = forms.CharField(
        label="Nombre compañía / Company Name", max_length=100
    )
    address = forms.CharField(label="Dirección / Address", max_length=200)
    email = forms.EmailField(label="Correo electrónico / Email")
    liaison_officer = forms.CharField(
        label="Persona contacto / Liaison officer", max_length=100
    )
    ssn = forms.CharField(
        label="Numero de Seguro Social / Social Security Number", max_length=11
    )
    tel = forms.CharField(label="Tel", max_length=20)
    fax = forms.CharField(label="Fax", max_length=20)
    business_function = forms.CharField(
        label="Función de negocio / Business function", max_length=100
    )
    legal_form = forms.ChoiceField(
        label="Forma legal de organización / Legal form of organization",
        choices=[
            ("Corporación", "Corporación"),
            ("Sociedad", "Sociedad"),
            ("Cooperativa", "Cooperativa"),
            ("Empresa Individual", "Empresa Individual"),
            ("Empresa sin fines pecuniarios", "Empresa sin fines pecuniarios"),
        ],
    )
    cfc = forms.ChoiceField(label="CEC", choices=[("Si", "Si"), ("No", "No")])
    closing_date = forms.DateField(
        label="Fecha de cierre de sus libros / Your accounting period closing date",
        widget=forms.SelectDateWidget,
    )
    start_year = forms.CharField(
        label="Año de inicio de operaciones / Year of start of operations",
        max_length=100,
    )
    end_year = forms.CharField(
        label="Año de cierre de operaciones / Year of end of operations", max_length=100
    )
    people_A_1 = forms.CharField(label="1. Personas - People", max_length=100)
    people_A_2 = forms.CharField(label="1. Personas - People", max_length=100)
    industries_businesses_A_1 = forms.CharField(
        label="2. Industrias y negocios - Industries and businesses", max_length=100
    )
    industries_businesses_A_2 = forms.CharField(
        label="2. Industrias y negocios - Industries and businesses", max_length=100
    )
    passenger_fares_1 = forms.CharField(
        label="3. Tarifas de pasajeros - Passenger fares", max_length=100
    )
    passenger_fares_2 = forms.CharField(
        label="3. Tarifas de pasajeros - Passenger fares", max_length=100
    )
    freight_1 = forms.CharField(label="4. Fletes - Freight", max_length=100)
    freight_2 = forms.CharField(label="4. Fletes - Freight", max_length=100)
    ship_USA_1 = forms.CharField(label="5. Barcos USA - Ships USA", max_length=100)
    ship_USA_2 = forms.CharField(label="5. Barcos USA - Ships USA", max_length=100)
    ship_VIRGISLND_1 = forms.CharField(
        label="6. Barcos Islas Vírgenes - Ships Virgin Islands", max_length=100
    )
    ship_VIRGISLND_2 = forms.CharField(
        label="6. Barcos Islas Vírgenes - Ships Virgin Islands", max_length=100
    )
    SHIP_fORECNTY_1 = forms.CharField(
        label="7. Barcos de otros países - Ships from other countries", max_length=100
    )
    SHIP_fORECNTY_2 = forms.CharField(
        label="7. Barcos de otros países - Ships from other countries", max_length=100
    )
    income_interest_1 = forms.CharField(
        label="8. Ingresos por intereses - Income from interests", max_length=100
    )
    income_interest_2 = forms.CharField(
        label="8. Ingresos por intereses - Income from interests", max_length=100
    )
    income_rent_1 = forms.CharField(
        label="9. Ingresos por renta - Income from rent", max_length=100
    )
    income_rent_2 = forms.CharField(
        label="9. Ingresos por renta - Income from rent", max_length=100
    )
    commissions_1 = forms.CharField(
        label="10. Comisiones - Commissions", max_length=100
    )
    commissions_2 = forms.CharField(
        label="10. Comisiones - Commissions", max_length=100
    )
    capital_gain_loss_1 = forms.CharField(
        label="11. Ganancia o pérdida de capital - Capital gain or loss", max_length=100
    )
    capital_gain_loss_2 = forms.CharField(
        label="11. Ganancia o pérdida de capital - Capital gain or loss", max_length=100
    )
    other_incomes_1 = forms.CharField(
        label="12. Otros ingresos - Other incomes", max_length=100
    )
    other_incomes_2 = forms.CharField(
        label="12. Otros ingresos - Other incomes", max_length=100
    )
    total_incomes_1 = forms.CharField(
        label="13. Total de ingresos (1-12) - Total incomes (1-12)", max_length=100
    )
    total_incomes_2 = forms.CharField(
        label="13. Total de ingresos (1-12) - Total incomes (1-12)", max_length=100
    )
    expenses_1 = forms.CharField(label="14. Gastos - Expenses", max_length=100)
    expenses_2 = forms.CharField(label="14. Gastos - Expenses", max_length=100)
    salaries_1 = forms.CharField(label="1. Salarios - Salaries", max_length=100)
    salaries_2 = forms.CharField(label="1. Salarios - Salaries", max_length=100)
    commissions_employees_1 = forms.CharField(
        label="2. Comisiones a empleados - Commissions to employees", max_length=100
    )
    commissions_employees_2 = forms.CharField(
        label="2. Comisiones a empleados - Commissions to employees", max_length=100
    )
    commissions_independent_1 = forms.CharField(
        label="3. Comisiones a independientes - Commissions to independent",
        max_length=100,
    )
    commissions_independent_2 = forms.CharField(
        label="3. Comisiones a independientes - Commissions to independent",
        max_length=100,
    )
    expenses_interests_1 = forms.CharField(
        label="4. Gastos por intereses - Expenses by interests", max_length=100
    )
    expenses_interests_2 = forms.CharField(
        label="4. Gastos por intereses - Expenses by interests", max_length=100
    )
    expenses_rents_1 = forms.CharField(
        label="5. Gastos por rentas - Expenses by rents", max_length=100
    )
    expenses_rents_2 = forms.CharField(
        label="5. Gastos por rentas - Expenses by rents", max_length=100
    )
    depreciation_1 = forms.CharField(
        label="6. Depreciación - Depreciation", max_length=100
    )
    depreciation_2 = forms.CharField(
        label="6. Depreciación - Depreciation", max_length=100
    )
    bad_debts_1 = forms.CharField(
        label="7. Cuentas incobrables - Bad debts", max_length=100
    )
    bad_debts_2 = forms.CharField(
        label="7. Cuentas incobrables - Bad debts", max_length=100
    )
    donations_1 = forms.CharField(label="8. Donaciones - Donations", max_length=100)
    donations_2 = forms.CharField(label="8. Donaciones - Donations", max_length=100)
    sales_tax_1 = forms.CharField(
        label="9. Impuesto sobre ventas y uso - Sales and use tax", max_length=100
    )
    sales_tax_2 = forms.CharField(
        label="9. Impuesto sobre ventas y uso - Sales and use tax", max_length=100
    )
    machinery_1 = forms.CharField(
        label="10. Compra de maquinaria - Purchase of machinery", max_length=100
    )
    machinery_2 = forms.CharField(
        label="10. Compra de maquinaria - Purchase of machinery", max_length=100
    )
    other_purchases_1 = forms.CharField(
        label="11. Otras compras - Other purchases", max_length=100
    )
    other_purchases_2 = forms.CharField(
        label="11. Otras compras - Other purchases", max_length=100
    )
    licenses_1 = forms.CharField(label="12. Licencias - Licenses", max_length=100)
    licenses_2 = forms.CharField(label="12. Licencias - Licenses", max_length=100)
    other_expenses_1 = forms.CharField(
        label="13. Otros gastos - Other expenses", max_length=100
    )
    other_expenses_2 = forms.CharField(
        label="13. Otros gastos - Other expenses", max_length=100
    )
    total_expenses_1 = forms.CharField(
        label="14. Total de gastos (1-13) - Total expenses (1-13)", max_length=100
    )
    total_expenses_2 = forms.CharField(
        label="14. Total de gastos (1-13) - Total expenses (1-13)", max_length=100
    )
    net_profit_1 = forms.CharField(
        label="15. Ganancia neta (13-14) - Net profit (13-14)", max_length=100
    )
    net_profit_2 = forms.CharField(
        label="15. Ganancia neta (13-14) - Net profit (13-14)", max_length=100
    )
    income_tax_1 = forms.CharField(
        label="16. Contribución sobre ingresos - Income tax", max_length=100
    )
    income_tax_2 = forms.CharField(
        label="16. Contribución sobre ingresos - Income tax", max_length=100
    )
    profit_after_tax_1 = forms.CharField(
        label="17. Ganancia después de contribución sobre ingresos - Profit after income tax",
        max_length=100,
    )
    profit_after_tax_2 = forms.CharField(
        label="17. Ganancia después de contribución sobre ingresos - Profit after income tax",
        max_length=100,
    )
    withheld_tax_1 = forms.CharField(
        label="18. Impuesto sobre ventas y uso retenido - Sales and use tax withheld",
        max_length=100,
    )
    withheld_tax_2 = forms.CharField(
        label="18. Impuesto sobre ventas y uso retenido - Sales and use tax withheld",
        max_length=100,
    )
    signature = forms.CharField(
        label="Name of person filling the questionnaire", max_length=100
    )
    rank = forms.CharField(label="Rank", max_length=100)


class JP_529(forms.Form):
    year1 = forms.CharField(label="Año / Year", max_length=100)
    year2 = forms.CharField(label="Año / Year", max_length=100)
    company = forms.CharField(label="Nombre de la Compañía", max_length=100)
    address = forms.CharField(label="Dirección", max_length=100)
    email = forms.EmailField(label="Correo Electrónico")
    liaison_officer = forms.CharField(label="Persona de Contacto", max_length=100)
    tel = forms.CharField(label="Teléfono", max_length=100)
    choice = forms.ChoiceField(label="choice", choices=[("Si", "Si"), ("No", "No")])
    agencia = forms.CharField(label="Agencia", max_length=100)
    agencia2 = forms.CharField(label="Agencia1", max_length=100)
    instuition1 = forms.CharField(label="Institución1", max_length=100)
    instuition2 = forms.CharField(label="Institución2", max_length=100)
    instuition3 = forms.CharField(label="Institución3", max_length=100)
    instuition4 = forms.CharField(label="Institución4", max_length=100)
    instuition5 = forms.CharField(label="Institución5", max_length=100)
    instuition6 = forms.CharField(label="Institución6", max_length=100)
    instuition7 = forms.CharField(label="Institución7", max_length=100)
    instuition8 = forms.CharField(label="Institución8", max_length=100)
    instuition9 = forms.CharField(label="Institución9", max_length=100)
    instuition10 = forms.CharField(label="Institución10", max_length=100)
    money1 = forms.CharField(label="Money1", max_length=100)
    money2 = forms.CharField(label="Money2", max_length=100)
    money3 = forms.CharField(label="Money3", max_length=100)
    money4 = forms.CharField(label="Money4", max_length=100)
    money5 = forms.CharField(label="Money5", max_length=100)
    money6 = forms.CharField(label="Money6", max_length=100)
    money7 = forms.CharField(label="Money7", max_length=100)
    money8 = forms.CharField(label="Money8", max_length=100)
    money9 = forms.CharField(label="Money9", max_length=100)
    money10 = forms.CharField(label="Money10", max_length=100)
    date1 = forms.CharField(label="Date1", max_length=100)
    date2 = forms.CharField(label="Date2", max_length=100)
    date3 = forms.CharField(label="Date3", max_length=100)
    date4 = forms.CharField(label="Date4", max_length=100)
    date5 = forms.CharField(label="Date5", max_length=100)
    date6 = forms.CharField(label="Date6", max_length=100)
    date7 = forms.CharField(label="Date7", max_length=100)
    date8 = forms.CharField(label="Date8", max_length=100)
    date9 = forms.CharField(label="Date9", max_length=100)
    date10 = forms.CharField(label="Date10", max_length=100)
    name = forms.CharField(label="Nombre", max_length=100)
    puesto = forms.CharField(label="Puesto", max_length=100)
    date = forms.CharField(label="Date", max_length=100)


class IP_490(forms.Form):
    company_name = forms.CharField(
        label="Nombre compañía / Company Name", max_length=100
    )
    address = forms.CharField(label="Dirección / Address", max_length=200)
    email = forms.EmailField(label="Correo electrónico / Email")
    liaison_officer = forms.CharField(
        label="Persona contacto / Liaison officer", max_length=100
    )
    ssn = forms.CharField(
        label="Numero de Seguro Social / Social Security Number", max_length=11
    )
    tel = forms.CharField(label="Tel", max_length=20)
    fax = forms.CharField(label="Fax", max_length=20)
    legal_form = forms.ChoiceField(
        label="Forma legal de organización / Legal form of organization",
        choices=[
            ("Corporación", "Corporación"),
            ("Sociedad", "Sociedad"),
            ("Cooperativa", "Cooperativa"),
            ("Empresa Individual", "Empresa Individual"),
            ("Empresa sin fines pecuniarios", "Empresa sin fines pecuniarios"),
        ],
    )
    cfc = forms.ChoiceField(label="CEC", choices=[("Si", "Si"), ("No", "No")])
    business_type = forms.CharField(
        label="Tipo de negocio / Business type", max_length=100
    )
    business_function = forms.CharField(
        label="Función de negocio / Business function", max_length=100
    )
    closing_date = forms.DateField(
        label="Fecha de cierre de sus libros / Your accounting period closing date",
        widget=forms.SelectDateWidget,
    )
    start_year = forms.CharField(
        label="Año de inicio de operaciones / Year of start of operations",
        max_length=100,
    )
    end_year = forms.CharField(
        label="Año de cierre de operaciones / Year of end of operations", max_length=100
    )
    income_operations_1 = forms.CharField(
        label="1. Ingresos por operaciones - Income from operations", max_length=100
    )
    income_operations_2 = forms.CharField(
        label="1. Ingresos por operaciones - Income from operations", max_length=100
    )
    people_A_1 = forms.CharField(label="2. Personas - People", max_length=100)
    people_A_2 = forms.CharField(label="2. Personas - People", max_length=100)
    industries_businesses_A_1 = forms.CharField(
        label="3. Industrias y negocios - Industries and businesses", max_length=100
    )
    industries_businesses_A_2 = forms.CharField(
        label="3. Industrias y negocios - Industries and businesses", max_length=100
    )
    interest_A_1 = forms.CharField(label="4. Intereses - Interests", max_length=100)
    interest_A_2 = forms.CharField(label="4. Intereses - Interests", max_length=100)
    rent_land_1 = forms.CharField(
        label="5. Renta de terreno - Rent of land", max_length=100
    )
    rent_land_2 = forms.CharField(
        label="5. Renta de terreno - Rent of land", max_length=100
    )
    capital_gain_1 = forms.CharField(
        label="6. Ganancia de capital - Capital gain", max_length=100
    )
    capital_gain_2 = forms.CharField(
        label="6. Ganancia de capital - Capital gain", max_length=100
    )
    other_income_A_1 = forms.CharField(
        label="7. Otros ingresos - Other income", max_length=100
    )
    other_income_A_2 = forms.CharField(
        label="7. Otros ingresos - Other income", max_length=100
    )
    total_income_A_1 = forms.CharField(
        label="8. Total de ingresos (1-7) - Total income (1-7)", max_length=100
    )
    total_income_A_2 = forms.CharField(
        label="8. Total de ingresos (1-7) - Total income (1-7)", max_length=100
    )
    salaries_wages_bonus_B_1 = forms.CharField(
        label="1. Salarios, sueldos y bonificaciones - Salaries, wages and bonuses",
        max_length=100,
    )
    salaries_wages_bonus_B_2 = forms.CharField(
        label="1. Salarios, sueldos y bonificaciones - Salaries, wages and bonuses",
        max_length=100,
    )
    interests_B_1 = forms.CharField(label="2. Intereses - Interests", max_length=100)
    interests_B_2 = forms.CharField(label="2. Intereses - Interests", max_length=100)
    rent_B_1 = forms.CharField(label="3. Renta - Rent", max_length=100)
    rent_B_2 = forms.CharField(label="3. Renta - Rent", max_length=100)
    depreciation_B_1 = forms.CharField(
        label="4. Depreciación - Depreciation", max_length=100
    )
    depreciation_B_2 = forms.CharField(
        label="4. Depreciación - Depreciation", max_length=100
    )
    donation_B_1 = forms.CharField(label="5. Donaciones - Donations", max_length=100)
    donation_B_2 = forms.CharField(label="5. Donaciones - Donations", max_length=100)
    sales_taxes_B_1 = forms.CharField(
        label="6. Impuesto sobre ventas y uso - Sales and use tax", max_length=100
    )
    sales_taxes_B_2 = forms.CharField(
        label="6. Impuesto sobre ventas y uso - Sales and use tax", max_length=100
    )
    purchases_B_1 = forms.CharField(label="7. Compras - Purchases", max_length=100)
    purchases_B_2 = forms.CharField(label="7. Compras - Purchases", max_length=100)
    other_purchases_B_1 = forms.CharField(
        label="8. Otras compras - Other purchases", max_length=100
    )
    other_purchases_B_2 = forms.CharField(
        label="8. Otras compras - Other purchases", max_length=100
    )
    other_operations_B_1 = forms.CharField(
        label="9. Otras operaciones - Other operations", max_length=100
    )
    other_operations_B_2 = forms.CharField(
        label="9. Otras operaciones - Other operations", max_length=100
    )
    total_expenses_B_1 = forms.CharField(
        label="10. Total de gastos (1-9) - Total expenses (1-9)", max_length=100
    )
    total_expenses_B_2 = forms.CharField(
        label="10. Total de gastos (1-9) - Total expenses (1-9)", max_length=100
    )
    net_profit_1 = forms.CharField(
        label="11. Ganancia neta (8-10) - Net profit (8-10)", max_length=100
    )
    net_profit_2 = forms.CharField(
        label="11. Ganancia neta (8-10) - Net profit (8-10)", max_length=100
    )
    income_C_1 = forms.CharField(
        label="12. Contribución sobre ingresos - Income tax", max_length=100
    )
    income_C_2 = forms.CharField(
        label="12. Contribución sobre ingresos - Income tax", max_length=100
    )
    profit_C_after_1 = forms.CharField(
        label="13. Ganacia después de contribución sobre ingresos - Profit after income tax",
        max_length=100,
    )
    profit_C_after_2 = forms.CharField(
        label="13. Ganacia después de contribución sobre ingresos - Profit after income tax",
        max_length=100,
    )
    sales_D_1 = forms.CharField(
        label="14. Impuesto sobre ventas y uso retenido - Sales and use tax withheld",
        max_length=100,
    )
    sales_D_2 = forms.CharField(
        label="14. Impuesto sobre ventas y uso retenido - Sales and use tax withheld",
        max_length=100,
    )
    name = forms.CharField(
        label="Name of person filling the questionnaire", max_length=100
    )
    rank = forms.CharField(label="Rank", max_length=100)


class IP_520(forms.Form):
    company_name = forms.CharField(
        label="Nombre compañía / Company Name", max_length=100
    )
    address = forms.CharField(label="Dirección / Address", max_length=200)
    email = forms.EmailField(label="Correo electrónico / Email")
    liaison_officer = forms.CharField(
        label="Persona contacto / Liaison officer", max_length=100
    )

    ssn = forms.CharField(
        label="Numero de Seguro Social / Social Security Number", max_length=11
    )
    tel = forms.CharField(label="Tel", max_length=20)
    fax = forms.CharField(label="Fax", max_length=20)

    legal_form = forms.ChoiceField(
        label="Forma legal de organización / Legal form of organization",
        choices=[
            ("Corporación", "Corporación"),
            ("Sociedad", "Sociedad"),
            ("Cooperativa", "Cooperativa"),
            ("Empresa Individual", "Empresa Individual"),
            ("Empresa sin fines pecuniarios", "Empresa sin fines pecuniarios"),
        ],
    )
    cfc = forms.ChoiceField(label="CEC", choices=[("Si", "Si"), ("No", "No")])
    business_type = forms.CharField(
        label="Tipo de negocio / Business type", max_length=100
    )
    closing_date = forms.DateField(
        label="Fecha de cierre de sus libros / Your accounting period closing date",
        widget=forms.SelectDateWidget,
    )
    branches = forms.CharField(label="Sucursales / Branches", max_length=100)
    start_year = forms.CharField(
        label="Año de inicio de operaciones / Year of start of operations",
        max_length=100,
    )
    end_year = forms.CharField(
        label="Año de cierre de operaciones / Year of end of operations", max_length=100
    )

    incomes_interests_1 = forms.CharField(
        label="1. Ingresos por intereses - Income from interests", max_length=100
    )
    incomes_interests_2 = forms.CharField(
        label="1. Ingresos por intereses - Income from interests", max_length=100
    )
    incomes_personal_loans_1 = forms.CharField(
        label="2. Ingresos por préstamos personales - Income from personal loans",
        max_length=100,
    )
    incomes_personal_loans_2 = forms.CharField(
        label="2. Ingresos por préstamos personales - Income from personal loans",
        max_length=100,
    )
    incomes_mortage_loans_1 = forms.CharField(
        label="3. Ingresos por préstamos hipotecarios - Income from mortage loans",
        max_length=100,
    )
    incomes_mortage_loans_2 = forms.CharField(
        label="3. Ingresos por préstamos hipotecarios - Income from mortage loans",
        max_length=100,
    )
    incomes_other_1 = forms.CharField(label="4. Otros - Other", max_length=100)
    incomes_other_2 = forms.CharField(label="4. Otros - Other", max_length=100)
    incomes_rent_1 = forms.CharField(
        label="5. Ingresos por renta - Income from rent", max_length=100
    )
    incomes_rent_2 = forms.CharField(
        label="5. Ingresos por renta - Income from rent", max_length=100
    )
    incomes_dividends_1 = forms.CharField(
        label="6. Ingresos por dividendos - Income from dividends", max_length=100
    )
    incomes_dividends_2 = forms.CharField(
        label="6. Ingresos por dividendos - Income from dividends", max_length=100
    )
    incomes_financing_charges_1 = forms.CharField(
        label="7. Cargos por financiamiento - Financing charges", max_length=100
    )
    incomes_financing_charges_2 = forms.CharField(
        label="7. Cargos por financiamiento - Financing charges", max_length=100
    )
    incomes_service_charges_1 = forms.CharField(
        label="8. Cargos por servicios - Service charges", max_length=100
    )
    incomes_service_charges_2 = forms.CharField(
        label="8. Cargos por servicios - Service charges", max_length=100
    )
    incomes_commissions_1 = forms.CharField(
        label="9. Comisiones - Commissions", max_length=100
    )
    incomes_commissions_2 = forms.CharField(
        label="9. Comisiones - Commissions", max_length=100
    )
    incomes_finance_leasing_1 = forms.CharField(
        label="10. Financiamiento de arrendamiento - Finance leasing", max_length=100
    )
    incomes_finance_leasing_2 = forms.CharField(
        label="10. Financiamiento de arrendamiento - Finance leasing", max_length=100
    )
    incomes_capital_gain_loss_1 = forms.CharField(
        label="11. Ganancia o pérdida de capital - Capital gain or loss", max_length=100
    )
    incomes_capital_gain_loss_2 = forms.CharField(
        label="11. Ganancia o pérdida de capital - Capital gain or loss", max_length=100
    )
    incomes_other_operations_1 = forms.CharField(
        label="12. Otras operaciones - Other operations", max_length=100
    )
    incomes_other_operations_2 = forms.CharField(
        label="12. Otras operaciones - Other operations", max_length=100
    )
    incomes_total_1 = forms.CharField(
        label="13. Total de ingresos (1-12) - Total incomes (1-12)", max_length=100
    )
    incomes_total_2 = forms.CharField(
        label="13. Total de ingresos (1-12) - Total incomes (1-12)", max_length=100
    )
    expenses_salaries_wages_bonus_1 = forms.CharField(
        label="1. Salarios, sueldos y bonificaciones - Salaries, wages and bonuses",
        max_length=100,
    )
    expenses_salaries_wages_bonus_2 = forms.CharField(
        label="1. Salarios, sueldos y bonificaciones - Salaries, wages and bonuses",
        max_length=100,
    )
    expenses_interests_1 = forms.CharField(
        label="2. Intereses - Interests", max_length=100
    )
    expenses_interests_2 = forms.CharField(
        label="2. Intereses - Interests", max_length=100
    )
    interests_to_individuals_1 = forms.CharField(
        label="3. Intereses a individuos - Interests to individuals", max_length=100
    )
    interests_to_individuals_2 = forms.CharField(
        label="3. Intereses a individuos - Interests to individuals", max_length=100
    )
    interests_to_corporations_1 = forms.CharField(
        label="4. Intereses a corporaciones - Interests to corporations", max_length=100
    )
    interests_to_corporations_2 = forms.CharField(
        label="4. Intereses a corporaciones - Interests to corporations", max_length=100
    )
    corporation_936_1 = forms.CharField(
        label="4. Corporación 936 - Corporation 936", max_length=100
    )
    corporation_936_2 = forms.CharField(
        label="4. Corporación 936 - Corporation 936", max_length=100
    )
    other_corporation_1 = forms.CharField(
        label="5. Otra corporación - Other corporation", max_length=100
    )
    other_corporation_2 = forms.CharField(
        label="5. Otra corporación - Other corporation", max_length=100
    )
    interests_other_1 = forms.CharField(
        label="6. Intereses a otros - Interests to other", max_length=100
    )
    interests_other_2 = forms.CharField(
        label="6. Intereses a otros - Interests to other", max_length=100
    )
    expenses_rent_1 = forms.CharField(label="7. Renta - Rent", max_length=100)
    expenses_rent_2 = forms.CharField(label="7. Renta - Rent", max_length=100)
    expenses_depreciation_1 = forms.CharField(
        label="8. Depreciación - Depreciation", max_length=100
    )
    expenses_depreciation_2 = forms.CharField(
        label="8. Depreciación - Depreciation", max_length=100
    )
    expenses_bad_debts_1 = forms.CharField(
        label="9. Cuentas incobrables - Bad debts", max_length=100
    )
    expenses_bad_debts_2 = forms.CharField(
        label="9. Cuentas incobrables - Bad debts", max_length=100
    )
    expenses_donations_1 = forms.CharField(
        label="10. Donativos - Donations", max_length=100
    )
    expenses_donations_2 = forms.CharField(
        label="10. Donativos - Donations", max_length=100
    )
    expenses_sales_taxes_1 = forms.CharField(
        label="11. Impuestos de ventas - Sales taxes", max_length=100
    )
    expenses_sales_taxes_2 = forms.CharField(
        label="11. Impuestos de ventas - Sales taxes", max_length=100
    )
    expenses_machinary_1 = forms.CharField(
        label="12. Compra de maquinaria - Purchase of machinery", max_length=100
    )
    expenses_machinary_2 = forms.CharField(
        label="12. Compra de maquinaria - Purchase of machinery", max_length=100
    )
    expenses_other_purchases_1 = forms.CharField(
        label="13. Otras compras - Other purchases", max_length=100
    )
    expenses_other_purchases_2 = forms.CharField(
        label="13. Otras compras - Other purchases", max_length=100
    )
    expenses_licenses_1 = forms.CharField(
        label="14. Licencias - Licenses", max_length=100
    )
    expenses_licenses_2 = forms.CharField(
        label="14. Licencias - Licenses", max_length=100
    )
    expenses_other_operations_1 = forms.CharField(
        label="15. Otras operaciones - Other operations", max_length=100
    )
    expenses_other_operations_2 = forms.CharField(
        label="15. Otras operaciones - Other operations", max_length=100
    )
    expenses_total_1 = forms.CharField(
        label="16. Total de gastos (1-15) - Total expenses (1-15)", max_length=100
    )
    expenses_total_2 = forms.CharField(
        label="16. Total de gastos (1-15) - Total expenses (1-15)", max_length=100
    )
    gross_profit_1 = forms.CharField(
        label="17. Ganancia bruta (13-16) - Gross profit (13-16)", max_length=100
    )
    gross_profit_2 = forms.CharField(
        label="17. Ganancia bruta (13-16) - Gross profit (13-16)", max_length=100
    )
    profit_income_tax_1 = forms.CharField(
        label="18. Contribución sobre ingresos - Income tax", max_length=100
    )
    profit_income_tax_2 = forms.CharField(
        label="18. Contribución sobre ingresos - Income tax", max_length=100
    )
    profit_after_income_tax_1 = forms.CharField(
        label="19. Ganancia después de contribución sobre ingresos - Profit after income tax",
        max_length=100,
    )
    profit_after_income_tax_2 = forms.CharField(
        label="19. Ganancia después de contribución sobre ingresos - Profit after income tax",
        max_length=100,
    )
    dividends_paid_1 = forms.CharField(
        label="20. Dividendos pagados - Dividends paid", max_length=100
    )
    dividends_paid_2 = forms.CharField(
        label="20. Dividendos pagados - Dividends paid", max_length=100
    )
    sales_tax_1 = forms.CharField(
        label="21. Impuesto sobre ventas y uso retenido - Sales and use tax withheld",
        max_length=100,
    )
    sales_tax_2 = forms.CharField(
        label="21. Impuesto sobre ventas y uso retenido - Sales and use tax withheld",
        max_length=100,
    )

    name = forms.CharField(
        label="Name of person filling the questionnaire", max_length=100
    )
    rank = forms.CharField(label="Rank", max_length=100)


class JP_536_2(forms.Form):
    start_year = forms.CharField(label="Año / Year", max_length=100)
    end_year = forms.CharField(label="Año / Year", max_length=100)
    inventario1 = forms.CharField(label="Inventario1", max_length=100)
    inventario2 = forms.CharField(label="Inventario2", max_length=100)
    compras1 = forms.CharField(label="Compras1", max_length=100)
    compras2 = forms.CharField(label="Compras2", max_length=100)
    depre1 = forms.CharField(label="Depre1", max_length=100)
    depre2 = forms.CharField(label="Depre2", max_length=100)
    maquinaria1 = forms.CharField(label="Maquinaria1", max_length=100)
    maquinaria2 = forms.CharField(label="Maquinaria2", max_length=100)
    equipo1 = forms.CharField(label="Equipo1", max_length=100)
    equipo2 = forms.CharField(label="Equipo2", max_length=100)
    computadora1 = forms.CharField(label="Computadora1", max_length=100)
    computadora2 = forms.CharField(label="Computadora2", max_length=100)
    alquiler1 = forms.CharField(label="Alquiler1", max_length=100)
    alquiler2 = forms.CharField(label="Alquiler2", max_length=100)
    licencia1 = forms.CharField(label="Licencia1", max_length=100)
    licencia2 = forms.CharField(label="Licencia2", max_length=100)
    company_name = forms.CharField(label="Nombre", max_length=100)
    phone = forms.CharField(label="Teléfono", max_length=100)
    name_title = forms.CharField(label="Título", max_length=100)
    date = forms.CharField(label="Fecha", max_length=100)


class IP_510(forms.Form):
    company_name = forms.CharField(
        label="Nombre compañía / Company Name", max_length=100
    )
    address = forms.CharField(label="Dirección / Address", max_length=200)
    email = forms.EmailField(label="Correo electrónico / Email")
    liaison_officer = forms.CharField(
        label="Persona contacto / Liaison officer", max_length=100
    )
    ssn = forms.CharField(
        label="Numero de Seguro Social / Social Security Number", max_length=11
    )
    tel = forms.CharField(label="Tel", max_length=20)
    fax = forms.CharField(label="Fax", max_length=20)
    legal_form = forms.ChoiceField(
        label="Forma legal de organización / Legal form of organization",
        choices=[
            ("Corporación", "Corporación"),
            ("Sociedad", "Sociedad"),
            ("Cooperativa", "Cooperativa"),
            ("Empresa Individual", "Empresa Individual"),
            ("Empresa sin fines pecuniarios", "Empresa sin fines pecuniarios"),
        ],
    )
    cfc = forms.ChoiceField(label="CEC", choices=[("Si", "Si"), ("No", "No")])
    accounting_period = forms.CharField(
        label="Período contable / Accounting period", max_length=100
    )
    main_product_1 = forms.CharField(
        label="Producto principal 1 / Main product 1", max_length=100
    )
    main_product_2 = forms.CharField(
        label="Producto principal 2 / Main product 2", max_length=100
    )
    raw_material_used = forms.CharField(
        label="Materia prima utilizada / Raw material used", max_length=100
    )
    closing_date = forms.DateField(
        label="Fecha de cierre de sus libros / Your accounting period closing date",
        widget=forms.SelectDateWidget,
    )
    start_year = forms.CharField(
        label="Año de inicio de operaciones / Year of start of operations",
        max_length=100,
    )
    end_year = forms.CharField(
        label="Año de cierre de operaciones / Year of end of operations", max_length=100
    )
    sales_from_persons_1 = forms.CharField(
        label="1. Ventas de personas - Sales from persons", max_length=100
    )
    sales_from_persons_2 = forms.CharField(
        label="1. Ventas de personas - Sales from persons", max_length=100
    )
    sales_industries_businesses_1 = forms.CharField(
        label="2. Ventas de industrias y negocios - Sales from industries and businesses",
        max_length=100,
    )
    sales_industries_businesses_2 = forms.CharField(
        label="2. Ventas de industrias y negocios - Sales from industries and businesses",
        max_length=100,
    )
    sales_goods_1 = forms.CharField(
        label="3. Ventas de bienes - Sales of goods", max_length=100
    )
    sales_goods_2 = forms.CharField(
        label="3. Ventas de bienes - Sales of goods", max_length=100
    )
    sales_exports_goods_1 = forms.CharField(
        label="4. Ventas de bienes exportados - Sales of exported goods", max_length=100
    )
    sales_exports_goods_2 = forms.CharField(
        label="4. Ventas de bienes exportados - Sales of exported goods", max_length=100
    )
    sales_goods_from_others_firms_1 = forms.CharField(
        label="5. Ventas de bienes de otras firmas - Sales of goods from other firms",
        max_length=100,
    )
    sales_goods_from_others_firms_2 = forms.CharField(
        label="5. Ventas de bienes de otras firmas - Sales of goods from other firms",
        max_length=100,
    )
    sales_exports_goods_other_firms_1 = forms.CharField(
        label="6. Ventas de bienes exportados de otras firmas - Sales of exported goods from other firms",
        max_length=100,
    )
    sales_exports_goods_other_firms_2 = forms.CharField(
        label="6. Ventas de bienes exportados de otras firmas - Sales of exported goods from other firms",
        max_length=100,
    )
    total_cost_1 = forms.CharField(
        label="7. Costo total (1-6) - Total cost (1-6)", max_length=100
    )
    total_cost_2 = forms.CharField(
        label="7. Costo total (1-6) - Total cost (1-6)", max_length=100
    )
    total_cost_inventories_begginning_1 = forms.CharField(
        label="8. Costo total de inventarios al principio - Total cost of inventories at the beginning",
        max_length=100,
    )
    total_cost_inventories_begginning_2 = forms.CharField(
        label="8. Costo total de inventarios al principio - Total cost of inventories at the beginning",
        max_length=100,
    )
    total_cost_purchases_1 = forms.CharField(
        label="9. Costo total de compras - Total cost of purchases", max_length=100
    )
    total_cost_purchases_2 = forms.CharField(
        label="9. Costo total de compras - Total cost of purchases", max_length=100
    )
    total_cost_total_raw_1 = forms.CharField(
        label="10. Costo total de materia prima - Total cost of raw material",
        max_length=100,
    )
    total_cost_total_raw_2 = forms.CharField(
        label="10. Costo total de materia prima - Total cost of raw material",
        max_length=100,
    )
    total_cost_imported_1 = forms.CharField(
        label="11. Costo total de importaciones - Total cost of imports", max_length=100
    )
    total_cost_imported_2 = forms.CharField(
        label="11. Costo total de importaciones - Total cost of imports", max_length=100
    )
    total_cost_others_1 = forms.CharField(
        label="12. Costo total de otros - Total cost of others", max_length=100
    )
    total_cost_others_2 = forms.CharField(
        label="12. Costo total de otros - Total cost of others", max_length=100
    )
    total_cost_direct_wages_1 = forms.CharField(
        label="13. Costo total de salarios directos - Total cost of direct wages",
        max_length=100,
    )
    total_cost_direct_wages_2 = forms.CharField(
        label="13. Costo total de salarios directos - Total cost of direct wages",
        max_length=100,
    )
    total_cost_depreciation_1 = forms.CharField(
        label="14. Costo total de depreciación - Total cost of depreciation",
        max_length=100,
    )
    total_cost_depreciation_2 = forms.CharField(
        label="14. Costo total de depreciación - Total cost of depreciation",
        max_length=100,
    )
    total_cost_rent_land_1 = forms.CharField(
        label="15. Costo total de renta de terreno - Total cost of rent of land",
        max_length=100,
    )
    total_cost_rent_land_2 = forms.CharField(
        label="15. Costo total de renta de terreno - Total cost of rent of land",
        max_length=100,
    )
    total_cost_other_direct_1 = forms.CharField(
        label="16. Costo total de otros directos - Total cost of other direct",
        max_length=100,
    )
    total_cost_other_direct_2 = forms.CharField(
        label="16. Costo total de otros directos - Total cost of other direct",
        max_length=100,
    )
    total_cost_indirect_cost_1 = forms.CharField(
        label="17. Costo total de costos indirectos - Total cost of indirect costs",
        max_length=100,
    )
    total_cost_indirect_cost_2 = forms.CharField(
        label="17. Costo total de costos indirectos - Total cost of indirect costs",
        max_length=100,
    )
    total_cost_inventories_end_1 = forms.CharField(
        label="18. Costo total de inventarios al final - Total cost of inventories at the end",
        max_length=100,
    )
    total_cost_inventories_end_2 = forms.CharField(
        label="18. Costo total de inventarios al final - Total cost of inventories at the end",
        max_length=100,
    )
    gross_profit_1 = forms.CharField(
        label="19. Ganancia bruta (7-18) - Gross profit (7-18)", max_length=100
    )
    gross_profit_2 = forms.CharField(
        label="19. Ganancia bruta (7-18) - Gross profit (7-18)", max_length=100
    )
    other_operating_1 = forms.CharField(
        label="20. Otras operaciones - Other operating", max_length=100
    )
    other_operating_2 = forms.CharField(
        label="20. Otras operaciones - Other operating", max_length=100
    )
    other_operating_interest_1 = forms.CharField(
        label="21. Intereses - Interests", max_length=100
    )
    other_operating_interest_2 = forms.CharField(
        label="21. Intereses - Interests", max_length=100
    )
    other_operating_rent_land_1 = forms.CharField(
        label="22. Renta de terreno - Rent of land", max_length=100
    )
    other_operating_rent_land_2 = forms.CharField(
        label="22. Renta de terreno - Rent of land", max_length=100
    )
    other_operating_capital_gain_1 = forms.CharField(
        label="23. Ganancia de capital - Capital gain", max_length=100
    )
    other_operating_capital_gain_2 = forms.CharField(
        label="23. Ganancia de capital - Capital gain", max_length=100
    )
    other_operating_other_1 = forms.CharField(label="24. Otros - Other", max_length=100)
    other_operating_other_2 = forms.CharField(label="24. Otros - Other", max_length=100)
    total_gross_1 = forms.CharField(
        label="25. Total bruto (19-24) - Total gross (19-24)", max_length=100
    )
    total_gross_2 = forms.CharField(
        label="25. Total bruto (19-24) - Total gross (19-24)", max_length=100
    )
    expenses_not_included_1 = forms.CharField(
        label="26. Gastos no incluidos - Expenses not included", max_length=100
    )
    expenses_not_included_2 = forms.CharField(
        label="26. Gastos no incluidos - Expenses not included", max_length=100
    )
    expenses_not_included_salaries_1 = forms.CharField(
        label="27. Salarios - Salaries", max_length=100
    )
    expenses_not_included_salaries_2 = forms.CharField(
        label="27. Salarios - Salaries", max_length=100
    )
    expenses_not_included_interest_1 = forms.CharField(
        label="28. Intereses - Interests", max_length=100
    )
    expenses_not_included_interest_2 = forms.CharField(
        label="28. Intereses - Interests", max_length=100
    )
    expenses_not_included_depreciation_1 = forms.CharField(
        label="29. Depreciación - Depreciation", max_length=100
    )
    expenses_not_included_depreciation_2 = forms.CharField(
        label="29. Depreciación - Depreciation", max_length=100
    )
    expenses_not_included_donations_1 = forms.CharField(
        label="30. Donaciones - Donations", max_length=100
    )
    expenses_not_included_donations_2 = forms.CharField(
        label="30. Donaciones - Donations", max_length=100
    )
    expenses_not_included_rent_land_1 = forms.CharField(
        label="31. Renta de terreno - Rent of land", max_length=100
    )
    expenses_not_included_rent_land_2 = forms.CharField(
        label="31. Renta de terreno - Rent of land", max_length=100
    )
    expenses_not_included_other_operating_1 = forms.CharField(
        label="32. Otras operaciones - Other operating", max_length=100
    )
    expenses_not_included_other_operating_2 = forms.CharField(
        label="32. Otras operaciones - Other operating", max_length=100
    )
    expenses_not_included_sales_tax_1 = forms.CharField(
        label="33. Impuesto sobre ventas y uso - Sales tax", max_length=100
    )
    expenses_not_included_sales_tax_2 = forms.CharField(
        label="33. Impuesto sobre ventas y uso - Sales tax", max_length=100
    )
    expenses_not_included_machinery_1 = forms.CharField(
        label="34. Compra de maquinaria - Purchase of machinery", max_length=100
    )
    expenses_not_included_machinery_2 = forms.CharField(
        label="34. Compra de maquinaria - Purchase of machinery", max_length=100
    )
    expenses_not_included_on_other_1 = forms.CharField(
        label="35. Gastos no incluidos en otros - Expenses not included on other",
        max_length=100,
    )
    expenses_not_included_on_other_2 = forms.CharField(
        label="35. Gastos no incluidos en otros - Expenses not included on other",
        max_length=100,
    )
    expenses_not_included_licenses_1 = forms.CharField(
        label="36. Licencias - Licenses", max_length=100
    )
    expenses_not_included_licenses_2 = forms.CharField(
        label="36. Licencias - Licenses", max_length=100
    )
    net_profit_loss_1 = forms.CharField(
        label="37. Ganancia neta o pérdida (25-36) - Net profit or loss (25-36)",
        max_length=100,
    )
    net_profit_loss_2 = forms.CharField(
        label="37. Ganancia neta o pérdida (25-36) - Net profit or loss (25-36)",
        max_length=100,
    )
    net_profit_loss_income_tax_1 = forms.CharField(
        label="38. Ganancia neta o pérdida después de contribución sobre ingresos - Net profit or loss after income tax",
        max_length=100,
    )
    net_profit_loss_income_tax_2 = forms.CharField(
        label="38. Ganancia neta o pérdida después de contribución sobre ingresos - Net profit or loss after income tax",
        max_length=100,
    )
    profit_after_tax_1 = forms.CharField(
        label="39. Ganancia después de contribución sobre ingresos - Profit after income tax",
        max_length=100,
    )
    profit_after_tax_2 = forms.CharField(
        label="39. Ganancia después de contribución sobre ingresos - Profit after income tax",
        max_length=100,
    )
    sales_and_use_withheld_1 = forms.CharField(
        label="40. Impuesto sobre ventas y uso retenido - Sales and use tax withheld",
        max_length=100,
    )
    sales_and_use_withheld_2 = forms.CharField(
        label="40. Impuesto sobre ventas y uso retenido - Sales and use tax withheld",
        max_length=100,
    )
    branches = forms.ChoiceField(
        label="Sucursales / Branches", choices=[("Si", "Si"), ("No", "No")]
    )
    branches_if_yes = forms.CharField(
        label="Si si, cuantas / If yes, how many", max_length=100
    )
    name = forms.CharField(
        label="Name of person filling the questionnaire", max_length=100
    )
    rank = forms.CharField(label="Rank", max_length=100)


class IP_520a(forms.Form):
    company_name = forms.CharField(
        label="Nombre compañía / Company Name", max_length=100
    )
    address = forms.CharField(label="Dirección / Address", max_length=200)
    email = forms.EmailField(label="Correo electrónico / Email")
    liaison_officer = forms.CharField(
        label="Persona contacto / Liaison officer", max_length=100
    )
    ssn = forms.CharField(
        label="Numero de Seguro Social / Social Security Number", max_length=11
    )
    tel = forms.CharField(label="Tel", max_length=20)
    fax = forms.CharField(label="Fax", max_length=20)
    legal_form = forms.ChoiceField(
        label="¿Cómo practica su profesión? -  How do you operate?",
        choices=[
            ("Privately", "Privately"),
            ("As employee", "As employee"),
            ("Both", "Both"),
        ],
    )
    cfc = forms.ChoiceField(label="CEC", choices=[("Si", "Si"), ("No", "No")])
    start_month = forms.CharField(
        label="Mes de inicio de operaciones / Month of start of operations",
        max_length=100,
    )
    start_year = forms.CharField(
        label="Año de inicio de operaciones / Year of start of operations",
        max_length=100,
    )
    end_year = forms.CharField(
        label="Año de cierre de operaciones / Year of end of operations", max_length=100
    )
    incomes_services_fee_1 = forms.CharField(
        label="1. Ingresos por servicios - Income from services", max_length=100
    )
    incomes_services_fee_2 = forms.CharField(
        label="1. Ingresos por servicios - Income from services", max_length=100
    )
    incomes_comissions_1 = forms.CharField(
        label="2. Comisiones - Commissions", max_length=100
    )
    incomes_comissions_2 = forms.CharField(
        label="2. Comisiones - Commissions", max_length=100
    )
    incomes_rent_1 = forms.CharField(
        label="3. Ingresos por renta - Income from rent", max_length=100
    )
    incomes_rent_2 = forms.CharField(
        label="3. Ingresos por renta - Income from rent", max_length=100
    )
    incomes_interest_1 = forms.CharField(
        label="4. Ingresos por intereses - Income from interests", max_length=100
    )
    incomes_interest_2 = forms.CharField(
        label="4. Ingresos por intereses - Income from interests", max_length=100
    )
    incomes_capital_gain_loss_1 = forms.CharField(
        label="5. Ganancia o pérdida de capital - Capital gain or loss", max_length=100
    )
    incomes_capital_gain_loss_2 = forms.CharField(
        label="5. Ganancia o pérdida de capital - Capital gain or loss", max_length=100
    )
    incomes_other_operating_1 = forms.CharField(
        label="6. Otras operaciones - Other operating", max_length=100
    )
    incomes_other_operating_2 = forms.CharField(
        label="6. Otras operaciones - Other operating", max_length=100
    )
    incomes_total_1 = forms.CharField(
        label="7. Total de ingresos (1-6) - Total incomes (1-6)", max_length=100
    )
    incomes_total_2 = forms.CharField(
        label="7. Total de ingresos (1-6) - Total incomes (1-6)", max_length=100
    )
    expenses_1 = forms.CharField(label="1. Gastos - Expenses", max_length=100)
    expenses_2 = forms.CharField(label="1. Gastos - Expenses", max_length=100)
    expenses_salaries_wages_bonus_1 = forms.CharField(
        label="2. Salarios, sueldos y bonificaciones - Salaries, wages and bonuses",
        max_length=100,
    )
    expenses_salaries_wages_bonus_2 = forms.CharField(
        label="2. Salarios, sueldos y bonificaciones - Salaries, wages and bonuses",
        max_length=100,
    )
    expenses_commissions_1 = forms.CharField(
        label="3. Comisiones - Commissions", max_length=100
    )
    expenses_commissions_2 = forms.CharField(
        label="3. Comisiones - Commissions", max_length=100
    )
    expenses_interests_1 = forms.CharField(
        label="4. Intereses - Interests", max_length=100
    )
    expenses_interests_2 = forms.CharField(
        label="4. Intereses - Interests", max_length=100
    )
    expenses_rent_1 = forms.CharField(label="5. Renta - Rent", max_length=100)
    expenses_rent_2 = forms.CharField(label="5. Renta - Rent", max_length=100)
    expenses_depreciation_1 = forms.CharField(
        label="6. Depreciación - Depreciation", max_length=100
    )
    expenses_depreciation_2 = forms.CharField(
        label="6. Depreciación - Depreciation", max_length=100
    )
    expenses_donation_1 = forms.CharField(
        label="7. Donativos - Donations", max_length=100
    )
    expenses_donation_2 = forms.CharField(
        label="7. Donativos - Donations", max_length=100
    )
    expenses_sales_tax_1 = forms.CharField(
        label="8. Impuesto sobre ventas - Sales tax", max_length=100
    )
    expenses_sales_tax_2 = forms.CharField(
        label="8. Impuesto sobre ventas - Sales tax", max_length=100
    )
    expenses_machinary_1 = forms.CharField(
        label="9. Compra de maquinaria - Purchase of machinery", max_length=100
    )
    expenses_machinary_2 = forms.CharField(
        label="9. Compra de maquinaria - Purchase of machinery", max_length=100
    )
    expenses_other_purchases_1 = forms.CharField(
        label="10. Otras compras - Other purchases", max_length=100
    )
    expenses_other_purchases_2 = forms.CharField(
        label="10. Otras compras - Other purchases", max_length=100
    )
    expenses_licenses_1 = forms.CharField(
        label="11. Licencias - Licenses", max_length=100
    )
    expenses_licenses_2 = forms.CharField(
        label="11. Licencias - Licenses", max_length=100
    )
    expenses_other_operation_1 = forms.CharField(
        label="12. Otras operaciones - Other operations", max_length=100
    )
    expenses_other_operation_2 = forms.CharField(
        label="12. Otras operaciones - Other operations", max_length=100
    )
    expenses_total_1 = forms.CharField(
        label="13. Total de gastos (1-12) - Total expenses (1-12)", max_length=100
    )
    expenses_total_2 = forms.CharField(
        label="13. Total de gastos (1-12) - Total expenses (1-12)", max_length=100
    )
    net_profit_loss_1 = forms.CharField(
        label="14. Ganancia neta o pérdida (7-13) - Net profit or loss (7-13)",
        max_length=100,
    )
    net_profit_loss_2 = forms.CharField(
        label="14. Ganancia neta o pérdida (7-13) - Net profit or loss (7-13)",
        max_length=100,
    )
    sales_tax_withheld_1 = forms.CharField(
        label="15. Impuesto sobre ventas y uso retenido - Sales and use tax withheld",
        max_length=100,
    )
    sales_tax_withheld_2 = forms.CharField(
        label="15. Impuesto sobre ventas y uso retenido - Sales and use tax withheld",
        max_length=100,
    )
    percent_local_enterprises = forms.CharField(
        label="16. Porciento de empresas locales - Percent of local enterprises",
        max_length=100,
    )
    percent_foreign_enterprises = forms.CharField(
        label="17. Porciento de empresas extranjeras - Percent of foreign enterprises",
        max_length=100,
    )
    name = forms.CharField(
        label="Name of person filling the questionnaire", max_length=100
    )
    rank = forms.CharField(label="Rank", max_length=100)


class JP_544(forms.Form):
    institucion1 = forms.CharField(label="Institución 1", max_length=100)
    proposito1 = forms.CharField(label="Propósito 1", max_length=100)
    dolares1 = forms.CharField(label="Dólares 1", max_length=100)

    institucion2 = forms.CharField(label="Institución 2", max_length=100)
    proposito2 = forms.CharField(label="Propósito 2", max_length=100)
    dolares2 = forms.CharField(label="Dólares 2", max_length=100)

    institucion3 = forms.CharField(label="Institución 3", max_length=100)
    proposito3 = forms.CharField(label="Propósito 3", max_length=100)
    dolares3 = forms.CharField(label="Dólares 3", max_length=100)

    institucion4 = forms.CharField(label="Institución 4", max_length=100)
    proposito4 = forms.CharField(label="Propósito 4", max_length=100)
    dolares4 = forms.CharField(label="Dólares 4", max_length=100)

    institucion5 = forms.CharField(label="Institución 5", max_length=100)
    proposito5 = forms.CharField(label="Propósito 5", max_length=100)
    dolares5 = forms.CharField(label="Dólares 5", max_length=100)

    institucion6 = forms.CharField(label="Institución 6", max_length=100)
    proposito6 = forms.CharField(label="Propósito 6", max_length=100)
    dolares6 = forms.CharField(label="Dólares 6", max_length=100)

    institucion7 = forms.CharField(label="Institución 7", max_length=100)
    proposito7 = forms.CharField(label="Propósito 7", max_length=100)
    dolares7 = forms.CharField(label="Dólares 7", max_length=100)

    institucion8 = forms.CharField(label="Institución 8", max_length=100)
    proposito8 = forms.CharField(label="Propósito 8", max_length=100)
    dolares8 = forms.CharField(label="Dólares 8", max_length=100)

    institucion9 = forms.CharField(label="Institución 9", max_length=100)
    proposito9 = forms.CharField(label="Propósito 9", max_length=100)
    dolares9 = forms.CharField(label="Dólares 9", max_length=100)

    institucion10 = forms.CharField(label="Institución 10", max_length=100)
    proposito10 = forms.CharField(label="Propósito 10", max_length=100)
    dolares10 = forms.CharField(label="Dólares 10", max_length=100)

    institucion11 = forms.CharField(label="Institución 11", max_length=100)
    proposito11 = forms.CharField(label="Propósito 11", max_length=100)
    dolares11 = forms.CharField(label="Dólares 11", max_length=100)

    institucion12 = forms.CharField(label="Institución 12", max_length=100)
    proposito12 = forms.CharField(label="Propósito 12", max_length=100)
    dolares12 = forms.CharField(label="Dólares 12", max_length=100)

    institucion13 = forms.CharField(label="Institución 13", max_length=100)
    proposito13 = forms.CharField(label="Propósito 13", max_length=100)
    dolares13 = forms.CharField(label="Dólares 13", max_length=100)

    institucion14 = forms.CharField(label="Institución 14", max_length=100)
    proposito14 = forms.CharField(label="Propósito 14", max_length=100)
    dolares14 = forms.CharField(label="Dólares 14", max_length=100)

    operation_expenses = forms.CharField(
        label="Gastos de operación - Operation expenses", max_length=100
    )
    salary = forms.CharField(label="Salario - Salary", max_length=100)
    SS_SD_SR_beneficios_marginales = forms.CharField(
        label="Beneficios marginales de SS, SD, SR - Marginal benefits of SS, SD, SR",
        max_length=100,
    )
    servicios_profecionales_c = forms.CharField(
        label="Servicios profesionales - Professional services", max_length=100
    )
    intereses = forms.CharField(label="Intereses - Interests", max_length=100)
    other_gastos = forms.CharField(
        label="Otros gastos - Other expenses", max_length=100
    )
    to_people = forms.CharField(label="A personas - To people", max_length=100)
    servicios_profecionales_a = forms.CharField(
        label="Servicios profesionales - Professional services", max_length=100
    )
    pensiones = forms.CharField(label="Pensiones - Pensions", max_length=100)
    name_other_1 = forms.CharField(label="Nombre - Name", max_length=100)
    quantity_other_1 = forms.CharField(label="Cantidad - Quantity", max_length=100)
    name_other_2 = forms.CharField(label="Nombre - Name", max_length=100)
    quantity_other_2 = forms.CharField(label="Cantidad - Quantity", max_length=100)
    name_other_3 = forms.CharField(label="Nombre - Name", max_length=100)
    quantity_other_3 = forms.CharField(label="Cantidad - Quantity", max_length=100)
    name_other_4 = forms.CharField(label="Nombre - Name", max_length=100)
    quantity_other_4 = forms.CharField(label="Cantidad - Quantity", max_length=100)
    agencia = forms.CharField(label="Agencia - Agency", max_length=100)
    prep = forms.CharField(label="Preparado por - Prepared by", max_length=100)
    titulo = forms.CharField(label="Título - Title", max_length=100)
    telefono = forms.CharField(label="Teléfono - Phone", max_length=100)
    fecha = forms.CharField(label="Fecha - Date", max_length=100)


class IP_520s(forms.Form):
    company_name = forms.CharField(
        label="Nombre compañía / Company Name", max_length=100
    )
    address = forms.CharField(label="Dirección / Address", max_length=200)
    email = forms.EmailField(label="Correo electrónico / Email")
    liaison_officer = forms.CharField(
        label="Persona contacto / Liaison officer", max_length=100
    )
    ssn = forms.CharField(
        label="Numero de Seguro Social / Social Security Number", max_length=11
    )
    tel = forms.CharField(label="Tel", max_length=20)
    fax = forms.CharField(label="Fax", max_length=20)
    legal_form = forms.ChoiceField(
        label="Forma legal de organización / Legal form of organization",
        choices=[
            ("Corporación", "Corporación"),
            ("Sociedad", "Sociedad"),
            ("Cooperativa", "Cooperativa"),
            ("Empresa Individual", "Empresa Individual"),
            ("Empresa sin fines pecuniarios", "Empresa sin fines pecuniarios"),
        ],
    )
    cfc = forms.ChoiceField(label="CEC", choices=[("Si", "Si"), ("No", "No")])
    business_type = forms.ChoiceField(
        label="5. Clase de negocio / Type of business:",
        choices=[
            ("Corredor", "Broker"),
            ("Agente no general", "Non-general agent"),
            ("Agente general", "General agent"),
            ("Compañía local", "Local company"),
        ],
    )
    other_business_type = forms.CharField(
        label="6. Otros negocios / Other businesses:", max_length=200
    )
    risk_type = forms.ChoiceField(
        label="risk type", choices=[("Vida", "Life"), ("Otro", "Other")]
    )
    branches = forms.ChoiceField(label="branches", choices=[("Si", "Si"), ("No", "No")])
    branches_if_yes = forms.CharField(label="branches if yes", max_length=100)
    closing_date = forms.DateField(label="closing date", widget=forms.SelectDateWidget)
    start_year = forms.CharField(label="start year", max_length=100)
    end_year = forms.CharField(label="end year", max_length=100)
    incomes_premium_earned_1 = forms.CharField(
        label="incomes premium earned 1", max_length=100
    )
    incomes_premium_earned_2 = forms.CharField(
        label="incomes premium earned 2", max_length=100
    )
    incomes_disability_1 = forms.CharField(label="incomes disability 1", max_length=100)
    incomes_disability_2 = forms.CharField(label="incomes disability 2", max_length=100)
    incomes_life_1 = forms.CharField(label="incomes life 1", max_length=100)
    incomes_life_2 = forms.CharField(label="incomes life 2", max_length=100)
    incomes_auto_1 = forms.CharField(label="incomes auto 1", max_length=100)
    incomes_auto_2 = forms.CharField(label="incomes auto 2", max_length=100)
    incomes_other_1 = forms.CharField(label="incomes other 1", max_length=100)
    incomes_other_2 = forms.CharField(label="incomes other 2", max_length=100)
    incomes_dividend_1 = forms.CharField(label="incomes dividend 1", max_length=100)
    incomes_dividend_2 = forms.CharField(label="incomes dividend 2", max_length=100)
    incomes_rent_1 = forms.CharField(label="incomes rent 1", max_length=100)
    incomes_rent_2 = forms.CharField(label="incomes rent 2", max_length=100)
    incomes_commissions_1 = forms.CharField(
        label="incomes commissions 1", max_length=100
    )
    incomes_commissions_2 = forms.CharField(
        label="incomes commissions 2", max_length=100
    )
    incomes_interests_1 = forms.CharField(label="incomes interests 1", max_length=100)
    incomes_interests_2 = forms.CharField(label="incomes interests 2", max_length=100)
    incomes_capital_gain_loss_1 = forms.CharField(
        label="incomes capital gain loss 1", max_length=100
    )
    incomes_capital_gain_loss_2 = forms.CharField(
        label="incomes capital gain loss 2", max_length=100
    )
    incomes_other_operation_1 = forms.CharField(
        label="incomes other operation 1", max_length=100
    )
    incomes_other_operation_2 = forms.CharField(
        label="incomes other operation 2", max_length=100
    )
    incomes_total_1 = forms.CharField(label="incomes total 1", max_length=100)
    incomes_total_2 = forms.CharField(label="incomes total 2", max_length=100)
    expenses_1 = forms.CharField(label="expenses 1", max_length=100)
    expenses_2 = forms.CharField(label="expenses 2", max_length=100)
    expenses_premium_earned_1 = forms.CharField(
        label="expenses premium earned 1", max_length=100
    )
    expenses_premium_earned_2 = forms.CharField(
        label="expenses premium earned 2", max_length=100
    )
    expenses_disability_1 = forms.CharField(
        label="expenses disability 1", max_length=100
    )
    expenses_disability_2 = forms.CharField(
        label="expenses disability 2", max_length=100
    )
    expenses_life_1 = forms.CharField(label="expenses life 1", max_length=100)
    expenses_life_2 = forms.CharField(label="expenses life 2", max_length=100)
    expenses_auto_1 = forms.CharField(label="expenses auto 1", max_length=100)
    expenses_auto_2 = forms.CharField(label="expenses auto 2", max_length=100)
    expenses_other_1 = forms.CharField(label="expenses other 1", max_length=100)
    expenses_other_2 = forms.CharField(label="expenses other 2", max_length=100)
    expenses_increase_reserves_1 = forms.CharField(
        label="expenses increase reserves 1", max_length=100
    )
    expenses_increase_reserves_2 = forms.CharField(
        label="expenses increase reserves 2", max_length=100
    )
    expenses_salaries_wages_bonus_1 = forms.CharField(
        label="expenses salaries wages bonus 1", max_length=100
    )
    expenses_salaries_wages_bonus_2 = forms.CharField(
        label="expenses salaries wages bonus 2", max_length=100
    )
    expenses_commissions_1 = forms.CharField(
        label="expenses commissions 1", max_length=100
    )
    expenses_commissions_2 = forms.CharField(
        label="expenses commissions 2", max_length=100
    )
    expenses_to_employees_1 = forms.CharField(
        label="expenses to employees 1", max_length=100
    )
    expenses_to_employees_2 = forms.CharField(
        label="expenses to employees 2", max_length=100
    )
    expenses_independent_agents_1 = forms.CharField(
        label="expenses independent agents 1", max_length=100
    )
    expenses_independent_agents_2 = forms.CharField(
        label="expenses independent agents 2", max_length=100
    )
    expenses_interest_1 = forms.CharField(label="expenses interest 1", max_length=100)
    expenses_interest_2 = forms.CharField(label="expenses interest 2", max_length=100)
    expenses_rent_1 = forms.CharField(label="expenses rent 1", max_length=100)
    expenses_rent_2 = forms.CharField(label="expenses rent 2", max_length=100)
    expenses_depreciation_1 = forms.CharField(
        label="expenses depreciation 1", max_length=100
    )
    expenses_depreciation_2 = forms.CharField(
        label="expenses depreciation 2", max_length=100
    )
    expenses_dividend_policy_holder_1 = forms.CharField(
        label="expenses dividend policy holder 1", max_length=100
    )
    expenses_dividend_policy_holder_2 = forms.CharField(
        label="expenses dividend policy holder 2", max_length=100
    )
    expenses_donation_1 = forms.CharField(label="expenses donation 1", max_length=100)
    expenses_donation_2 = forms.CharField(label="expenses donation 2", max_length=100)
    expenses_sales_tax_1 = forms.CharField(label="expenses sales tax 1", max_length=100)
    expenses_sales_tax_2 = forms.CharField(label="expenses sales tax 2", max_length=100)
    expenses_machinary_1 = forms.CharField(label="expenses machinary 1", max_length=100)
    expenses_machinary_2 = forms.CharField(label="expenses machinary 2", max_length=100)
    expenses_other_purchases_1 = forms.CharField(
        label="expenses other purchases 1", max_length=100
    )
    expenses_other_purchases_2 = forms.CharField(
        label="expenses other purchases 2", max_length=100
    )
    expenses_licenses_1 = forms.CharField(label="expenses licenses 1", max_length=100)
    expenses_licenses_2 = forms.CharField(label="expenses licenses 2", max_length=100)
    expenses_other_operating_1 = forms.CharField(
        label="expenses other operating 1", max_length=100
    )
    expenses_other_operating_2 = forms.CharField(
        label="expenses other operating 2", max_length=100
    )
    expenses_total_1 = forms.CharField(label="expenses total 1", max_length=100)
    expenses_total_2 = forms.CharField(label="expenses total 2", max_length=100)
    gross_profit_1 = forms.CharField(label="gross profit 1", max_length=100)
    gross_profit_2 = forms.CharField(label="gross profit 2", max_length=100)
    sales_tax_withheld_1 = forms.CharField(label="sales tax withheld 1", max_length=100)
    sales_tax_withheld_2 = forms.CharField(label="sales tax withheld 2", max_length=100)
    name = forms.CharField(
        label="Name of person filling the questionnaire", max_length=100
    )
    rank = forms.CharField(label="Rank", max_length=100)


class IP_530(forms.Form):
    company_name = forms.CharField(
        label="Nombre compañía / Company Name", max_length=100
    )
    address = forms.CharField(label="Dirección / Address", max_length=200)
    email = forms.EmailField(label="Correo electrónico / Email")
    liaison_officer = forms.CharField(
        label="Persona contacto / Liaison officer", max_length=100
    )

    ssn = forms.CharField(
        label="Numero de Seguro Social / Social Security Number", max_length=11
    )
    tel = forms.CharField(label="Tel", max_length=20)
    fax = forms.CharField(label="Fax", max_length=20)

    legal_form = forms.ChoiceField(
        label="Forma legal de organización / Legal form of organization",
        choices=[
            ("Corporación", "Corporación"),
            ("Sociedad", "Sociedad"),
            ("Cooperativa", "Cooperativa"),
            ("Empresa Individual", "Empresa Individual"),
            ("Empresa sin fines pecuniarios", "Empresa sin fines pecuniarios"),
        ],
    )
    cfc = forms.ChoiceField(label="CEC", choices=[("Si", "Si"), ("No", "No")])
    business_type = forms.CharField(
        label="Tipo de negocio / Business type", max_length=100
    )
    other_business_type = forms.CharField(
        label="Otro tipo de negocio / Other business type", max_length=100
    )
    closing_date = forms.DateField(
        label="Fecha de cierre de sus libros / Your accounting period closing date",
        widget=forms.SelectDateWidget,
    )
    start_year = forms.CharField(
        label="Año de inicio de operaciones / Year of start of operations",
        max_length=100,
    )
    end_year = forms.CharField(
        label="Año de cierre de operaciones / Year of end of operations", max_length=100
    )

    incomes_from_persons_1 = forms.CharField(
        label="1. Ingresos de personas - Incomes from persons", max_length=100
    )
    incomes_from_persons_2 = forms.CharField(
        label="1. Ingresos de personas - Incomes from persons", max_length=100
    )
    incomes_industries_businesses_1 = forms.CharField(
        label="2. Ingresos de industrias y negocios - Incomes from industries and businesses",
        max_length=100,
    )
    incomes_industries_businesses_2 = forms.CharField(
        label="2. Ingresos de industrias y negocios - Incomes from industries and businesses",
        max_length=100,
    )
    incomes_rent_1 = forms.CharField(
        label="3. Ingresos por renta - Incomes from rent", max_length=100
    )
    incomes_rent_2 = forms.CharField(
        label="3. Ingresos por renta - Incomes from rent", max_length=100
    )
    incomes_interests_1 = forms.CharField(
        label="4. Ingresos por intereses - Incomes from interests", max_length=100
    )
    incomes_interests_2 = forms.CharField(
        label="4. Ingresos por intereses - Incomes from interests", max_length=100
    )
    incomes_comissions_1 = forms.CharField(
        label="5. Comisiones - Comissions", max_length=100
    )
    incomes_comissions_2 = forms.CharField(
        label="5. Comisiones - Comissions", max_length=100
    )
    incomes_gain_loss_1 = forms.CharField(
        label="6. Ganancia de capital - Capital gain", max_length=100
    )
    incomes_gain_loss_2 = forms.CharField(
        label="6. Ganancia de capital - Capital gain", max_length=100
    )
    incomes_operating_1 = forms.CharField(
        label="7. Otros ingresos - Other incomes", max_length=100
    )
    incomes_operating_2 = forms.CharField(
        label="7. Otros ingresos - Other incomes", max_length=100
    )
    expenses_salaries_wages_bonus_1 = forms.CharField(
        label="1. Salarios, sueldos y bonificaciones - Salaries, wages and bonuses",
        max_length=100,
    )
    expenses_salaries_wages_bonus_2 = forms.CharField(
        label="1. Salarios, sueldos y bonificaciones - Salaries, wages and bonuses",
        max_length=100,
    )
    expenses_interests_1 = forms.CharField(
        label="2. Gastos por intereses - Expenses by interests", max_length=100
    )
    expenses_interests_2 = forms.CharField(
        label="2. Gastos por intereses - Expenses by interests", max_length=100
    )
    expenses_rent_1 = forms.CharField(
        label="3. Gastos por rentas - Expenses by rents", max_length=100
    )
    expenses_rent_2 = forms.CharField(
        label="3. Gastos por rentas - Expenses by rents", max_length=100
    )
    expenses_depreciation_1 = forms.CharField(
        label="4. Depreciación - Depreciation", max_length=100
    )
    expenses_depreciation_2 = forms.CharField(
        label="4. Depreciación - Depreciation", max_length=100
    )
    expenses_donations_1 = forms.CharField(
        label="5. Donaciones - Donations", max_length=100
    )
    expenses_donations_2 = forms.CharField(
        label="5. Donaciones - Donations", max_length=100
    )
    expenses_sales_tax_1 = forms.CharField(
        label="6. Impuesto sobre ventas y uso - Sales and use tax", max_length=100
    )
    expenses_sales_tax_2 = forms.CharField(
        label="6. Impuesto sobre ventas y uso - Sales and use tax", max_length=100
    )
    expenses_machinary_equipment_1 = forms.CharField(
        label="7. Compra de maquinaria - Purchase of machinery", max_length=100
    )
    expenses_machinary_equipment_2 = forms.CharField(
        label="7. Compra de maquinaria - Purchase of machinery", max_length=100
    )
    expenses_other_purchases_1 = forms.CharField(
        label="8. Otras compras - Other purchases", max_length=100
    )
    expenses_other_purchases_2 = forms.CharField(
        label="8. Otras compras - Other purchases", max_length=100
    )
    expenses_licenses_1 = forms.CharField(
        label="9. Licencias - Licenses", max_length=100
    )
    expenses_licenses_2 = forms.CharField(
        label="9. Licencias - Licenses", max_length=100
    )
    expenses_other_operations_1 = forms.CharField(
        label="10. Otros gastos - Other expenses", max_length=100
    )
    expenses_other_operations_2 = forms.CharField(
        label="10. Otros gastos - Other expenses", max_length=100
    )
    expenses_total_1 = forms.CharField(
        label="11. Total de gastos (1-10) - Total expenses (1-10)", max_length=100
    )
    expenses_total_2 = forms.CharField(
        label="11. Total de gastos (1-10) - Total expenses (1-10)", max_length=100
    )
    gross_profit_1 = forms.CharField(
        label="12. Ganancia bruta (6-11) - Gross profit (6-11)", max_length=100
    )
    gross_profit_2 = forms.CharField(
        label="12. Ganancia bruta (6-11) - Gross profit (6-11)", max_length=100
    )
    profit_income_tax_1 = forms.CharField(
        label="13. Contribución sobre ingresos - Income tax", max_length=100
    )
    profit_income_tax_2 = forms.CharField(
        label="13. Contribución sobre ingresos - Income tax", max_length=100
    )
    profit_after_income_tax_1 = forms.CharField(
        label="14. Ganancia después de contribución sobre ingresos - Profit after income tax",
        max_length=100,
    )
    profit_after_income_tax_2 = forms.CharField(
        label="14. Ganancia después de contribución sobre ingresos - Profit after income tax",
        max_length=100,
    )
    sales_tax_withheld_1 = forms.CharField(
        label="15. Impuesto sobre ventas y uso retenido - Sales and use tax withheld",
        max_length=100,
    )
    sales_tax_withheld_2 = forms.CharField(
        label="15. Impuesto sobre ventas y uso retenido - Sales and use tax withheld",
        max_length=100,
    )

    name = forms.CharField(
        label="Name of person filling the questionnaire", max_length=100
    )
    rank = forms.CharField(label="Rank", max_length=100)


class IP_540(forms.Form):
    company_name = forms.CharField(
        label="Nombre compañía / Company Name", max_length=100
    )
    address = forms.CharField(label="Dirección / Address", max_length=200)
    email = forms.EmailField(label="Correo electrónico / Email")
    liaison_officer = forms.CharField(
        label="Persona contacto / Liaison officer", max_length=100
    )
    ssn = forms.CharField(
        label="Numero de Seguro Social / Social Security Number", max_length=11
    )
    tel = forms.CharField(label="Tel", max_length=20)
    fax = forms.CharField(label="Fax", max_length=20)
    legal_form = forms.ChoiceField(
        label="Forma legal de organización / Legal form of organization",
        choices=[
            ("Corporación", "Corporación"),
            ("Sociedad", "Sociedad"),
            ("Cooperativa", "Cooperativa"),
            ("Empresa Individual", "Empresa Individual"),
            ("Empresa sin fines pecuniarios", "Empresa sin fines pecuniarios"),
        ],
    )
    cfc = forms.ChoiceField(label="CEC", choices=[("Si", "Si"), ("No", "No")])
    business_type = forms.ChoiceField(
        label="Tipo de negocio / Business type",
        choices=[
            ("Comercio", "Comercio"),
            ("Manufactura", "Manufactura"),
            ("Servicios", "Servicios"),
            ("Agricultura", "Agricultura"),
            ("Otros", "Otros"),
        ],
    )
    business_function = forms.ChoiceField(
        label="Función del negocio / Business function",
        choices=[
            ("Venta de productos", "Venta de productos"),
            ("Venta de servicios", "Venta de servicios"),
            ("Venta de productos y servicios", "Venta de productos y servicios"),
        ],
    )
    branches = forms.ChoiceField(
        label="Sucursales / Branches", choices=[("Si", "Si"), ("No", "No")]
    )
    branches_yes = forms.CharField(
        label="Si si, cuantas / If yes, how many", max_length=100
    )
    closing_date = forms.DateField(
        label="Fecha de cierre de sus libros / Your accounting period closing date",
        widget=forms.SelectDateWidget,
    )
    start_year = forms.CharField(
        label="Año de inicio de operaciones / Year of start of operations",
        max_length=100,
    )
    end_year = forms.CharField(
        label="Año de cierre de operaciones / Year of end of operations", max_length=100
    )
    incomes_services_rendered_1 = forms.CharField(
        label="1. Ingresos por servicios prestados - Incomes from services rendered",
        max_length=100,
    )
    incomes_services_rendered_2 = forms.CharField(
        label="1. Ingresos por servicios prestados - Incomes from services rendered",
        max_length=100,
    )
    incomes_from_persons_1 = forms.CharField(
        label="2. Ingresos de personas - Incomes from persons", max_length=100
    )
    incomes_from_persons_2 = forms.CharField(
        label="2. Ingresos de personas - Incomes from persons", max_length=100
    )
    incomes_from_industries_and_businesses_1 = forms.CharField(
        label="3. Ingresos de industrias y negocios - Incomes from industries and businesses",
        max_length=100,
    )
    incomes_from_industries_and_businesses_2 = forms.CharField(
        label="3. Ingresos de industrias y negocios - Incomes from industries and businesses",
        max_length=100,
    )
    incomes_sale_merchandise_1 = forms.CharField(
        label="4. Ingresos por venta de mercancía - Incomes from sale of merchandise",
        max_length=100,
    )
    incomes_sale_merchandise_2 = forms.CharField(
        label="4. Ingresos por venta de mercancía - Incomes from sale of merchandise",
        max_length=100,
    )
    incomes_rent_machinery_and_equipment_1 = forms.CharField(
        label="5. Ingresos por renta de maquinaria y equipo - Incomes from rent of machinery and equipment",
        max_length=100,
    )
    incomes_rent_machinery_and_equipment_2 = forms.CharField(
        label="5. Ingresos por renta de maquinaria y equipo - Incomes from rent of machinery and equipment",
        max_length=100,
    )
    incomes_rent_land_and_building_1 = forms.CharField(
        label="6. Ingresos por renta de terreno y edificio - Incomes from rent of land and building",
        max_length=100,
    )
    incomes_rent_land_and_building_2 = forms.CharField(
        label="6. Ingresos por renta de terreno y edificio - Incomes from rent of land and building",
        max_length=100,
    )
    incomes_interests_1 = forms.CharField(
        label="7. Ingresos por intereses - Incomes from interests", max_length=100
    )
    incomes_interests_2 = forms.CharField(
        label="7. Ingresos por intereses - Incomes from interests", max_length=100
    )
    incomes_capital_gain_or_loss_1 = forms.CharField(
        label="8. Ganancia o pérdida de capital - Capital gain or loss", max_length=100
    )
    incomes_capital_gain_or_loss_2 = forms.CharField(
        label="8. Ganancia o pérdida de capital - Capital gain or loss", max_length=100
    )
    incomes_other_operating_income_1 = forms.CharField(
        label="9. Otros ingresos operacionales - Other operating income", max_length=100
    )
    incomes_other_operating_income_2 = forms.CharField(
        label="9. Otros ingresos operacionales - Other operating income", max_length=100
    )
    expenses_salaries_wages_bonus_1 = forms.CharField(
        label="1. Salarios, sueldos y bonificaciones - Salaries, wages and bonuses",
        max_length=100,
    )
    expenses_salaries_wages_bonus_2 = forms.CharField(
        label="1. Salarios, sueldos y bonificaciones - Salaries, wages and bonuses",
        max_length=100,
    )
    expenses_interests_1 = forms.CharField(
        label="2. Intereses - Interests", max_length=100
    )
    expenses_interests_2 = forms.CharField(
        label="2. Intereses - Interests", max_length=100
    )
    expenses_rent_1 = forms.CharField(label="3. Renta - Rent", max_length=100)
    expenses_rent_2 = forms.CharField(label="3. Renta - Rent", max_length=100)
    expenses_depreciation_1 = forms.CharField(
        label="4. Depreciación - Depreciation", max_length=100
    )
    expenses_depreciation_2 = forms.CharField(
        label="4. Depreciación - Depreciation", max_length=100
    )
    expenses_bad_debts_1 = forms.CharField(
        label="5. Malos créditos - Bad debts", max_length=100
    )
    expenses_bad_debts_2 = forms.CharField(
        label="5. Malos créditos - Bad debts", max_length=100
    )
    expenses_donations_1 = forms.CharField(
        label="6. Donaciones - Donations", max_length=100
    )
    expenses_donations_2 = forms.CharField(
        label="6. Donaciones - Donations", max_length=100
    )
    expenses_other_donations_1 = forms.CharField(
        label="7. Otras donaciones - Other donations", max_length=100
    )
    expenses_other_donations_2 = forms.CharField(
        label="7. Otras donaciones - Other donations", max_length=100
    )
    expenses_sales_taxes_1 = forms.CharField(
        label="8. Impuesto sobre ventas - Sales taxes", max_length=100
    )
    expenses_sales_taxes_2 = forms.CharField(
        label="8. Impuesto sobre ventas - Sales taxes", max_length=100
    )
    expenses_purchases_machinery_1 = forms.CharField(
        label="9. Compra de maquinaria - Purchase of machinery", max_length=100
    )
    expenses_purchases_machinery_2 = forms.CharField(
        label="9. Compra de maquinaria - Purchase of machinery", max_length=100
    )
    expenses_other_purchases_1 = forms.CharField(
        label="10. Otras compras - Other purchases", max_length=100
    )
    expenses_other_purchases_2 = forms.CharField(
        label="10. Otras compras - Other purchases", max_length=100
    )
    expenses_licenses_1 = forms.CharField(
        label="11. Licencias - Licenses", max_length=100
    )
    expenses_licenses_2 = forms.CharField(
        label="11. Licencias - Licenses", max_length=100
    )
    net_profit_1 = forms.CharField(
        label="12. Ganancia neta (1-11) - Net profit (1-11)", max_length=100
    )
    net_profit_2 = forms.CharField(
        label="12. Ganancia neta (1-11) - Net profit (1-11)", max_length=100
    )
    profit_income_tax_1 = forms.CharField(
        label="13. Ganancia después de contribución sobre ingresos - Profit after income tax",
        max_length=100,
    )
    profit_income_tax_2 = forms.CharField(
        label="13. Ganancia después de contribución sobre ingresos - Profit after income tax",
        max_length=100,
    )
    profit_after_income_tax_1 = forms.CharField(
        label="14. Ganancia después de contribución sobre ingresos - Profit after income tax",
        max_length=100,
    )
    profit_after_income_tax_2 = forms.CharField(
        label="14. Ganancia después de contribución sobre ingresos - Profit after income tax",
        max_length=100,
    )
    sales_tax_withheld_1 = forms.CharField(
        label="15. Impuesto sobre ventas y uso retenido - Sales tax withheld",
        max_length=100,
    )
    sales_tax_withheld_2 = forms.CharField(
        label="15. Impuesto sobre ventas y uso retenido - Sales tax withheld",
        max_length=100,
    )
    name = forms.CharField(
        label="Name of person filling the questionnaire", max_length=100
    )
    rank = forms.CharField(label="Rank", max_length=100)


class IP_540J(forms.Form):
    company_name = forms.CharField(
        label="Nombre compañía / Company Name", max_length=100
    )
    address = forms.CharField(label="Dirección / Address", max_length=200)
    email = forms.EmailField(label="Correo electrónico / Email")
    liaison_officer = forms.CharField(
        label="Persona contacto / Liaison officer", max_length=100
    )

    ssn = forms.CharField(
        label="Numero de Seguro Social / Social Security Number", max_length=11
    )
    tel = forms.CharField(label="Tel", max_length=20)
    fax = forms.CharField(label="Fax", max_length=20)

    legal_form = forms.ChoiceField(
        label="Forma legal de organización / Legal form of organization",
        choices=[
            ("Corporación", "Corporación"),
            ("Sociedad", "Sociedad"),
            ("Cooperativa", "Cooperativa"),
            ("Empresa Individual", "Empresa Individual"),
            ("Empresa sin fines pecuniarios", "Empresa sin fines pecuniarios"),
        ],
    )
    cfc = forms.ChoiceField(label="CEC", choices=[("Si", "Si"), ("No", "No")])
    business_type = forms.CharField(
        label="Tipo de negocio / Business type", max_length=100
    )
    business_function = forms.ChoiceField(
        label="Función de negocio / Business function",
        choices=[
            ("Corredor", "Broker"),
            ("Agente no general", "Non-general agent"),
            ("Agente general", "General agent"),
            ("Compañía local", "Local company"),
        ],
    )
    closing_date = forms.DateField(
        label="Fecha de cierre de sus libros / Your accounting period closing date",
        widget=forms.SelectDateWidget,
    )
    start_year = forms.CharField(
        label="Año de inicio de operaciones / Year of start of operations",
        max_length=100,
    )
    end_year = forms.CharField(
        label="Año de cierre de operaciones / Year of end of operations", max_length=100
    )

    incomes_from_persons_1 = forms.CharField(
        label="1. Ingresos de personas - Incomes from persons", max_length=100
    )
    incomes_from_persons_2 = forms.CharField(
        label="1. Ingresos de personas - Incomes from persons", max_length=100
    )
    incomes_industries_business_1 = forms.CharField(
        label="2. Ingresos de industrias y negocios - Incomes from industries and businesses",
        max_length=100,
    )
    incomes_industries_business_2 = forms.CharField(
        label="2. Ingresos de industrias y negocios - Incomes from industries and businesses",
        max_length=100,
    )
    expenses_newspapers_1 = forms.CharField(
        label="3. Gastos de periódicos - Expenses of newspapers", max_length=100
    )
    expenses_newspapers_2 = forms.CharField(
        label="3. Gastos de periódicos - Expenses of newspapers", max_length=100
    )
    expenses_radio_television_1 = forms.CharField(
        label="4. Gastos de radio y televisión - Expenses of radio and television",
        max_length=100,
    )
    expenses_radio_television_2 = forms.CharField(
        label="4. Gastos de radio y televisión - Expenses of radio and television",
        max_length=100,
    )
    expenses_other_1 = forms.CharField(
        label="5. Otros gastos - Other expenses", max_length=100
    )
    expenses_other_2 = forms.CharField(
        label="5. Otros gastos - Other expenses", max_length=100
    )
    gross_profit_1 = forms.CharField(
        label="6. Ganancia bruta - Gross profit", max_length=100
    )
    gross_profit_2 = forms.CharField(
        label="6. Ganancia bruta - Gross profit", max_length=100
    )
    dividends_paid_1 = forms.CharField(
        label="7. Dividendos pagados - Dividends paid", max_length=100
    )
    dividends_paid_2 = forms.CharField(
        label="7. Dividendos pagados - Dividends paid", max_length=100
    )
    expenses_interests_1 = forms.CharField(
        label="8. Gastos de intereses - Expenses of interests", max_length=100
    )
    expenses_interests_2 = forms.CharField(
        label="8. Gastos de intereses - Expenses of interests", max_length=100
    )
    expenses_rent_1 = forms.CharField(
        label="9. Gastos de renta - Expenses of rent", max_length=100
    )
    expenses_rent_2 = forms.CharField(
        label="9. Gastos de renta - Expenses of rent", max_length=100
    )
    expenses_gain_loss_1 = forms.CharField(
        label="10. Ganancia o pérdida - Gain or loss", max_length=100
    )
    expenses_gain_loss_2 = forms.CharField(
        label="10. Ganancia o pérdida - Gain or loss", max_length=100
    )
    dividends_paid_other_1 = forms.CharField(
        label="11. Dividendos pagados a otros - Dividends paid to others",
        max_length=100,
    )
    dividends_paid_other_2 = forms.CharField(
        label="11. Dividendos pagados a otros - Dividends paid to others",
        max_length=100,
    )
    incomes_total_1 = forms.CharField(
        label="12. Total de ingresos - Total incomes", max_length=100
    )
    incomes_total_2 = forms.CharField(
        label="12. Total de ingresos - Total incomes", max_length=100
    )
    expenses_total_1 = forms.CharField(
        label="13. Total de gastos - Total expenses", max_length=100
    )
    expenses_total_2 = forms.CharField(
        label="13. Total de gastos - Total expenses", max_length=100
    )
    salaries_wages_bonus_1 = forms.CharField(
        label="14. Salarios, sueldos y bonificaciones - Salaries, wages and bonuses",
        max_length=100,
    )
    salaries_wages_bonus_2 = forms.CharField(
        label="14. Salarios, sueldos y bonificaciones - Salaries, wages and bonuses",
        max_length=100,
    )
    interests_1 = forms.CharField(label="15. Intereses - Interests", max_length=100)
    interests_2 = forms.CharField(label="15. Intereses - Interests", max_length=100)
    rents_1 = forms.CharField(label="16. Renta - Rent", max_length=100)
    rents_2 = forms.CharField(label="16. Renta - Rent", max_length=100)
    depreciation_1 = forms.CharField(
        label="17. Depreciación - Depreciation", max_length=100
    )
    depreciation_2 = forms.CharField(
        label="17. Depreciación - Depreciation", max_length=100
    )
    other_taxes_1 = forms.CharField(
        label="18. Otros impuestos - Other taxes", max_length=100
    )
    other_taxes_2 = forms.CharField(
        label="18. Otros impuestos - Other taxes", max_length=100
    )
    donations_1 = forms.CharField(label="19. Donativos - Donations", max_length=100)
    donations_2 = forms.CharField(label="19. Donativos - Donations", max_length=100)
    sales_tax_1 = forms.CharField(
        label="20. Impuesto sobre ventas - Sales tax", max_length=100
    )
    sales_tax_2 = forms.CharField(
        label="20. Impuesto sobre ventas - Sales tax", max_length=100
    )
    machinery_1 = forms.CharField(
        label="21. Compra de maquinaria - Purchase of machinery", max_length=100
    )
    machinery_2 = forms.CharField(
        label="21. Compra de maquinaria - Purchase of machinery", max_length=100
    )
    other_purchases_1 = forms.CharField(
        label="22. Otras compras - Other purchases", max_length=100
    )
    other_purchases_2 = forms.CharField(
        label="22. Otras compras - Other purchases", max_length=100
    )
    licenses_1 = forms.CharField(label="23. Licencias - Licenses", max_length=100)
    licenses_2 = forms.CharField(label="23. Licencias - Licenses", max_length=100)
    other_operating_expenses_1 = forms.CharField(
        label="24. Otras operaciones - Other operations", max_length=100
    )
    other_operating_expenses_2 = forms.CharField(
        label="24. Otras operaciones - Other operations", max_length=100
    )
    profit_incomes_tax_1 = forms.CharField(
        label="25. Ganancia después de contribución sobre ingresos - Profit after income tax",
        max_length=100,
    )
    profit_incomes_tax_2 = forms.CharField(
        label="25. Ganancia después de contribución sobre ingresos - Profit after income tax",
        max_length=100,
    )
    profit_incomes_mortage_loans_1 = forms.CharField(
        label="26. Ganancia después de contribución sobre ingresos y préstamos hipotecarios - Profit after income tax and mortgage loans",
        max_length=100,
    )
    profit_incomes_mortage_loans_2 = forms.CharField(
        label="26. Ganancia después de contribución sobre ingresos y préstamos hipotecarios - Profit after income tax and mortgage loans",
        max_length=100,
    )
    sales_tax_withheld_1 = forms.CharField(
        label="27. Impuesto sobre ventas y uso retenido - Sales and use tax withheld",
        max_length=100,
    )
    sales_tax_withheld_2 = forms.CharField(
        label="27. Impuesto sobre ventas y uso retenido - Sales and use tax withheld",
        max_length=100,
    )

    name = forms.CharField(
        label="Name of person filling the questionnaire", max_length=100
    )
    rank = forms.CharField(label="Rank", max_length=100)


class IP_620(forms.Form):
    company_name = forms.CharField(
        label="Nombre compañía / Company Name", max_length=100
    )
    address = forms.CharField(label="Dirección / Address", max_length=200)
    email = forms.EmailField(label="Correo electrónico / Email")
    liaison_officer = forms.CharField(
        label="Persona contacto / Liaison officer", max_length=100
    )
    ssn = forms.CharField(
        label="Numero de Seguro Social / Social Security Number", max_length=11
    )
    tel = forms.CharField(label="Tel", max_length=20)
    fax = forms.CharField(label="Fax", max_length=20)
    legal_form = forms.ChoiceField(
        label="Forma legal de organización / Legal form of organization",
        choices=[
            ("Corporación", "Corporación"),
            ("Sociedad", "Sociedad"),
            ("Cooperativa", "Cooperativa"),
            ("Empresa Individual", "Empresa Individual"),
            ("Empresa sin fines pecuniarios", "Empresa sin fines pecuniarios"),
        ],
    )
    cfc = forms.ChoiceField(label="CEC", choices=[("Si", "Si"), ("No", "No")])
    business_type = forms.CharField(
        label="Tipo de negocio / Business type", max_length=100
    )
    business_function = forms.CharField(
        label="Función de negocio / Business function", max_length=100
    )
    branches = forms.ChoiceField(
        label="Sucursales / Branches", choices=[("Si", "Si"), ("No", "No")]
    )
    branches_yes = forms.CharField(
        label="Si si, cuantas / If yes, how many", max_length=100
    )
    closing_date = forms.DateField(
        label="Fecha de cierre de sus libros / Your accounting period closing date",
        widget=forms.SelectDateWidget,
    )
    start_year = forms.CharField(
        label="Año de inicio de operaciones / Year of start of operations",
        max_length=100,
    )
    end_year = forms.CharField(
        label="Año de cierre de operaciones / Year of end of operations", max_length=100
    )

    patients_service_revenue_from_persons_1 = forms.CharField(
        label="1. Ingresos por servicios prestados a personas - Patients service revenue from persons",
        max_length=100,
    )
    patients_service_revenue_from_persons_2 = forms.CharField(
        label="1. Ingresos por servicios prestados a personas - Patients service revenue from persons",
        max_length=100,
    )
    patients_service_revenue_from_industries_business_1 = forms.CharField(
        label="2. Ingresos por servicios prestados a industrias y negocios - Patients service revenue from industries and businesses",
        max_length=100,
    )
    patients_service_revenue_from_industries_business_2 = forms.CharField(
        label="2. Ingresos por servicios prestados a industrias y negocios - Patients service revenue from industries and businesses",
        max_length=100,
    )
    contractual_adjustments_1 = forms.CharField(
        label="3. Ajustes contractuales - Contractual adjustments", max_length=100
    )
    contractual_adjustments_2 = forms.CharField(
        label="3. Ajustes contractuales - Contractual adjustments", max_length=100
    )
    net_patient_service_revenue_1 = forms.CharField(
        label="4. Ingresos netos por servicios a pacientes - Net patient service revenue",
        max_length=100,
    )
    net_patient_service_revenue_2 = forms.CharField(
        label="4. Ingresos netos por servicios a pacientes - Net patient service revenue",
        max_length=100,
    )
    other_incomes_1 = forms.CharField(
        label="5. Otros ingresos - Other incomes", max_length=100
    )
    other_incomes_2 = forms.CharField(
        label="5. Otros ingresos - Other incomes", max_length=100
    )
    other_incomes_rent_1 = forms.CharField(
        label="6. Ingresos por renta - Incomes from rent", max_length=100
    )
    other_incomes_rent_2 = forms.CharField(
        label="6. Ingresos por renta - Incomes from rent", max_length=100
    )
    other_incomes_interest_1 = forms.CharField(
        label="7. Ingresos por intereses - Incomes from interests", max_length=100
    )
    other_incomes_interest_2 = forms.CharField(
        label="7. Ingresos por intereses - Incomes from interests", max_length=100
    )
    other_incomes_capital_gain_loss_1 = forms.CharField(
        label="8. Ganancia o pérdida de capital - Capital gain or loss", max_length=100
    )
    other_incomes_capital_gain_loss_2 = forms.CharField(
        label="8. Ganancia o pérdida de capital - Capital gain or loss", max_length=100
    )
    other_incomes_operating_1 = forms.CharField(
        label="9. Otros ingresos operacionales - Other operating income", max_length=100
    )
    other_incomes_operating_2 = forms.CharField(
        label="9. Otros ingresos operacionales - Other operating income", max_length=100
    )
    total_incomes_1 = forms.CharField(
        label="10. Total de ingresos - Total incomes", max_length=100
    )
    total_incomes_2 = forms.CharField(
        label="10. Total de ingresos - Total incomes", max_length=100
    )
    total_expenses_1 = forms.CharField(
        label="11. Total de gastos - Total expenses", max_length=100
    )
    total_expenses_2 = forms.CharField(
        label="11. Total de gastos - Total expenses", max_length=100
    )
    expenses_salaries_wages_bonus_1 = forms.CharField(
        label="1. Salarios, sueldos y bonificaciones - Salaries, wages and bonuses",
        max_length=100,
    )
    expenses_salaries_wages_bonus_2 = forms.CharField(
        label="1. Salarios, sueldos y bonificaciones - Salaries, wages and bonuses",
        max_length=100,
    )
    expenses_interest_1 = forms.CharField(
        label="2. Gastos por intereses - Expenses by interests", max_length=100
    )
    expenses_interest_2 = forms.CharField(
        label="2. Gastos por intereses - Expenses by interests", max_length=100
    )
    expenses_rent_1 = forms.CharField(
        label="3. Gastos por rentas - Expenses by rents", max_length=100
    )
    expenses_rent_2 = forms.CharField(
        label="3. Gastos por rentas - Expenses by rents", max_length=100
    )
    expenses_food_patients_1 = forms.CharField(
        label="4. Gastos de alimentos para pacientes - Expenses of food for patients",
        max_length=100,
    )
    expenses_food_patients_2 = forms.CharField(
        label="4. Gastos de alimentos para pacientes - Expenses of food for patients",
        max_length=100,
    )
    expenses_free_food_to_employees_1 = forms.CharField(
        label="5. Gastos de alimentos gratis a empleados - Expenses of free food to employees",
        max_length=100,
    )
    expenses_free_food_to_employees_2 = forms.CharField(
        label="5. Gastos de alimentos gratis a empleados - Expenses of free food to employees",
        max_length=100,
    )
    expenses_uniforms_1 = forms.CharField(
        label="6. Gastos de uniformes - Expenses of uniforms", max_length=100
    )
    expenses_uniforms_2 = forms.CharField(
        label="6. Gastos de uniformes - Expenses of uniforms", max_length=100
    )
    expenses_depreciation_1 = forms.CharField(
        label="7. Depreciación - Depreciation", max_length=100
    )
    expenses_depreciation_2 = forms.CharField(
        label="7. Depreciación - Depreciation", max_length=100
    )
    expenses_bad_debts_1 = forms.CharField(
        label="8. Malos créditos - Bad debts", max_length=100
    )
    expenses_bad_debts_2 = forms.CharField(
        label="8. Malos créditos - Bad debts", max_length=100
    )
    expenses_donations_1 = forms.CharField(
        label="9. Donaciones - Donations", max_length=100
    )
    expenses_donations_2 = forms.CharField(
        label="9. Donaciones - Donations", max_length=100
    )
    expenses_sales_tax_1 = forms.CharField(
        label="10. Impuesto sobre ventas y uso - Sales and use tax", max_length=100
    )
    expenses_sales_tax_2 = forms.CharField(
        label="10. Impuesto sobre ventas y uso - Sales and use tax", max_length=100
    )
    expenses_machinery_1 = forms.CharField(
        label="11. Compra de maquinaria - Purchase of machinery", max_length=100
    )
    expenses_machinery_2 = forms.CharField(
        label="11. Compra de maquinaria - Purchase of machinery", max_length=100
    )
    expenses_on_other_purchases_1 = forms.CharField(
        label="12. Otras compras - Other purchases", max_length=100
    )
    expenses_on_other_purchases_2 = forms.CharField(
        label="12. Otras compras - Other purchases", max_length=100
    )
    expenses_licenses_1 = forms.CharField(
        label="13. Licencias - Licenses", max_length=100
    )
    expenses_licenses_2 = forms.CharField(
        label="13. Licencias - Licenses", max_length=100
    )
    expenses_other_operating_1 = forms.CharField(
        label="14. Otros gastos - Other expenses", max_length=100
    )
    expenses_other_operating_2 = forms.CharField(
        label="14. Otros gastos - Other expenses", max_length=100
    )
    net_profit_loss_1 = forms.CharField(
        label="15. Ganancia neta (1-14) - Net profit (1-14)", max_length=100
    )
    net_profit_loss_2 = forms.CharField(
        label="15. Ganancia neta (1-14) - Net profit (1-14)", max_length=100
    )
    net_profit_loss_income_tax_1 = forms.CharField(
        label="16. Ganancia neta después de contribución sobre ingresos - Net profit after income tax",
        max_length=100,
    )
    net_profit_loss_income_tax_2 = forms.CharField(
        label="16. Ganancia neta después de contribución sobre ingresos - Net profit after income tax",
        max_length=100,
    )
    net_profit_after_tax_1 = forms.CharField(
        label="17. Ganancia neta después de contribución sobre ingresos - Net profit after income tax",
        max_length=100,
    )
    net_profit_after_tax_2 = forms.CharField(
        label="17. Ganancia neta después de contribución sobre ingresos - Net profit after income tax",
        max_length=100,
    )
    sales_and_use_withheld_1 = forms.CharField(
        label="18. Impuesto sobre ventas y uso retenido - Sales and use tax withheld",
        max_length=100,
    )
    sales_and_use_withheld_2 = forms.CharField(
        label="18. Impuesto sobre ventas y uso retenido - Sales and use tax withheld",
        max_length=100,
    )
    name = forms.CharField(
        label="Name of person filling the questionnaire", max_length=100
    )
    rank = forms.CharField(label="Rank", max_length=100)


class IP_610(forms.Form):
    company_name = forms.CharField(
        label="Nombre compañía / Company Name", max_length=100
    )
    address = forms.CharField(label="Dirección / Address", max_length=200)
    email = forms.EmailField(label="Correo electrónico / Email")
    liaison_officer = forms.CharField(
        label="Persona contacto / Liaison officer", max_length=100
    )
    ssn = forms.CharField(
        label="Numero de Seguro Social / Social Security Number", max_length=11
    )
    tel = forms.CharField(label="Tel", max_length=20)
    fax = forms.CharField(label="Fax", max_length=20)
    legal_form = forms.ChoiceField(
        label="Forma legal de organización / Legal form of organization",
        choices=[
            ("Corporación", "Corporación"),
            ("Sociedad", "Sociedad"),
            ("Cooperativa", "Cooperativa"),
            ("Empresa Individual", "Empresa Individual"),
            ("Empresa sin fines pecuniarios", "Empresa sin fines pecuniarios"),
        ],
    )
    cfc = forms.ChoiceField(label="CEC", choices=[("Si", "Si"), ("No", "No")])
    business_type = forms.CharField(
        label="Clase de negocio / Type of business", max_length=200
    )
    business_function = forms.CharField(
        label="Describa brevemente la función principal del negocio / Explain briefly the main function of the business activity",
        widget=forms.Textarea,
    )
    branches = forms.ChoiceField(
        label="¿Opera sucursuales esta firma? / Do you have branch operations?",
        choices=[("Si", "Si"), ("No", "No")],
    )
    branches_yes = forms.ChoiceField(
        label="afirmativo a branches",
        choices=[
            ("todas las sucursales", "todas las sucursales"),
            ("este establecimiento", "este establecimiento"),
        ],
    )
    closing_date = forms.DateField(
        label="Fecha de cierre de sus libros / Your accounting period closing date",
        widget=forms.SelectDateWidget,
    )

    start_year = forms.CharField(
        label="Año de inicio de operaciones / Year of start of operations",
        max_length=100,
    )
    end_year = forms.CharField(
        label="Año de cierre de operaciones / Year of end of operations", max_length=100
    )

    incomes_services_rendered_1 = forms.CharField(
        label="1. Ingresos por servicios - Services rendered", max_length=100
    )
    incomes_services_rendered_2 = forms.CharField(
        label="1. Ingresos por servicios - Services rendered", max_length=100
    )
    incomes_unrestricted_A_1 = forms.CharField(
        label="a. Sin asignar - Unrestricted", max_length=100
    )
    incomes_unrestricted_A_2 = forms.CharField(
        label="a. Sin asignar - Unrestricted", max_length=100
    )
    incomes_restricted_A_1 = forms.CharField(
        label="b. Restricto - Restricted", max_length=100
    )
    incomes_restricted_A_2 = forms.CharField(
        label="b. Restricto - Restricted", max_length=100
    )
    incomes_sales_1 = forms.CharField(label="2. Ventas - Sales", max_length=100)
    incomes_sales_2 = forms.CharField(label="2. Ventas - Sales", max_length=100)
    incomes_rents_1 = forms.CharField(
        label="3. Renta de terreno y edificio - Rent of land and building",
        max_length=100,
    )
    incomes_rents_2 = forms.CharField(
        label="3. Renta de terreno y edificio - Rent of land and building",
        max_length=100,
    )
    incomes_interests_1 = forms.CharField(
        label="4. Intereses - Interests", max_length=100
    )
    incomes_interests_2 = forms.CharField(
        label="4. Intereses - Interests", max_length=100
    )
    incomes_capital_1 = forms.CharField(
        label="5. Ganancia o pérdida de capital - Capital gain or loss", max_length=100
    )
    incomes_capital_2 = forms.CharField(
        label="5. Ganancia o pérdida de capital - Capital gain or loss", max_length=100
    )
    incomes_total_1 = forms.CharField(
        label="6. Total de ingresos - Total incomes", max_length=100
    )
    incomes_total_2 = forms.CharField(
        label="6. Total de ingresos - Total incomes", max_length=100
    )

    expenses_salaries_1 = forms.CharField(
        label="1. Salarios, jornales, bono de Navidad y comisiones - Salaries, wages, Christmas bonus, <br>&emsp;and commissions",
        max_length=100,
    )
    expenses_salaries_2 = forms.CharField(
        label="1. Salarios, jornales, bono de Navidad y comisiones - Salaries, wages, Christmas bonus, <br>&emsp;and commissions",
        max_length=100,
    )
    expenses_interests_1 = forms.CharField(
        label="2. Intereses - Interests", max_length=100
    )
    expenses_interests_2 = forms.CharField(
        label="2. Intereses - Interests", max_length=100
    )
    expenses_rents_1 = forms.CharField(
        label="3. Renta de terreno y edificio - Rent of land and building",
        max_length=100,
    )
    expenses_rents_2 = forms.CharField(
        label="3. Renta de terreno y edificio - Rent of land and building",
        max_length=100,
    )
    expenses_depreciation_1 = forms.CharField(
        label="4. Depreciación - Depreciation", max_length=100
    )
    expenses_depreciation_2 = forms.CharField(
        label="4. Depreciación - Depreciation", max_length=100
    )
    expenses_debts_1 = forms.CharField(
        label="5.  Rentas incobrables - Bad debts", max_length=100
    )
    expenses_debts_2 = forms.CharField(
        label="5.  Rentas incobrables - Bad debts", max_length=100
    )
    expenses_donations_1 = forms.CharField(
        label="6. Donaciones - Donations", max_length=100
    )
    expenses_donations_2 = forms.CharField(
        label="6. Donaciones - Donations", max_length=100
    )
    expenses_tax_1 = forms.CharField(
        label="7. Impuesto sobre ventas y uso - Sales and use tax", max_length=100
    )
    expenses_tax_2 = forms.CharField(
        label="7. Impuesto sobre ventas y uso - Sales and use tax", max_length=100
    )
    expenses_machinery_1 = forms.CharField(
        label="a. Por Compra de maquinaria y equipo - On purchases of machinery and equipment",
        max_length=100,
    )
    expenses_machinery_2 = forms.CharField(
        label="a. Por Compra de maquinaria y equipo - On purchases of machinery and equipment",
        max_length=100,
    )
    other_purchases_1 = forms.CharField(
        label="b. Por otras compras - On other purchases", max_length=100
    )
    other_purchases_2 = forms.CharField(
        label="b. Por otras compras - On other purchases", max_length=100
    )
    expenses_licenses_1 = forms.CharField(
        label="8. Licencias y patentes - Licenses and patents", max_length=100
    )
    expenses_licenses_2 = forms.CharField(
        label="8. Licencias y patentes - Licenses and patents", max_length=100
    )
    expenses_other_1 = forms.CharField(
        label="9. Otros gastos de operación - Other operating expenses", max_length=100
    )
    expenses_other_2 = forms.CharField(
        label="9. Otros gastos de operación - Other operating expenses", max_length=100
    )
    net_profit_1 = forms.CharField(
        label="C. Ganancia o pérdida neta ( + ó - ) - Net profit or loss",
        max_length=100,
    )
    net_profit_2 = forms.CharField(
        label="C. Ganancia o pérdida neta ( + ó - ) - Net profit or loss",
        max_length=100,
    )
    income_tax_1 = forms.CharField(
        label="1. Contribución sobre ingresos - Income tax", max_length=100
    )
    income_tax_2 = forms.CharField(
        label="1. Contribución sobre ingresos - Income tax", max_length=100
    )
    profit_after_tax_1 = forms.CharField(
        label="2. Ganancia después de contribución sobre ingresos - Profit after income tax",
        max_length=100,
    )
    profit_after_tax_2 = forms.CharField(
        label="2. Ganancia después de contribución sobre ingresos - Profit after income tax",
        max_length=100,
    )
    withheld_tax_1 = forms.CharField(
        label="D. Impuesto sobre ventas y uso retenido - Sales and use tax Withheld",
        max_length=100,
    )
    withheld_tax_2 = forms.CharField(
        label="D. Impuesto sobre ventas y uso retenido - Sales and use tax Withheld",
        max_length=100,
    )

    signature = forms.CharField(
        label="Firma del contribuyente o representante legal / Signature of taxpayer or legal representative",
        max_length=100,
    )
    rank = forms.CharField(label="Rango / Rank", max_length=100)


class IP_710(forms.Form):
    company_name = forms.CharField(
        label="Nombre compañía / Company Name", max_length=100
    )
    address = forms.CharField(label="Dirección / Address", max_length=200)
    email = forms.EmailField(label="Correo electrónico / Email")
    liaison_officer = forms.CharField(
        label="Persona contacto / Liaison officer", max_length=100
    )

    ssn = forms.CharField(
        label="Numero de Seguro Social / Social Security Number", max_length=11
    )
    tel = forms.CharField(label="Tel", max_length=20)
    fax = forms.CharField(label="Fax", max_length=20)

    legal_form = forms.ChoiceField(
        label="Forma legal de organización / Legal form of organization",
        choices=[
            ("Corporación", "Corporación"),
            ("Sociedad", "Sociedad"),
            ("Cooperativa", "Cooperativa"),
            ("Empresa Individual", "Empresa Individual"),
            ("Empresa sin fines pecuniarios", "Empresa sin fines pecuniarios"),
        ],
    )
    cfc = forms.ChoiceField(label="CEC", choices=[("Si", "Si"), ("No", "No")])
    business_type = forms.ChoiceField(
        label="Tipo de negocio / Business type",
        choices=[
            ("Comercio", "Comercio"),
            ("Manufactura", "Manufactura"),
            ("Servicios", "Servicios"),
            ("Agricultura", "Agricultura"),
            ("Otros", "Otros"),
        ],
    )
    business_function = forms.ChoiceField(
        label="Función del negocio / Business function",
        choices=[
            ("Venta de productos", "Venta de productos"),
            ("Venta de servicios", "Venta de servicios"),
            ("Venta de productos y servicios", "Venta de productos y servicios"),
        ],
    )
    branches = forms.ChoiceField(
        label="Sucursales / Branches", choices=[("Si", "Si"), ("No", "No")]
    )
    branches_yes = forms.CharField(
        label="Si si, cuantas / If yes, how many", max_length=100
    )
    closing_date = forms.DateField(
        label="Fecha de cierre de sus libros / Your accounting period closing date",
        widget=forms.SelectDateWidget,
    )
    start_year = forms.CharField(
        label="Año de inicio de operaciones / Year of start of operations",
        max_length=100,
    )
    end_year = forms.CharField(
        label="Año de cierre de operaciones / Year of end of operations", max_length=100
    )
    total_income_1 = forms.CharField(
        label="A. Ingresos totales - Total income", max_length=100
    )
    total_income_2 = forms.CharField(
        label="A. Ingresos totales - Total income", max_length=100
    )
    incomes_service_1 = forms.CharField(
        label="1. Ingresos por servicios - Incomes from services", max_length=100
    )
    incomes_service_2 = forms.CharField(
        label="1. Ingresos por servicios - Incomes from services", max_length=100
    )
    incomes_from_persons_1 = forms.CharField(
        label="2. Ingresos de personas - Incomes from persons", max_length=100
    )
    incomes_from_persons_2 = forms.CharField(
        label="2. Ingresos de personas - Incomes from persons", max_length=100
    )
    incomes_from_industries_1 = forms.CharField(
        label="3. Ingresos de industrias - Incomes from industries", max_length=100
    )
    incomes_from_industries_2 = forms.CharField(
        label="3. Ingresos de industrias - Incomes from industries", max_length=100
    )
    incomes_from_sales_1 = forms.CharField(
        label="4. Ingresos por ventas - Incomes from sales", max_length=100
    )
    incomes_from_sales_2 = forms.CharField(
        label="4. Ingresos por ventas - Incomes from sales", max_length=100
    )
    income_rent_machinery_1 = forms.CharField(
        label="5. Ingresos por renta de maquinaria - Incomes from rent of machinery",
        max_length=100,
    )
    income_rent_machinery_2 = forms.CharField(
        label="5. Ingresos por renta de maquinaria - Incomes from rent of machinery",
        max_length=100,
    )
    income_rent_land_1 = forms.CharField(
        label="6. Ingresos por renta de terreno - Incomes from rent of land",
        max_length=100,
    )
    income_rent_land_2 = forms.CharField(
        label="6. Ingresos por renta de terreno - Incomes from rent of land",
        max_length=100,
    )
    income_interests_1 = forms.CharField(
        label="7. Ingresos por intereses - Incomes from interests", max_length=100
    )
    income_interests_2 = forms.CharField(
        label="7. Ingresos por intereses - Incomes from interests", max_length=100
    )
    income_capital_gain_or_loss_1 = forms.CharField(
        label="8. Ganancia o pérdida de capital - Capital gain or loss", max_length=100
    )
    income_capital_gain_or_loss_2 = forms.CharField(
        label="8. Ganancia o pérdida de capital - Capital gain or loss", max_length=100
    )
    income_other_operating_1 = forms.CharField(
        label="9. Otros ingresos operacionales - Other operating income", max_length=100
    )
    income_other_operating_2 = forms.CharField(
        label="9. Otros ingresos operacionales - Other operating income", max_length=100
    )
    total_expenses_1 = forms.CharField(
        label="B. Total de gastos - Total expenses", max_length=100
    )
    total_expenses_2 = forms.CharField(
        label="B. Total de gastos - Total expenses", max_length=100
    )
    expenses_salaries_1 = forms.CharField(
        label="1. Salarios - Salaries", max_length=100
    )
    expenses_salaries_2 = forms.CharField(
        label="1. Salarios - Salaries", max_length=100
    )
    expenses_interests_1 = forms.CharField(
        label="2. Intereses - Interests", max_length=100
    )
    expenses_interests_2 = forms.CharField(
        label="2. Intereses - Interests", max_length=100
    )
    expenses_rent_land_1 = forms.CharField(
        label="3. Renta de terreno - Rent of land", max_length=100
    )
    expenses_rent_land_2 = forms.CharField(
        label="3. Renta de terreno - Rent of land", max_length=100
    )
    expenses_depreciation_1 = forms.CharField(
        label="4. Depreciación - Depreciation", max_length=100
    )
    expenses_depreciation_2 = forms.CharField(
        label="4. Depreciación - Depreciation", max_length=100
    )
    expenses_bad_debts_1 = forms.CharField(
        label="5. Malos créditos - Bad debts", max_length=100
    )
    expenses_bad_debts_2 = forms.CharField(
        label="5. Malos créditos - Bad debts", max_length=100
    )
    expenses_donations_1 = forms.CharField(
        label="6. Donaciones - Donations", max_length=100
    )
    expenses_donations_2 = forms.CharField(
        label="6. Donaciones - Donations", max_length=100
    )
    expenses_other_operating_1 = forms.CharField(
        label="7. Otros gastos operacionales - Other operating expenses", max_length=100
    )
    expenses_other_operating_2 = forms.CharField(
        label="7. Otros gastos operacionales - Other operating expenses", max_length=100
    )
    expenses_sales_and_use_1 = forms.CharField(
        label="8. Impuesto sobre ventas y uso - Sales and use tax", max_length=100
    )
    expenses_sales_and_use_2 = forms.CharField(
        label="8. Impuesto sobre ventas y uso - Sales and use tax", max_length=100
    )
    expenses_purchases_machinery_1 = forms.CharField(
        label="9. Compra de maquinaria - Purchase of machinery", max_length=100
    )
    expenses_purchases_machinery_2 = forms.CharField(
        label="9. Compra de maquinaria - Purchase of machinery", max_length=100
    )
    expenses_other_purchases_1 = forms.CharField(
        label="10. Otras compras - Other purchases", max_length=100
    )
    expenses_other_purchases_2 = forms.CharField(
        label="10. Otras compras - Other purchases", max_length=100
    )
    expenses_licenses_1 = forms.CharField(
        label="11. Licencias - Licenses", max_length=100
    )
    expenses_licenses_2 = forms.CharField(
        label="11. Licencias - Licenses", max_length=100
    )
    profit_incomes_tax_1 = forms.CharField(
        label="12. Ganancia después de contribución sobre ingresos - Profit after income tax",
        max_length=100,
    )
    profit_incomes_tax_2 = forms.CharField(
        label="12. Ganancia después de contribución sobre ingresos - Profit after income tax",
        max_length=100,
    )
    profit_after_income_tax_1 = forms.CharField(
        label="13. Ganancia después de contribución sobre ingresos - Profit after income tax",
        max_length=100,
    )
    profit_after_income_tax_2 = forms.CharField(
        label="13. Ganancia después de contribución sobre ingresos - Profit after income tax",
        max_length=100,
    )
    sales_tax_withheld_1 = forms.CharField(
        label="14. Impuesto sobre ventas y uso retenido - Sales tax withheld",
        max_length=100,
    )
    sales_tax_withheld_2 = forms.CharField(
        label="14. Impuesto sobre ventas y uso retenido - Sales tax withheld",
        max_length=100,
    )
    name = forms.CharField(
        label="Name of person filling the questionnaire", max_length=100
    )
    rank = forms.CharField(label="Rank", max_length=100)


class JP_544_2(forms.Form):
    university_name = forms.CharField(label="Nombre de la universidad / University name", max_length=100)
    phone = forms.CharField(label="Teléfono / Phone", max_length=20)
    contact_person = forms.CharField(label="Persona de contacto / Contact person", max_length=100)
    title_position = forms.CharField(label="Título / Cargo / Title / Position", max_length=100)

    federal_agency_name_1 = forms.CharField(label="Nombre de la agencia federal / Federal agency name", max_length=100)
    federal_program_1 = forms.CharField(label="Programa federal / Federal program", max_length=100)
    federal_recieived_amount_1 = forms.CharField(label="Cantidad recibida / Amount received", max_length=100)
    federal_date_receipt_1 = forms.DateField(label="Fecha de recibo / Date of receipt", widget=forms.SelectDateWidget)
    
    federal_agency_name_2 = forms.CharField(label="Nombre de la agencia federal / Federal agency name", max_length=100)
    federal_program_2 = forms.CharField(label="Programa federal / Federal program", max_length=100)
    federal_recieived_amount_2 = forms.CharField(label="Cantidad recibida / Amount received", max_length=100)
    federal_date_receipt_2 = forms.DateField(label="Fecha de recibo / Date of receipt", widget=forms.SelectDateWidget)
    
    federal_agency_name_3 = forms.CharField(label="Nombre de la agencia federal / Federal agency name", max_length=100)
    federal_program_3 = forms.CharField(label="Programa federal / Federal program", max_length=100)
    federal_recieived_amount_3 = forms.CharField(label="Cantidad recibida / Amount received", max_length=100)
    federal_date_receipt_3 = forms.DateField(label="Fecha de recibo / Date of receipt", widget=forms.SelectDateWidget)
    
    federal_agency_name_4 = forms.CharField(label="Nombre de la agencia federal / Federal agency name", max_length=100)
    federal_program_4 = forms.CharField(label="Programa federal / Federal program", max_length=100)
    federal_recieived_amount_4 = forms.CharField(label="Cantidad recibida / Amount received", max_length=100)
    federal_date_receipt_4 = forms.DateField(label="Fecha de recibo / Date of receipt", widget=forms.SelectDateWidget)
    
    federal_agency_name_5 = forms.CharField(label="Nombre de la agencia federal / Federal agency name", max_length=100)
    federal_program_5 = forms.CharField(label="Programa federal / Federal program", max_length=100)
    federal_recieived_amount_5 = forms.CharField(label="Cantidad recibida / Amount received", max_length=100)
    federal_date_receipt_5 = forms.DateField(label="Fecha de recibo / Date of receipt", widget=forms.SelectDateWidget)
    
    federal_agency_name_6 = forms.CharField(label="Nombre de la agencia federal / Federal agency name", max_length=100)
    federal_program_6 = forms.CharField(label="Programa federal / Federal program", max_length=100)
    federal_recieived_amount_6 = forms.CharField(label="Cantidad recibida / Amount received", max_length=100)
    federal_date_receipt_6 = forms.DateField(label="Fecha de recibo / Date of receipt", widget=forms.SelectDateWidget)
    
    federal_agency_name_7 = forms.CharField(label="Nombre de la agencia federal / Federal agency name", max_length=100)
    federal_program_7 = forms.CharField(label="Programa federal / Federal program", max_length=100)
    federal_recieived_amount_7 = forms.CharField(label="Cantidad recibida / Amount received", max_length=100)
    federal_date_receipt_7 = forms.DateField(label="Fecha de recibo / Date of receipt", widget=forms.SelectDateWidget)
    
    federal_agency_name_8 = forms.CharField(label="Nombre de la agencia federal / Federal agency name", max_length=100)
    federal_program_8 = forms.CharField(label="Programa federal / Federal program", max_length=100)
    federal_recieived_amount_8 = forms.CharField(label="Cantidad recibida / Amount received", max_length=100)
    federal_date_receipt_8 = forms.DateField(label="Fecha de recibo / Date of receipt", widget=forms.SelectDateWidget)

    local_agency_name_1 = forms.CharField(label="Nombre de la agencia local / Local agency name", max_length=100)
    agency_program_1 = forms.CharField(label="Programa de la agencia / Agency program", max_length=100)
    agency_recieived_amount_1 = forms.CharField(label="Cantidad recibida / Amount received", max_length=100)
    agency_date_receipt_1 = forms.DateField(label="Fecha de recibo / Date of receipt", widget=forms.SelectDateWidget)
    
    local_agency_name_2 = forms.CharField(label="Nombre de la agencia local / Local agency name", max_length=100)
    agency_program_2 = forms.CharField(label="Programa de la agencia / Agency program", max_length=100)
    agency_recieived_amount_2 = forms.CharField(label="Cantidad recibida / Amount received", max_length=100)
    agency_date_receipt_2 = forms.DateField(label="Fecha de recibo / Date of receipt", widget=forms.SelectDateWidget)
    
    local_agency_name_3 = forms.CharField(label="Nombre de la agencia local / Local agency name", max_length=100)
    agency_program_3 = forms.CharField(label="Programa de la agencia / Agency program", max_length=100)
    agency_recieived_amount_3 = forms.CharField(label="Cantidad recibida / Amount received", max_length=100)
    agency_date_receipt_3 = forms.DateField(label="Fecha de recibo / Date of receipt", widget=forms.SelectDateWidget)
    
    local_agency_name_4 = forms.CharField(label="Nombre de la agencia local / Local agency name", max_length=100)
    agency_program_4 = forms.CharField(label="Programa de la agencia / Agency program", max_length=100)
    agency_recieived_amount_4 = forms.CharField(label="Cantidad recibida / Amount received", max_length=100)
    agency_date_receipt_4 = forms.DateField(label="Fecha de recibo / Date of receipt", widget=forms.SelectDateWidget)
    
    local_agency_name_5 = forms.CharField(label="Nombre de la agencia local / Local agency name", max_length=100)
    agency_program_5 = forms.CharField(label="Programa de la agencia / Agency program", max_length=100)
    agency_recieived_amount_5 = forms.CharField(label="Cantidad recibida / Amount received", max_length=100)
    agency_date_receipt_5 = forms.DateField(label="Fecha de recibo / Date of receipt", widget=forms.SelectDateWidget)
    
    total_students_enrolled = forms.CharField(label="Total de estudiantes matriculados / Total students enrolled", max_length=100)
    students_recived_amount = forms.CharField(label="Cantidad recibida / Amount received", max_length=100)
    
    total_pell_grant_students = forms.CharField(label="Total de estudiantes con beca Pell / Total Pell grant students", max_length=100)
    pell_grant_students_amount = forms.CharField(label="Cantidad recibida / Amount received", max_length=100)

    total_no_resident_student = forms.CharField(label="Total de estudiantes no residentes / Total non-resident students", max_length=100)
    no_resident_student_amount = forms.CharField(label="Cantidad recibida / Amount received", max_length=100)
    
    no_resident_students_bills = forms.CharField(label="Facturas de estudiantes no residentes / Non-resident students bills", max_length=100)

    loans_granted = forms.CharField(label="Préstamos otorgados / Loans granted", max_length=100)
    loans_granted_amount = forms.CharField(label="Cantidad recibida / Amount received", max_length=100)

    donations_institution_name_1 = forms.CharField(label="Nombre de la institución donante / Donations institution name", max_length=100)
    donations_amount_1 = forms.CharField(label="Cantidad recibida / Amount received", max_length=100)
    donations_date_1 = forms.DateField(label="Fecha de recibo / Date of receipt", widget=forms.SelectDateWidget)
    
    donations_institution_name_2 = forms.CharField(label="Nombre de la institución donante / Donations institution name", max_length=100)
    donations_amount_2 = forms.CharField(label="Cantidad recibida / Amount received", max_length=100)
    donations_date_2 = forms.DateField(label="Fecha de recibo / Date of receipt", widget=forms.SelectDateWidget)
    
    donations_institution_name_3 = forms.CharField(label="Nombre de la institución donante / Donations institution name", max_length=100)
    donations_amount_3 = forms.CharField(label="Cantidad recibida / Amount received", max_length=100)
    donations_date_3 = forms.DateField(label="Fecha de recibo / Date of receipt", widget=forms.SelectDateWidget)
    
    donations_institution_name_4 = forms.CharField(label="Nombre de la institución donante / Donations institution name", max_length=100)
    donations_amount_4 = forms.CharField(label="Cantidad recibida / Amount received", max_length=100)
    donations_date_4 = forms.DateField(label="Fecha de recibo / Date of receipt", widget=forms.SelectDateWidget)
    
    donations_institution_name_5 = forms.CharField(label="Nombre de la institución donante / Donations institution name", max_length=100)
    donations_amount_5 = forms.CharField(label="Cantidad recibida / Amount received", max_length=100)
    donations_date_5 = forms.DateField(label="Fecha de recibo / Date of receipt", widget=forms.SelectDateWidget)
    
    profesional_services_amount = forms.CharField(label="Cantidad recibida / Amount received", max_length=100)
    profesional_services_payment = forms.CharField(label="Pago / Payment", max_length=100)
    
    other_payment_relations_1 = forms.CharField(label="Otras relaciones de pago / Other payment relations", max_length=100)
    other_payment_relations_amount_1 = forms.CharField(label="Cantidad recibida / Amount received", max_length=100)
    other_payment_relations_payment_1 = forms.CharField(label="Pago / Payment", max_length=100)
    
    other_payment_relations_2 = forms.CharField(label="Otras relaciones de pago / Other payment relations", max_length=100)
    other_payment_relations_amount_2 = forms.CharField(label="Cantidad recibida / Amount received", max_length=100)
    other_payment_relations_payment_2 = forms.CharField(label="Pago / Payment", max_length=100)
    
    other_payment_relations_3 = forms.CharField(label="Otras relaciones de pago / Other payment relations", max_length=100)
    other_payment_relations_amount_3 = forms.CharField(label="Cantidad recibida / Amount received", max_length=100)
    other_payment_relations_payment_3 = forms.CharField(label="Pago / Payment", max_length=100)
    
    other_payment_relations_4 = forms.CharField(label="Otras relaciones de pago / Other payment relations", max_length=100)
    other_payment_relations_amount_4 = forms.CharField(label="Cantidad recibida / Amount received", max_length=100)
    other_payment_relations_payment_4 = forms.CharField(label="Pago / Payment", max_length=100)
    
    acquired_value = forms.CharField(label="Valor adquirido / Acquired value", max_length=100)
    investment_amount = forms.CharField(label="Cantidad invertida / Amount invested", max_length=100)
    recived_interest = forms.CharField(label="Intereses recibidos / Interest received", max_length=100)


class IP_540P(forms.Form):
    company_name = forms.CharField(
        label="Nombre compañía / Company Name", max_length=100
    )
    address = forms.CharField(label="Dirección / Address", max_length=200)
    email = forms.EmailField(label="Correo electrónico / Email")
    liaison_officer = forms.CharField(
        label="Persona contacto / Liaison officer", max_length=100
    )
    ssn = forms.CharField(
        label="Numero de Seguro Social / Social Security Number", max_length=11
    )
    tel = forms.CharField(label="Tel", max_length=20)
    fax = forms.CharField(label="Fax", max_length=20)
    legal_form = forms.ChoiceField(
        label="Forma legal de organización / Legal form of organization",
        choices=[
            ("Corporación", "Corporación"),
            ("Sociedad", "Sociedad"),
            ("Cooperativa", "Cooperativa"),
            ("Empresa Individual", "Empresa Individual"),
            ("Empresa sin fines pecuniarios", "Empresa sin fines pecuniarios"),
        ],
    )
    cfc = forms.ChoiceField(label="CEC", choices=[("Si", "Si"), ("No", "No")])
    business_type = forms.CharField(
        label="Clase de negocio / Type of business", max_length=200
    )
    business_function = forms.CharField(
        label="Describa brevemente la función principal del negocio / Explain briefly the main function of the business activity",
        widget=forms.Textarea,
    )
    branches = forms.ChoiceField(
        label="¿Opera sucursuales esta firma? / Do you have branch operations?",
        choices=[("Si", "Si"), ("No", "No")],
    )
    branches_yes = forms.ChoiceField(
        label="afirmativo a branches",
        choices=[
            ("todas las sucursales", "todas las sucursales"),
            ("este establecimiento", "este establecimiento"),
        ],
    )
    closing_date = forms.DateField(
        label="Fecha de cierre de sus libros / Your accounting period closing date",
        widget=forms.SelectDateWidget,
    )
    start_year = forms.CharField(
        label="Año de inicio de operaciones / Year of start of operations",
        max_length=100,
    )
    end_year = forms.CharField(
        label="Año de cierre de operaciones / Year of end of operations", max_length=100
    )

    incomes_from_persons_1 = forms.CharField(
        label="1. Ingresos de personas - Incomes from persons", max_length=100
    )
    incomes_from_persons_2 = forms.CharField(
        label="1. Ingresos de personas - Incomes from persons", max_length=100
    )
    incomes_from_industries_and_businesses_1 = forms.CharField(
        label="2. Ingresos de industrias y negocios - Incomes from industries and businesses",
        max_length=100,
    )
    incomes_from_industries_and_businesses_2 = forms.CharField(
        label="2. Ingresos de industrias y negocios - Incomes from industries and businesses",
        max_length=100,
    )
    incomes_commissions_received_1 = forms.CharField(
        label="3. Comisiones recibidas - Commissions received", max_length=100
    )
    incomes_commissions_received_2 = forms.CharField(
        label="3. Comisiones recibidas - Commissions received", max_length=100
    )
    incomes_from_air_fare_1 = forms.CharField(
        label="4. Ingresos de pasajes aéreos - Incomes from air fare", max_length=100
    )
    incomes_from_air_fare_2 = forms.CharField(
        label="4. Ingresos de pasajes aéreos - Incomes from air fare", max_length=100
    )
    incomes_from_maritime_1 = forms.CharField(
        label="5. Ingresos de pasajes marítimos - Incomes from maritime", max_length=100
    )
    incomes_from_maritime_2 = forms.CharField(
        label="5. Ingresos de pasajes marítimos - Incomes from maritime", max_length=100
    )
    incomes_rent_1 = forms.CharField(
        label="6. Ingresos de renta - Incomes from rent", max_length=100
    )
    incomes_rent_2 = forms.CharField(
        label="6. Ingresos de renta - Incomes from rent", max_length=100
    )
    incomes_interests_1 = forms.CharField(
        label="7. Ingresos de intereses - Incomes from interests", max_length=100
    )
    incomes_interests_2 = forms.CharField(
        label="7. Ingresos de intereses - Incomes from interests", max_length=100
    )
    incomes_capital_gain_loss_1 = forms.CharField(
        label="8. Ganancia o pérdida de capital - Capital gain or loss", max_length=100
    )
    incomes_capital_gain_loss_2 = forms.CharField(
        label="8. Ganancia o pérdida de capital - Capital gain or loss", max_length=100
    )
    incomes_other_operating_1 = forms.CharField(
        label="9. Otros ingresos operacionales - Other operating income", max_length=100
    )
    incomes_other_operating_2 = forms.CharField(
        label="9. Otros ingresos operacionales - Other operating income", max_length=100
    )
    total_incomes_1 = forms.CharField(
        label="10. Total de ingresos - Total incomes", max_length=100
    )
    total_incomes_2 = forms.CharField(
        label="10. Total de ingresos - Total incomes", max_length=100
    )
    expenses_salaries_wages_bonus_1 = forms.CharField(
        label="1. Salarios, jornales, bono de Navidad y comisiones - Salaries, wages, Christmas bonus, <br>&emsp;and commissions",
        max_length=100,
    )
    expenses_salaries_wages_bonus_2 = forms.CharField(
        label="1. Salarios, jornales, bono de Navidad y comisiones - Salaries, wages, Christmas bonus, <br>&emsp;and commissions",
        max_length=100,
    )
    expenses_interests_1 = forms.CharField(
        label="2. Intereses - Interests", max_length=100
    )
    expenses_interests_2 = forms.CharField(
        label="2. Intereses - Interests", max_length=100
    )
    expenses_rent_1 = forms.CharField(
        label="3. Renta de terreno y edificio - Rent of land and building",
        max_length=100,
    )
    expenses_rent_2 = forms.CharField(
        label="3. Renta de terreno y edificio - Rent of land and building",
        max_length=100,
    )
    expenses_depreciation_1 = forms.CharField(
        label="4. Depreciación - Depreciation", max_length=100
    )
    expenses_depreciation_2 = forms.CharField(
        label="4. Depreciación - Depreciation", max_length=100
    )
    expenses_donations_1 = forms.CharField(
        label="5. Donaciones - Donations", max_length=100
    )
    expenses_donations_2 = forms.CharField(
        label="5. Donaciones - Donations", max_length=100
    )
    expenses_sales_taxes_1 = forms.CharField(
        label="6. Impuesto sobre ventas y uso - Sales and use tax", max_length=100
    )
    expenses_sales_taxes_2 = forms.CharField(
        label="6. Impuesto sobre ventas y uso - Sales and use tax", max_length=100
    )
    expenses_purchases_machinery_1 = forms.CharField(
        label="a. Por Compra de maquinaria y equipo - On purchases of machinery and equipment",
        max_length=100,
    )
    expenses_purchases_machinery_2 = forms.CharField(
        label="a. Por Compra de maquinaria y equipo - On purchases of machinery and equipment",
        max_length=100,
    )
    expenses_other_purchases_1 = forms.CharField(
        label="b. Por otras compras - On other purchases", max_length=100
    )
    expenses_other_purchases_2 = forms.CharField(
        label="b. Por otras compras - On other purchases", max_length=100
    )
    expenses_licenses_1 = forms.CharField(
        label="7. Licencias y patentes - Licenses and patents", max_length=100
    )
    expenses_licenses_2 = forms.CharField(
        label="7. Licencias y patentes - Licenses and patents", max_length=100
    )
    expenses_other_operating_1 = forms.CharField(
        label="8. Otros gastos de operación - Other operating expenses", max_length=100
    )
    expenses_other_operating_2 = forms.CharField(
        label="8. Otros gastos de operación - Other operating expenses", max_length=100
    )
    total_expenses_1 = forms.CharField(
        label="9. Total de gastos - Total expenses", max_length=100
    )
    total_expenses_2 = forms.CharField(
        label="9. Total de gastos - Total expenses", max_length=100
    )
    net_profit_1 = forms.CharField(
        label="C. Ganancia o pérdida neta ( + ó - ) - Net profit or loss",
        max_length=100,
    )
    net_profit_2 = forms.CharField(
        label="C. Ganancia o pérdida neta ( + ó - ) - Net profit or loss",
        max_length=100,
    )
    profit_income_tax_1 = forms.CharField(
        label="1. Contribución sobre ingresos - Income tax", max_length=100
    )
    profit_income_tax_2 = forms.CharField(
        label="1. Contribución sobre ingresos - Income tax", max_length=100
    )
    profit_after_income_tax_1 = forms.CharField(
        label="2. Ganancia después de contribución sobre ingresos - Profit after income tax",
        max_length=100,
    )
    profit_after_income_tax_2 = forms.CharField(
        label="2. Ganancia después de contribución sobre ingresos - Profit after income tax",
        max_length=100,
    )
    sales_tax_withheld_1 = forms.CharField(
        label="D. Impuesto sobre ventas y uso retenido - Sales and use tax Withheld",
        max_length=100,
    )
    sales_tax_withheld_2 = forms.CharField(
        label="D. Impuesto sobre ventas y uso retenido - Sales and use tax Withheld",
        max_length=100,
    )

    name = forms.CharField(
        label="Name of person filling the questionnaire", max_length=100
    )
    rank = forms.CharField(label="Rank", max_length=100)


class IP_540S(forms.Form):
    company_name = forms.CharField(
        label="Nombre compañía / Company Name", max_length=100
    )
    address = forms.CharField(label="Dirección / Address", max_length=200)
    email = forms.EmailField(label="Correo electrónico / Email")
    liaison_officer = forms.CharField(
        label="Persona contacto / Liaison officer", max_length=100
    )
    ssn = forms.CharField(
        label="Numero de Seguro Social / Social Security Number", max_length=11
    )
    tel = forms.CharField(label="Tel", max_length=20)
    fax = forms.CharField(label="Fax", max_length=20)
    legal_form = forms.ChoiceField(
        label="Forma legal de organización / Legal form of organization",
        choices=[
            ("Corporación", "Corporación"),
            ("Sociedad", "Sociedad"),
            ("Cooperativa", "Cooperativa"),
            ("Empresa Individual", "Empresa Individual"),
            ("Empresa sin fines pecuniarios", "Empresa sin fines pecuniarios"),
        ],
    )
    cfc = forms.ChoiceField(label="CEC", choices=[("Si", "Si"), ("No", "No")])
    business_type = forms.ChoiceField(
        label="Tipo de negocio / Business type",
        choices=[
            ("Comercio", "Comercio"),
            ("Manufactura", "Manufactura"),
            ("Servicios", "Servicios"),
            ("Agricultura", "Agricultura"),
            ("Otros", "Otros"),
        ],
    )
    business_function = forms.ChoiceField(
        label="Función del negocio / Business function",
        choices=[
            ("Venta de productos", "Venta de productos"),
            ("Venta de servicios", "Venta de servicios"),
            ("Venta de productos y servicios", "Venta de productos y servicios"),
        ],
    )
    closing_date = forms.DateField(
        label="Fecha de cierre de sus libros / Your accounting period closing date",
        widget=forms.SelectDateWidget,
    )
    start_year = forms.CharField(
        label="Año de inicio de operaciones / Year of start of operations",
        max_length=100,
    )
    end_year = forms.CharField(
        label="Año de cierre de operaciones / Year of end of operations", max_length=100
    )
    incomes_from_persons_1 = forms.CharField(
        label="incomes from persons 1", max_length=100
    )
    incomes_from_persons_2 = forms.CharField(
        label="incomes from persons 2", max_length=100
    )
    incomes_from_industries_and_businesses_1 = forms.CharField(
        label="incomes from industries and businesses 1", max_length=100
    )
    incomes_from_industries_and_businesses_2 = forms.CharField(
        label="incomes from industries and businesses 2", max_length=100
    )
    expenses_newspapers_1 = forms.CharField(
        label="expenses newspapers 1", max_length=100
    )
    expenses_newspapers_2 = forms.CharField(
        label="expenses newspapers 2", max_length=100
    )
    expenses_radio_1 = forms.CharField(label="expenses radio 1", max_length=100)
    expenses_radio_2 = forms.CharField(label="expenses radio 2", max_length=100)
    expenses_other_1 = forms.CharField(label="expenses other 1", max_length=100)
    expenses_other_2 = forms.CharField(label="expenses other 2", max_length=100)
    gross_profit_1 = forms.CharField(label="gross profit 1", max_length=100)
    gross_profit_2 = forms.CharField(label="gross profit 2", max_length=100)
    gross_other_income_1 = forms.CharField(label="gross other income 1", max_length=100)
    gross_other_income_2 = forms.CharField(label="gross other income 2", max_length=100)
    gross_interests_1 = forms.CharField(label="gross interests 1", max_length=100)
    gross_interests_2 = forms.CharField(label="gross interests 2", max_length=100)
    gross_rent_land_1 = forms.CharField(label="gross rent land 1", max_length=100)
    gross_rent_land_2 = forms.CharField(label="gross rent land 2", max_length=100)
    gross_capital_gain_1 = forms.CharField(label="gross capital gain 1", max_length=100)
    gross_capital_gain_2 = forms.CharField(label="gross capital gain 2", max_length=100)
    gross_other_1 = forms.CharField(label="gross other 1", max_length=100)
    gross_other_2 = forms.CharField(label="gross other 2", max_length=100)
    income_total_income_1 = forms.CharField(
        label="income total income 1", max_length=100
    )
    income_total_income_2 = forms.CharField(
        label="income total income 2", max_length=100
    )
    income_total_expenses_1 = forms.CharField(
        label="income total expenses 1", max_length=100
    )
    income_total_expenses_2 = forms.CharField(
        label="income total expenses 2", max_length=100
    )
    expenses_salaries_wages_bonus_1 = forms.CharField(
        label="expenses salaries wages bonus 1", max_length=100
    )
    expenses_salaries_wages_bonus_2 = forms.CharField(
        label="expenses salaries wages bonus 2", max_length=100
    )
    expenses_interests_1 = forms.CharField(label="expenses interests 1", max_length=100)
    expenses_interests_2 = forms.CharField(label="expenses interests 2", max_length=100)
    expenses_rent_1 = forms.CharField(label="expenses rent 1", max_length=100)
    expenses_rent_2 = forms.CharField(label="expenses rent 2", max_length=100)
    expenses_depreciation_1 = forms.CharField(
        label="expenses depreciation 1", max_length=100
    )
    expenses_depreciation_2 = forms.CharField(
        label="expenses depreciation 2", max_length=100
    )
    expenses_other_taxes_1 = forms.CharField(
        label="expenses other taxes 1", max_length=100
    )
    expenses_other_taxes_2 = forms.CharField(
        label="expenses other taxes 2", max_length=100
    )
    expenses_donations_1 = forms.CharField(label="expenses donations 1", max_length=100)
    expenses_donations_2 = forms.CharField(label="expenses donations 2", max_length=100)
    expenses_sales_taxes_1 = forms.CharField(
        label="expenses sales taxes 1", max_length=100
    )
    expenses_sales_taxes_2 = forms.CharField(
        label="expenses sales taxes 2", max_length=100
    )
    expenses_purchases_machinery_1 = forms.CharField(
        label="expenses purchases machinery 1", max_length=100
    )
    expenses_purchases_machinery_2 = forms.CharField(
        label="expenses purchases machinery 2", max_length=100
    )
    expenses_other_purchases_1 = forms.CharField(
        label="expenses other purchases 1", max_length=100
    )
    expenses_other_purchases_2 = forms.CharField(
        label="expenses other purchases 2", max_length=100
    )
    expenses_licenses_1 = forms.CharField(label="expenses licenses 1", max_length=100)
    expenses_licenses_2 = forms.CharField(label="expenses licenses 2", max_length=100)
    expenses_other_operation_1 = forms.CharField(
        label="expenses other operation 1", max_length=100
    )
    expenses_other_operation_2 = forms.CharField(
        label="expenses other operation 2", max_length=100
    )
    net_profit_1 = forms.CharField(label="net profit 1", max_length=100)
    net_profit_2 = forms.CharField(label="net profit 2", max_length=100)
    profit_income_tax_1 = forms.CharField(label="profit income tax 1", max_length=100)
    profit_income_tax_2 = forms.CharField(label="profit income tax 2", max_length=100)
    profit_after_income_tax_1 = forms.CharField(
        label="profit after income tax 1", max_length=100
    )
    profit_after_income_tax_2 = forms.CharField(
        label="profit after income tax 2", max_length=100
    )
    sales_tax_withheld_1 = forms.CharField(label="sales_tax_withheld_1", max_length=100)
    sales_tax_withheld_2 = forms.CharField(label="sales_tax_withheld_2", max_length=100)
    name = forms.CharField(
        label="Name of person filling the questionnaire", max_length=100
    )
    rank = forms.CharField(label="Rank", max_length=100)


class IP_540a(forms.Form):
    company_name = forms.CharField(
        label="Nombre compañía / Company Name", max_length=100
    )
    address = forms.CharField(label="Dirección / Address", max_length=200)
    email = forms.EmailField(label="Correo electrónico / Email")
    liaison_officer = forms.CharField(
        label="Persona contacto / Liaison officer", max_length=100
    )
    ssn = forms.CharField(
        label="Numero de Seguro Social / Social Security Number", max_length=11
    )
    tel = forms.CharField(label="Tel", max_length=20)
    fax = forms.CharField(label="Fax", max_length=20)
    legal_form = forms.ChoiceField(
        label="Forma legal de organización / Legal form of organization",
        choices=[
            ("Corporación", "Corporación"),
            ("Sociedad", "Sociedad"),
            ("Cooperativa", "Cooperativa"),
            ("Empresa Individual", "Empresa Individual"),
            ("Empresa sin fines pecuniarios", "Empresa sin fines pecuniarios"),
        ],
    )
    cfc = forms.ChoiceField(label="CEC", choices=[("Si", "Si"), ("No", "No")])
    business_type = forms.ChoiceField(
        label="Tipo de negocio / Business type",
        choices=[
            ("Comercio", "Comercio"),
            ("Manufactura", "Manufactura"),
            ("Servicios", "Servicios"),
            ("Agricultura", "Agricultura"),
            ("Otros", "Otros"),
        ],
    )
    business_function = forms.ChoiceField(
        label="Función del negocio / Business function",
        choices=[
            ("Venta de productos", "Venta de productos"),
            ("Venta de servicios", "Venta de servicios"),
            ("Venta de productos y servicios", "Venta de productos y servicios"),
        ],
    )
    branches = forms.ChoiceField(
        label="Sucursales / Branches", choices=[("Si", "Si"), ("No", "No")]
    )
    branches_yes = forms.CharField(
        label="Si si, cuantas / If yes, how many", max_length=100
    )
    closing_date = forms.DateField(
        label="Fecha de cierre de sus libros / Your accounting period closing date",
        widget=forms.SelectDateWidget,
    )

    start_year = forms.CharField(
        label="Año de inicio de operaciones / Year of start of operations",
        max_length=100,
    )
    end_year = forms.CharField(
        label="Año de cierre de operaciones / Year of end of operations", max_length=100
    )

    billings_1 = forms.CharField(
        label="A. Facturación o ventas  - Billing or sales", max_length=100
    )
    billings_2 = forms.CharField(
        label="A. Facturación o ventas  - Billing or sales", max_length=100
    )
    incomes_from_persons_1 = forms.CharField(
        label="1. De personas - From persons", max_length=100
    )
    incomes_from_persons_2 = forms.CharField(
        label="1. De personas - From persons", max_length=100
    )
    incomes_from_industries_and_businesses_1 = forms.CharField(
        label="2. De industrias y negocios - From industries and businesses",
        max_length=100,
    )
    incomes_from_industries_and_businesses_2 = forms.CharField(
        label="2. De industrias y negocios - From industries and businesses",
        max_length=100,
    )

    billing_expenses_1 = forms.CharField(
        label="B. Gastos de facturación - Billing expenses", max_length=100
    )
    billing_expenses_2 = forms.CharField(
        label="B. Gastos de facturación - Billing expenses", max_length=100
    )
    expenses_newspapers_1 = forms.CharField(
        label="1. Periódicos - Newspapers", max_length=100
    )
    expenses_newspapers_2 = forms.CharField(
        label="1. Periódicos - Newspapers", max_length=100
    )
    expenses_radio_television_1 = forms.CharField(
        label="2. Radio y televisión - Radio and television", max_length=100
    )
    expenses_radio_television_2 = forms.CharField(
        label="2. Radio y televisión - Radio and television", max_length=100
    )
    expenses_others_1 = forms.CharField(label="3. Otros - Others", max_length=100)
    expenses_others_2 = forms.CharField(label="3. Otros - Others", max_length=100)

    gross_profit_1 = forms.CharField(
        label="C. Ganancia bruta (A-B) - Gross profit (A-B)", max_length=100
    )
    gross_profit_2 = forms.CharField(
        label="C. Ganancia bruta (A-B) - Gross profit (A-B)", max_length=100
    )

    other_incomes_1 = forms.CharField(
        label="D. Otros ingresos - Other incomes", max_length=100
    )
    other_incomes_2 = forms.CharField(
        label="D. Otros ingresos - Other incomes", max_length=100
    )
    other_interests_1 = forms.CharField(
        label="1. Intereses - Interests", max_length=100
    )
    other_interests_2 = forms.CharField(
        label="1. Intereses - Interests", max_length=100
    )
    rent_of_land_1 = forms.CharField(
        label="2. Renta de terreno y edificio - Rent of land and building",
        max_length=100,
    )
    rent_of_land_2 = forms.CharField(
        label="2. Renta de terreno y edificio - Rent of land and building",
        max_length=100,
    )
    capital_1 = forms.CharField(
        label="3. Ganancia de capital - Capital gain", max_length=100
    )
    capital_2 = forms.CharField(
        label="3. Ganancia de capital - Capital gain", max_length=100
    )
    others_1 = forms.CharField(label="4. Otros - Others", max_length=100)
    others_2 = forms.CharField(label="4. Otros - Others", max_length=100)

    total_incomes_1 = forms.CharField(
        label="E. Total de ingresos (C+D) - Total incomes (C+D)", max_length=100
    )
    total_incomes_2 = forms.CharField(
        label="E. Total de ingresos (C+D) - Total incomes (C+D)", max_length=100
    )

    total_expenses_1 = forms.CharField(
        label="F. Total de gastos - Total expenses", max_length=100
    )
    total_expenses_2 = forms.CharField(
        label="F. Total de gastos - Total expenses", max_length=100
    )
    expenses_salaries_bonus_1 = forms.CharField(
        label="1. Salario, jornales, bono de Navidad y comisiones - Salaries, wages, Christmas bonus and comissions",
        max_length=100,
    )
    expenses_salaries_bonus_2 = forms.CharField(
        label="1. Salario, jornales, bono de Navidad y comisiones - Salaries, wages, Christmas bonus and comissions",
        max_length=100,
    )
    expenses_interests_1 = forms.CharField(
        label="2. Intereses - Interests", max_length=100
    )
    expenses_interests_2 = forms.CharField(
        label="2. Intereses - Interests", max_length=100
    )
    expenses_rent_1 = forms.CharField(
        label="3. Renta de terreno y edificio - Rent of land and building",
        max_length=100,
    )
    expenses_rent_2 = forms.CharField(
        label="3. Renta de terreno y edificio - Rent of land and building",
        max_length=100,
    )
    expenses_depreciation_1 = forms.CharField(
        label="4. Depreciación - Depreciation", max_length=100
    )
    expenses_depreciation_2 = forms.CharField(
        label="4. Depreciación - Depreciation", max_length=100
    )
    expenses_other_donations_1 = forms.CharField(
        label="5. Otras contribuciones - Other taxes", max_length=100
    )
    expenses_other_donations_2 = forms.CharField(
        label="5. Otras contribuciones - Other taxes", max_length=100
    )
    expenses_donations_1 = forms.CharField(
        label="6. Donaciones - Donations", max_length=100
    )
    expenses_donations_2 = forms.CharField(
        label="6. Donaciones - Donations", max_length=100
    )
    expenses_sales_taxes_1 = forms.CharField(
        label="7. Impuesto sobre ventas y uso - Sales and use tax", max_length=100
    )
    expenses_sales_taxes_2 = forms.CharField(
        label="7. Impuesto sobre ventas y uso - Sales and use tax", max_length=100
    )
    expenses_purchases_machinery_1 = forms.CharField(
        label="a. Por compra de maquinaria y equipo - On purchases of machinery and equipment",
        max_length=100,
    )
    expenses_purchases_machinery_2 = forms.CharField(
        label="a. Por compra de maquinaria y equipo - On purchases of machinery and equipment",
        max_length=100,
    )
    expenses_other_purchases_1 = forms.CharField(
        label="b. Otras compras - Other purchases", max_length=100
    )
    expenses_other_purchases_2 = forms.CharField(
        label="b. Otras compras - Other purchases", max_length=100
    )
    expenses_licenses_1 = forms.CharField(
        label="8. Licencias y patentes - Licenses and patents", max_length=100
    )
    expenses_licenses_2 = forms.CharField(
        label="8. Licencias y patentes - Licenses and patents", max_length=100
    )
    expenses_other_operationg_1 = forms.CharField(
        label="9. Otros gastos operacionales - Other operating expenses", max_length=100
    )
    expenses_other_operationg_2 = forms.CharField(
        label="9. Otros gastos operacionales - Other operating expenses", max_length=100
    )

    net_profit_1 = forms.CharField(
        label="G. Ganancia o pérdida neta (+ ó -) - Net profit or loss (+ or -)",
        max_length=100,
    )
    net_profit_2 = forms.CharField(
        label="G. Ganancia o pérdida neta (+ ó -) - Net profit or loss (+ or -)",
        max_length=100,
    )
    profit_income_tax_1 = forms.CharField(
        label="1. Contribución sobre ingresos - Income tax", max_length=100
    )
    profit_income_tax_2 = forms.CharField(
        label="1. Contribución sobre ingresos - Income tax", max_length=100
    )
    profit_after_income_tax_1 = forms.CharField(
        label="2. Ganancia después de contribución sobre ingresos - Profit after income tax",
        max_length=100,
    )
    profit_after_income_tax_2 = forms.CharField(
        label="2. Ganancia después de contribución sobre ingresos - Profit after income tax",
        max_length=100,
    )

    sales_tax_withheld_1 = forms.CharField(
        label="H. Impuesto sobre ventas y uso retenido - Sales tax withheld",
        max_length=100,
    )
    sales_tax_withheld_2 = forms.CharField(
        label="H. Impuesto sobre ventas y uso retenido - Sales tax withheld, max_length=100"
    )

    name = forms.CharField(
        label="Name of person filling the questionnaire", max_length=100
    )
    rank = forms.CharField(label="Rank", max_length=100)


class IP_540v(forms.Form):
    company_name = forms.CharField(
        label="Nombre compañía / Company Name", max_length=100
    )
    address = forms.CharField(label="Dirección / Address", max_length=200)
    email = forms.EmailField(label="Correo electrónico / Email")
    liaison_officer = forms.CharField(
        label="Persona contacto / Liaison officer", max_length=100
    )
    ssn = forms.CharField(
        label="Numero de Seguro Social / Social Security Number", max_length=11
    )
    tel = forms.CharField(label="Tel", max_length=20)
    fax = forms.CharField(label="Fax", max_length=20)
    legal_form = forms.ChoiceField(
        label="Forma legal de organización / Legal form of organization",
        choices=[
            ("Corporación", "Corporación"),
            ("Sociedad", "Sociedad"),
            ("Cooperativa", "Cooperativa"),
            ("Empresa Individual", "Empresa Individual"),
            ("Empresa sin fines pecuniarios", "Empresa sin fines pecuniarios"),
        ],
    )
    cfc = forms.ChoiceField(label="CEC", choices=[("Si", "Si"), ("No", "No")])
    business_type = forms.ChoiceField(
        label="Tipo de negocio / Business type",
        choices=[
            ("Comercio", "Comercio"),
            ("Manufactura", "Manufactura"),
            ("Servicios", "Servicios"),
            ("Agricultura", "Agricultura"),
            ("Otros", "Otros"),
        ],
    )
    business_function = forms.ChoiceField(
        label="Función del negocio / Business function",
        choices=[
            ("Venta de productos", "Venta de productos"),
            ("Venta de servicios", "Venta de servicios"),
            ("Venta de productos y servicios", "Venta de productos y servicios"),
        ],
    )
    branches = forms.ChoiceField(
        label="Sucursales / Branches", choices=[("Si", "Si"), ("No", "No")]
    )
    branches_yes = forms.CharField(
        label="Si si, cuantas / If yes, how many", max_length=100
    )
    closing_date = forms.DateField(
        label="Fecha de cierre de sus libros / Your accounting period closing date",
        widget=forms.SelectDateWidget,
    )
    start_year = forms.CharField(
        label="Año de inicio de operaciones / Year of start of operations",
        max_length=100,
    )
    end_year = forms.CharField(
        label="Año de cierre de operaciones / Year of end of operations", max_length=100
    )
    incomes_services_rendered_1 = forms.CharField(
        label="1. Ingresos por servicios prestados - Incomes from services rendered",
        max_length=100,
    )
    incomes_services_rendered_2 = forms.CharField(
        label="1. Ingresos por servicios prestados - Incomes from services rendered",
        max_length=100,
    )
    incomes_to_business_1 = forms.CharField(
        label="2. Ingresos a negocios - Incomes to business", max_length=100
    )
    incomes_to_business_2 = forms.CharField(
        label="2. Ingresos a negocios - Incomes to business", max_length=100
    )
    incomes_to_personal_pets_1 = forms.CharField(
        label="3. Ingresos a mascotas personales - Incomes to personal pets",
        max_length=100,
    )
    incomes_to_personal_pets_2 = forms.CharField(
        label="3. Ingresos a mascotas personales - Incomes to personal pets",
        max_length=100,
    )
    incomes_sale_merchandise_1 = forms.CharField(
        label="4. Ingresos por venta de mercancía - Incomes sale merchandise",
        max_length=100,
    )
    incomes_sale_merchandise_2 = forms.CharField(
        label="4. Ingresos por venta de mercancía - Incomes sale merchandise",
        max_length=100,
    )
    incomes_rent_of_land_and_building_1 = forms.CharField(
        label="5. Ingresos por renta de terreno y edificio - Incomes rent of land and building",
        max_length=100,
    )
    incomes_rent_of_land_and_building_2 = forms.CharField(
        label="5. Ingresos por renta de terreno y edificio - Incomes rent of land and building",
        max_length=100,
    )
    incomes_interests_1 = forms.CharField(
        label="6. Ingresos por intereses - Incomes interests", max_length=100
    )
    incomes_interests_2 = forms.CharField(
        label="6. Ingresos por intereses - Incomes interests", max_length=100
    )
    incomes_capital_gain_or_loss_1 = forms.CharField(
        label="7. Ganancia o pérdida de capital - Capital gain or loss", max_length=100
    )
    incomes_capital_gain_or_loss_2 = forms.CharField(
        label="7. Ganancia o pérdida de capital - Capital gain or loss", max_length=100
    )
    incomes_other_operating_income_1 = forms.CharField(
        label="8. Otros ingresos operacionales - Other operating income", max_length=100
    )
    incomes_other_operating_income_2 = forms.CharField(
        label="8. Otros ingresos operacionales - Other operating income", max_length=100
    )
    incomes_total_1 = forms.CharField(
        label="9. Total de ingresos - Total incomes", max_length=100
    )
    incomes_total_2 = forms.CharField(
        label="9. Total de ingresos - Total incomes", max_length=100
    )
    total_expenses_1 = forms.CharField(
        label="10. Total de gastos - Total expenses", max_length=100
    )
    total_expenses_2 = forms.CharField(
        label="10. Total de gastos - Total expenses", max_length=100
    )
    expenses_salaries_wages_bonus_1 = forms.CharField(
        label="1. Salarios, jornales, bono de Navidad y comisiones - Salaries, wages, Christmas bonus, and commissions",
        max_length=100,
    )
    expenses_salaries_wages_bonus_2 = forms.CharField(
        label="1. Salarios, jornales, bono de Navidad y comisiones - Salaries, wages, Christmas bonus, and commissions",
        max_length=100,
    )
    expenses_interests_1 = forms.CharField(
        label="2. Intereses - Interests", max_length=100
    )
    expenses_interests_2 = forms.CharField(
        label="2. Intereses - Interests", max_length=100
    )
    expenses_rent_1 = forms.CharField(
        label="3. Renta de terreno y edificio - Rent of land and building",
        max_length=100,
    )
    expenses_rent_2 = forms.CharField(
        label="3. Renta de terreno y edificio - Rent of land and building",
        max_length=100,
    )
    expenses_depreciation_1 = forms.CharField(
        label="4. Depreciación - Depreciation", max_length=100
    )
    expenses_depreciation_2 = forms.CharField(
        label="4. Depreciación - Depreciation", max_length=100
    )
    expenses_bad_debts_1 = forms.CharField(
        label="5. Malos créditos - Bad debts", max_length=100
    )
    expenses_bad_debts_2 = forms.CharField(
        label="5. Malos créditos - Bad debts", max_length=100
    )
    expenses_donations_1 = forms.CharField(
        label="6. Donaciones - Donations", max_length=100
    )
    expenses_donations_2 = forms.CharField(
        label="6. Donaciones - Donations", max_length=100
    )
    expenses_sales_taxes_1 = forms.CharField(
        label="7. Impuesto sobre ventas y uso - Sales and use tax", max_length=100
    )
    expenses_sales_taxes_2 = forms.CharField(
        label="7. Impuesto sobre ventas y uso - Sales and use tax", max_length=100
    )
    expenses_purchases_machinery_1 = forms.CharField(
        label="8. Por compra de maquinaria y equipo - On purchases of machinery and equipment",
        max_length=100,
    )
    expenses_purchases_machinery_2 = forms.CharField(
        label="8. Por compra de maquinaria y equipo - On purchases of machinery and equipment",
        max_length=100,
    )
    expenses_other_purchases_1 = forms.CharField(
        label="9. Por otras compras - On other purchases", max_length=100
    )
    expenses_other_purchases_2 = forms.CharField(
        label="9. Por otras compras - On other purchases", max_length=100
    )
    expenses_licenses_1 = forms.CharField(
        label="10. Licencias y patentes - Licenses and patents", max_length=100
    )
    expenses_licenses_2 = forms.CharField(
        label="10. Licencias y patentes - Licenses and patents", max_length=100
    )
    expenses_other_operating_1 = forms.CharField(
        label="11. Otros gastos de operación - Other operating expenses", max_length=100
    )
    expenses_other_operating_2 = forms.CharField(
        label="11. Otros gastos de operación - Other operating expenses", max_length=100
    )
    expenses_total_expenses_1 = forms.CharField(
        label="12. Total de gastos - Total expenses", max_length=100
    )
    expenses_total_expenses_2 = forms.CharField(
        label="12. Total de gastos - Total expenses", max_length=100
    )
    net_profit_1 = forms.CharField(
        label="13. Ganancia o pérdida neta ( + ó - ) - Net profit or loss",
        max_length=100,
    )
    net_profit_2 = forms.CharField(
        label="13. Ganancia o pérdida neta ( + ó - ) - Net profit or loss",
        max_length=100,
    )
    profit_income_tax_1 = forms.CharField(
        label="1. Contribución sobre ingresos - Income tax", max_length=100
    )
    profit_income_tax_2 = forms.CharField(
        label="1. Contribución sobre ingresos - Income tax", max_length=100
    )
    profit_after_income_tax_1 = forms.CharField(
        label="2. Ganancia después de contribución sobre ingresos - Profit after income tax",
        max_length=100,
    )
    profit_after_income_tax_2 = forms.CharField(
        label="2. Ganancia después de contribución sobre ingresos - Profit after income tax",
        max_length=100,
    )
    sales_tax_withheld_1 = forms.CharField(
        label="14. Impuesto sobre ventas y uso retenido - Sales and use tax Withheld",
        max_length=100,
    )
    sales_tax_withheld_2 = forms.CharField(
        label="14. Impuesto sobre ventas y uso retenido - Sales and use tax Withheld",
        max_length=100,
    )
    name = forms.CharField(
        label="Name of person filling the questionnaire", max_length=100
    )
    rank = forms.CharField(label="Rank", max_length=100)


class IP_720(forms.Form):
    company_name = forms.CharField(
        label="Nombre compañía / Company Name", max_length=100
    )
    address = forms.CharField(label="Dirección / Address", max_length=200)
    email = forms.EmailField(label="Correo electrónico / Email")
    liaison_officer = forms.CharField(
        label="Persona contacto / Liaison officer", max_length=100
    )
    ssn = forms.CharField(
        label="Numero de Seguro Social / Social Security Number", max_length=11
    )
    tel = forms.CharField(label="Tel", max_length=20)
    fax = forms.CharField(label="Fax", max_length=20)
    legal_form = forms.ChoiceField(
        label="Forma legal de organización / Legal form of organization",
        choices=[
            ("Corporación", "Corporación"),
            ("Sociedad", "Sociedad"),
            ("Cooperativa", "Cooperativa"),
            ("Empresa Individual", "Empresa Individual"),
            ("Empresa sin fines pecuniarios", "Empresa sin fines pecuniarios"),
        ],
    )
    cfc = forms.ChoiceField(label="CEC", choices=[("Si", "Si"), ("No", "No")])
    closing_date = forms.DateField(
        label="Fecha de cierre de sus libros / Your accounting period closing date",
        widget=forms.SelectDateWidget,
    )
    start_year = forms.CharField(
        label="Año de inicio de operaciones / Year of start of operations",
        max_length=100,
    )
    end_year = forms.CharField(
        label="Año de cierre de operaciones / Year of end of operations", max_length=100
    )
    total_incomes_1 = forms.CharField(
        label="1. Total de ingresos - Total incomes", max_length=100
    )
    total_incomes_2 = forms.CharField(
        label="1. Total de ingresos - Total incomes", max_length=100
    )
    incomes_from_persons_1 = forms.CharField(
        label="2. De personas - From persons", max_length=100
    )
    incomes_from_persons_2 = forms.CharField(
        label="2. De personas - From persons", max_length=100
    )
    incomes_from_industries_1 = forms.CharField(
        label="3. De industrias - From industries", max_length=100
    )
    incomes_from_industries_2 = forms.CharField(
        label="3. De industrias - From industries", max_length=100
    )
    incomes_room_rental_1 = forms.CharField(
        label="4. De alquiler de habitaciones - From room rental", max_length=100
    )
    incomes_room_rental_2 = forms.CharField(
        label="4. De alquiler de habitaciones - From room rental", max_length=100
    )
    incomes_casino_1 = forms.CharField(
        label="5. De casino - From casino", max_length=100
    )
    incomes_casino_2 = forms.CharField(
        label="5. De casino - From casino", max_length=100
    )
    incomes_less_prizes_1 = forms.CharField(
        label="6. Menos premios - Less prizes", max_length=100
    )
    incomes_less_prizes_2 = forms.CharField(
        label="6. Menos premios - Less prizes", max_length=100
    )
    incomes_food_beverages_1 = forms.CharField(
        label="7. De alimentos y bebidas - From food and beverages", max_length=100
    )
    incomes_food_beverages_2 = forms.CharField(
        label="7. De alimentos y bebidas - From food and beverages", max_length=100
    )
    incomes_interests_1 = forms.CharField(
        label="8. De intereses - From interests", max_length=100
    )
    incomes_interests_2 = forms.CharField(
        label="8. De intereses - From interests", max_length=100
    )
    incomes_rent_1 = forms.CharField(label="9. De renta - From rent", max_length=100)
    incomes_rent_2 = forms.CharField(label="9. De renta - From rent", max_length=100)
    incomes_capital_gain_loss_1 = forms.CharField(
        label="10. De ganancia o pérdida de capital - From capital gain or loss",
        max_length=100,
    )
    incomes_capital_gain_loss_2 = forms.CharField(
        label="10. De ganancia o pérdida de capital - From capital gain or loss",
        max_length=100,
    )
    other_incomes_1 = forms.CharField(
        label="11. Otros ingresos - Other incomes", max_length=100
    )
    other_incomes_2 = forms.CharField(
        label="11. Otros ingresos - Other incomes", max_length=100
    )
    total_expenses_1 = forms.CharField(
        label="12. Total de gastos - Total expenses", max_length=100
    )
    total_expenses_2 = forms.CharField(
        label="12. Total de gastos - Total expenses", max_length=100
    )
    expenses_food_beverages_1 = forms.CharField(
        label="1. De alimentos y bebidas - From food and beverages", max_length=100
    )
    expenses_food_beverages_2 = forms.CharField(
        label="1. De alimentos y bebidas - From food and beverages", max_length=100
    )
    expenses_food_1 = forms.CharField(
        label="2. De alimentos - From food", max_length=100
    )
    expenses_food_2 = forms.CharField(
        label="2. De alimentos - From food", max_length=100
    )
    expenses_beverages_1 = forms.CharField(
        label="3. De bebidas - From beverages", max_length=100
    )
    expenses_beverages_2 = forms.CharField(
        label="3. De bebidas - From beverages", max_length=100
    )
    expenses_music_entertainment_1 = forms.CharField(
        label="4. De música y entretenimiento - From music and entertainment",
        max_length=100,
    )
    expenses_music_entertainment_2 = forms.CharField(
        label="4. De música y entretenimiento - From music and entertainment",
        max_length=100,
    )
    expenses_salaries_wages_bonus_1 = forms.CharField(
        label="5. Salarios, jornales, bono de Navidad y comisiones - Salaries, wages, Christmas bonus, and commissions",
        max_length=100,
    )
    expenses_salaries_wages_bonus_2 = forms.CharField(
        label="5. Salarios, jornales, bono de Navidad y comisiones - Salaries, wages, Christmas bonus, and commissions",
        max_length=100,
    )
    expenses_uniform_1 = forms.CharField(
        label="6. De uniformes - From uniforms", max_length=100
    )
    expenses_uniform_2 = forms.CharField(
        label="6. De uniformes - From uniforms", max_length=100
    )
    expenses_interests_1 = forms.CharField(
        label="7. De intereses - From interests", max_length=100
    )
    expenses_interests_2 = forms.CharField(
        label="7. De intereses - From interests", max_length=100
    )
    expenses_rent_1 = forms.CharField(label="8. De renta - From rent", max_length=100)
    expenses_rent_2 = forms.CharField(label="8. De renta - From rent", max_length=100)
    expenses_depreciation_1 = forms.CharField(
        label="9. De depreciación - From depreciation", max_length=100
    )
    expenses_depreciation_2 = forms.CharField(
        label="9. De depreciación - From depreciation", max_length=100
    )
    expenses_bad_debts_1 = forms.CharField(
        label="10. De malos créditos - From bad debts", max_length=100
    )
    expenses_bad_debts_2 = forms.CharField(
        label="10. De malos créditos - From bad debts", max_length=100
    )
    expenses_donations_1 = forms.CharField(
        label="11. De donaciones - From donations", max_length=100
    )
    expenses_donations_2 = forms.CharField(
        label="11. De donaciones - From donations", max_length=100
    )
    expenses_free_food_employees_1 = forms.CharField(
        label="12. De comida gratis a empleados - From free food to employees",
        max_length=100,
    )
    expenses_free_food_employees_2 = forms.CharField(
        label="12. De comida gratis a empleados - From free food to employees",
        max_length=100,
    )
    expenses_sales_tax_1 = forms.CharField(
        label="13. De impuesto sobre ventas y uso - From sales and use tax",
        max_length=100,
    )
    expenses_sales_tax_2 = forms.CharField(
        label="13. De impuesto sobre ventas y uso - From sales and use tax",
        max_length=100,
    )
    expenses_purchases_machinery_1 = forms.CharField(
        label="14. Por compra de maquinaria y equipo - On purchases of machinery and equipment",
        max_length=100,
    )
    expenses_purchases_machinery_2 = forms.CharField(
        label="14. Por compra de maquinaria y equipo - On purchases of machinery and equipment",
        max_length=100,
    )
    expenses_other_purchases_1 = forms.CharField(
        label="15. Por otras compras - On other purchases", max_length=100
    )
    expenses_other_purchases_2 = forms.CharField(
        label="15. Por otras compras - On other purchases", max_length=100
    )
    expenses_licenses_1 = forms.CharField(
        label="16. De licencias y patentes - From licenses and patents", max_length=100
    )
    expenses_licenses_2 = forms.CharField(
        label="16. De licencias y patentes - From licenses and patents", max_length=100
    )
    other_expenses_1 = forms.CharField(
        label="17. Otros gastos - Other expenses", max_length=100
    )
    other_expenses_2 = forms.CharField(
        label="17. Otros gastos - Other expenses", max_length=100
    )
    net_profit_loss_1 = forms.CharField(
        label="18. Ganancia o pérdida neta (+ ó -) - Net profit or loss (+ or -)",
        max_length=100,
    )
    net_profit_loss_2 = forms.CharField(
        label="18. Ganancia o pérdida neta (+ ó -) - Net profit or loss (+ or -)",
        max_length=100,
    )
    profit_incomes_tax_1 = forms.CharField(
        label="1. Contribución sobre ingresos - Income tax", max_length=100
    )
    profit_incomes_tax_2 = forms.CharField(
        label="1. Contribución sobre ingresos - Income tax", max_length=100
    )
    profit_after_income_tax_1 = forms.CharField(
        label="2. Ganancia después de contribución sobre ingresos - Profit after income tax",
        max_length=100,
    )
    profit_after_income_tax_2 = forms.CharField(
        label="2. Ganancia después de contribución sobre ingresos - Profit after income tax",
        max_length=100,
    )
    sales_tax_withheld_1 = forms.CharField(
        label="19. Impuesto sobre ventas y uso retenido - Sales and use tax withheld",
        max_length=100,
    )
    sales_tax_withheld_2 = forms.CharField(
        label="19. Impuesto sobre ventas y uso retenido - Sales and use tax withheld",
        max_length=100,
    )
    name = forms.CharField(
        label="Name of person filling the questionnaire", max_length=100
    )
    rank = forms.CharField(label="Rank", max_length=100)
    
class IP_810(forms.Form):
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
    business_type = forms.ChoiceField(
        label='Tipo de negocio / Business type', 
        choices=[('Comercio', 'Comercio'), ('Manufactura', 'Manufactura'), ('Servicios', 'Servicios'), ('Agricultura', 'Agricultura'), ('Otros', 'Otros')]
    )
    business_function = forms.ChoiceField(
        label='Función del negocio / Business function', 
        choices=[('Venta de productos', 'Venta de productos'), ('Venta de servicios', 'Venta de servicios'), ('Venta de productos y servicios', 'Venta de productos y servicios')]
    )
    branches = forms.ChoiceField(label='Sucursales / Branches', choices=[('Si', 'Si'), ('No', 'No')])
    branches_yes = forms.CharField(label='Si si, cuantas / If yes, how many', max_length=100)
    closing_date = forms.DateField(label='Fecha de cierre de sus libros / Your accounting period closing date', widget=forms.SelectDateWidget)
    
    start_year = forms.CharField(label='Año de inicio de operaciones / Year of start of operations', max_length=100)
    end_year = forms.CharField(label='Año de cierre de operaciones / Year of end of operations', max_length=100)
    
    total_income_1 = forms.CharField(label='A. Total de ingreso por servicios - Total income', max_length=100)
    total_income_2 = forms.CharField(label='A. Total de ingreso por servicios - Total income', max_length=100)
    services_rendered_1 = forms.CharField(label='1. Ingreso por servicios - Services renderes', max_length=100)
    services_rendered_2 = forms.CharField(label='1. Ingreso por servicios - Services renderes', max_length=100)
    from_persons_1 = forms.CharField(label='a. De personas - From persons', max_length=100)
    from_persons_2 = forms.CharField(label='a. De personas - From persons', max_length=100)
    industries_businesses_1 = forms.CharField(label='b. De industrias y negocios - From industries and businesses', max_length=100)
    industries_businesses_2 = forms.CharField(label='b. De industrias y negocios - From industries and businesses', max_length=100)
    sales_1 = forms.CharField(label='2. De ventas - Sales', max_length=100)
    sales_2 = forms.CharField(label='2. De ventas - Sales', max_length=100)
    rent_machinery_1 = forms.CharField(label='3. Renta de maquinaria y equipo - Rent of machinery and equipment', max_length=100)
    rent_machinery_2 = forms.CharField(label='3. Renta de maquinaria y equipo - Rent of machinery and equipment', max_length=100)
    rent_land_1 = forms.CharField(label='4. Renta de terreno y edificio - Rent of land and building', max_length=100)
    rent_land_2 = forms.CharField(label='4. Renta de terreno y edificio - Rent of land and building', max_length=100)
    interest_1 = forms.CharField(label='5. Intereses* - Interest*', max_length=100)
    interest_2 = forms.CharField(label='5. Intereses* - Interest*', max_length=100)
    capitan_gain_loss_1 = forms.CharField(label='6. Ganancia o pérdida de capital - Capital gain or loss', max_length=100)
    capitan_gain_loss_2 = forms.CharField(label='6. Ganancia o pérdida de capital - Capital gain or loss', max_length=100)
    
    total_expenses_1 = forms.CharField(label='B. Total de gastos - Total expenses', max_length=100)
    total_expenses_2 = forms.CharField(label='B. Total de gastos - Total expenses', max_length=100)
    salaries_1 = forms.CharField(label='1. Salarios, jornales, bono de Navidad y comisiones - Salaries, wages, Christmas bonus, and commissions', max_length=100)
    salaries_2 = forms.CharField(label='1. Salarios, jornales, bono de Navidad y comisiones - Salaries, wages, Christmas bonus, and commissions', max_length=100)
    expenses_interests_1 = forms.CharField(label='2. Intereses - Interests', max_length=100)
    expenses_interests_2 = forms.CharField(label='2. Intereses - Interests', max_length=100)
    expenses_rents_1 = forms.CharField(label='3. Renta de terreno y edificio - Rent of land and building', max_length=100)
    expenses_rents_2 = forms.CharField(label='3. Renta de terreno y edificio - Rent of land and building', max_length=100)
    depreciation_1 = forms.CharField(label='4. Depreciación - Depreciation', max_length=100)
    depreciation_2 = forms.CharField(label='4. Depreciación - Depreciation', max_length=100)
    bad_debts_1 = forms.CharField(label='5. Cuentas incobrables - Bad debts', max_length=100)
    bad_debts_2 = forms.CharField(label='5. Cuentas incobrables - Bad debts', max_length=100)
    donations_1 = forms.CharField(label='6. Donaciones - Donations', max_length=100)
    donations_2 = forms.CharField(label='6. Donaciones - Donations', max_length=100)
    other_operating_expenses_1 = forms.CharField(label='7. Otros gastos de operación - Other operating expenses', max_length=100)
    other_operating_expenses_2 = forms.CharField(label='7. Otros gastos de operación - Other operating expenses', max_length=100)
    sales_tax_1 = forms.CharField(label='8. Impuesto sobre ventas y uso - Sales and use tax', max_length=100)
    sales_tax_2 = forms.CharField(label='8. Impuesto sobre ventas y uso - Sales and use tax', max_length=100)
    purchases_1 = forms.CharField(label='a. Por compra de maquinaria y equipo - On purchases of machinery and equipment', max_length=100)
    purchases_2 = forms.CharField(label='a. Por compra de maquinaria y equipo - On purchases of machinery and equipment', max_length=100)
    other_purchases_1 = forms.CharField(label='b. Por otras compras - On other purchases', max_length=100)
    other_purchases_2 = forms.CharField(label='b. Por otras compras - On other purchases', max_length=100)
    licenses_patents_1 = forms.CharField(label='9. Licencias y patentes - Licenses and patents', max_length=100)
    licenses_patents_2 = forms.CharField(label='9. Licencias y patentes - Licenses and patents', max_length=100)
    
    net_profit_loss_1 = forms.CharField(label='C. Ganancia o pérdida neta (A-B) - Net profit or loss (A-B)', max_length=100)
    net_profit_loss_2 = forms.CharField(label='C. Ganancia o pérdida neta (A-B) - Net profit or loss (A-B)', max_length=100)
    income_tax_1 = forms.CharField(label='1. Contribución sobre ingresos - Income tax', max_length=100)
    income_tax_2 = forms.CharField(label='1. Contribución sobre ingresos - Income tax', max_length=100)
    profit_after_tax_1 = forms.CharField(label='2. Ganancia después de contribución sobre ingresos - Profit after tax', max_length=100)
    profit_after_tax_2 = forms.CharField(label='2. Ganancia después de contribución sobre ingresos - Profit after tax', max_length=100)
    
    withheld_tax_1 = forms.CharField(label='D. Impuesto sobre ventas y uso retenido - Sales and use tax withheld', max_length=100)
    withheld_tax_2 = forms.CharField(label='D. Impuesto sobre ventas y uso retenido - Sales and use tax withheld', max_length=100)
    
    name = forms.CharField(label='Nombre', max_length=100)
    rank = forms.CharField(label='Rango', max_length=100)

class JP_547(forms.Form):
    agency_form = forms.CharField(label='From:', max_length=100)
    agency_to = forms.CharField(label='To:', max_length=100)
    
    salaries_wages = forms.CharField(label='1. Salaries and wages (gross of destructions, including COLA)', max_length=100)
    civil_service = forms.CharField(label='a. Civil service retirement', max_length=100)
    federal_employee_retirement = forms.CharField(label='b. Federal employee retirement', max_length=100)
    thrift_savings_disbursements = forms.CharField(label='c. Thrift savings plan (TSP)', max_length=100)
    socal_security = forms.CharField(label='d. Social security', max_length=100)
    life_insurance_health_disbursements = forms.CharField(label='e. Life insurance and health benefits', max_length=100)
    other_disbursements = forms.CharField(label='f. Other (specify)', max_length=100)
    construction_contracts = forms.CharField(label='3. Construction contracts', max_length=100)
    rent_disbursements = forms.CharField(label='4. Rent', max_length=100)
    other_purchases = forms.CharField(label='5. Other purchasesin Puerto Rico', max_length=100)
    equipment_supplies = forms.CharField(label='6. Equipment, materials, and supplies received from other mainland Federal Government agencies', max_length=100)
    rent_sales = forms.CharField(label='1. Rent', max_length=100)
    other_sales = forms.CharField(label='2. Other sales of goods and services', max_length=100)
    income_tax = forms.CharField(label='1. Income tax', max_length=100)
    other_taxes_licenses = forms.CharField(label='2. Other taxes and licenses', max_length=100)
    fines_penalties = forms.CharField(label='3. Fines and penalties', max_length=100)
    interest = forms.CharField(label='4. Interest', max_length=100)
    other_collections_1 = forms.CharField(label='5. Other (specify)', max_length=100)
    other_collections_amount_1 = forms.CharField(label='', max_length=100)
    other_collections_2 = forms.CharField(label='', max_length=100)
    other_collections_amount_2 = forms.CharField(label='', max_length=100)
    other_collections_3 = forms.CharField(label='', max_length=100)
    other_collections_amount_3 = forms.CharField(label='', max_length=100)
    civil_service_2 = forms.CharField(label='1. Civil service retirement', max_length=100)
    federal_employee = forms.CharField(label='2. Federal employee', max_length=100)
    thrift_saving_deductions = forms.CharField(label='3. Thrift savings plan (TSP)', max_length=100)
    social_security = forms.CharField(label='4. Social security', max_length=100)
    life_insurance_health_deductions = forms.CharField(label='5. Life insurance and health benefits', max_length=100)
    income_tax_deductions = forms.CharField(label='6. Income tax', max_length=100)
    saving_bonds = forms.CharField(label='7. U.S. Government saving bonds', max_length=100)
    other_deductions = forms.CharField(label='8. Other (specify)', max_length=100)
    other_deductions_amount = forms.CharField(label='', max_length=100)
    commonwealth = forms.CharField(label='a. Commonwealth Government', max_length=100)
    municipal = forms.CharField(label='b. Municipal Government', max_length=100)
    individuals_private_institutions = forms.CharField(label='c. Individuals and private institutions', max_length=100)
    death_disability = forms.CharField(label='d. Death and disability', max_length=100)
    other_payments_1 = forms.CharField(label='e. Other (specify)', max_length=100)
    other_payments_amount_1 = forms.CharField(label='', max_length=100)
    other_payments_2 = forms.CharField(label='', max_length=100)
    other_payments_amount_2 = forms.CharField(label='', max_length=100)
    loans_advances = forms.CharField(label='1. Loans and advances', max_length=100)
    repayments_loans = forms.CharField(label='2. Repayments of loans and advances', max_length=100)
    total_loans_amount = forms.CharField(label='3. Total amount of loans made in Puerto Rico and sold to individuals and /or financial institutions in Puerto Rico', max_length=100)
    loans_cancelled = forms.CharField(label='4. Loans cancelled by acquisition of collateral', max_length=100)
    other_credits = forms.CharField(label='5. Other credits to principal of loans and advances', max_length=100)
    loans_and_advances = forms.CharField(label='6. Amount of principal of loans and advances outstanding as of', max_length=100)
    loans_and_advances_amount = forms.CharField(label='', max_length=100) 
    interest_collected = forms.CharField(label='7. Interest collected on loans and advances', max_length=100)
    forgiveness_credit = forms.CharField(label='8.  Forgiveness credit to Puerto Rican residents', max_length=100)
    
    reporting_agency = forms.CharField(label='Reporting agency', max_length=100)



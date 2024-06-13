from django import forms

class AgricultureForm(forms.Form):
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
    industries_businesses_12 = forms.CharField(label='Industrias y negocios - Industries and businesses'),
    


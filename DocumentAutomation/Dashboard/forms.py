from django import forms


# Form Documents
class SpecialTestimonyForm(forms.Form):
    DAYS_CHOICES_LETTERS = [
        ('uno', 'uno'),
        ('dos', 'dos'),
        ('tres', 'tres'),
        ('cuatro', 'cuatro'),
        ('cinco', 'cinco'),
        ('seis', 'seis'),
        ('siete', 'siete'),
        ('ocho', 'ocho'),
        ('nueve', 'nueve'),
        ('diez', 'diez'),
        ('once', 'once'),
        ('doce', 'doce'),
        ('trece', 'trece'),
        ('catorce', 'catorce'),
        ('quince', 'quince'),
        ('dieciséis', 'dieciséis'),
        ('diecisiete', 'diecisiete'),
        ('dieciocho', 'dieciocho'),
        ('diecinueve', 'diecinueve'),
        ('veinte', 'veinte'),
        ('veintiuno', 'veintiuno'),
        ('veintidós', 'veintidós'),
        ('veintitrés', 'veintitrés'),
        ('veinticuatro', 'veinticuatro'),
        ('veinticinco', 'veinticinco'),
        ('veintiséis', 'veintiséis'),
        ('veintisiete', 'veintisiete'),
        ('veintiocho', 'veintiocho'),
        ('veintinueve', 'veintinueve'),
        ('treinta', 'treinta'),
        ('treinta y uno', 'treinta y uno'),
    ]
    DAYS_CHOICES_DIGITS = [(str(i), f'{i}') for i in range(1, 32)]
    MONTHS_CHOICES_LETTERS = [
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
        ('diciembre', 'diciembre')
    ]
    YEARS_CHOICES_LETTERS = [
        ('dos mil veinte', 'dos mil veinte'),
        ('dos mil veintiuno', 'dos mil veintiuno'),
        ('dos mil veintidós', 'dos mil veintidós'),
        ('dos mil veintitrés', 'dos mil veintitrés'),
        ('dos mil veinticuatro', 'dos mil veinticuatro'),
        ('dos mil veinticinco', 'dos mil veinticinco'),
        ('dos mil veintiséis', 'dos mil veintiséis'),
        ('dos mil veintisiete', 'dos mil veintisiete'),
        ('dos mil veintiocho', 'dos mil veintiocho'),
        ('dos mil veintinueve', 'dos mil veintinueve'),
        ('dos mil treinta', 'dos mil treinta'),
        ('dos mil treinta y uno', 'dos mil treinta y uno'),
        ('dos mil treinta y dos', 'dos mil treinta y dos'),
        ('dos mil treinta y tres', 'dos mil treinta y tres'),
        ('dos mil treinta y cuatro', 'dos mil treinta y cuatro'),
        ('dos mil treinta y cinco', 'dos mil treinta y cinco')
    ]
    YEARS_CHOICES_DIGITS = [(str(year), str(year)) for year in range(2020, 2036)]
    NOTARY_OFFICES = [
        ('notario', 'notario'),
        ('notaria', 'notaria'),
    ]
    deed_numbers_letters = forms.CharField(label='Número de escritura (en letras)', max_length=500)
    deed_numbers_digits = forms.CharField(label='Número de escritura (en números)', max_length=500)
    municipality = forms.CharField(label='Municipio de autorización de la escritura pública', max_length=100)
    department = forms.CharField(label='Departamento de autorización de la escritura pública', max_length=100)
    day_letters = forms.ChoiceField(label='Día en que se autorizó la escritura pública (en letras)',
                                    choices=DAYS_CHOICES_LETTERS)
    day_digits = forms.ChoiceField(label='Dia en que se está generando el documento (en numeros)',
                                   choices=DAYS_CHOICES_DIGITS)
    month_letters_a = forms.ChoiceField(label='Mes en que se autorizó la escritura pública (en letras)',
                                        choices=MONTHS_CHOICES_LETTERS)
    month_letters_g = forms.ChoiceField(label='Mes en que se está generando el documento (en letras)',
                                        choices=MONTHS_CHOICES_LETTERS)
    year_letters = forms.ChoiceField(label='Año en que se autorizó la escritura pública (en letras)',
                                     choices=YEARS_CHOICES_LETTERS)
    year_digits = forms.ChoiceField(label='Año en que se está generando el documento (en numeros)',
                                    choices=YEARS_CHOICES_DIGITS)
    notary_office = forms.ChoiceField(label='Notario/Notaria', choices=NOTARY_OFFICES)
    name_notary_office = forms.CharField(label='Nombre Notario/Notaria', max_length=100)
    number_of_pages = forms.CharField(label='Numero de hojas donde quedó impresa la escritura (en letras)',
                                      max_length=10)
    she = forms.CharField(widget=forms.HiddenInput(), required=False)


class IvaSalesTestimonyForm(forms.Form):
    DAYS_CHOICES_LETTERS = [
        ('uno', 'uno'),
        ('dos', 'dos'),
        ('tres', 'tres'),
        ('cuatro', 'cuatro'),
        ('cinco', 'cinco'),
        ('seis', 'seis'),
        ('siete', 'siete'),
        ('ocho', 'ocho'),
        ('nueve', 'nueve'),
        ('diez', 'diez'),
        ('once', 'once'),
        ('doce', 'doce'),
        ('trece', 'trece'),
        ('catorce', 'catorce'),
        ('quince', 'quince'),
        ('dieciséis', 'dieciséis'),
        ('diecisiete', 'diecisiete'),
        ('dieciocho', 'dieciocho'),
        ('diecinueve', 'diecinueve'),
        ('veinte', 'veinte'),
        ('veintiuno', 'veintiuno'),
        ('veintidós', 'veintidós'),
        ('veintitrés', 'veintitrés'),
        ('veinticuatro', 'veinticuatro'),
        ('veinticinco', 'veinticinco'),
        ('veintiséis', 'veintiséis'),
        ('veintisiete', 'veintisiete'),
        ('veintiocho', 'veintiocho'),
        ('veintinueve', 'veintinueve'),
        ('treinta', 'treinta'),
        ('treinta y uno', 'treinta y uno'),
    ]
    DAYS_CHOICES_DIGITS = [(str(i), f'{i}') for i in range(1, 32)]
    MONTHS_CHOICES_LETTERS = [
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
        ('diciembre', 'diciembre')
    ]
    YEARS_CHOICES_LETTERS = [
        ('dos mil veinte', 'dos mil veinte'),
        ('dos mil veintiuno', 'dos mil veintiuno'),
        ('dos mil veintidós', 'dos mil veintidós'),
        ('dos mil veintitrés', 'dos mil veintitrés'),
        ('dos mil veinticuatro', 'dos mil veinticuatro'),
        ('dos mil veinticinco', 'dos mil veinticinco'),
        ('dos mil veintiséis', 'dos mil veintiséis'),
        ('dos mil veintisiete', 'dos mil veintisiete'),
        ('dos mil veintiocho', 'dos mil veintiocho'),
        ('dos mil veintinueve', 'dos mil veintinueve'),
        ('dos mil treinta', 'dos mil treinta'),
        ('dos mil treinta y uno', 'dos mil treinta y uno'),
        ('dos mil treinta y dos', 'dos mil treinta y dos'),
        ('dos mil treinta y tres', 'dos mil treinta y tres'),
        ('dos mil treinta y cuatro', 'dos mil treinta y cuatro'),
        ('dos mil treinta y cinco', 'dos mil treinta y cinco')
    ]
    YEARS_CHOICES_DIGITS = [(str(year), str(year)) for year in range(2020, 2036)]
    NOTARY_OFFICES = [
        ('notario', 'notario'),
        ('notaria', 'notaria'),
    ]
    deed_numbers_letters = forms.CharField(label='Número de escritura (en letras)', max_length=500)
    deed_numbers_digits = forms.CharField(label='Número de escritura (en números)', max_length=500)
    municipality = forms.CharField(label='Municipio de autorización de la escritura pública', max_length=100)
    department = forms.CharField(label='Departamento de autorización de la escritura pública', max_length=100)
    day_letters = forms.ChoiceField(label='Día en que se autorizó la escritura pública (en letras)',
                                    choices=DAYS_CHOICES_LETTERS)
    month_letters_a = forms.ChoiceField(label='Mes en que se autorizó la escritura publica (en letras)',
                                        choices=MONTHS_CHOICES_LETTERS)
    year_letters = forms.ChoiceField(label='Año en que se autorizó la escritura publica (en letras)',
                                     choices=YEARS_CHOICES_LETTERS)
    day_digits = forms.ChoiceField(label='Dia en que se está generando el documento (en numeros)',
                                   choices=DAYS_CHOICES_DIGITS)
    month_letters_g = forms.ChoiceField(label='Mes en que se está generando el documento (en letras)',
                                        choices=MONTHS_CHOICES_LETTERS)
    year_digits = forms.ChoiceField(label='Año en que se está generando el documento (en numeros)',
                                    choices=YEARS_CHOICES_DIGITS)
    notary_office = forms.ChoiceField(label='Notario/Notaria', choices=NOTARY_OFFICES)
    name_notary_office = forms.CharField(label='Nombre Notario/Notaria', max_length=100)
    buyer_name = forms.CharField(label='Nombre del comprador')
    number_of_pages = forms.CharField(label='Numero de hojas donde quedó impresa la escritura (en letras)',
                                      max_length=10)
    number_form_letters = forms.CharField(label='Numero de formulario en letras', max_length=100)
    number_form_digits = forms.CharField(label='Número de formulario en números', max_length=100)
    amount_to_pay_letters = forms.CharField(label='Cantidad a pagar en letras (Quetzales)', max_length=100)
    amount_to_pay_digits = forms.CharField(label='Cantidad a pagar en numeros (Quetzales)', max_length=100)
    she = forms.CharField(widget=forms.HiddenInput(), required=False)


class MunicipalityNoticesForm(forms.Form):
    DAYS_CHOICES_LETTERS = [
        ('uno', 'uno'),
        ('dos', 'dos'),
        ('tres', 'tres'),
        ('cuatro', 'cuatro'),
        ('cinco', 'cinco'),
        ('seis', 'seis'),
        ('siete', 'siete'),
        ('ocho', 'ocho'),
        ('nueve', 'nueve'),
        ('diez', 'diez'),
        ('once', 'once'),
        ('doce', 'doce'),
        ('trece', 'trece'),
        ('catorce', 'catorce'),
        ('quince', 'quince'),
        ('dieciséis', 'dieciséis'),
        ('diecisiete', 'diecisiete'),
        ('dieciocho', 'dieciocho'),
        ('diecinueve', 'diecinueve'),
        ('veinte', 'veinte'),
        ('veintiuno', 'veintiuno'),
        ('veintidós', 'veintidós'),
        ('veintitrés', 'veintitrés'),
        ('veinticuatro', 'veinticuatro'),
        ('veinticinco', 'veinticinco'),
        ('veintiséis', 'veintiséis'),
        ('veintisiete', 'veintisiete'),
        ('veintiocho', 'veintiocho'),
        ('veintinueve', 'veintinueve'),
        ('treinta', 'treinta'),
        ('treinta y uno', 'treinta y uno'),
    ]
    MONTHS_CHOICES_LETTERS = [
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
        ('diciembre', 'diciembre')
    ]
    YEARS_CHOICES_LETTERS = [
        ('dos mil veinte', 'dos mil veinte'),
        ('dos mil veintiuno', 'dos mil veintiuno'),
        ('dos mil veintidós', 'dos mil veintidós'),
        ('dos mil veintitrés', 'dos mil veintitrés'),
        ('dos mil veinticuatro', 'dos mil veinticuatro'),
        ('dos mil veinticinco', 'dos mil veinticinco'),
        ('dos mil veintiséis', 'dos mil veintiséis'),
        ('dos mil veintisiete', 'dos mil veintisiete'),
        ('dos mil veintiocho', 'dos mil veintiocho'),
        ('dos mil veintinueve', 'dos mil veintinueve'),
        ('dos mil treinta', 'dos mil treinta'),
        ('dos mil treinta y uno', 'dos mil treinta y uno'),
        ('dos mil treinta y dos', 'dos mil treinta y dos'),
        ('dos mil treinta y tres', 'dos mil treinta y tres'),
        ('dos mil treinta y cuatro', 'dos mil treinta y cuatro'),
        ('dos mil treinta y cinco', 'dos mil treinta y cinco')
    ]
    YEARS_CHOICES_DIGITS = [(str(year), str(year)) for year in range(2020, 2036)]
    DAYS_CHOICES_DIGITS = [(str(i), f'{i}') for i in range(1, 32)]
    NOTARY_OFFICES = [
        ('notario', 'notario'),
        ('notaria', 'notaria'),
    ]
    LAWYER_OFFICES = [
        ('abogado', 'abogado'),
        ('abogada', 'abogada'),
    ]
    municipality = forms.CharField(label='Municipalidad', max_length=50)
    department = forms.CharField(label='Departamento', max_length=50)
    deed_numbers_letters = forms.CharField(label='Número de escritura en letras', max_length=500)
    deed_numbers_digits = forms.CharField(label='Número de escritura en digitos', max_length=500)
    address_property = forms.CharField(label='Dirección del inmueble', max_length=100)
    municipality_property = forms.CharField(label='Municipio del inmueble', max_length=50)
    department_property = forms.CharField(label='Departamento del inmueble', max_length=50)
    number_farm_letters = forms.CharField(label='Número de finca en letras', max_length=50)
    number_farm_digits = forms.CharField(label='Número de finca en digitos', max_length=50)
    number_folio_letters = forms.CharField(label='Número de folio en letras', max_length=50)
    number_folio_digits = forms.CharField(label='Número de folio en digitos', max_length=50)
    number_book_letters = forms.CharField(label='Número de libro en letras', max_length=50)
    number_book_digits = forms.CharField(label='Número de libro en digitos', max_length=50)
    area_state_letters = forms.CharField(label='Área de la finca en letras (metros cuadrados)', max_length=50)
    area_state_digits = forms.CharField(label='Área de la finca en digitos (metros cuadrados)', max_length=50)
    value_property_letters = forms.CharField(label='Valor del inmueble en letras (Quetzales)', max_length=50)
    value_property_digits = forms.CharField(label='Valor del inmueble en digitos (Quetzales)', max_length=50)
    day_letters = forms.ChoiceField(label='Día en que se autorizó la escritura pública (En letras)',
                                    choices=DAYS_CHOICES_LETTERS)
    month_letters_a = forms.ChoiceField(label='Mes en que se autorizó la escritura pública (En letras)',
                                        choices=MONTHS_CHOICES_LETTERS)
    year_letters = forms.ChoiceField(label='Año en que se autorizó la escritura pública (En letras)',
                                     choices=YEARS_CHOICES_LETTERS)
    day_digits = forms.ChoiceField(label='Día en que se está generando el documento (En dígitos)',
                                   choices=DAYS_CHOICES_DIGITS)
    month_letters_g = forms.ChoiceField(label='Mes en que se está generando el documento (En letras)',
                                        choices=MONTHS_CHOICES_LETTERS)
    year_digits = forms.ChoiceField(label='Año en que se está generando el documento (En dígitos)',
                                    choices=YEARS_CHOICES_DIGITS)
    notary_office = forms.ChoiceField(label='Notario o Notaría', choices=NOTARY_OFFICES)
    lawyer_office = forms.ChoiceField(label='Abogado o Abogada', choices=LAWYER_OFFICES)
    name_notary_office = forms.CharField(label='Nombre del Notario o Notaria', max_length=100)
    collegiate_number = forms.CharField(label='Numero de colegiado', max_length=50)
    address_receive_notifications = forms.CharField(label='Dirección para recibir notificaciones', max_length=100)
    municipality_receive_notifications = forms.CharField(label='Municipio para recibir notificaciones', max_length=50)
    department_receive_notifications = forms.CharField(label='Departamento para recibir notificaciones', max_length=50)
    email_notary_office = forms.CharField(label='Correo electronico del notario o notaria', max_length=50)
    seller_name = forms.CharField(label='Nombre del vendedor', max_length=100)
    seller_dpi_number = forms.CharField(label='Número del dpi del vendedor', max_length=15)
    seller_nit_number = forms.CharField(label='Número del nit del vendedor', max_length=8)
    seller_home_address = forms.CharField(label='Dirección domiciliaria del vendedor', max_length=100)
    seller_home_municipality = forms.CharField(label='Municipio domiciliar del vendedor', max_length=50)
    seller_home_department = forms.CharField(label='Departamento domiciliar del vendedor', max_length=50)
    seller_registration = forms.CharField(
        label='Matrícula del vendedor',
        max_length=500,
        required=False,
        initial='No tiene, abrir conforme lo establece el Decreto 15-98 del Congreso de la República.'
    )
    buyer_name = forms.CharField(label='Nombre del comprador', max_length=100)
    buyer_dpi_number = forms.CharField(label='Número del dpi del comprador', max_length=15)
    buyer_nit_number = forms.CharField(label='Número del nit del comprador', max_length=8)
    buyer_home_address = forms.CharField(label='Dirección domiciliaria del comprador', max_length=100)
    buyer_home_municipality = forms.CharField(label='Municipio domiciliar del comprador', max_length=50)
    buyer_home_department = forms.CharField(label='Departamento domiciliar del comprador', max_length=50)
    buyer_registration = forms.CharField(
        label='Matrícula del comprador',
        max_length=500,
        required=False,
        initial='No tiene, abrir conforme lo establece el Decreto 15-98 del Congreso de la República.'
    )
    she = forms.CharField(widget=forms.HiddenInput(), required=False)


class BuySellForm(forms.Form):
    civil_status_choices = [
        ('soltero', 'soltero'),
        ('soltera', 'soltera'),
        ('casado', 'casado'),
        ('casada', 'casada'),
    ]
    deed_number_letters = forms.CharField(label='Número de escritura en letras', max_length=500)
    deed_number_digits = forms.CharField(label='Número de escritura en dígitos', max_length=500)
    municipality = forms.CharField(label='Ciudad', max_length=100)
    day_choices = [
        ('uno', 'uno'),
        ('dos', 'dos'),
        ('tres', 'tres'),
        ('cuatro', 'cuatro'),
        ('cinco', 'cinco'),
        ('seis', 'seis'),
        ('siete', 'siete'),
        ('ocho', 'ocho'),
        ('nueve', 'nueve'),
        ('diez', 'diez'),
        ('once', 'once'),
        ('doce', 'doce'),
        ('trece', 'trece'),
        ('catorce', 'catorce'),
        ('quince', 'quince'),
        ('dieciséis', 'dieciséis'),
        ('diecisiete', 'diecisiete'),
        ('dieciocho', 'dieciocho'),
        ('diecinueve', 'diecinueve'),
        ('veinte', 'veinte'),
        ('veintiuno', 'veintiuno'),
        ('veintidós', 'veintidós'),
        ('veintitrés', 'veintitrés'),
        ('veinticuatro', 'veinticuatro'),
        ('veinticinco', 'veinticinco'),
        ('veintiséis', 'veintiséis'),
        ('veintisiete', 'veintisiete'),
        ('veintiocho', 'veintiocho'),
        ('veintinueve', 'veintinueve'),
        ('treinta', 'treinta'),
        ('treinta y uno', 'treinta y uno'),
    ]
    day_letters = forms.ChoiceField(label='Día de generación del documento (En letras)', choices=day_choices)
    month_choices = [
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
        ('diciembre', 'diciembre')
    ]
    month_letters = forms.ChoiceField(label='Mes de generación del documento (En letras)', choices=month_choices)
    year_choices = [
        ('dos mil veinte', 'dos mil veinte'),
        ('dos mil veintiuno', 'dos mil veintiuno'),
        ('dos mil veintidós', 'dos mil veintidós'),
        ('dos mil veintitrés', 'dos mil veintitrés'),
        ('dos mil veinticuatro', 'dos mil veinticuatro'),
        ('dos mil veinticinco', 'dos mil veinticinco'),
        ('dos mil veintiséis', 'dos mil veintiséis'),
        ('dos mil veintisiete', 'dos mil veintisiete'),
        ('dos mil veintiocho', 'dos mil veintiocho'),
        ('dos mil veintinueve', 'dos mil veintinueve'),
        ('dos mil treinta', 'dos mil treinta'),
        ('dos mil treinta y uno', 'dos mil treinta y uno'),
        ('dos mil treinta y dos', 'dos mil treinta y dos'),
        ('dos mil treinta y tres', 'dos mil treinta y tres'),
        ('dos mil treinta y cuatro', 'dos mil treinta y cuatro'),
        ('dos mil treinta y cinco', 'dos mil treinta y cinco')
    ]
    year_letters = forms.ChoiceField(label='Año de generación del documento (En letras)', choices=year_choices)
    notary_name = forms.CharField(label='Nombre del Notario/Notaría', max_length=100)
    notary_office_choices = [
        ('notario', 'notario'),
        ('notaria', 'notaria'),
    ]
    notary_office = forms.ChoiceField(label='Notario/Notaria', choices=notary_office_choices)
    seller_name = forms.CharField(label='Nombre del Vendedor', max_length=100)
    seller_age_letters = forms.CharField(label='Edad del Vendedor en letras', max_length=50)
    seller_civil_status = forms.ChoiceField(label='Estado Civil del Vendedor', choices=civil_status_choices)
    seller_nationality = forms.CharField(label='Nacionalidad del Vendedor', max_length=50)
    seller_profession = forms.CharField(label='Profesión del Vendedor', max_length=100)
    seller_department = forms.CharField(label='Departamento de domicilio del Vendedor', max_length=100)
    seller_dpi_number_letters = forms.CharField(label='Número de DPI del Vendedor en letras', max_length=200)
    seller_dpi_number_digits = forms.CharField(label='Número de DPI del Vendedor en dígitos', max_length=15)
    buyer_name = forms.CharField(label='Nombre del Comprador', max_length=100)
    buyer_age_letters = forms.CharField(label='Edad del Comprador en letras', max_length=50)
    buyer_civil_status = forms.ChoiceField(label='Estado Civil del Comprador', choices=civil_status_choices)
    buyer_nationality = forms.CharField(label='Nacionalidad del Comprador', max_length=50)
    buyer_profession = forms.CharField(label='Profesión del Comprador', max_length=100)
    buyer_department = forms.CharField(label='Departamento de domicilio del Comprador', max_length=100)
    buyer_dpi_number_letters = forms.CharField(label='Número de DPI del Comprador en letras', max_length=200)
    buyer_dpi_number_digits = forms.CharField(label='Número de DPI del Comprador en dígitos', max_length=15)
    farm_number_letters = forms.CharField(label='Número de Finca en letras', max_length=50)
    farm_number_digits = forms.CharField(label='Número de Finca en dígitos', max_length=50)
    folio_number_letters = forms.CharField(label='Número de Folio en letras', max_length=50)
    folio_number_digits = forms.CharField(label='Número de Folio en dígitos', max_length=50)
    book_number_letters = forms.CharField(label='Número de Libro en letras', max_length=50)
    book_number_digits = forms.CharField(label='Número de Libro en dígitos', max_length=50)
    property_department = forms.CharField(label='Departamento del Inmueble', max_length=100)
    municipality_address = forms.CharField(label='Municipio del Inmueble', max_length=100)
    property_address = forms.CharField(label='Dirección del Inmueble', max_length=100)
    property_type_choices = [
        ('rústica', 'rústica'),
        ('urbana', 'urbana'),
    ]
    property_type = forms.ChoiceField(label='Tipo de Finca', choices=property_type_choices)
    sale_value_letters = forms.CharField(label='Valor de Venta en letras (Quetzales)', max_length=50)
    sale_value_digits = forms.CharField(label='Valor de Venta en dígitos (Quetzales)', max_length=50)
    she = forms.CharField(widget=forms.HiddenInput(), required=False)

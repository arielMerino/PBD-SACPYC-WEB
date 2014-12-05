# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Administrador',
            fields=[
                ('correo_admin', models.CharField(max_length=45, serialize=False, primary_key=True, db_column='CORREO_ADMIN')),
                ('clave_admin', models.CharField(max_length=45, db_column='CLAVE_ADMIN', blank=True)),
                ('nombre_admin', models.CharField(max_length=25, db_column='NOMBRE_ADMIN', blank=True)),
                ('apellido', models.CharField(max_length=25, db_column='APELLIDO', blank=True)),
                ('rol', models.CharField(max_length=10, db_column='ROL', blank=True)),
            ],
            options={
                'db_table': 'ADMINISTRADOR',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='AgendamientoEvento',
            fields=[
                ('idagendamientoevento', models.IntegerField(serialize=False, primary_key=True, db_column='IDAGENDAMIENTOEVENTO')),
                ('fecha_agendamiento_evento', models.DateField(null=True, db_column='FECHA_AGENDAMIENTO_EVENTO', blank=True)),
                ('hora_agendamiento_evento', models.TimeField(null=True, db_column='HORA_AGENDAMIENTO_EVENTO', blank=True)),
                ('duracion_agendamiento_evento', models.IntegerField(null=True, db_column='DURACION_AGENDAMIENTO_EVENTO', blank=True)),
                ('estado', models.CharField(max_length=10, db_column='ESTADO', blank=True)),
            ],
            options={
                'db_table': 'AGENDAMIENTO_EVENTO',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Auditoria',
            fields=[
                ('id_auditoria', models.IntegerField(serialize=False, primary_key=True, db_column='ID_AUDITORIA')),
                ('usuario', models.IntegerField(null=True, db_column='USUARIO', blank=True)),
                ('fecha', models.DateField(null=True, db_column='FECHA', blank=True)),
                ('tabla', models.CharField(max_length=30, db_column='TABLA', blank=True)),
                ('operacion', models.CharField(max_length=10, db_column='OPERACION', blank=True)),
                ('atributo', models.CharField(max_length=20, db_column='ATRIBUTO', blank=True)),
                ('valorantes', models.CharField(max_length=100, db_column='VALORANTES', blank=True)),
                ('valordespues', models.CharField(max_length=100, db_column='VALORDESPUES', blank=True)),
            ],
            options={
                'db_table': 'AUDITORIA',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='CantidadHistorica',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cantidad', models.IntegerField(null=True, db_column='CANTIDAD', blank=True)),
                ('numero_personas', models.IntegerField(null=True, db_column='NUMERO_PERSONAS', blank=True)),
                ('fecha', models.DateField(null=True, db_column='FECHA', blank=True)),
            ],
            options={
                'db_table': 'CANTIDAD_HISTORICA',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('mail_cliente', models.CharField(max_length=45, serialize=False, primary_key=True, db_column='MAIL_CLIENTE')),
                ('telefono_cliente', models.IntegerField(null=True, db_column='TELEFONO_CLIENTE', blank=True)),
                ('nombre_cliente', models.CharField(max_length=25, db_column='NOMBRE_CLIENTE', blank=True)),
                ('apellido_cliente', models.CharField(max_length=25, db_column='APELLIDO_CLIENTE', blank=True)),
            ],
            options={
                'db_table': 'CLIENTE',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='CompraIngrediente',
            fields=[
                ('idcompraingrediente', models.IntegerField(serialize=False, primary_key=True, db_column='IDCOMPRAINGREDIENTE')),
                ('total_compra_ingrediente', models.IntegerField(null=True, db_column='TOTAL_COMPRA_INGREDIENTE', blank=True)),
                ('fecha_compra_ingrediente', models.DateField(null=True, db_column='FECHA_COMPRA_INGREDIENTE', blank=True)),
            ],
            options={
                'db_table': 'COMPRA_INGREDIENTE',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='CompraIngredienteIngrediente',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cantidad_compra_ingrediente', models.IntegerField(null=True, db_column='CANTIDAD_COMPRA_INGREDIENTE', blank=True)),
                ('precio_compra_ingrediente', models.IntegerField(null=True, db_column='PRECIO_COMPRA_INGREDIENTE', blank=True)),
            ],
            options={
                'db_table': 'COMPRA_INGREDIENTE_INGREDIENTE',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='CompraUtensilio',
            fields=[
                ('idcomprautensilio', models.IntegerField(serialize=False, primary_key=True, db_column='IDCOMPRAUTENSILIO')),
                ('total_compra_utensilio', models.IntegerField(null=True, db_column='TOTAL_COMPRA_UTENSILIO', blank=True)),
                ('fecha_compra_utensilio', models.DateTimeField(null=True, db_column='FECHA_COMPRA_UTENSILIO', blank=True)),
            ],
            options={
                'db_table': 'COMPRA_UTENSILIO',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='CompraUtensilioUtensilio',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cantidad_compra_utensilio', models.IntegerField(null=True, db_column='CANTIDAD_COMPRA_UTENSILIO', blank=True)),
                ('precio_compra_utensilio', models.IntegerField(null=True, db_column='PRECIO_COMPRA_UTENSILIO', blank=True)),
            ],
            options={
                'db_table': 'COMPRA_UTENSILIO_UTENSILIO',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Cotizacion',
            fields=[
                ('id_cotizacion', models.IntegerField(serialize=False, primary_key=True, db_column='ID_COTIZACION')),
                ('estado_aceptacion', models.CharField(max_length=10, db_column='ESTADO_ACEPTACION', blank=True)),
                ('valor_cotizacion', models.IntegerField(null=True, db_column='VALOR_COTIZACION', blank=True)),
            ],
            options={
                'db_table': 'COTIZACION',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Garzon',
            fields=[
                ('mail_garzon', models.CharField(max_length=45, serialize=False, primary_key=True, db_column='MAIL_GARZON')),
                ('telefono_garzon', models.IntegerField(null=True, db_column='TELEFONO_GARZON', blank=True)),
                ('nombre_garzon', models.CharField(max_length=25, db_column='NOMBRE_GARZON', blank=True)),
                ('apellido_garzon', models.CharField(max_length=25, db_column='APELLIDO_GARZON', blank=True)),
            ],
            options={
                'db_table': 'GARZON',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='GarzonEvento',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('respuesta', models.CharField(max_length=5, db_column='RESPUESTA', blank=True)),
            ],
            options={
                'db_table': 'GARZON_EVENTO',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Ingrediente',
            fields=[
                ('idingrediente', models.IntegerField(serialize=False, primary_key=True, db_column='IDINGREDIENTE')),
                ('nombre_ingrediente', models.CharField(max_length=45, db_column='NOMBRE_INGREDIENTE', blank=True)),
                ('stock_ingrediente', models.IntegerField(null=True, db_column='STOCK_INGREDIENTE', blank=True)),
                ('stock_minimo_ingrediente', models.IntegerField(null=True, db_column='STOCK_MINIMO_INGREDIENTE', blank=True)),
            ],
            options={
                'db_table': 'INGREDIENTE',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='IngredienteItem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cantidad_ingrediente_especial', models.IntegerField(null=True, db_column='CANTIDAD_INGREDIENTE_ESPECIAL', blank=True)),
                ('unidad_ingrediente_especial', models.CharField(max_length=10, db_column='UNIDAD_INGREDIENTE_ESPECIAL', blank=True)),
            ],
            options={
                'db_table': 'INGREDIENTE_ITEM',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='IngredienteItemEspecial',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cantidad_ingrediente_especial', models.IntegerField(null=True, db_column='CANTIDAD_INGREDIENTE_ESPECIAL', blank=True)),
                ('unidad_ingrediente_especial', models.CharField(max_length=10, db_column='UNIDAD_INGREDIENTE_ESPECIAL', blank=True)),
            ],
            options={
                'db_table': 'INGREDIENTE_ITEM_ESPECIAL',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('iditem', models.IntegerField(serialize=False, primary_key=True, db_column='IDITEM')),
                ('nombre_item', models.CharField(max_length=25, db_column='NOMBRE_ITEM', blank=True)),
            ],
            options={
                'db_table': 'ITEM',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ItemEspecial',
            fields=[
                ('id_item_especial', models.IntegerField(serialize=False, primary_key=True, db_column='ID_ITEM_ESPECIAL')),
                ('nombre_item', models.CharField(max_length=25, db_column='NOMBRE_ITEM', blank=True)),
                ('cantidad', models.IntegerField(null=True, db_column='CANTIDAD', blank=True)),
                ('precio', models.IntegerField(null=True, db_column='PRECIO', blank=True)),
            ],
            options={
                'db_table': 'ITEM_ESPECIAL',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ItemSolicitudDeCotizacion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cantidad_item', models.IntegerField(null=True, db_column='CANTIDAD_ITEM', blank=True)),
            ],
            options={
                'db_table': 'ITEM_SOLICITUD_DE_COTIZACION',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ProveedorIngrediente',
            fields=[
                ('idproveedoringrediente', models.IntegerField(serialize=False, primary_key=True, db_column='IDPROVEEDORINGREDIENTE')),
                ('nombre_proveedor_ingrediente', models.CharField(max_length=45, db_column='NOMBRE_PROVEEDOR_INGREDIENTE', blank=True)),
                ('telefono_proveedor_ingrediente', models.IntegerField(null=True, db_column='TELEFONO_PROVEEDOR_INGREDIENTE', blank=True)),
                ('direccion_proveedor_ingrediente', models.CharField(max_length=45, db_column='DIRECCION_PROVEEDOR_INGREDIENTE', blank=True)),
            ],
            options={
                'db_table': 'PROVEEDOR_INGREDIENTE',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ProveedorUtensilio',
            fields=[
                ('idproveedorutensilio', models.IntegerField(serialize=False, primary_key=True, db_column='IDPROVEEDORUTENSILIO')),
                ('nombre_proveedor_utensilio', models.CharField(max_length=45, db_column='NOMBRE_PROVEEDOR_UTENSILIO', blank=True)),
                ('telefono_proveedor_utensilio', models.IntegerField(null=True, db_column='TELEFONO_PROVEEDOR_UTENSILIO', blank=True)),
                ('direccion_proveedor_utensilio', models.CharField(max_length=45, db_column='DIRECCION_PROVEEDOR_UTENSILIO', blank=True)),
            ],
            options={
                'db_table': 'PROVEEDOR_UTENSILIO',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Seguimiento',
            fields=[
                ('idseguimiento', models.IntegerField(serialize=False, primary_key=True, db_column='IDSEGUIMIENTO')),
                ('fecha_acuerdo', models.DateField(null=True, db_column='FECHA_ACUERDO', blank=True)),
                ('fecha_vencimiento', models.DateField(null=True, db_column='FECHA_VENCIMIENTO', blank=True)),
            ],
            options={
                'db_table': 'SEGUIMIENTO',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SolicitudDeCotizacion',
            fields=[
                ('idsolicitudcotizacion', models.IntegerField(serialize=False, primary_key=True, db_column='IDSOLICITUDCOTIZACION')),
                ('cantidad_asistentes', models.IntegerField(null=True, db_column='CANTIDAD_ASISTENTES', blank=True)),
                ('fecha_tentativa', models.DateTimeField(null=True, db_column='FECHA_TENTATIVA', blank=True)),
                ('duracion_tentativa', models.IntegerField(null=True, db_column='DURACION_TENTATIVA', blank=True)),
                ('comentarios_field', models.CharField(max_length=250, db_column='COMENTARIOS_', blank=True)),
                ('nombre_evento', models.CharField(max_length=25, db_column='NOMBRE_EVENTO', blank=True)),
                ('direccion_evento', models.CharField(max_length=45, db_column='DIRECCION_EVENTO', blank=True)),
                ('estado_solicitud', models.CharField(max_length=20, db_column='ESTADO_SOLICITUD', blank=True)),
            ],
            options={
                'db_table': 'SOLICITUD_DE_COTIZACION',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TipoEvento',
            fields=[
                ('idtipoevento', models.IntegerField(serialize=False, primary_key=True, db_column='IDTIPOEVENTO')),
                ('nombre_tipo_evento', models.CharField(max_length=25, db_column='NOMBRE_TIPO_EVENTO', blank=True)),
            ],
            options={
                'db_table': 'TIPO_EVENTO',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TipoItem',
            fields=[
                ('idtipo', models.IntegerField(serialize=False, primary_key=True, db_column='IDTIPO')),
                ('nombre_tipo', models.CharField(max_length=25, db_column='NOMBRE_TIPO', blank=True)),
            ],
            options={
                'db_table': 'TIPO_ITEM',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TipoMenu',
            fields=[
                ('idtipomenu', models.IntegerField(serialize=False, primary_key=True, db_column='IDTIPOMENU')),
                ('nombre_tipo_menu', models.CharField(max_length=25, db_column='NOMBRE_TIPO_MENU', blank=True)),
            ],
            options={
                'db_table': 'TIPO_MENU',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TipoUtensilio',
            fields=[
                ('idtipoutensilio', models.IntegerField(serialize=False, primary_key=True, db_column='IDTIPOUTENSILIO')),
                ('nombre_tipo_utensilio', models.CharField(max_length=25, db_column='NOMBRE_TIPO_UTENSILIO', blank=True)),
            ],
            options={
                'db_table': 'TIPO_UTENSILIO',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Utensilio',
            fields=[
                ('idutensilio', models.IntegerField(serialize=False, primary_key=True, db_column='IDUTENSILIO')),
                ('nombre_utensilio', models.CharField(max_length=25, db_column='NOMBRE_UTENSILIO', blank=True)),
                ('stock_utensilio', models.IntegerField(null=True, db_column='STOCK_UTENSILIO', blank=True)),
                ('stock_minimo_utensilio', models.IntegerField(null=True, db_column='STOCK_MINIMO_UTENSILIO', blank=True)),
            ],
            options={
                'db_table': 'UTENSILIO',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UtensilioEvento',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('utensilios_utilizados', models.IntegerField(null=True, db_column='UTENSILIOS_UTILIZADOS', blank=True)),
                ('utensilios_rotos', models.IntegerField(null=True, db_column='UTENSILIOS_ROTOS', blank=True)),
            ],
            options={
                'db_table': 'UTENSILIO_EVENTO',
                'managed': False,
            },
            bases=(models.Model,),
        ),
    ]

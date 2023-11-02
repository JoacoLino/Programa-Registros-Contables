from tkinter import ttk
import tkinter as tk
from db import *
from datetime import datetime

class Ingresar(tk.Frame):
    def __init__(self,master=None, ):
        super().__init__(master,width=400,height=400)
        self.master = master
        self.place(relx=0,rely=0)
        self.create_widgets()

    def create_widgets(self):

        self.ingresar = tk.Label(self, font=("Arial",16), text="-----------------Ingreso de Gastos-----------------")
        self.ingresar.place(relx=0,rely=0)


        self.dia = tk.Label(self, font=("Arial",12), text="Dia" )
        self.dia.place(relx=0.02,rely=0.12)
        self.dia2 = tk.Text(self, width=5, height=1)
        self.dia2.place(relx=0.15,rely=0.12)

        self.mes = tk.Label(self, font=("Arial",12), text="Mes" )
        self.mes.place(relx=0.28,rely=0.12)
        self.mes2 = tk.Text(self, width=5,height=1)
        self.mes2.place(relx=0.38,rely=0.12)

        self.year = tk.Label(self, font=("Arial",12), text="Año" )
        self.year.place(relx=0.50,rely=0.12)
        self.year2 = tk.Text(self, width=5,height=1)
        self.year2.place(relx=0.60,rely=0.12)

        self.monto = tk.Label(self, font=("Arial",12), text="Monto" )
        self.monto.place(relx=0.02,rely=0.20)
        self.monto2 = tk.Entry(self, width=20)
        self.monto2.place(relx=0.25,rely=0.20)

        self.motivo = tk.Label(self, font=("Arial",12), text="Motivo" )
        self.motivo.place(relx=0.02,rely=0.28)
        self.motivo2 = tk.Text(self, width=20,height=1)
        self.motivo2.place(relx=0.25, rely=0.28)

        self.ingresatbtt = tk.Button(self, width=20, height=1, command=self.IngresarDatos)
        self.ingresatbtt["text"] = "Ingresar"
        self.ingresatbtt.place(relx=0.27,rely=0.38)

        self.realizado = tk.Text(self, width=14, height=2)
        self.realizado.place(relx=0.7,rely=0.18)

        self.borrar = tk.Label(self, font=("Arial",16), text="-------------------Borrar Datos-------------------")
        self.borrar.place(relx=0,rely=0.52)

        self.dia_2 = tk.Label(self, font=("Arial",12), text="Dia" )
        self.dia_2.place(relx=0.02,rely=0.62)
        self.dia_22 = tk.Text(self, width=5, height=1)
        self.dia_22.place(relx=0.15,rely=0.62)

        self.mes_2 = tk.Label(self, font=("Arial",12), text="Mes" )
        self.mes_2.place(relx=0.28,rely=0.62)
        self.mes_22 = tk.Text(self, width=5,height=1)
        self.mes_22.place(relx=0.38,rely=0.62)

        self.year_2 = tk.Label(self, font=("Arial",12), text="Año" )
        self.year_2.place(relx=0.50,rely=0.62)
        self.year_22 = tk.Text(self, width=5,height=1)
        self.year_22.place(relx=0.60,rely=0.62)

        self.montos = tk.Label(self, font=("Arial",12), text="Monto" )
        self.montos.place(relx=0.02,rely=0.70)
        self.montos2 = tk.Text(self, width=20,height=1)
        self.montos2.place(relx=0.25,rely=0.70)

        self.motivos = tk.Label(self, font=("Arial",12), text="Motivo" )
        self.motivos.place(relx=0.02,rely=0.78)
        self.motivos2 = tk.Text(self, width=20,height=1)
        self.motivos2.place(relx=0.25, rely=0.78)

        self.borarbtt = tk.Button(self, width=20, height=1, command=self.BorrarDatos)
        self.borarbtt["text"] = "Borrar"
        self.borarbtt.place(relx=0.27,rely=0.88)

        self.realizado2 = tk.Text(self, width=14, height=2)
        self.realizado2.place(relx=0.7,rely=0.68)


    def IngresarDatos(self):
        dia_texto = self.dia2.get("1.0", "end").strip()
        mes_texto = self.mes2.get("1.0", "end").strip()
        year_texto = self.year2.get("1.0", "end").strip()
        dia = int(dia_texto)
        mes = int(mes_texto)
        year = int(year_texto)

        
        montoingresar = self.monto2.get().strip()
        motivoingresar = self.motivo2.get("1.0", "end").strip()
        try:
            monto = int(montoingresar)
            fecha = datetime(year, mes, dia)
            insert(fecha,monto,motivoingresar)
            
            self.realizado.delete("1.0", "end")
            self.realizado.insert("1.0", "Realizado")
        except ValueError as e:
            self.realizado.delete("1.0", "end")
            self.realizado.insert("1.0", "Error")
            
        
    def BorrarDatos(self):
        dia_texto = self.dia_22.get("1.0", "end").strip()
        mes_texto = self.mes_22.get("1.0", "end").strip()
        year_texto = self.year_22.get("1.0", "end").strip()
        dia = int(dia_texto)
        mes = int(mes_texto)
        year = int(year_texto)

        
        montoingresar = self.montos2.get().strip()
        motivoingresar = self.motivos2.get("1.0", "end").strip()
        try:
            monto = int(montoingresar)
            fecha = datetime(year, mes, dia)
            EliminarDatos(fecha,monto,motivoingresar)
            
        except ValueError as e:
        
            print(f"Error al borrar datos: {str(e)}")




class Tabla(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master, width=1150, height=900)
        self.master = master
        self.place(relx=0.258, rely=0)
        self.create_widgets()


    def create_widgets(self):

        # Crear el boton para la tabla
        self.actualizarbttn = tk.Button(self, width=20, height=1, command=self.MostrarTabla)
        self.actualizarbttn["text"] = "Actualizar"
        self.actualizarbttn.place(relx=0.45,rely=0.005)

        # Crear el boton para borrar directamente de la tabla
        self.motivobttn = tk.Button(self, width=15, height=1, command=self.EliminarDatoTabla)
        self.motivobttn["text"] = "Borrar"
        self.motivobttn.place(relx=0.89,rely=0.05)

        self.total = tk.Label(self, font=("Arial",12), text="Total" )
        self.total.place(relx=0.68,rely=0.95)
        self.total2 = tk.Text(self, width=20,height=1)
        self.total2.place(relx=0.73, rely=0.95)
          
        self.modificarlabel = tk.Label(self, font=("Arial",16), text="Modificar Datos")
        self.modificarlabel.place(relx=0.02,rely=0.01)

        self.modificarlabel = tk.Label(self, font=("Arial",16), text="|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n")
        self.modificarlabel.place(relx=0,rely=0)

        self.dialabel = tk.Label(self, font=("Arial",12), text="Dia" )
        self.dialabel.place(relx=0.02,rely=0.05)
        self.diatext = tk.Text(self, width=20,height=1)
        self.diatext.place(relx=0.02, rely=0.08)

        
        self.montolabel = tk.Label(self, font=("Arial",12), text="Monto" )
        self.montolabel.place(relx=0.02,rely=0.15)
        self.montotext = tk.Text(self, width=20,height=1)
        self.montotext.place(relx=0.02, rely=0.18)

        
        self.motivolavel = tk.Label(self, font=("Arial",12), text="Motivo" )
        self.motivolavel.place(relx=0.02,rely=0.25)
        self.motivotext = tk.Text(self, width=20,height=1)
        self.motivotext.place(relx=0.02, rely=0.28)
                
        self.totalbttn = tk.Button(self, width=15, height=1, command=self.SeleccionarLineaParaModificar)
        self.totalbttn["text"] = "Seleccionar Linea"
        self.totalbttn.place(relx=0.89,rely=0.1)

        self.totalbttn = tk.Button(self, width=15, height=1, command=self.Modificar)
        self.totalbttn["text"] = "Modificar"
        self.totalbttn.place(relx=0.04,rely=0.33)

        # Agrega un Combobox para seleccionar el mes
        self.mes_combobox = ttk.Combobox(self, values=["Todos", "Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"])
        self.mes_combobox.set("Todos")  # Establece un mes predeterminado
        self.mes_combobox.place(relx=0.59,rely=0.008)

        # Agrega un Combobox para seleccionar el año
        self.year_combobox = ttk.Combobox(self, values=["2022","2023"])
        self.year_combobox.set("2023")  # Establece un mes predeterminado
        self.year_combobox.place(relx=0.74,rely=0.008)

        # Crear un Treeview para mostrar la tabla
        self.tree = ttk.Treeview(self, columns=("id","dia", "motivo", "monto"), show="headings", height=39)

        # Configurar las columnas
        self.tree.heading("id", text="ID")
        self.tree.heading("dia", text="Día")
        self.tree.heading("motivo", text="Motivo")
        self.tree.heading("monto", text="Monto")

        # Ajustar el ancho de las columnas
        self.tree.column("id", width=20)
        self.tree.column("dia", width=200)
        self.tree.column("motivo", width=400)
        self.tree.column("monto", width=200)

        # Agregar el Treeview a la ventana principal
        self.tree.place(relx=0.17, rely=0.04)

        self.realizadoM = tk.Text(self, width=20,height=1)
        self.realizadoM.place(relx=0.02, rely=0.4)

    def Ingresar(self):

        motivoingresar = self.motivos2.get("1.0", "end").strip()
        try:
            insertar(motivoingresar)
            
        except ValueError as e:
        
            print(f"Error al ingresar datos: {str(e)}")

    def SeleccionarMes(self, mes):
        mes_actualizado = "0"
        if mes == "Enero":
            mes_actualizado = "1"
        elif mes == "Febrero":
            mes_actualizado = "2"
        elif mes == "Marzo":
            mes_actualizado = "3"
        elif mes == "Abril":
            mes_actualizado = "4"
        elif mes == "Mayo":
            mes_actualizado = "5"
        elif mes == "Junio":
            mes_actualizado = "6"
        elif mes == "Julio":
            mes_actualizado = "7"
        elif mes == "Agosto":
            mes_actualizado = "8"
        elif mes == "Septiembre":
            mes_actualizado = "9"
        elif mes == "Octubre":
            mes_actualizado = "10"
        elif mes == "Noviembre":
            mes_actualizado = "11"
        elif mes == "Diciembre":
            mes_actualizado = "12"
        
        return mes_actualizado
    
    def MostrarTabla(self):
    # Borra todos los elementos actuales en el Treeview
        for item in self.tree.get_children():
            self.tree.delete(item)

        # Obtener el mes seleccionado del Combobox
        mes_seleccionado = self.mes_combobox.get()
        mes = self.SeleccionarMes(mes_seleccionado)
        year_seleccionado = self.year_combobox.get()
        # Actualiza la tabla
        if mes == "0":
            InsertarTablaCompleta(self.tree, year_seleccionado)
        else:
            InsertarTabla(self.tree, mes, year_seleccionado)
        self.ActualizarSuma()

    def ActualizarCombobox(self):
        valores = ObtenerValoresDesdeDB()
        self.motivo_combox['values'] = valores

    def EliminarDatoTabla(self):
        selected_item = self.tree.selection()

        if not selected_item:
            print("Por favor, seleccione un elemnto de la tabla ")
            return
        
        values = self.tree.item(selected_item, "values")

        id_registro = values[0]

        EliminarDato(id_registro)
        self.MostrarTabla()

    def ActualizarSuma(self):
        self.total2.delete("1.0", "end")
        suma = 0
        year = self.year_combobox.get()
        mes = self.mes_combobox.get()
        mes_seleccionado = self.SeleccionarMes(mes)
        suma = SumarMontos(mes_seleccionado,year)
        self.total2.insert("1.0", str(suma))
    
    def SeleccionarLineaParaModificar(self):
        lista_datos = self.obtener_datos()
        self.diatext.delete("1.0", "end")
        self.diatext.insert("1.0", lista_datos[1])
        self.motivotext.delete("1.0", "end")
        self.motivotext.insert("1.0", lista_datos[2])
        self.montotext.delete("1.0", "end")
        self.montotext.insert("1.0", lista_datos[3])

    
    def Modificar(self):
        lista_datos = self.obtener_datos()
        dia_texto = self.diatext.get("1.0", "end").strip()
        nuevo_monto = self.montotext.get("1.0", "end").strip()
        nuevo_motivo = self.motivotext.get("1.0", "end").strip()

        id = lista_datos[0]
        nuevo_id = lista_datos[0]

        dia = lista_datos[1]
        motivo = lista_datos[2]
        monto = lista_datos[3]
        ModificarDatos(id, dia, motivo, monto, nuevo_monto, nuevo_id, dia_texto, nuevo_motivo)


    def obtener_datos(self):
        # Accede a los datos del TreeView a través de la instancia de ClaseB
        datos = self.obtener_seleccion()
        return datos
    

    def obtener_seleccion(self):
        valores = None
        # Obtiene la fila seleccionada
        seleccion = self.tree.selection()

        if seleccion:
            # Obtiene los valores de la fila seleccionada
            valores = self.tree.item(seleccion, "values")
        
        return valores

class Ingresos(tk.Frame):       
    def __init__(self, master=None):
        super().__init__(master, width=400, height=500)
        self.master = master
        self.place(relx=0, rely=0.444)
        self.create_widgets()

    def create_widgets(self):
        
        self.ingresolabel = tk.Label(self, font=("Arial",12), text="Ingreso" )
        self.ingresolabel.place(relx=0.02,rely=0.12)
        self.ingresotext = tk.Text(self, width=17, height=1)
        self.ingresotext.place(relx=0.20,rely=0.12)

        self.meslabel = tk.Label(self, font=("Arial",12), text="Mes" )
        self.meslabel.place(relx=0.02,rely=0.20)

        self.mes_combobox = ttk.Combobox(self, values=["01-Enero", "02-Febrero", "03-Marzo", "04-Abril", "05-Mayo", "06-Junio", "07-Julio", "08-Agosto", "09-Septiembre", "10-Octubre", "11-Noviembre", "12-Diciembre"])
        self.mes_combobox.set("Mes")  # Establece un mes predeterminado
        self.mes_combobox.place(relx=0.20,rely=0.20)

        self.ingresolabel = tk.Label(self, font=("Arial",12), text="Año" )
        self.ingresolabel.place(relx=0.02,rely=0.28)

        self.year_combobox = ttk.Combobox(self, values=["2022","2023","2024"])
        self.year_combobox.set("Año")  # Establece un mes predeterminado
        self.year_combobox.place(relx=0.20,rely=0.28)

        self.ingresarbttn = tk.Button(self, width=15, height=1, command=self.Ingresar)
        self.ingresarbttn["text"] = "Ingresar"
        self.ingresarbttn.place(relx=0.65,rely=0.20)

        self.mostrar_tabla_ingresosbttn = tk.Button(self, width=15, height=1, command=self.MostrarTablaIngresos)
        self.mostrar_tabla_ingresosbttn["text"] = "Mostrar Ingresos"
        self.mostrar_tabla_ingresosbttn.place(relx=0.65,rely=0.30)

        self.mostrar_tabla_saldosbttn = tk.Button(self, width=15, height=1, command=self.MostrarTablaSaldos)
        self.mostrar_tabla_saldosbttn["text"] = "Mostrar Saldos"
        self.mostrar_tabla_saldosbttn.place(relx=0.45,rely=0.68)

        self.year_combobox_saldos = ttk.Combobox(self, values=["2022","2023","2024"])
        self.year_combobox_saldos.set("Año")  # Establece un año predeterminado
        self.year_combobox_saldos.place(relx=0.50,rely=0.60)

        self.mes_combobox_saldos = ttk.Combobox(self, values=["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"])
        self.mes_combobox_saldos.set("Mes")  # Establece un mes predeterminado
        self.mes_combobox_saldos.place(relx=0.05,rely=0.60)

        self.saldo_ingresosbttn = tk.Button(self, width=15, height=1, command=self.IngresarSaldo)
        self.saldo_ingresosbttn["text"] = "Ingresar Saldo"
        self.saldo_ingresosbttn.place(relx=0.10,rely=0.68)
    
        self.total_saldo_label = tk.Label(self, font=("Arial",12), text="Total saldo" )
        self.total_saldo_label.place(relx=0.02,rely=0.76)
        self.total_saldo_text = tk.Text(self, width=17, height=1)
        self.total_saldo_text.place(relx=0.30,rely=0.76)

        self.saldo_totalbttn = tk.Button(self, width=15, height=1, command=self.CalcularSaldo)
        self.saldo_totalbttn["text"] = "Calcular saldo"
        self.saldo_totalbttn.place(relx=0.70,rely=0.752)
    
        self.titulo_ingresos_label = tk.Label(self, font=("Arial",16), text="---------------------Ingresos---------------------" )
        self.titulo_ingresos_label.place(relx=0,rely=0.03)
    
        self.titulo_saldos_label = tk.Label(self, font=("Arial",16), text="----------------------Saldos----------------------" )
        self.titulo_saldos_label.place(relx=0,rely=0.5)

        self.id_ingresos_label = tk.Label(self, font=("Arial",12), text="ID" )
        self.id_ingresos_label.place(relx=0.15,rely=0.43)
        self.id_text = tk.Text(self, width=6, height=1)
        self.id_text.place(relx=0.25,rely=0.43)

        self.ingreso_borrarbttn = tk.Button(self, width=15, height=1, command=self.BorrarIngreso)
        self.ingreso_borrarbttn["text"] = "Borrar Ingreso"
        self.ingreso_borrarbttn.place(relx=0.45,rely=0.42)

        self.titulo_saldos_borrar_label = tk.Label(self, font=("Arial",16), text="-------------Borrar Ingreso por ID-------------" )
        self.titulo_saldos_borrar_label.place(relx=0,rely=0.36)

        self.titulo_saldos_label = tk.Label(self, font=("Arial",16), text="--------------Borrar Saldo por ID--------------" )
        self.titulo_saldos_label.place(relx=0,rely=0.81)

        self.id_saldos_label = tk.Label(self, font=("Arial",12), text="ID" )
        self.id_saldos_label.place(relx=0.15,rely=0.88)
        self.id_saldos_text = tk.Text(self, width=6, height=1)
        self.id_saldos_text.place(relx=0.25,rely=0.88)

        self.saldo_borrarbttn = tk.Button(self, width=15, height=1, command=self.BorrarSaldo)
        self.saldo_borrarbttn["text"] = "Borrar Saldo"
        self.saldo_borrarbttn.place(relx=0.45,rely=0.87)

    def Ingresar(self):
        monto = self.ingresotext.get("1.0", "end").strip()
        mes = self.mes_combobox.get()
        year = self.year_combobox.get()

        try:
            insertaringresos(monto,mes,year)
            
        except ValueError as e:
        
            print(f"Error al ingresar datos: {str(e)}")

    def MostrarTablaIngresos(self):
        ventana_tabla = tk.Toplevel()
        ventana_tabla.title("Tabla Ingresos")

        treeview = ttk.Treeview(ventana_tabla, columns=("id","mes", "año", "monto"))
        treeview.heading("id", text="ID")
        treeview.heading("mes", text="Mes")
        treeview.heading("año", text="Año")
        treeview.heading("monto", text="Monto")
        
        treeview["show"] = "headings" #Oculta la columna #0

        # Ajustar el ancho de las columnas
        treeview.column("id", width=100)
        treeview.column("mes", width=200)
        treeview.column("año", width=200)
        treeview.column("monto", width=200)
        treeview.pack()
        
    # Borra todos los elementos actuales en el Treeview
        for item in treeview.get_children():
            treeview.delete(item)

        #BorrarDatos()
        MostrarTablaIngresosDb(treeview)

    def IngresarSaldo(self):
        saldo = 0
        mes = self.mes_combobox_saldos.get()
        year = self.year_combobox_saldos.get()
        mes_actualizado =  self.SeleccionarMes(mes)
        mes_actualizado2 = self.SeleccionarMes2(mes)

        saldo = SumarMontosIngresos(mes_actualizado2,year) - SumarMontosGastos(mes_actualizado,year)
        print(saldo)
        ingresos = SumarMontosIngresos(mes_actualizado2,year)
        gastos = SumarMontosGastos(mes_actualizado,year)
        duplicado = VerificarSiExiste(mes,year)
        print(duplicado)
        #BorrarDatos()
        if duplicado == False:
            IngresarDatosSaldo(mes,year,ingresos,gastos,saldo)
            print("Entro")
        else:
            ActualizarDatos(mes,year,ingresos,gastos,saldo)
            print("Entro al otro")



    def SeleccionarMes(self, mes):
        mes_actualizado = "0"
        if mes == "Enero":
            mes_actualizado = "1"
        elif mes == "Febrero":
            mes_actualizado = "2"
        elif mes == "Marzo":
            mes_actualizado = "3"
        elif mes == "Abril":
            mes_actualizado = "4"
        elif mes == "Mayo":
            mes_actualizado = "5"
        elif mes == "Junio":
            mes_actualizado = "6"
        elif mes == "Julio":
            mes_actualizado = "7"
        elif mes == "Agosto":
            mes_actualizado = "8"
        elif mes == "Septiembre":
            mes_actualizado = "9"
        elif mes == "Octubre":
            mes_actualizado = "10"
        elif mes == "Noviembre":
            mes_actualizado = "11"
        elif mes == "Diciembre":
            mes_actualizado = "12"
        
        return mes_actualizado


    def SeleccionarMes2(self, mes):
        mes_actualizado = "0"
        if mes == "Enero":
            mes_actualizado = "01-Enero"
        elif mes == "Febrero":
            mes_actualizado = "02-Febrero"
        elif mes == "Marzo":
            mes_actualizado = "03-Marzo"
        elif mes == "Abril":
            mes_actualizado = "04-Abril"
        elif mes == "Mayo":
            mes_actualizado = "05-Mayo"
        elif mes == "Junio":
            mes_actualizado = "06-Junio"
        elif mes == "Julio":
            mes_actualizado = "07-Julio"
        elif mes == "Agosto":
            mes_actualizado = "08-Agosto"
        elif mes == "Septiembre":
            mes_actualizado = "09-Septiembre"
        elif mes == "Octubre":
            mes_actualizado = "10-Octubre"
        elif mes == "Noviembre":
            mes_actualizado = "11-Noviembre"
        elif mes == "Diciembre":
            mes_actualizado = "12-Diciembre"
        
        return mes_actualizado

    
    def MostrarTablaSaldos(self):
        ventana_tabla = tk.Toplevel()
        ventana_tabla.title("Tabla Saldos")

        treeview = ttk.Treeview(ventana_tabla, columns=("id","mes", "año", "ingresos", "gastos", "saldo"))
        treeview.heading("id", text="ID")
        treeview.heading("mes", text="Mes")
        treeview.heading("año", text="Año")
        treeview.heading("ingresos", text="Ingresos")
        treeview.heading("gastos", text="Gastos")
        treeview.heading("saldo", text="Saldo")
        
        treeview["show"] = "headings" #Oculta la columna #0

        # Ajustar el ancho de las columnas
        treeview.column("id", width=100)
        treeview.column("mes", width=200)
        treeview.column("año", width=200)
        treeview.column("ingresos", width=200)
        treeview.column("gastos", width=200)
        treeview.column("saldo", width=200)
        treeview.pack()

        # Borra todos los elementos actuales en el Treeview
        for item in treeview.get_children():
            treeview.delete(item)

        #BorrarDatos()
        MostrarTablaSaldosDb(treeview)

    def CalcularSaldo(self):
        self.total_saldo_text.delete("1.0", "end")
        suma = SumarSaldos()
        self.total_saldo_text.insert("1.0", str(suma))
    
    def BorrarIngreso(self):
        id = self.id_text.get("1.0", "end").strip()
        EliminarIngreso(id)
    
    def BorrarSaldo(self):
        id = self.id_saldos_text.get("1.0", "end").strip()
        EliminarSaldo(id)

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Registro Contable")
    root.geometry("1550x900")
    root.config(bg="orange")
    ingresar_borrar = Ingresar(master=root)
    mostrar_tabla = Tabla(master=root)
    ingresos = Ingresos(master=root)
    connection = ConectarDB()
    root.mainloop()
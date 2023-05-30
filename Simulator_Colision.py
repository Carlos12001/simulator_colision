from tkinter import *
from tkinter import messagebox
import tkinter
import time
from threading import Thread
import random
import sys
import winsound
sys.setrecursionlimit(500000)

def sonidos(num):
    if num==0:
        t=Thread(target=mecanico_sonido)
        t.daemon=True
        t.start()
    elif num==1:
        t=Thread(target=bola_sonido)
        t.daemon=True
        t.start()
    elif num==2:
        t=Thread(target=mecanico_sonido)
        t.daemon=True
        t.start()
    elif num==3:
        t=Thread(target=inicio_sonido)
        t.daemon=True
        t.start()
    elif num==4:
        t=Thread(target=start_sonido)
        t.daemon=True
        t.start()
    elif num==5:
        t=Thread(target=pito_sonido)
        t.daemon=True
        t.start()
    elif num==6:
        t=Thread(target=choco_sonido)
        t.daemon=True
        t.start()

def mecanico_sonido():
    winsound.PlaySound("sounds/mecanica.wav", winsound.SND_ALIAS)
def bola_sonido():
    winsound.PlaySound("sounds/bola_rebote.wav", winsound.SND_ALIAS)
def inicio_sonido():
    winsound.PlaySound("sounds/empieza.wav", winsound.SND_ALIAS)
def start_sonido():
    winsound.PlaySound("sounds/boton_start.wav", winsound.SND_ALIAS)
def pito_sonido():
    winsound.PlaySound("sounds/claxon.wav", winsound.SND_ALIAS)
def choco_sonido():
    winsound.PlaySound("sounds/choque.wav", winsound.SND_ALIAS)

        

#Ventana Principal
class Menu():
    def __init__(self):


                                                                    #Configuraciones de la ventana principal
        self.menu=Tk()
        #Ventana
        self.menu.title("Menu Principal")
        self.menu.geometry("1000x1000+300+0")
        self.menu.resizable(width=False,height=False)

        # Imagenes
        fondo= PhotoImage(file='resource/fondo.png')

        #Labels
        self.fondo_label=Label(self.menu,image=fondo,width=1000,height=1000)
        self.nombre_label=Label(self.menu,text='Colision Simulator\nPor Carlos Andrés Mata Calderón', bg='#f8d8a9', font=( 'Comic Sans MS',26) )

        # Botones de la ventana
        self.boton_configuracion=Button( self.menu , text='Taller del \nautomóvil', bg='#e88068', command= self.ingresar2,font=( 'Comic Sans MS',26)     )

        #Posiciones de del incio del Menu
        #Posicion label
        self.fondo_label.place(x=0, y=0)
        self.nombre_label.place(x=240, y=100)
        #Posicion boton
        self.boton_configuracion.place(x=380, y=300)






                        #Configuraciones de la ventana del juego (No tienen posicion ya que la ventan constantemente se  va estar modificando sola)

        global opcion, value, archivo1,archivo2,tiempo_usario,permiso
        #Variables a ocupar del de configuraciones
        fuente=( 'Comic Sans MS',24)
        opcion=IntVar()
        value=StringVar()
        archivo1=open('data.txt','w')
        archivo2=open('data.txt','r')
        tiempo_usario=IntVar()
        fondo_3=PhotoImage(file='resource/fondo_3.png')
        permiso=False

        #Labels
        self.fondo_label_3 = Label(self.menu, image=fondo_3)
        self.label_info_1=Label(self.menu,text='Escoga el la distancia \n   del CW-EB', bg='#dadbdd', font=fuente)
        self.label_info_2=Label(self.menu,text='Tiempo del salva pantallas', bg='#dadbdd',font=fuente)


       #Botones de modo configuracion
        self.boton_guardar = Button(self.menu, text='Guardar', bg='#f8a9a9', font=('Comic Sans MS',36), command=self.choice)
        self.boton_salir = Button(self.menu, text='Salir', bg='#c8dae7', command=self.ingresar3, font=('Comic Sans MS',24))

        #Radio button modo configuracion
        self.radio_buttonx1 = Radiobutton(self.menu, text='Choque', value=1, variable=opcion,font = fuente,bg='#dadbdd')
        self.radio_buttonx2 = Radiobutton(self.menu, text='Corto', value=2, variable=opcion,font = fuente,bg='#dadbdd')
        self.radio_buttonx3 = Radiobutton(self.menu, text='Medio', value=3, variable=opcion,font = fuente,bg='#dadbdd')
        self.radio_buttonx4 = Radiobutton(self.menu, text='Largo', value=4, variable=opcion,font = fuente,bg='#dadbdd')

        #Spin Box
        self.spinbox_mode = Spinbox(self.menu, values=('Esquivar','Frenado'),font = fuente,bg='#a9adb4',textvariable = value)
        self.spinbox_tiempo= Spinbox(self.menu, from_=5,to=120,font = fuente,bg='#a9adb4',textvariable = tiempo_usario,width=5)






                            # Modo inicia el carga pantallas (No tienen posicion ya que la ventan constantemente se  va estar modificando sola)

        #Imagenes importadas
        fondo_2=PhotoImage(file='resource/fondo_2.png')

        #Canvas
        self.canvas_animacion=Canvas(self.menu,width=1000,height=1000)
        self.canva_fondo=self.canvas_animacion.create_image(500,500,image=fondo_2)





                                                    #Modo inicio del juego

        #Import Images
        fondo_4=PhotoImage(file='resource/fondo_4.png')
        #Labels
        self.fondo_label_4=Label(self.menu,image=fondo_4)
        #Botones
        self.boton_start = Button(self.menu, text='Start', bg='#e88068', command=self.ingresar, font=('Comic Sans MS', 48))


        self.menu.mainloop()








    #Acceder a la pantalla del Juego
    def ingresar(self):
        time.sleep(3)
        sonidos(4)
        # Destruir esta ventana
        self.menu.destroy()
        # Crear la nueva ventana
        Simulacion()





    #Es es el la funcion que cambia las posiones para poner la posicion de las configuraciones
    def ingresar2(self):
        #Color del fondo
        self.menu.config(bg='#b0ebe1')



        # Posiciones  FALSAS del incio del Menu

        # Posicion label
        self.fondo_label.place(x=50000, y=0)
        # Posicion boton
        self.boton_configuracion.place(x=-360, y=-425)



        # Lugares reales del modo configuracion

        #Posicions de los Labels
        self.fondo_label_3.place(x=0,y=0)
        self.label_info_1.place(x=120, y=50)
        self.label_info_2.place(x=580,y=50)

        #Posicion de los botones
        self.boton_guardar.place(x=350, y=550)
        self.boton_salir.place(x=5, y=5)

        # Posicion falsa de los spinbox
        self.radio_buttonx1.place(x=120, y=160)
        self.radio_buttonx2.place(x=120, y=220)
        self.radio_buttonx3.place(x=120, y=270)
        self.radio_buttonx4.place(x=120, y=320)

        #Posicion de la spinbox
        self.spinbox_tiempo.place(x=580,y=150)


    def choice(self):
        sonidos(0)
        time.sleep(3)
        global opcion, archivo1,tiempo_usario,value,permiso
        archivo1.seek(0)
        permiso=True
        if opcion.get() == 1:
            self.spinbox_mode.place(x=-200, y=-460)
            archivo1.write('False\n')
            archivo1.write('False\n')
            archivo1.write('100\n')
            archivo1.write(f'{tiempo_usario.get()}\n')


        elif opcion.get() == 2:
            self.spinbox_mode.place(x=200, y=460)
            archivo1.write('Trued\n')
            archivo1.write('False\n')
            archivo1.write('150\n')
            archivo1.write(f'{tiempo_usario.get()}\n')

        elif opcion.get() == 3:
            self.spinbox_mode.place(x=200, y=460)
            archivo1.write('Trued\n')
            archivo1.write('False\n')
            archivo1.write('250\n')
            archivo1.write(f'{tiempo_usario.get()}\n')

        elif opcion.get() == 4:
            self.spinbox_mode.place(x=200, y=460)
            archivo1.write('Trued\n')
            archivo1.write('False\n')
            archivo1.write('350\n')
            archivo1.write(f'{tiempo_usario.get()}\n')


        else:
            self.spinbox_mode.place(x=-200, y=-460)
            archivo1.write('Trued\n')
            archivo1.write('False\n')
            archivo1.write('250\n')
            archivo1.write(f'{tiempo_usario.get()}\n')


    def ingresar3(self):
        global archivo1,archivo2,value,tiempo_usario,permiso
        if permiso:
            archivo1.close()
            #Para guardar el parametro
            archivo2.seek(14)
            Parametro=int(archivo2.readline(3))

            #Logica para saber que opcion escogio
            if Parametro == 100:
                archivo1 = open('data.txt', 'w')
                archivo1.write('False\n')
                archivo1.write('False\n')
                archivo1.write('100\n')
                archivo1.write(f'{tiempo_usario.get()}\n')

            elif value.get()=='Frenado':
                archivo1 = open('data.txt', 'w')
                archivo1.write('False\n')
                archivo1.write('Trued\n')
                archivo1.write(f'{Parametro}\n')
                archivo1.write(f'{tiempo_usario.get()}\n')

            else:
                archivo1 = open('data.txt', 'r')


            #Cierre de archivo de texto
            archivo1.close()



            #Quita el montaje de configuraciones
            # Color del fondo
            self.menu.config(bg='white')


            # Lugares falsos del modo configuracion

            # Posicions de los Labels
            self.fondo_label_3.place(x=-12000, y=-50000)
            self.label_info_1.place(x=-12000, y=-50000)
            self.label_info_2.place(x=-58000, y=-50000)

            # Posicion de los botones
            self.boton_guardar.place(x=-35000, y=-70000)
            self.boton_salir.place(x=5000000, y=50000)

            # Posicion falsa de los spinbox
            self.radio_buttonx1.place(x=12000, y=16000)
            self.radio_buttonx2.place(x=12000, y=22000)
            self.radio_buttonx3.place(x=12000, y=27000)
            self.radio_buttonx4.place(x=12000, y=32000)

            # Posicion de la spinbox
            self.spinbox_tiempo.place(x=58000, y=150000)
            self.spinbox_mode.place(x=-20000, y=-54000)



            #Pone montaje de la animacion

            #Posicion Canvas
            self.canvas_animacion.place(x=0,y=0)

            #llamada a aniamacion
            archivo2.seek(19)
            self.animacion(int(archivo2.read()))
        else:
            messagebox.showwarning('Saliste sin guardar','Tienes que guardar primero antes de salir de configuraciones')

    def animacion(self,tiempo):
        global finalizar
        finalizar=True
        self.create_circle(1,tiempo)
        self.menu.after(tiempo*1000,self.ingresar4)


    def create_circle(self,num,tiempo):
        global finalizar
        circulo = Bolitas(self.canvas_animacion,self.menu)
        circulo_thread = Thread(target=circulo.move)
        circulo_thread.daemon = True
        circulo_thread.start()
        if num < 8 and finalizar and tiempo>12:
           self.menu.after(2 * 1000, self.create_circle, num + 1,tiempo)
        elif num<4 and finalizar:
            self.menu.after( 1000, self.create_circle, num + 1,tiempo)

    def ingresar4(self):
        global finalizar
        finalizar=False
        #Quito el montaje de animacion y pone el boton de inciar el juego
        self.canvas_animacion.delete('all')
        self.canvas_animacion.place(x=5000,y=2000)

        sonidos(3)
        
        self.fondo_label_4.place(x=0,y=0)
       
        self.boton_start.place(x=200, y=600)
         






# BOUNCING BALL CLASS #
class Bolitas:
    def __init__(self, canvas,menu):
        self.menu=menu
        self.canvas = canvas
        x = random.randint(50, 100)
        y = random.randint(0, 200)
        multi = random.randint(20, 42)
        colores = ['#616bd4', '#e6ed5a', '#bbe68e', '#e66b2e', '#e38ddc', '#edc077', '#7a7977', '#89afe8']
        self.xspeed = random.randint(1, 4)
        self.yspeed = random.randint(1, 3)
        self.bola = canvas.create_oval(x, y, x + multi * 2, y + multi * 2, fill=random.choice(colores))
        self.terminar=True

    def move(self):
        try:
            while self.terminar:
                self.canvas.move(self.bola, self.xspeed, self.yspeed)
                pos = self.canvas.coords(self.bola)
                if pos[3] >= 1000 or pos[1] <= 0:
                    self.yspeed = -self.yspeed
                    sonidos(1)
                if pos[2] >= 1000 or pos[0] <= 0:
                    self.xspeed = -self.xspeed
                    sonidos(1)
                self.menu.update()
                time.sleep(0.01)
        except:
            pass



























#Ventana del juego
class Simulacion():
    # Es una variable que va terminiar la animacion dependiendo la escogiencia del usario
    global terminar
    terminar=True

    def __init__(self):
        global terminar
        terminar=True

        #Ventana
        self.ventana=Tk()
        self.ventana.title("Simulador")
        self.ventana.geometry("600x900+500+50")
        self.ventana.resizable(width=False, height=False)

        # IMPORT Imagenes
        carro1 = PhotoImage(file='resource/1.png')
        carro2 = PhotoImage(file='resource/2.png')
        carro3 = PhotoImage(file='resource/3.png')
        carro4 = PhotoImage(file='resource/4.png')
        carro5 = PhotoImage(file='resource/5.png')
        lista_de_carros = [carro1, carro2, carro3, carro4, carro5]



        #Canvas de pasto
        canvas_wallpaper = Canvas(self.ventana, width=1000, height=1000, bg='#458c45')
        canvas_wallpaper.pack()


        #Calle del Juego se hace atributo por comveniencia
        self.canvas_calle = Canvas(self.ventana,bg='#353635', width=300, height=1000)
        self.canvas_calle.place(x=150,y=0)

        #Decoracion de movimiento
        self.yspeed=10

        tamano_y=0
        self.raya1 = self.canvas_calle.create_rectangle(140,tamano_y,160,tamano_y+90,fill='white')

        self.raya3 = self.canvas_calle.create_rectangle(140, tamano_y + 310, 160, tamano_y + 400, fill='white')

        self.raya5 = self.canvas_calle.create_rectangle(140, tamano_y + 530, 160, tamano_y + 630, fill='white')

        self.raya7 = self.canvas_calle.create_rectangle(140, tamano_y + 760, 160, tamano_y + 830, fill='white')

        



        #Labels
        self.warning_label=Label(self.ventana)





        #Buttons
        Button(self.ventana,text='X',bg='red',font=('Comic Sans MS',18,'bold'),command=self.salir).place(x=5,y=5)





        # Creacion de la instancia Carrrito y atributo de la Clase Juego
        self.carro = Carrito(self.canvas_calle,lista_de_carros)


        # Se creo la izquierda y derecha carro
        self.car_izquerda = Carros_Aleatorios(self.canvas_calle, 75,lista_de_carros)
        self.car_derecha = Carros_Aleatorios(self.canvas_calle, 225,lista_de_carros)


        # Llamada al maetodo de moeve aleatorio de cual empieza primero
        self.move_ramdoms_cars()


        #FLAG PARA PAUSA DEL JUEGO

        self.loops_thread= Thread(target=self.loop,args=[])
        self.loops_thread.daemon=True
        self.loops_thread.start()

        self.ventana.mainloop()



    def decoracion(self):

        global terminar

        if terminar:
            self.canvas_calle.move(self.raya1, 0, 15)

            self.canvas_calle.move(self.raya3, 0, 15)

            self.canvas_calle.move(self.raya5, 0, 15)

            self.canvas_calle.move(self.raya7, 0, 15)


            if self.canvas_calle.coords(self.raya1)[3] >= 1000:
                self.canvas_calle.move(self.raya1, 0, -1010)



            if self.canvas_calle.coords(self.raya3)[3] >= 1000:
                self.canvas_calle.move(self.raya3, 0, -1010)



            if self.canvas_calle.coords(self.raya5)[3] >= 1000:
                self.canvas_calle.move(self.raya5, 0, -1010)



            if self.canvas_calle.coords(self.raya7)[3] >= 1000:
                self.canvas_calle.move(self.raya7, 0, -1010)



            self.canvas_calle.after(20 ,self.decoracion)

            self.canvas_calle.update()







    # Parte logica del programa que crea los el Carrito y Obstaculos y su intereacion


    # Funcion externa para del Carrito movimiento que crea el Hilo
    def presion_tecla_hilo_start(self,evento):


        global terminar
        if terminar:

            #Truco para que el Thread funcione ya que el solo recibe o lista o tuplas
            self.move_carrito=Thread (target=self.carro.presion_tecla_aux,         args=[evento])
            self.move_carrito.daemon = True
            self.move_carrito.run()


    def move_ramdoms_cars(self):

        global terminar
        if terminar:    #Termina la animcacion

            #Movimiento de decoracion
            self.move_decoracion = Thread(target=self.decoracion,args=[])
            self.move_decoracion.daemon = True
            self.move_decoracion.run()

            #Accion de Movimiento del carro Aleateorio
            self.move_ramdom_car_izquierda = Thread(target = self.car_izquerda.movimiento,args=[random.choice([60,70,100]) ])
            self.move_ramdom_car_izquierda.daemon=True
            self.move_ramdom_car_izquierda.run()


                                                                                            #Caso contrario
            # Accion de Movimiento del carro Aleateorio
            self.move_ramdom_car_derecha = Thread(target=self.car_derecha.movimiento,args=[random.choice([60,70,100]) ] )
            self.move_ramdom_car_derecha.daemon=True
            self.move_ramdom_car_derecha.run()


        else:
            pass



            #Funcion booleana que ver si los carros esta cerca
        
    def cw_eb(self):
        archivo=open('data.txt','r')
        archivo2.seek(14)
        Parametro=int(archivo2.readline(3))

        global terminar

        if terminar:  # Termina la animcacion


            if abs( self.carro.get_Car_Y() - self.car_izquerda.get_Obstaculo_Y())< Parametro and abs(self.carro.get_Car_Y() - self.car_derecha.get_Obstaculo_Y()) < Parametro:

                self.warning_label.config(text='No es factible\n ningun Cambio',bg='red',font=(12))
                self.warning_label.place(x=200, y=800)
                return [True,'dos']


            elif abs( self.carro.get_Car_Y() - self.car_izquerda.get_Obstaculo_Y())< Parametro  or abs(  self.carro.get_Car_Y()  -100-self.car_izquerda.get_Obstaculo_y_Arriba())<Parametro:

                self.warning_label.config(text='Estas muy proximo\n del Auto',bg='red',font=(12))
                self.warning_label.place(x=200, y=800)
                return [True,'izquierda']


            elif abs(self.carro.get_Car_Y() - self.car_derecha.get_Obstaculo_Y()) < Parametro or abs(  self.carro.get_Car_Y()  -100-self.car_derecha.get_Obstaculo_y_Arriba())<Parametro:
                self.warning_label.config(text='Estas muy proximo\n del Auto', bg='red',font=(12))
                self.warning_label.place(x=200, y=800)
                return [True,'derecha']



            else:
                self.warning_label.place(x=-200, y=-800)
                return [False,'']




    #Logica con cw_wb desactivado
    def choque(self):
        Parametro = 100

        global terminar
        if terminar:  # Termina la animcacion

            if abs( self.carro.get_Car_Y() - self.car_izquerda.get_Obstaculo_Y())< Parametro and abs(self.carro.get_Car_Y() - self.car_derecha.get_Obstaculo_Y()) < Parametro:

                return [True,'dos']


            elif abs( self.carro.get_Car_Y() - self.car_izquerda.get_Obstaculo_Y())< Parametro  or abs(  self.carro.get_Car_Y()  -100-self.car_izquerda.get_Obstaculo_y_Arriba())<Parametro:

                return [True,'izquierda']


            elif abs(self.carro.get_Car_Y() - self.car_derecha.get_Obstaculo_Y()) < Parametro or abs(  self.carro.get_Car_Y()  -100-self.car_derecha.get_Obstaculo_y_Arriba())<Parametro:

                return [True,'derecha']

            else:

                return[ False,'']





    def loop(self): #Aqui va la opcion si cambia de carril, frena o choca
        global terminar

        # Forma de acceder los datos
        archivo=open('data.txt','r')


        archivo.seek(0)
        cambio = archivo.readline(4) == 'True'



        archivo.seek(7)
        frenado= archivo.readline(4) == 'True'




        while terminar: #Termina la animcacion





            #Logica si se escogio opcion de esquivar
            if cambio:


                #Llamada al metodo de dectecion de cercania con los autos
                valores_del_cw_eb=self.cw_eb()

                if valores_del_cw_eb[0]:


                    #Cambio hacia la derecha
                    if valores_del_cw_eb[1]=='izquierda':
                        self.carro.esquivar('izquierda', self.car_izquerda.get_Obstaculo_X())       #Aqui tengo que saber cual carro esta cerca, se utiliza el cw_eb
                       


                    # Cambio hacia la izquierda
                    elif  valores_del_cw_eb[1]=='derecha':
                        self.carro.esquivar('derecha',self.car_derecha.get_Obstaculo_X())       # Aqui tengo que saber cual carro esta cerca, se utiliza el cw_eb
                        


                    #Cambio no factible
                    else:
                        
                        terminar=False
                        #Mensaje de Advertencia
                        sonidos(5)
                        yes_no=messagebox.showinfo('Cambio no factible CW-EB','Se detuvo la animacion ya que hubo un Cambio no Factible\n,'
                                                                          'debido que el CW-EB detecto una cercania con los 2 autos\n'
                                                                          'Si quieres salir del programa presiona la ''X'', para cerrar el programa')




                else:
                    if terminar:
                        # Llamada al metodo de movimiento que crea el el Hilo del movimiento del carro
                        self.ventana.bind("<KeyPress>", self.presion_tecla_hilo_start)








            #Logica si se escogio opcion de frenado
            elif frenado:

                # Llamada al metodo de dectecion de cercania con los autos
                valores_del_cw_eb = self.cw_eb()

                # Llamada al metodo de dectecion de cercania con los autos
                if valores_del_cw_eb[0]:



                    #Logica paro izquierda
                    if valores_del_cw_eb[1] == 'izquierda' and self.carro.frenado_automatico('izquierda',self.car_izquerda.get_Obstaculo_X()):
                        self.warning_label.config(text='Frenado de Emergencia\n del Auto', bg='red',font=(12))
                        terminar = False
                        sonidos(5)
                        yes_no = messagebox.showinfo('Choque Evitado',
                                                     'Se detuvo la animacion debido que el CW-EB detecto\n'
                                                     '            una cercania con 1 auto  \n\n'
                                                     'Si quieres salir del programa presiona la ''X'', para cerrar el programa')



                     #Logica paro derecha
                    elif valores_del_cw_eb[1] == 'derecha'and self.carro.frenado_automatico('derecha',self.car_derecha.get_Obstaculo_X()):
                        self.warning_label.config(text='Frenado de Emergencia\n del Auto', bg='red',font=(12))
                        terminar = False
                        sonidos(5)
                        yes_no = messagebox.showinfo('Choque Evitado',
                                                     'Se detuvo la animacion debido que el CW-EB detecto\n'
                                                     '            una cercania con 1 auto.  \n\n'
                                                     'Si quieres salir del programa presiona la ''X'', para cerrar el programa' )




                    #Logica de frenado de emergencia
                    elif valores_del_cw_eb[1]=='dos':
                        self.warning_label.config(text='Frenado de Emergencia\n del Auto', bg='red',font=(12))
                        terminar = False
                        sonidos(5)
                        yes_no = messagebox.showinfo('Choque Evitado',
                                                     'Se detuvo la animacion debido que el CW-EB detecto\n'
                                                     '            una cercania con los 2 autos. \n\n'
                                                     'Si quieres salir del programa presiona la ''X'', para cerrar el programa' )

                    else:
                        pass




                #Movimiento libre del auto
                else:
                    if terminar:
                        # Llamada al metodo de movimiento que crea el el Hilo del movimiento del carro
                        self.ventana.bind("<KeyPress>", self.presion_tecla_hilo_start)
                    else:
                        pass










            #Commandos de finalizacion de choque
            else:

                valores_del_choque=self.choque()

                if valores_del_choque[0]:
                    if valores_del_choque[1] == 'izquierda' and self.carro.choque_de_carro('izquierda',self.car_izquerda.get_Obstaculo_X()):
                        sonidos(6)
                        terminar=False


                        yes_no = messagebox.showinfo('Choque',
                                                     'Se detuvo la animacion debido que el auto chocó'
                                                     ' con otro auto. \n\n'
                                                     'Si quieres salir del programa presiona la ''X'', para cerrar el programa')

                    elif valores_del_choque[1] == 'derecha' and self.carro.choque_de_carro('derecha', self.car_derecha.get_Obstaculo_X()):
                        sonidos(6)
                        terminar = False


                        yes_no = messagebox.showinfo('Choque',
                                                     'Se detuvo la animacion debido que el auto chocó'
                                                     ' con otro auto. \n\n'
                                                     'Si quieres salir del programa presiona la ''X'', para cerrar el programa')

                    else:
                        pass

                # Movimiento del auto
                else:
                    if terminar:
                        # Llamada al metodo de movimiento que crea el el Hilo del movimiento del carro
                        self.ventana.bind("<KeyPress>", self.presion_tecla_hilo_start)







    #Salir del juego
    def salir(self):
        self.ventana.destroy()

        start=Menu()















#Clase que crea el nuevo obstaculo
class Carros_Aleatorios:


    def __init__(self,canvas,derecha_o_izquierda,lista_de_carros):
        #Creacion de objeto canvas para manejarlo
        self.canvas=canvas
        #Variables de movimiento
        self.Obstaculo_X= derecha_o_izquierda
        self.Obstaculo_Y=   -random.randint(1100,4500)

        #Imagen del auto


        
        self.lista=lista_de_carros
        imagen_carro=self.lista[random.randint(0,3)]

        #Se crea el objeto a mover
        self.obstaculo = self.canvas.create_image(self.Obstaculo_X, self.Obstaculo_Y, image=imagen_carro)

    def movimiento(self,velocidad):

        global terminar
        if terminar:
            #Movimiento del auto aleatorio
            self.canvas.move(self.obstaculo, 0, 10)


            # Velocidad aleatoria del carros
            if terminar: #Termina la animcacion


                self.canvas.after(velocidad, self.movimiento,velocidad)

                if self.Obstaculo_Y<1000:
                    #Ubiacacion del carro en el canvas
                    self.Obstaculo_Y+=10

                else:

                    # Ubiacacion del carro afuera del canvas
                    para_afuera=random.randint(3100,6000)
                    self.Obstaculo_Y -= para_afuera
                    self.canvas.itemconfig(self.obstaculo,image=self.lista[random.randint(0,3)])
                    #El nuevo parametro de velocidad
                    velocidad = random.choice([60,70,100])
                    velocidad +=0

                    self.canvas.move(self.obstaculo, 0, -para_afuera)
                    self.canvas.update()


    def get_Obstaculo_X(self):
        return self.Obstaculo_X

    def get_Obstaculo_Y(self):
        return self.Obstaculo_Y + 150

    def get_Obstaculo_y_Arriba(self):
        return self.Obstaculo_Y -150

    






#Clase Carrito
class Carrito:



    def __init__(self,canvas,lista_de_carros):

        #Creacion de objeto canvas para manejarlo
        self.canvas=canvas
        #Variables de movimiento
        self.Car_X=75
        self.Car_Y=650

        carro = lista_de_carros[4]


        self.car = self.canvas.create_image( self.Car_X, self.Car_Y,image=carro)




    #Movimiento de ese carro
    def presion_tecla_aux(self,evento):


        global terminar
        if terminar:

            #Derecha
            if evento.keysym == 'Right' and self.Car_X<225:
                self.Car_X+=25
                self.canvas.move(self.car, 25, 0)
            #Izquierda
            if evento.keysym == 'Left'  and self.Car_X>75:
                self.Car_X-=25
                self.canvas.move(self.car, -25, 0)
            #Abajo
            if evento.keysym == 'Down'  and self.Car_Y<625:
                self.Car_Y+=25
                self.canvas.move(self.car, 0, 25)
            #Arriba
            if evento.keysym == 'Up'    and self.Car_Y>300:
                self.Car_Y-=25
                self.canvas.move(self.car, 0, -25)




    #Se obtine posicion de X del auto
    def get_Car_X(self):
        return self.Car_X

    # Se obtine posicion de X del auto
    def get_Car_Y(self):
        return self.Car_Y





    def esquivar(self,derecha_o_izquierda,posicion):

        #Revisa a donde tiene que moverse el auto si para la izquierda o derecha
        if derecha_o_izquierda=='izquierda':


            #Se mueve de la izquierda hacia la derecha
            if self.get_Car_X() < posicion+150:
                self.Car_Y -= 5
                self.Car_X += 5
                self.canvas.move(self.car,5,-5)
                # Metodos del canvas para movimiento continuo
                self.canvas.after(1000000000, self.esquivar,derecha_o_izquierda,posicion)
                self.canvas.update()


        else:


            #Se mueve de la derecha hacia la izquierda
            if self.get_Car_X()+150 > posicion:
                self.Car_Y -= 5
                self.Car_X -= 5
                self.canvas.move(self.car, -5, -5)
                # Metodos del canvas para movimiento continuo
                self.canvas.after(100000000000, self.esquivar,derecha_o_izquierda,posicion)
                self.canvas.update()

    #lOGICA DEL COCHE POR SI CHOCA
    def frenado_automatico(self,derecha_o_izquierda,posicion):

        #Revisa Si en realidad hay un posible choque
        if derecha_o_izquierda=='izquierda':


            #Se mueve de la izquierda hacia la derecha
            if self.get_Car_X() < posicion+150:
                return True
            else:
                return False
        # Revisa Si en realidad hay un posible choque
        elif derecha_o_izquierda=='derecha':
            #Se mueve de la derecha hacia la izquierda
            if self.get_Car_X()+150 > posicion:
                return True
            else:
                return False
        # Revisa Si en realidad hay un posible choque
        elif derecha_o_izquierda == 'dos':
            return False
        else:
            return False

    def choque_de_carro(self, derecha_o_izquierda, posicion):

        # Revisa Si en realidad es un choque
        if derecha_o_izquierda == 'izquierda':

            # Se mueve de la izquierda hacia la derecha
            if self.get_Car_X() <= posicion+110:

                return True
            else:
                return False
        # Revisa Si en realidad es un choque
        elif derecha_o_izquierda == 'derecha':
            # Se mueve de la derecha hacia la izquierda
            if self.get_Car_X() >= posicion-110:
                return True
            else:
                return False
        # Revisa Si en realidad es un choque
        elif derecha_o_izquierda == 'dos':
            return False
        else:
            return False


global start
#Loop de la ventana
start=Menu()


import tkinter as tk
from tkinter import ttk
from tkinter import *

#Creando la Ventana principal
def rgb_hack(rgb):
    return "#%02x%02x%02x" % rgb 
ws=tk.Tk()
ws.geometry("1000x1200")
ws.title("Malezas del Sur de Córdoba")
ws.config(bg=rgb_hack((9,100,24)))

#Etiqueta para el titulo
ttk.Label(ws, text= "Plantulas de malezas problema",
          background='black', foreground="white",
         font="Arial 20").grid(row=2, column=2)

#Etiqueta para cada una de las imagenes
ttk.Label(ws, text="Conyza bonaeriensis",
         font=("Times New Roman", 16,"italic")).grid(column=1, 
                                           row=3, padx=10, pady=25)

ttk.Label(ws, text="Amarantus quitensis",
         font=("Times New Roman", 16, "italic")).grid(column=2, 
                                           row=3, padx=10, pady=25)

ttk.Label(ws, text="Carduus acanthoides",
         font=("Times New Roman", 16, "italic")).grid(column=3, 
                                           row=3, padx=10, pady=25)

ttk.Label(ws, text="Hirschfeldia incaca",
         font=("Times New Roman", 16, "italic")).grid(column=1, 
                                           row=5, padx=10, pady=25)

ttk.Label(ws, text="Sorghum halepense",
         font=("Times New Roman", 16,"italic")).grid(column=2, 
                                           row=5, padx=10, pady=25)

ttk.Label(ws, text="Lolium multiflorum",
         font=("Times New Roman", 16,"italic")).grid(column=3, 
                                           row=5, padx=10, pady=25)
#Descargando imagenes
im1=PhotoImage(file="amaranto.png")
im2=PhotoImage(file="conyza.gif")
im3=PhotoImage(file="cardo.png")
im4=PhotoImage(file="mostacilla.png")
im5=PhotoImage(file="sorgo.png")
im6=PhotoImage(file="raigras.png")

#Configuracion de las ventanas emergentes

def amarantus():
    amarantus.ventana=tk.Tk()
    amarantus.ventana.title("Amaranthus quitensis")
    T=tk.Text(amarantus.ventana, height=30, width=75)
    fuente=("Comic Sans MS", 12, "bold")
    T.configure(font=fuente)
    info="""
    Maleza primavero-estival\n
    Taxonomia: Dicotyledonae>Caryophyllaes>Amaranthaceae\n
    Descripción:Plántula de porte arrosetado. Cotiledón lineal oblongo,violáceo en el envés.
    Pecíolo rojizo de 5 mm. de longitud.
    Primera y segunda hoja oblongas de borde ondeado con tintes violáceos en el 
    envés.
    Pecíolo breve. 
    La planta adulta posee tallo erguido a veces con ramas decumbentes, muy hojoso, 
    rojizo e    specialmente hacia el final de su ciclo. 
    Hojas pecioladas, flores verdosas o rojizas reunidas en glomérulos axilares y 
    terminales, erguidos o péndulos, formadas por cinco tépalos.
    Los frutos son pixidios uniseminados dehiscentes, sub-globosos, algo rugosos. 
    Se propaga por semillas, estas son lenticulares, negras o castañas, brillosas, 
    de aproximadamente 1mm de diámetro. Es una espcie de ciclo anual, primavero-estival,
    emerge y vegeta en primavera, florece y fructifica en verano hasta mediados de otoño.
    Su ciclo coincide con los barbechos previos a cultivos extensivos y con cultivos
    primavero-estivales como soja, maíz y girasol. Desde el punto de vista fisiológico es 
    una especie C4, con alta eficiencia en la producción de materia seca cuando 1
    las temperaturas son elevadas.\n
    Esta especie ha presentado resistencia a los siguientes sitios de acción: 
    inhibidor de la ALS (B/2), inhibidor de la EPSPs(G/9), síntesis de auxinas (O/4), y
    resistencia múltiple: inhibidor de la ALS (B/2) e inhibidor de la EPSPs (G/9), 
    y resistencia múltiple: inhibidor de la EPSPs (G/9) y síntesis de auxinas (O/4)."""
    T.pack()
    T.insert(tk.END,info)
   
    amarantus.ventana.mainloop()
    
def conyza():
    conyza.ventana=tk.Tk()
    conyza.ventana.title("Conyza bonariensis")
    T=tk.Text(conyza.ventana, height=30, width=75)
    fuente=("Comic Sans MS", 12, "bold")
    T.configure(font=fuente)
    info="""
    Maleza Otoño-invierno-primaveral\n
    Taxonomía:Dicotyledonae > Asterales > Asteraceae\n
    Descripción:
    Es nativa de América del Sur, es una especie anual, de emergencia primavero-estival, 
    erecta, su altura está condicionada por el ambiente y puede variar entre 20 cm y 2 m. 
    Cotiledones con pecíolos bien diferenciados, lámina color verde grisáceo, ovada, margen 
    entero, ápice redondeado. Nervio central visible en el envés. Las hojas son alternas,
    margen con uno a dos dientes. El número y tamaño de dientes aumenta en hojas sucesivas
    y el ápice es más agudo. Capítulos ordenados en pseudocorimbos muy laxos. 
    La característica de rama negra es que luego de la germinación otoñal, permanece 
    en estado de roseta durante esta estación y parte del invierno, comenzando a elongar
    el tallo aproximadamente en el mes de agosto 
    para la Argentina. Considerando la germinación primaveral, el estado de roseta es
    breve y la elongación del tallo se da a los pocos días de haber emergido.
    Flores blancas, dimorfas, las tubulosas centrales y en número de 15 a 20, más cortas 
    que las flores filiformes que son marginales y muy numerosas. Aquenios oblongos,
    comprimidos y con el margen engrosado, pubescentes, con papus blanco o amarillento, 
    piloso. Una vez que logra llegar a fructificación, rama negra logra formar 
    200.000 semillas.
    Se multiplica por semillas, las cuales germinan principalmente en otoño e invierno, 
    aunque un pequeño porcentaje es capaz de germinar en primavera. En general, germina 
    bajo temperatura entre 10 y 25°C. La mayor germinación se produce bajo la luz, siendo 
    mayor en suelos con pH neutro a alcalino que en los suelos ácidos.
    La emergencia de plántulas es mayor y más rápida en suelos de texturas francas,
    que en suelos arcillosos, siendo la germinación mayor entre 0 y 0,5 cm de profundidad.

    Esta especie ha presentado resistencia en el país al siguiente sitio de acción:
    inhibidor de la EPSPs (G/9)."""
    T.pack()
    T.insert(tk.END, info)
    
    conyza.ventana.mainloop()
    
def cardo():
    cardo.ventana=tk.Tk()
    cardo.ventana.title("Carduus acanthoides")
    T=tk.Text(cardo.ventana, height=30, width=75)
    fuente=("Comic Sans MS", 12, "bold")
    T.configure(font=fuente)
    info="""
    Maleza Otoño-invernal\n
    Taxonomía: Dicotyledonae > Asterales > Asteraceae\n

    Plántula de porte arrosetado. Cotiledones elípticos, brillantes, de ápice obtuso. 
    Pecíolo breve. Primer par de hojas enteras, dentado-epinescentes en el margen. 
    Pubescencia rala en el haz, y más densa sobre la nervadura del envés.
    Pecíolo breve. Tallo erguido. Poco ramificado, con alas espinosas que llegan 
    hasta los capítulos. Hojas: las basales en roseta, pinnatisectas, epinescentes 
    en el margen, con pubescencia   rala en el haz y densa en el envés. Las superiores 
    alternas, enteras a lobuladas y epinescentes 
    en el margen. Flores rosado-violáceas, dispuestas en capítulos erguidos, terminales,
    epinescentes.  Anual. Inverno-primaveral. Esta especie ha presentado 
    resistencia múltiple en el país a los siguientes sitios de acción: inhibidor 
    de la EPSPs (G/9) y síntesis de auxinas (O/4)."""
    T.pack()
    T.insert(tk.END, info)
    cardo.ventana.mainloop()

def mostacilla():
    mostacilla.ventana=tk.Tk()
    mostacilla.ventana.title("Hirschfeldia incana")
    T=tk.Text(mostacilla.ventana, height=30, width=75)
    fuente=("Comic Sans MS", 12, "bold")
    T.configure(font=fuente)
    info="""
    Maleza Otoño-invernal\n

    Taxonomía: Dicotyledonae > Capparales > Brassicaceae

    Hierba robusta, erecta, anual, bianual o perenne, muy ramificada en su parte superior. 
    Planta grisácea por su pubescencia híspida, especialmente densa en las porciones jóvenes.
    De 20 cm a un metro. Tallo: Generalmente muy ramificado desde la base. Hojas: basales
    arrosetadas, pecioladas con el lóbulo terminal mayor, caducas, con pequeños mucrones 
    cartilaginosos. Hojas superiores lineares, paulatinamente más pequeñas tendiendo a sésiles
    y enteras, todas provistas de pelos. Inflorescencia: Racimo corimbiforme, 
    alargado en la fructificación. Flores: Sépalos oblongos, de alrededor de 2.5 mm de largo,
    pétalos amarillos a amarillo cremosos, obovados, unguiculados, de 5 a 8 mm de largo.
    Frutos y semillas: silícuas lineares, erectas, de 8 a 15 mm de largo, de 1 a 1.5 mm de
    ancho, pegados al eje principal de la inflorescencia, glabras a casi glabras, evemente 
    trinervadas a la madurez con 3 a 9 semillas. El fruto tiene un pico de aproximadamente
    5 mm que frecuentemente es algo inflado y contiene 1-2 semillas adicionales.
    Semillas rojizas o café, y se cubren con mucilago cuando están húmedas.Raíz: Napiforme.
    Esta especie ha presentado resistencia en el país a los siguientes sitios de acción: 
    inhibidor de la ALS (B/2), inhibidor del 2,4-D (0/4) y glifosato (G/9), e inhibidor
    de la EPSPs (G/9) y 2,4 D."""
    T.pack()
    T.insert(tk.END,info)
    mostacilla.ventana.mainloop()

def sorgo():
    sorgo.ventana=tk.Tk()
    sorgo.ventana.title("Sorghum halepense")
    T=tk.Text(sorgo.ventana, height=30, width=75)
    fuente=("Comic Sans MS", 12, "bold")
    T.configure(font=fuente)
    info="""
    Maleza primavero-estival\n
    Taxonomía: Monocotyledonae > Poales > Poaceae\n
    Plántula de porte erguido. Primera y segunda hoja: vaina abierta,
    blanco-rosada en la base, lámina  lineal-lanceolada, con la 
    nervadura central prominente en el envés. Lígula membranosa,
    irregularmente dentada. 
    El rebrote es a partir de los rizomas, en donde se originan
    macollos formados por hojas de prefoliación
    convolutada, con las vainas rojizas en la base y las 
    láminas con la nervadura central prominente en el envés. 
    La planta adulta posee a) tallo aéreo: caña erguida, 
    generalmente hueca, de hasta 1,5 m de altura; b) tallo subterráneo: 
    rizoma indefinido, muy invasor, grueso, 
    cubiertos por escamas blanco-rojizas. Hojas glabras, 
    con nervadura central prominente, de 2,0 - 2,5 m de largo. 
    Espiguilla aovada, plano-convexa, brevemente aristada, con dos 
    segmentos de raquilla ensanchados en los extremos y frecuentemente
    cubiertos con pelos. Espiguilla de 4,3-5,5 mm de largo por 1,5-2mm de ancho.
    Cariopse aovado, área escutelar oval u obovada; castaño-rojizo 
    a castaño claro cerca del escutelo; 
    de 2-3 mm de largo por 1,3-1,8 mm de ancho.Ciclo: perenne. 
    Primavero-estival.Esta especie ha presentado resistencia en el país a los 
    siguientes sitios de acción: Inhibidor de la EPSPs (G/9),
    inhibidor de la ACCasa (A/1) y resistencia múltiple: Inhibidor de la ACCasa (A/1)
    - Inhibidor de la EPSPs (G/9)."""
    T.pack()
    T.insert(tk.END,info)
    sorgo.ventana.mainloop()

def raigras():
    raigras.ventana=tk.Tk()
    raigras.ventana.title("Lolium multiflorum")
    T=tk.Text(raigras.ventana, height=30, width=75)
    fuente=("Comic Sans MS", 12, "bold")
    T.configure(font=fuente)
    info="""
    Maleza otoño-invernal\n
    Taxonomía: Monocotyledonae > Poales > Poaceae\n

    Lolium multiflorum es una especie originaria de Europa y naturalizada en América.
    Difundida de manera espontánea, ya sea como recurso forrajero y como maleza. Especie 
    anual, glabra, con cañas erguidas de 30 a 90 cm de altura. Su vaina presenta matices
    rosados o rojizos, entera en las primeras hojas de cada macollo. Innovaciones 
    intravaginales. Glabra. Prefoliación convoluta
    (las formas pequeñas a veces son conduplicadas).
    Lámina carenada a plana, glabra, lisa, brillante en el envés. 
    Nervio medio poco perceptible en el haz. Lígula membranosa de borde entero o subentero.
    Aurículas de 0,5 a 2,5 mm de longitud. Emergencia otoño-invernal; habiendo 
    cumplido su vernalización, florece en nuestro país entre los meses de octubre y noviembre. 
    Posee un elevado grado de alogamia y puede alcanzar una producción de 10-12 mil semillas. 
    Cariopsis de ± 4 mm de largo. La persistencia 
    en el banco edáfico de semillas es de, aproximadamente, no más de dos años.
    Esta especie ha presentado resistencia en el país a los siguientes sitios de acción: 
    inhibidor de la EPSPs (G/9); inhibidor de la ACCasa (A/1); inhibidor de la ALS (B/2)."""
    T.pack()
    T.insert(tk.END, info)
    raigras.ventana.mainloop()

#Configuracion de los botones
b1=Button(ws, image=im1, borderwidth=3, relief="raised", padx=5, pady=10, command=amarantus)
b2=Button(ws, image=im2, borderwidth=3, relief="raised", padx=5, pady=10, command=conyza)
b3=Button(ws, image=im3, borderwidth=3, relief="raised", padx=5, pady=10, command=cardo )
b4=Button(ws, image=im4, borderwidth=3, relief="raised", padx=5, pady=10, command=mostacilla )
b5=Button(ws, image=im5, borderwidth=3, relief="raised", padx=5, pady=10, command=sorgo )
b6=Button(ws, image=im6, borderwidth=3, relief="raised", padx=5, pady=10, command=raigras )

#Ubicación de los botones
b1.grid(row=4, column=2, pady=10)
b2.grid(row=4, column=1, padx=30,pady=10)
b3.grid(row=4, column=3, pady=10)
b4.grid(row=6, column=1, padx=30,pady=10)
b5.grid(row=6, column=2, pady=10)
b6.grid(row=6, column=3, pady=10)

ws.mainloop()
    
    

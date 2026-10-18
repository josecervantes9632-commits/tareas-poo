# ============================================================
# ACTIVIDAD: HERENCIA MÚLTIPLE  (super() + **kwargs + MRO)
# ============================================================

# SUPERCLASE 1
class Jugador:
    def __init__(self, juego, rango, **kwargs):
        # Toma juego y rango; el resto viaja en **kwargs a la siguiente clase del MRO
        super().__init__(**kwargs)
        self.juego = juego
        self.rango = rango

    def jugar(self):
        print(f"Jugando {self.juego} con rango {self.rango}.")


# SUPERCLASE 2
class Streamer:
    def __init__(self, plataforma, seguidores, **kwargs):
        # Toma plataforma y seguidores; kwargs ya llega vacío -> object
        super().__init__(**kwargs)
        self.plataforma = plataforma
        self.seguidores = seguidores

    def transmitir(self):
        print(f"Transmitiendo en {self.plataforma} para {self.seguidores} seguidores.")


# SUBCLASE CON HERENCIA MÚLTIPLE
# MRO: StreamerGamer -> Jugador -> Streamer -> object
class StreamerGamer(Jugador, Streamer):
    def __init__(self, nombre, juego, rango, plataforma, seguidores):
        self.nombre = nombre
        # Envía todos los parámetros; cada clase toma los suyos
        super().__init__(
            juego=juego,
            rango=rango,
            plataforma=plataforma,
            seguidores=seguidores,
        )

    def presentarse(self):
        print(f"Hola, soy {self.nombre}.")
        self.jugar()       # viene de Jugador
        self.transmitir()  # viene de Streamer


# PRUEBA
sg = StreamerGamer(
    nombre="José",
    juego="Valorant",
    rango="Diamante",
    plataforma="Twitch",
    seguidores=1500,
)
sg.presentarse()

print("\n--- MRO de StreamerGamer ---")
for i, cls in enumerate(StreamerGamer.__mro__, 1):
    print(f"{i}. {cls.__name__}")

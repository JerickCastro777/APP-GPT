from resumen import Resumentexto
import os
from dotenv import load_dotenv

# Cargar variables de entorno desde el archivo .env
load_dotenv()

# Obtener la clave de API desde las variables de entorno
api_key = os.environ.get("OPENAI_API_KEY")

# Inicializar la clase Resumentexto con la clave de API
gpt_resumen = Resumentexto(api_key=api_key)

# Texto a resumir
texto = """
La teoría de juegos es un área de la matemática aplicada que utiliza modelos para estudiar interacciones en estructuras formalizadas de incentivos (los llamados «juegos»). La teoría de juegos se ha convertido en una herramienta sumamente importante tanto para la ciencia económica como para la administración de empresas y ha contribuido a comprender más adecuadamente la conducta humana frente a la toma de decisiones. Sus investigadores estudian las estrategias óptimas, así como el comportamiento previsto y observado de individuos en juegos. Tipos de interacción aparentemente distintos pueden presentar en realidad una estructura de incentivo similar y, por lo tanto, se puede representar mil veces conjuntamente un mismo juego.

Desarrollada en sus comienzos como una herramienta para entender el comportamiento de la economía, la teoría de juegos se ha ido extendiendo a muchos otros campos, como la biología, las ciencias de la computación, la sociología, la politología, la psicología y la filosofía. Experimentó un crecimiento sustancial y se formalizó por primera vez a partir de los trabajos de John von Neumann y Oskar Morgenstern, antes y durante la Guerra Fría, debido sobre todo a su aplicación a la estrategia militar, en particular a causa del concepto de destrucción mutua garantizada. Desde los setenta, la teoría de juegos se ha aplicado a la conducta animal, incluyendo el desarrollo de las especies por la selección natural. A raíz de juegos como el dilema del prisionero, en los que el egoísmo generalizado perjudica a los jugadores, la teoría de juegos ha atraído también la atención de los investigadores en informática, usándose en inteligencia artificial y cibernética.

Los conflictos entre seres racionales que recelan uno del otro, o la pugna entre competidores que interactúan y se influyen mutuamente, que piensan y que, incluso, pueden ser capaces de traicionarse uno al otro, constituyen el campo de estudio de la teoría de juegos, la cual se basa en un análisis matemático riguroso pero que, sin embargo, surge de manera natural al observar y analizar un conflicto desde un punto de vista racional. Desde el enfoque de esta teoría, un «juego» es una situación conflictiva en la que priman intereses contrapuestos de individuos o instituciones, y en ese contexto una parte, al tomar una decisión, influye sobre la decisión que tomará la otra; así, el resultado del conflicto se determina a partir de todas las decisiones tomadas por todos los actuantes.

La teoría de juegos plantea que debe haber una forma racional de jugar a cualquier «juego» (o de negociar en un conflicto), especialmente en el caso de haber muchas situaciones engañosas y segundas intenciones; así, por ejemplo, la anticipación mutua de las intenciones del contrario, que sucede en juegos como el ajedrez o el póquer, da lugar a cadenas de razonamiento teóricamente infinitas, las cuales pueden también trasladarse al ámbito de resolución de conflictos reales y complejos. En síntesis, y tal como se comentó, los individuos, al interactuar en un conflicto, obtendrán resultados que de algún modo son totalmente dependientes de tal interacción.

Así, desde que Von Neumann, Morgenstern y John Nash delinearon los postulados básicos de esta teoría durante las décadas del 40 y 50, varias han sido las aplicaciones que se le han otorgado a esta herramienta en el campo de las decisiones económicas, llegando incluso a modificar el modo en que los economistas interpretaban la toma de decisiones y la consecución del bienestar común.
"""

# Idioma del resumen
idioma = "es"  # Cambia a "en" para inglés u otro código de idioma

# Obtener y mostrar el resumen del texto en el idioma seleccionado
resumen = gpt_resumen.resumen(texto, idioma)
print(f"\nResumen en {idioma}:\n{resumen}")

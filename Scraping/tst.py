import csv
from bs4 import BeautifulSoup
import requests
import statistics

# Documentación Beautiful Soup https://www.crummy.com/software/BeautifulSoup/bs4/doc/
# Documentacion Requests https://requests.readthedocs.io/en/latest/

WEB = 'https://www.elconfidencial.com'
SELECTOR_CSS_TITULO_ARTICULO = ".titleArticleEditable"

x = requests.get(WEB)

print(x.status_code) # Si es 200, ha ido ok

# Para acceder al HTML usamos la propiedad text
x.text

# Parseamos el documento
parsed_document = BeautifulSoup(x.text, "html.parser")

# Selectores CSS
all_titles_nodes = parsed_document.css.select(".titleArticleEditable")

# Comprobamos que estamos extrayendo el titular
all_titles_nodes[0].text

# Extraemos todos los artículos
all_titles = [article.text.replace("\n", " ").lstrip().rstrip() for article in all_titles_nodes]
    
# Print(all_nodes)
print(all_titles)


# Hacer programa que estraiga los datos de https://www.expansion.com/mercados/cotizaciones/indices/ibex35_I.IB.html


#### Export csv
import csv
 
def export_list_to_csv(rows, columns=None, filename="output", delimiter=";"):

    if type(rows[0]) == str:
        rows = [[row] for row in rows]

    if columns:
        assert len(columns) == len(rows[0]), "There should be the same number of columns and rows elements"
 
    with open(f"{filename}.csv", 'w') as f:
        write = csv.writer(f, delimiter=delimiter)

        if columns:
            write.writerow(columns)

        write.writerows(rows)

export_list_to_csv(all_titles, columns = ["titulares"])

# Chunk splitter
def chunks(lst, n):
    return [lst[i:i + n] for i in range(0, len(lst), n)]


# Posibles trabajos:
## Conectarse y descargar los datos de una web (pej las cotizaciones diarias de la bolsa), cargarlo en pandas y hacer un análisis exploratorio
## Conectarse y descargar los datos de una web (pej las cotizaciones diarias de la bolsa), cargarlo en pandas y hacer un análisis exploratorio (texto, contar palabras, ) https://www.letras.com/sfdk/

x = requests.get("https://www.expansion.com/mercados/cotizaciones/indices/igbolsamadrid_I.MA.html")
parsed_document = BeautifulSoup(x.text, "html.parser")

all_values_nodes = parsed_document.css.select("#listado_valores td")
all_values = [article.text for article in all_values_nodes]

chunks(all_values, 11)



##### GRUPOS DE MÚSICA #####

WEB = "https://www.letras.com"
GRUPO = "nach"
x = requests.get(WEB + "/" + GRUPO)
parsed_document = BeautifulSoup(x.text, "html.parser")

all_values_nodes = parsed_document.css.select("#cnt-artist-songlist a.songList-table-songName")
all_values = [[article.text, f"{WEB}{article.attrs['href']}"] for article in all_values_nodes]

#export_list_to_csv(all_values, ['cancion', 'direccion'])

def get_lyrics(url):

    #Nos descargamos la web y parseamos su contenido con beautiful soup
    y = requests.get(url)
    parsed_song = BeautifulSoup(y.text, "html.parser")

    # Seleccionamos los párrafos con las letras
    song_lyrics_nodes = parsed_song.css.select(".lyric p")

    # Reemplazamos saltos de línea
    for el in song_lyrics_nodes:
        [br.replace_with("\n").text for br in el.select("br")]

    #Convertimos a texto plano
    song_lyrics_nodes = [p.text for p in song_lyrics_nodes]
    song_lyrics_nodes = "\n".join(song_lyrics_nodes)

    # Imprimir cancion
    #print(song_lyrics_nodes)

    palabras_diferentes = set(song_lyrics_nodes.replace("\n", " ").split(" "))

    return len(palabras_diferentes)

canciones = {all_values[i][0] : get_lyrics(all_values[i][1]) for i in range(len(all_values))}
    
print(statistics.mean([canciones[key] for key in canciones.keys()]))

# Toteking
317.59090909090907

# SFDK
293.9012345679012

# Violadores del Verso
412.7037037037037

# Nach
321.6333333333333

#####

# TEORÍA - DE QUE SE COMPONE UNA WEB - HTML, CSS Y JAVASCRIPT
# PETICIONES HTTP - GET, POST, PUT, DELETE, PATCH, ... https://developer.mozilla.org/es/docs/Web/HTTP/Methods
# HTML - ETIQUETAS, ATRIBUTOS, https://developer.mozilla.org/es/docs/Web/HTML
# SELECTORES CSS - https://www.w3schools.com/cssref/css_selectors.php
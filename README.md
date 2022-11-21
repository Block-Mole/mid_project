# mid_project
Proyecto mitad de bootcamp bdmlpt0922

Dataset : UEFA EURO 2020

Datos de los partidos y resultados del último torneo de la Eurocopa celebrado en 2020.

Objetivos del proyecto:

Crear una API que conecte con una base de datos y envíe la información a un servidor cloud desde el cual podremos mostrar un dashboard interactivo con la visualizacion de los datos.

Etapas:

1. Limpieza y enriquecimiento del los datos
2. Crear la base de datos en un servidor
3. API
4. Streamlite
5. Empaquetar
6. Subir el paquete a un servidor cloud


# UEFA EURO 2020 (Mid Project BDMLPT0922) 

<p align="center"> 
  LA funcion de esta api es poder acceder a diferentes metricas de los partidos del campeonato de la UEFA EURO 2020.
</p>

<p align="center">
  <img src="https://github.com/Crypto-topo/mid_project/blob/mp1/img/football-field-6351717_960_720.jpg?raw=true" width="400">
</p>

<p align="center">
 Dispones en el side bar todas las opciones para navegar entre las disferentes metricas.
</p>

## Getting Started

### Requirements:

- [API](https://github.com/Crypto-topo/mid_project/blob/mp1/api/requirements.txt)
- [DASHBOARD]()


Uvicorn run:
```sh
  uvicorn api.main:app 
  ```
  This command is to run the API in our computer

Streamlit run:
```sh
  streamlit run main.py
  ```
  This command is to run the dashboard in our computer 
  
 ## Roadmap
 
 - [x] Limpiar base de datos
 - [x] Conectar con api
 - [x] Creacion de diferentes dashboards con streamlit
 - [ ] Añadir datos geoespaciales de los estadios a la db
 - [ ] Crear una dashboard con un mapa de los estadios en donde se jugo cada partido
 - [ ] Export to PDF

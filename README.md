# UEFA EURO 2020 (Mid Project BDMLPT0922) 
Proyecto mitad de bootcamp bdmlpt0922

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
- [DASHBOARD](https://github.com/Crypto-topo/mid_project/blob/mp1/streamlit/requirements.txt)


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
 - [ ] Empaquetar con Docker
 - [ ] Subir a Heroku

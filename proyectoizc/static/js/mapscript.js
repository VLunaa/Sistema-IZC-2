var municipios = [
    { id: "municipio1", nombre: "Zacatecas", registros: 10 },
    { id: "municipio2", nombre: "Municipio 2", registros: 5 },
    { id: "municipio4", nombre: "Municipio 3", registros: 7 },
    { id: "municipio5", nombre: "Municipio 3", registros: 7 },
    { id: "municipio6", nombre: "Municipio 3", registros: 7 },
    { id: "municipio7", nombre: "Municipio 3", registros: 7 },
    { id: "municipio8", nombre: "Municipio 3", registros: 7 },
    { id: "municipio9", nombre: "Municipio 3", registros: 7 },
    { id: "municipio10", nombre: "Municipio 3", registros: 7 },
    { id: "municipio11", nombre: "Municipio 3", registros: 7 },
    { id: "municipio12", nombre: "Municipio 3", registros: 7 },
    { id: "municipio13", nombre: "Municipio 3", registros: 7 },
    { id: "municipio14", nombre: "Municipio 3", registros: 7 },
    { id: "municipio15", nombre: "Municipio 3", registros: 7 },
    { id: "municipio16", nombre: "Municipio 3", registros: 7 },
    { id: "municipio17", nombre: "Municipio 3", registros: 7 },
    { id: "municipio18", nombre: "Municipio 3", registros: 7 },
    { id: "municipio19", nombre: "Municipio 3", registros: 7 },
    { id: "municipio20", nombre: "Municipio 3", registros: 7 },
    { id: "municipio21", nombre: "Municipio 3", registros: 7 },
    { id: "municipio22", nombre: "Municipio 3", registros: 7 },
    { id: "municipio23", nombre: "Municipio 3", registros: 7 },
    { id: "municipio24", nombre: "Municipio 3", registros: 7 },
    { id: "municipio25", nombre: "Municipio 3", registros: 7 },
    { id: "municipio26", nombre: "Municipio 3", registros: 7 },
    { id: "municipio27", nombre: "Municipio 3", registros: 7 },
    { id: "municipio28", nombre: "Municipio 3", registros: 7 },
    { id: "municipio29", nombre: "Municipio 3", registros: 7 },
    { id: "municipio30", nombre: "Municipio 3", registros: 7 },
    { id: "municipio31", nombre: "Municipio 3", registros: 7 },
    { id: "municipio32", nombre: "Municipio 3", registros: 7 },
    { id: "municipio33", nombre: "Municipio 3", registros: 7 },
    { id: "municipio34", nombre: "Municipio 3", registros: 7 },
    { id: "municipio35", nombre: "Municipio 3", registros: 7 },
    { id: "municipio36", nombre: "Municipio 3", registros: 7 },
    { id: "municipio37", nombre: "Municipio 3", registros: 7 },
    { id: "municipio38", nombre: "Municipio 3", registros: 7 },
    { id: "municipio39", nombre: "Municipio 3", registros: 7 },
    { id: "municipio40", nombre: "Municipio 3", registros: 7 },
    { id: "municipio41", nombre: "Municipio 3", registros: 7 },
    { id: "municipio42", nombre: "Municipio 3", registros: 7 },
    { id: "municipio43", nombre: "Municipio 3", registros: 7 },
    { id: "municipio44", nombre: "Municipio 3", registros: 7 },
    { id: "municipio45", nombre: "Municipio 3", registros: 7 },
    { id: "municipio46", nombre: "Municipio 3", registros: 7 },
    { id: "municipio47", nombre: "Municipio 3", registros: 7 },
    { id: "municipio48", nombre: "Municipio 3", registros: 7 },
    { id: "municipio49", nombre: "Municipio 3", registros: 7 },
    { id: "municipio50", nombre: "Municipio 3", registros: 7 },
    { id: "municipio51", nombre: "Municipio 3", registros: 7 },
    { id: "municipio52", nombre: "Municipio 3", registros: 7 },
    { id: "municipio53", nombre: "Municipio 3", registros: 7 },
    { id: "municipio54", nombre: "Municipio 3", registros: 7 },
    { id: "municipio55", nombre: "Municipio 3", registros: 7 },
    { id: "municipio56", nombre: "Municipio 3", registros: 7 },
    { id: "municipio57", nombre: "Municipio 3", registros: 7 },
    { id: "municipio58", nombre: "Municipio 3", registros: 7 },
];






// Iterar sobre la lista de municipios
municipios.forEach(function(municipio) {
    // Seleccionar el elemento del mapa SVG correspondiente al municipio
    var path = document.getElementById(municipio.municipioEvento);
    
    // Agregar un atributo onmouseover al elemento
    path.setAttribute("onmouseover", "mostrarDatos('" + municipio.municipioEvento + "', '" + municipio.num_eventos + "')");
  });
  
  // Función para mostrar los datos del municipio
  function mostrarDatos(municipio, num_eventos) {
    // Seleccionar el elemento HTML donde se mostrarán los datos
    var info = document.getElementById("info-municipio");
    
    // Agregar los datos del municipio al elemento HTML
    info.innerHTML = "<p>Municipio: " + municipio + ", Eventos: " + num_eventos + "</p>";
  }
  
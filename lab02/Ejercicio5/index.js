document.getElementById("formulario").addEventListener("submit", function(event) {
    event.preventDefault();
    
    var cantidadValores = document.getElementById("cantidad").value;
    
    crearTabla(cantidadValores);
    document.getElementById("calcular-btn").disabled = false;
  });
  
  function crearTabla(cantidadFilas) {
    var tablaContainer = document.getElementById("tabla-container");
    tablaContainer.innerHTML = ""; // Limpiar contenido anterior
    
    var tabla = document.createElement("table");
    tabla.setAttribute("id", "tabla");
    
    for (var i = 0; i < cantidadFilas; i++) {
      var fila = document.createElement("tr");
      
      var celdaNumero = document.createElement("td");
      var numeroInput = document.createElement("input");
      numeroInput.setAttribute("type", "number");
      celdaNumero.appendChild(numeroInput);
      
      fila.appendChild(celdaNumero);
      tabla.appendChild(fila);
    }
    
    tablaContainer.appendChild(tabla);
    
    // Crear botón de calcular suma
    var calcularBtn = document.createElement("button");
    calcularBtn.setAttribute("id", "calcular-btn");
    calcularBtn.textContent = "Calcular suma";
    calcularBtn.disabled = true;
    tablaContainer.appendChild(calcularBtn);
    
    calcularBtn.addEventListener("click", function() {
      var valores = document.querySelectorAll("#tabla input");
      var suma = 0;
      
      for (var i = 0; i < valores.length; i++) {
        suma += parseInt(valores[i].value);
      }
      
      var resultado = document.getElementById("resultado");
      resultado.textContent = "La suma de los valores es: " + suma;
    });
  }
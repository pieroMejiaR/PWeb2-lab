function crearTabla(cantidad) {
    for (i=0; i < cantidad.value; i++) {
        document.getElementById("tabla").innerHTML =`
        <tr>
            <td>{i}</td>
        </tr>`;
  }

    document.getElementById("tabla").innerHTML = `<button onclick= sumar()>Sumar</button>`;
}

function sumar() {
        
}
function obtenerCodigo( url ) {
    const link = url.value;
    
    const codigoGuiones = link.substring(link.lastIndexOf("/") + 1, link.lenght);
    const codigo = codigoGuiones.substring(0, codigoGuiones.indexOf("-"))+codigoGuiones.substring(codigoGuiones.indexOf("-")+1, codigoGuiones.lastIndexOf("-"))+codigoGuiones.substring(codigoGuiones.lastIndexOf("-") +1 , codigoGuiones.length);

    document.getElementById("nuevoCodigo").innerHTML = codigo;
}

function diasRestantesArequipa() {
    const diaDeArequipa = new Date( '2023/8/15');
    const fechaActual = new Date();
    const resta = diaDeArequipa.getTime() - fechaActual.getTime();
    const diasRestantes = Math.round(resta / (1000*60*60*24));
    document.getElementById("dias").innerHTML = diasRestantes;
}

diasRestantesArequipa();    

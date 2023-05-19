
const fechaActual = new Date();

function diaDeLaSemana(dia) {
      const diasSemana = ['Domingo', 'Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado'];
      const hoy = dia.getDay();
      return diasSemana[hoy];
}

console.log( diaDeLaSemana(fechaActual));
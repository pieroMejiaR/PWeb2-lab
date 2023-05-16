
const date = new Date();

function diaDeLaSemana(d) {
  hoy = d.getDay();
  if (hoy == 0) {
        return 'Domingo';
  }
  else if (hoy == 1) {
        return 'Lunes';
  }
  else if (hoy == 2) {
        return 'Martes';
  }
  else if (hoy == 3) {
        return 'Miercoles';
  }
  else if (hoy == 4) {
        return 'Jueves';
  }
  else if (hoy == 5) {
        return 'Viernes';
  }
  else {
        return 'Sabado';
  }
  
}

diaDeLaSemana(date);
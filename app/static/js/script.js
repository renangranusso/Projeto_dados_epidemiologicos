var hora = document.getElementById('mostrarHora');

function time() {
  var d = new Date();
  var s = d.getSeconds();
  var m = d.getMinutes();
  var h = d.getHours();

  if (h < 10){
      h = "0" + h
  }
  if (m < 10){
      m = "0" + m
  }
  if(s < 10){
      s = "0" + s
  }
  
  hora.textContent = "Hora Atual: " + h + ":" + m + ":" + s
}

setInterval(time, 1000);
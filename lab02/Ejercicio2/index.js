function invertirPalabra( word) {
    var inverso="";
    for(i=word.value.length; i >= 0; i--) {
        inverso += word.value.charAt(i);
    }
    document.getElementById("nuevo").innerHTML = inverso;
}
function cores(){
    var red = Math.floor(Math.random()*256);
    var green = Math.floor(Math.random()*256);
    var blue = Math.floor(Math.random()*256);
    return "rgb("+red+","+green+","+blue+")";
}
function jogo(){
    document.getElementById("botao1").style.backgroundColor = cores();
    document.getElementById("botao2").style.backgroundColor = cores();
    document.getElementById("botao3").style.backgroundColor = cores();
    document.getElementById("botao4").style.backgroundColor = cores();
    document.getElementById("botao5").style.backgroundColor = cores();
    document.getElementById("botao6").style.backgroundColor = cores();
    var aux = Math.floor(Math.random()*6);
    document.getElementById("cordita").innerHTML = document.getElementById("botao"+aux).style.backgroundColor;
    return "botao"+aux;
}
function ganho(idCor){
    var id = jogo();
    var escolha = "botao"+idCor;
    if(escolha == id){
        alert("Acertou!");
        jogo();
    } else{
        alert("Burrão em");
    }
}
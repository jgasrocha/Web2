// script.js

// Obter o modal
var modal = document.getElementById("myModal");

// Obter a imagem que abre o modal
var images = document.getElementsByClassName("open-modal");

// Adiciona evento de clique a cada imagem
for (var i = 0; i < images.length; i++) {
    images[i].onclick = function() {
        var locationImageUrl = this.getAttribute("data-location-image");
        document.getElementById("locationImage").src = locationImageUrl;
        modal.style.display = "block"; // Mostra o modal
    }
}

// Obter o elemento <span> que fecha o modal
var span = document.getElementsByClassName("close")[0];

// Quando o usuário clicar em <span> (x), fecha o modal
span.onclick = function() {
    modal.style.display = "none";
}

// Quando o usuário clicar em qualquer lugar fora do modal, fecha-o
window.onclick = function(event) {
    if (event.target == modal) {
        modal.style.display = "none";
    }
}

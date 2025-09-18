
// Récupère tous les boutons avec la classe "choix"
const boutons = document.querySelectorAll(".choix");

// Ajoute un "écouteur" sur chaque bouton
boutons.forEach(bouton => {
    bouton.addEventListener("click", () => {
        // Récupère la valeur du bouton cliqué
        const choix = bouton.value;

        // Affiche le choix dans le paragraphe
        document.getElementById("resultat").innerText = "Tu as choisi : " + choix;
    });
});
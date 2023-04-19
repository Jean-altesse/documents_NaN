// Récupération de la liste des informations dans le localstorage
let infoList = JSON.parse(localStorage.getItem('infoList')) || [];

// Récupération des éléments HTML
const form = document.querySelector('form');
const firstNameInput = document.getElementById('firstName');
const lastNameInput = document.getElementById('lastName');
const ageInput = document.getElementById('age');
const heightInput = document.getElementById('height');
const infoListElement = document.getElementById('infoList');
const ajout = document.querySelector('#ajout')

ajout.addEventListener('click', ()=>{
    form.style.display = "block"
})

// Fonction qui affiche la liste des informations
function displayInfoList() {
    // Suppression des anciens éléments de la liste
    infoListElement.innerHTML = '';
  
    // Ajout de chaque information à la liste
    for (let i = 0; i < infoList.length; i++) {
      const info = infoList[i];
      const tr = document.createElement('tr');
      tr.innerHTML = `
            <td>${info.firstName}</td> 
            <td>${info.lastName}</td> 
            <td>${info.age} ans</td> 
            <td>${info.height} cm</td>
        `;
  
      const deleteButton = document.createElement('button');
      deleteButton.innerText = 'Supprimer';
      deleteButton.addEventListener('click', function() {
        // Suppression de l'information de la liste et du localstorage
        infoList.splice(i, 1);
        localStorage.setItem('infoList', JSON.stringify(infoList));
  
        // Mise à jour de l'affichage de la liste
        displayInfoList();
      });
  
      tr.appendChild(deleteButton);
      infoListElement.appendChild(tr);
    }
  }
  
  // Ajout d'un événement au formulaire pour ajouter une nouvelle information
  form.addEventListener('submit', function(event) {
    event.preventDefault();
  
    // Récupération des valeurs du formulaire
    const firstName = firstNameInput.value;
    const lastName = lastNameInput.value;
    const age = parseInt(ageInput.value);
    const height = parseInt(heightInput.value);
  
    // Ajout de l'information à la liste et au localstorage
    const newInfo = {
      firstName,
      lastName,
      age,
      height
    };
    infoList.push(newInfo);
    localStorage.setItem('infoList', JSON.stringify(infoList));
  
    // Mise à jour de l'affichage de la liste
    displayInfoList(); 
  
    // Réinitialisation du formulaire
    form.reset();
  });
  
  // Affichage initial de la liste des informations
  displayInfoList();
  
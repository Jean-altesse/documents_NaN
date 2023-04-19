// Récupération de la table HTML et des boutons
const table = document.getElementById('table');
const addBtn = document.getElementById('btn-ajouter');
const cancelBtn = document.getElementById('btn-annuler');
const saveBtn = document.getElementById('btn-enregistrer');

// Récupération des champs du formulaire
const nomInput = document.getElementById('nom');
const prenomInput = document.getElementById('prenom');
const domaineInput = document.getElementById('domaine');
const localiteInput = document.getElementById('localite');
const ageInput = document.getElementById('age');
const telInput = document.getElementById('telephone');

// Écouteur de clic sur le bouton "Ajouter un contact"
addBtn.addEventListener('click', () => {
  // Afficher la fenêtre modale
  document.getElementById('modal-ajouter').classList.add('show');
});

// Écouteur de clic sur le bouton "Annuler"
cancelBtn.addEventListener('click', () => {
  // Masquer la fenêtre modale et effacer les champs du formulaire
  document.getElementById('modal-ajouter').classList.remove('show');
  nomInput.value = '';
  prenomInput.value = '';
  domaineInput.value = '';
  localiteInput.value = '';
  ageInput.value = '';
  telInput.value = '';
});

// Écouteur de clic sur le bouton "Enregistrer"
saveBtn.addEventListener('click', () => {
  // Récupérer les valeurs des champs du formulaire
  const nom = nomInput.value;
  const prenom = prenomInput.value;
  const domaine = domaineInput.value;
  const localite = localiteInput.value;
  const age = ageInput.value;
  const tel = telInput.value;

  // Créer une nouvelle ligne pour la table
  const newRow = table.insertRow();

  // Ajouter les cellules à la nouvelle ligne
  const nomCell = newRow.insertCell();
  const prenomCell = newRow.insertCell();
  const domaineCell = newRow.insertCell();
  const localiteCell = newRow.insertCell();
  const ageCell = newRow.insertCell();
  const telCell = newRow.insertCell();
  const supprimerCell = newRow.insertCell();

  // Remplir les cellules avec les valeurs du formulaire
  nomCell.innerText = nom;
  prenomCell.innerText = prenom;
  domaineCell.innerText = domaine;
  localiteCell.innerText = localite;
  ageCell.innerText = age;
  telCell.innerText = tel;

  // Ajouter le bouton "Supprimer" à la nouvelle ligne
  const supprimerBtn = document.createElement('button');
  supprimerBtn.innerText = 'Supprimer';
  supprimerBtn.addEventListener('click', () => {
    table.deleteRow(newRow.rowIndex);
  });
  supprimerCell.appendChild(supprimerBtn);

  // Masquer la fenêtre modale et effacer les champs du formulaire
  document.getElementById('modal-ajouter').classList.remove('show');
  nomInput.value = '';
  prenomInput.value = '';
  domaineInput.value = '';
  localiteInput.value = '';
  ageInput.value = '';
  telInput.value = '';
});

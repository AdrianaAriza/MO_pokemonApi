var button = document.getElementById("search-button");
button = addEventListener("click", function (e) {
  e.preventDefault;
  var name = document.getElementById("search-input").value;
  getResults(name);
});

function getResults(name) {
  fetch("https://mopokemonapi.herokuapp.com/api/" + name)
    .then((response) => {
      return response.json();
    })
    .then((json) => {
      console.log(json);
      let imgHTML = "";
      let evolutionHTML = "";
      let pevolutionHTML = "";
      let notFoundHTML = "";
      const resultsEl = document.getElementById("trend-results");
      const preevolutions = document.getElementById("pre-evolution");
      const evolution = document.getElementById("evolution");

      if (json.name == "pokemon not found") {
        notFoundHTML += `
        <h1>
          POKEMON NOT FOUND
        </h1>`;
        resultsEl.innerHTML = notFoundHTML;
        preevolutions.innerHTML = "";
        evolution.innerHTML = "";
      } else {
        var evolutionsList = [];
        var pevolutionList = [];
        json.evolutions.forEach((evolution) => {
          if (evolution.evolutionType == "evolution") {
            evolutionsList.push(evolution);
          } else {
            pevolutionList.push(evolution);
          }
        });
        imgHTML += `<img src = "${json.image}" class = "item" width = "20%" height = "20%"> 
                  <p>NAME: ${json.name}</p>
                  <p>ID: ${json.id}</p>
                  <p>HEIGHT: ${json.height}</p>
                  <p>WEIGHT: ${json.weight}</p>`;
        resultsEl.innerHTML = imgHTML;
        evolutionsList.forEach((evolution) => {
          evolutionHTML += `
        <div class="pokemon">
          <div class="pokemon-characteristics">
            <img src = "${evolution.image}" class = "item" width = "100px" height = "100px"> 
          </div>
          <div class="pokemon-characteristics">
            <p>NAME: ${evolution.name}</p>
            <p>ID: ${evolution.id}</p>
          </div>
        </div>`;
        });
        evolution.innerHTML = evolutionHTML;
        pevolutionList.forEach((evolution) => {
          pevolutionHTML += `<div class="pokemon">
          <div class="pokemon-characteristics">
            <img src = "${evolution.image}" class = "item" width = "100px" height = "100px"> 
          </div>
          <div class="pokemon-characteristics">
            <p>NAME: ${evolution.name}</p>
            <p>ID: ${evolution.id}</p>
          </div>
        </div>`;
        });
        preevolutions.innerHTML = pevolutionHTML;
      }
    });
}

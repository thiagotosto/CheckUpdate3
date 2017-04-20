function change_field_value(value) {
  document.getElementById('active').innerHTML = value.concat(' <span class="caret"></span>')
  document.getElementById('campo').value = value
}

function set_type(value) {
  document.getElementById('valor').type = value
}

function validateInsert() {
    var campo = document.forms["clausula"]["campo"].value;
    var valor = document.forms["clausula"]["valor"].value;


    //'Fabricante' check
    if (campo == "Fabricante"){
      if ((valor != "dell") && (valor != "hp") && (valor != "cisco")) {
          alert("O valor deve 'DELL' ou 'HP' ou 'CISCO'");
          return false;
    };
  };

    //'Em uso?' check
    if (campo == "Em uso?"){
      if ((valor != "S") && (valor != "N")) {
          alert("O valor deve 'S' ou 'N'");
          return false;
    };
  };
}

function set_placeholder(value) {
  document.getElementById('valor').placeholder = value
}

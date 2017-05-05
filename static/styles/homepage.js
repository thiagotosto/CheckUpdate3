//INDEX

function change_field_value(value) {
  document.getElementById('active').innerHTML = value.concat(' <span class="caret"></span>')
  document.getElementById('campo').value = value
}

function set_type(value) {
  document.getElementById('valor').type = value
}

//Valida inserts enviados
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

//coloca o placeholder no formulário
function set_placeholder(value) {
  document.getElementById('valor').placeholder = value
}


//CONSULTA RESULT

//update orquestrador
function update_orquestrador(value) {
    set_modal_title(value);
    change_hidden_input_consres(value);
}

//muda titulo do modal
function set_modal_title(value) {
  //alert(value)
  //console.log(value.serial)
  //console.log(value.rack)
  //console.log(value.categoria)
  //console.log(value.modelo)
  //console.log(value.patrimonio)
  //console.log(value.end_date)
  //console.log(value.start_date)
  //console.log(value)
  //console.log(value.)
  //console.log(value.)
  //alert({{ object.serial }})
  document.getElementById('modal-title').innerHTML = value;
}

function change_hidden_input_consres(value) {
  document.getElementById('serial-id').value = value
}


/*
function setObjectModal(object) {
  alert('Passei em setObjectModal')
  document.getElementById('modal-title').value = object.nome;
}*/

//INDEX

function change_field_value(value) {
  document.getElementById('active').innerHTML = value.concat(' <span class="caret"></span>')
  document.getElementById('campo').value = value
}

function set_type(value) {
  document.getElementById('valor').type = value
}

//Valida inserts enviados
function validateConsulta() {
    var campo = document.forms["clausula"]["campo"].value;
    var valor = document.forms["clausula"]["valor"].value.toLowerCase();

    //'Fabricante' check
    if (campo == "Fabricante"){
      if ((valor != "dell") && (valor != "hp") && (valor != "cisco")) {
          alert("O valor deve 'DELL' ou 'HP' ou 'CISCO'");
          return false;
    };
  };

    //'Em uso?' check
    if (campo == "Em uso?"){
      if ((valor != "s") && (valor != "n")) {
          alert("O valor deve 'S' ou 'N'");
          return false;
    };
  };

  if (campo == "Localizacao"){
    if ((valor != "sala de equipamentos") && (valor != "hpa") && (valor != "sala de equipamentos sp")) {
        alert("O valor deve ser 'Sala de equipamentos' ou 'HPA' ou 'Sala de equipamentos SP'");
        return false;
    };
  };

  if (campo == "Legado"){
    if ((valor != "Produção") && (valor != "Legado")){
        alert("O valor deve ser 'Legado' ou 'Produção'");
        return false;
    };
  }
}

//coloca o placeholder no formulário
function set_placeholder(value) {
  document.getElementById('valor').placeholder = value
}


function set_buttons_place() {
  document.getElementById('add').style.marginLeft = "30px";
}

//CONSULTA RESULT

function validateUpdate() {
  var form = document.forms['edicao'];

  //'Fabricante' check
  if ((form['Fabricante'].value.toLowerCase() != "dell") && (form['Fabricante'].value.toLowerCase() != "hp") && (form['Fabricante'].value.toLowerCase() != "cisco") && (form['Fabricante'].value.toLowerCase() != '')) {
      alert("O valor de 'Fabricante' deve ser 'DELL' ou 'HP' ou 'CISCO'");
      return false;
  };


  //'Em uso?' check
  if ((form['Em uso?'].value.toLowerCase() != "s") && (form['Em uso?'].value.toLowerCase() != "n") && (form['Em uso?'].value.toLowerCase() != '')) {
      alert("O valor de 'Em uso?' deve ser 'S' ou 'N'");
      return false;
  };

  if ((form['Localizacao'].value.toLowerCase() != "sala de equipamentos") && (form['Localizacao'].value.toLowerCase() != "hpa") && (form['Localizacao'].value.toLowerCase() != "sala de equipamentos sp") && (form['Localizacao'].value.toLowerCase() != '')) {
      alert("O valor deve ser 'Sala de equipamentos' ou 'HPA' ou 'Sala de equipamentos SP'");
      return false;
  };

  if ((form['Legado'].value.toLowerCase() != "Legado") && (form['Legado'].value.toLowerCase() != "Produção") && (form['Legado'].value.toLowerCase() != '')) {
      alert("O valor deve ser 'Legado' ou 'Produção'");
      return false;
  }
}

function validateInsert() {
  var form = document.forms['insert'];

  //'Serial' check
  if (form['Serial'].value == '') {
      alert("Por favor insira um serial");
      return false;
  };

  //'Fabricante' check
  if ((form['Fabricante'].value.toLowerCase() != "dell") && (form['Fabricante'].value.toLowerCase() != "hp") && (form['Fabricante'].value.toLowerCase() != "cisco") && (form['Fabricante'].value.toLowerCase() != '')) {
      alert("O valor de 'Fabricante' deve ser 'DELL' ou 'HP' ou 'CISCO'");
      return false;
  };


  //'Em uso?' check
  if ((form['Em uso?'].value.toLowerCase() != "s") && (form['Em uso?'].value.toLowerCase() != "n") && (form['Em uso?'].value.toLowerCase() != '')) {
      alert("O valor de 'Em uso?' deve ser 'S' ou 'N'");
      return false;
  };

  if ((form['Localizacao'].value.toLowerCase() != "sala de equipamentos") && (form['Localizacao'].value.toLowerCase() != "hpa") && (form['Localizacao'].value.toLowerCase() != "sala de equipamentos sp") && (form['Localizacao'].value.toLowerCase() != '')) {
      alert("O valor deve ser 'Sala de equipamentos' ou 'HPA' ou 'Sala de equipamentos SP'");
      return false;
  };

  if ((form['Legado'].value.toLowerCase() != "Legado") && (form['Legado'].value.toLowerCase() != "Produção") && (form['Legado'].value.toLowerCase() != '')) {
      alert("O valor deve ser 'Legado' ou 'Produção'");
      return false;
  }

}

//muda titulo do modal
function set_modal_title(value, flag) {
  if (flag == 'u'){
    document.getElementById('modal-title-update').innerHTML = value;
  } else if (flag == 'r') {
    document.getElementById('modal-title-remove').innerHTML = value;
  };
}

//update orquestrador
function update_orquestrador(value) {
    set_modal_title(value, 'u');
    change_hidden_input_consres(value, 'u');
}

var global_serial;

function remove_orquestrador(value) {
    set_modal_title(value, 'r');
    change_hidden_input_consres(value, 'r');
    global_serial = value;
}

function validateRemove() {
  if (global_serial != document.forms['remove']['serial-confirmation'].value.toUpperCase()) {
    alert('O valor de serial não bate com o do elemento em questão');
    return false;
  }
}

function change_hidden_input_consres(value, flag) {
  if (flag == 'u') {
    document.getElementById('serial-id-update').value = value;
  } else if (flag == 'r') {
    document.getElementById('serial-id-remove').value = value;
  };
}


function teste_object(object) {
  console.log(object[0]['serial']);
  console.log(object[0]['fabricante']);
}

function throw_error(erro) {
  alert(erro);
}

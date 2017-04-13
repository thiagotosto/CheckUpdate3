function change_field_value(value) {
  document.getElementById('active').innerHTML = value.concat(' <span class="caret"></span>')
  document.getElementById('campo').value = value
}

function set_type(value) {
  document.getElementById('valor').type = value
}

function set_placeholder(value) {
  document.getElementById('valor').placeholder = value
}

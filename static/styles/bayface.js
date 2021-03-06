var xinitial = 50;
var yinitial = 50;
var slotAmount = 44;
var slotHeigth = 20;
var slotWidth = 120;
var sideWidth = 20;
var cor_dell = '#EEE9E9';
var cor_hp = '#0096d6';
var cor_cisco = '#FF8000';
var cor_brocade = '#A91D3E';
var cor_supermicro = "#97B860"

function drawBases(rack, server) {

  //se tiver servidor
  if (server.length >= 1) {
    getCanvasHeight();
    drawRack(rack);
    drawLegend();

    console.log(server);


    for (i = 0; i < server.length; i++){
      console.log(server[i].posicao);
      if (server[i].posicao[0] > 0){
        drawServer(server[i]);
      }
    }
  }
}

function getCanvasHeight() {
  canvas = document.getElementById('canvas')
  canvas.height = slotHeigth*slotAmount + 56;
}

function drawLegend() {
   var canvas = document.getElementById("canvas");
      if (canvas.getContext) {
        var ctx = canvas.getContext("2d");
      }

   var xLegendInitial = xinitial + slotWidth + sideWidth + 20;
   var yLegendInitial = yinitial + slotAmount*slotHeigth - 10;

   //desenhando indicativos
   roundedRect(ctx,xLegendInitial,yinitial + slotAmount*slotHeigth - 70,10,10,2,'#222', cor_dell);
   roundedRect(ctx,xLegendInitial,yinitial + slotAmount*slotHeigth - 55,10,10,2,'#222', cor_hp);
   roundedRect(ctx,xLegendInitial,yinitial + slotAmount*slotHeigth - 40,10,10,2,'#222', cor_cisco);
   roundedRect(ctx,xLegendInitial,yinitial + slotAmount*slotHeigth - 25,10,10,2,'#222', cor_brocade);
   roundedRect(ctx,xLegendInitial,yinitial + slotAmount*slotHeigth - 10,10,10,2,'#222', cor_supermicro);

   //escrevendo legendas
   ctx.font = "13px Helvetica";
   ctx.fillStyle = "#222";
   ctx.fillText("DELL", xLegendInitial + 20, yLegendInitial - 50);
   ctx.fillText("HP", xLegendInitial + 20, yLegendInitial - 35);
   ctx.fillText("CISCO", xLegendInitial + 20, yLegendInitial - 20);
   ctx.fillText("BROCADE", xLegendInitial + 20, yLegendInitial - 5);
   ctx.fillText("SUPERMICRO", xLegendInitial + 20, yLegendInitial + 10);
}


function drawRack(rackNumber) {
   var canvas = document.getElementById("canvas");
      if (canvas.getContext) {
        var ctx = canvas.getContext("2d");
      }



    //setando cor do rack
    ctx.strokeStyle = '#222';
    ctx.fillStyle = '#222';

    //desenhando topo
    var xTopInitial = xinitial - sideWidth;
    var yTopInitial = yinitial - slotHeigth;

    ctx.strokeRect(xTopInitial, yTopInitial, slotWidth + 2*sideWidth, slotHeigth);
    ctx.fillRect(xTopInitial, yTopInitial, slotWidth + 2*sideWidth, slotHeigth);

    //desenhando laterais
    ctx.strokeRect(xinitial - sideWidth,yinitial, sideWidth, slotHeigth*slotAmount);
    ctx.strokeRect(xinitial + slotWidth,yinitial, sideWidth, slotHeigth*slotAmount);
    ctx.fillRect(xinitial - sideWidth,yinitial, sideWidth, slotHeigth*slotAmount);
    ctx.fillRect(xinitial + slotWidth,yinitial, sideWidth, slotHeigth*slotAmount);

    //desenhando esqueleto do rack
    for (i=0; i<slotAmount; i++) {
      ctx.strokeRect(xinitial, yinitial + slotHeigth*i, slotWidth, slotHeigth);

    }

    //numeração
    ctx.fillStyle = 'white';
    for (i=0; i<slotAmount; i++) {
      ctx.fillText((slotAmount+1)-i-1, xinitial - 12, yinitial + slotHeigth*(i+1) - 3);
    }
    //numero do rack
    ctx.font = 'bold 14px Helvetica'
    ctx.fillText(rackNumber.toUpperCase(), xTopInitial + sideWidth + slotWidth/2 - 6, yTopInitial + slotHeigth - 4);
}




function drawServer(server) {

    var canvas = document.getElementById("canvas");
      if (canvas.getContext) {
        var ctx = canvas.getContext("2d");
      }


   //definindo altura do servidor
   if (server['posicao'].length == 2) {
     var serverHeight = server['posicao'][1] - server['posicao'][0] + 1;

     //invertendo posição no rack (rack de cabeça pra baixo!!!)
     var aux = server['posicao'][0];
     server['posicao'][0] = (slotAmount+1) - server['posicao'][1]
     server['posicao'][1] = (slotAmount+1) - aux


   } else {
     //invertendo posicao no rack
     server['posicao'][0] = (slotAmount+1) - server['posicao'][0]

     var serverHeight = 1;
   }

  //definindo cor pelo fabricante
   if (server['fabricante'] == 'DELL') {
     ctx.fillStyle = cor_dell;
   } else if (server['fabricante'] == 'HP'){
     ctx.fillStyle = cor_hp;
   } else if (server['fabricante'] == 'CISCO') {
     ctx.fillStyle = cor_cisco;
   } else if (server['fabricante'] == 'BROCADE') {
       ctx.fillStyle = cor_brocade;
   } else if (server['fabricante'] == 'SUPERMICRO') {
       ctx.fillStyle = cor_supermicro;
   }


  ctx.fillRect(xinitial, yinitial + (server['posicao'][0]-1)*slotHeigth, slotWidth, serverHeight*slotHeigth);
  //desenhando contorno do servidor
  ctx.strokeStyle = '#222';
  ctx.strokeRect(xinitial, yinitial + (server['posicao'][0]-1)*slotHeigth, slotWidth, serverHeight*slotHeigth);



  //colcocando informação
  putInfo(server);

   //indicador de ligado ou desligado
  if (server.em_uso == 'S') {
    ctx.fillStyle = 'LimeGreen';
    ctx.strokeStyle = 'LimeGreen';
  } else if(server.em_uso == 'N') {
    ctx.fillStyle = 'red';
    ctx.strokeStyle = 'red';
  }


  ctx.beginPath();
  ctx.arc(xinitial + slotWidth - 4, yinitial + (server['posicao'][0]-1)*slotHeigth + 4, 2, 0, Math.PI*2);
  ctx.stroke();
  ctx.fill();

}

function putInfo(server) {
  var canvas = document.getElementById("canvas");


  //definindo altura do servidor
  if (server['posicao'].length == 2) {
    var serverHeight = server['posicao'][1] - server['posicao'][0] + 1;
  } else {
    var serverHeight = 1;
  }


  if (canvas.getContext) {
    var ctx = canvas.getContext("2d");
  }

  ctx.font = '13px Helvetica';
  ctx.textAlign = "center";

  //var xaddition = slotWidth/2 - server['serial'].length/2*8;
  ctx.fillStyle = '#222';
  if ((server['hostname'] != 'None') && (server['hostname'] != ' ') && (server['hostname'] != '-')) {
    ctx.fillText(server['hostname'], xinitial + slotWidth/2, yinitial + (server['posicao'][0]-1)*slotHeigth + slotHeigth*serverHeight/2 + 12/2);
  } else {
    ctx.fillText(server['serial'], xinitial + slotWidth/2, yinitial + (server['posicao'][0]-1)*slotHeigth + slotHeigth*serverHeight/2 + 12/2);
  }


}

function roundedRect(ctx,x,y,width,height,radius,strokeColor,fillColor){
  ctx.beginPath();
  ctx.moveTo(x,y+radius);
  ctx.lineTo(x,y+height-radius);
  ctx.quadraticCurveTo(x,y+height,x+radius,y+height);
  ctx.lineTo(x+width-radius,y+height);
  ctx.quadraticCurveTo(x+width,y+height,x+width,y+height-radius);
  ctx.lineTo(x+width,y+radius);
  ctx.quadraticCurveTo(x+width,y,x+width-radius,y);
  ctx.lineTo(x+radius,y);
  ctx.quadraticCurveTo(x,y,x,y+radius);
  ctx.strokeStyle = strokeColor;
  ctx.stroke();
  ctx.fillStyle = fillColor;
  ctx.fill();
}

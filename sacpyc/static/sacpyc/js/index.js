document.getElementById('np').className="btn btn-default active";
botonMenu('coffe-break');
function botonMenu(id){
	document.getElementById('coffe-break').style.display='none';
	document.getElementById('catering').style.display='none';
	document.getElementById('cumpleano').style.display='none';
	document.getElementById('cena').style.display='none';
	document.getElementById('matrimonio').style.display='none';
	document.getElementById(id).style.display='block';
}
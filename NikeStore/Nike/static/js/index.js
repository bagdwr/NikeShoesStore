let btn=document.getElementsByClassName('burgerMenu');
for(let i=0; i<btn.length; i++){
	btn[i].addEventListener('click',function(){
        let cont=document.getElementById('navUlID');
        if (cont.getAttribute('id')=='navUlID') {
        	  if (cont.style.maxHeight) {
                cont.style.maxHeight=null;

           }else{
             	cont.style.maxHeight=200+'px';
           }
        }
	});
}


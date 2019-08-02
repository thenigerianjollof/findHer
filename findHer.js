/*carousel();
function carousel(){
  var y;
  var t =document.getElementsByClassname("theSlides");
  for (y=0; y < t.length; i++) {
    t[y].style.display = "none";
  }
  index++;
  if (index > t.length) {index=1}
  x[index-1].style.display = "block";
  setTimeout(carousel,2000); //change image evry 2 seconds
}*/


function scrollabout(){
  var yay = document.getElementById('about');
  yay.scrollIntoView();
}

function scrollconsider(){
  var yay = document.getElementById('forfuture');
  yay.scrollIntoView();
}

function scrollpartner(){
  var yay = document.getElementById('partner');
  yay.scrollIntoView();
}


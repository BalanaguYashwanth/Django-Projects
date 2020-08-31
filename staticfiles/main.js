var slideIndex = 0;
showSlides();

function showSlides() {
  var i;
  var slides = document.getElementsByClassName("mySlides");
  var dots = document.getElementsByClassName("dot");
  for (i = 0; i < slides.length; i++) {
    slides[i].style.display = "none";  
  }
  slideIndex++;
  if (slideIndex > slides.length) {slideIndex = 1}    
  for (i = 0; i < dots.length; i++) {
    dots[i].className = dots[i].className.replace(" active", "");
  }
  slides[slideIndex-1].style.display = "block";  
  dots[slideIndex-1].className += " active";
  setTimeout(showSlides, 2000); // Change image every 2 seconds
}

const menuBtn = document.querySelector(".menu-icon span");
const searchBtn = document.querySelector(".search-icon");
const cancelBtn = document.querySelector(".cancel-icon");
const items = document.querySelector(".nav-items");
const form = document.querySelector("form");
menuBtn.onclick = ()=>{
  items.classList.add("active");
  menuBtn.classList.add("hide");
  searchBtn.classList.add("hide");
  cancelBtn.classList.add("show");
}
cancelBtn.onclick = ()=>{
  items.classList.remove("active");
  menuBtn.classList.remove("hide");
  searchBtn.classList.remove("hide");
  cancelBtn.classList.remove("show");
  form.classList.remove("active");
  cancelBtn.style.color = "#ff3d00";
}
searchBtn.onclick = ()=>{
  form.classList.add("active");
  searchBtn.classList.add("hide");
  cancelBtn.classList.add("show");
}



function orderpost()
{
  xmlhttp = new XMLHttpRequest();
  xmlhttp.onreadystatechange=function()
  {
    if(xmlhttp.readyState==4 && xmlhttp.status==200)
    {
       document.getElementById("posting").innerHTML=xmlhttp.responseText;
    }
  }
   
  var orderdatas={
    "name": document.getElementById("name").value,
    "item": document.getElementById("item").value,
    "time": document.getElementById("time").value,
  }

  xmlhttp.open("POST","http://127.0.0.1:8000/api/v1/orderdetailed/",true);
  xmlhttp.setRequestHeader("Content-type","application/json");
  xmlhttp.setRequestHeader("X-CSRFToken", csrfcookie());
  xmlhttp.send(JSON.stringify(orderdatas));
   
}


function contactpost()
{
  xmlhttp = new XMLHttpRequest();
  xmlhttp.onreadystatechange=function()
  {
    if(xmlhttp.readyState==4 && xmlhttp.status==200)
    {
       document.getElementById("posting").innerHTML=xmlhttp.responseText;
    }
  }
   
  var contactdatas={
    "person": document.getElementById("person").value,
    "place": document.getElementById("place").value,
    "phone": document.getElementById("phone").value,
    "email": document.getElementById("email").value,
  }

  xmlhttp.open("POST","http://127.0.0.1:8000/api/v1/detailed/",true);
  xmlhttp.setRequestHeader("Content-type","application/json");
  xmlhttp.setRequestHeader("X-CSRFToken", csrfcookie());
  xmlhttp.send(JSON.stringify(contactdatas));
   
}






function slidechange()
{
    xmlhttp= new XMLHttpRequest();
    xmlhttp.onreadystatechange=function()
    {
        if(xmlhttp.readyState==4 && xmlhttp.status==200)
          {
            var xdata=JSON.parse(xmlhttp.responseText);       
            for(var obj in xdata)
            {
              var divdata = document.createElement("div");
              divdata.setAttribute("class","mySlides fade");
                
              var divtext = document.createElement("div");
               divtext.setAttribute("class","text");
               divtext.innerHTML+= xdata[obj].sname;
               divdata.appendChild(divtext);
                
                var imgslide=document.createElement("img");
                imgslide.setAttribute('alt','slideimage');
                imgslide.setAttribute('src',xdata[obj].sfile);
                imgslide.setAttribute('style','width:100%');
                divdata.appendChild(imgslide);
                document.getElementById("slidediv").appendChild(divdata);


                var dotspan =document.createElement("span");
                dotspan.setAttribute('class','dot');
                document.getElementById("dotdiv").appendChild(dotspan);   
            }
        }
    }
    xmlhttp.open("GET","http://127.0.0.1:8000/api/v1/slidedatadetailed/",true);
    xmlhttp.setRequestHeader("Content-type","application/json");
    xmlhttp.setRequestHeader("X-CSRFToken",csrfcookie());
    xmlhttp.send();
}


function change()
{
    xmlhttp1= new XMLHttpRequest();
    xmlhttp1.onreadystatechange=function()
    {
        if(xmlhttp1.readyState==4 && xmlhttp1.status==200)
          {
            var x=JSON.parse(xmlhttp1.responseText);       
            for(var obj in x)
            {
              var mydiv = document.createElement("div");
              mydiv.setAttribute("class","column");

                var img=document.createElement("img");
                img.setAttribute('class','image');
                img.setAttribute('alt','image');
                img.setAttribute('src',x[obj].myfile);
                img.setAttribute('style','width:100%');
                
                mydiv.appendChild(img);
                document.getElementById("row").appendChild(mydiv);

            }
        }
    }
    xmlhttp1.open("GET","http://127.0.0.1:8000/api/v1/filesdatadetailed/",true);
    xmlhttp1.setRequestHeader("Content-type","application/json");
    xmlhttp1.setRequestHeader("X-CSRFToken", csrfcookie());
    xmlhttp1.send();
}


function loaddata()
{
  slidechange();
  change();
 
} 



var csrfcookie = function() {
  var cookieValue = null,
      name = 'csrftoken';
  if (document.cookie && document.cookie !== '') {
      var cookies = document.cookie.split(';');
      for (var i = 0; i < cookies.length; i++) {
          var cookie = cookies[i].trim();
          if (cookie.substring(0, name.length + 1) == (name + '=')) {
              cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
              break;
          }
      }
  }
  return cookieValue;
};




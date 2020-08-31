
// function change1()
// {
//     xmlhttp=new XMLHttpRequest();

//     xmlhttp.onreadystatechange=function()
//     {
//      if(xmlhttp.readyState==4 && xmlhttp.status==200)
//       {
//         //document.getElementById("status").innerHTML="";
//         var x=JSON.parse(xmlhttp.responseText);
//         for(var obj in x)
//         {
//             var img=document.createElement('IMG');
//             img.setAttribute('src',x[obj].myfile);
//             img.setAttribute('width','304');
//             img.setAttribute('heigth','228');
//             document.getElementById("mydiv").appendChild(img);
//             var br = document.createElement("br");
//             document.getElementById("mydiv").appendChild(br);
//             var br = document.createElement("br");
//             document.getElementById("mydiv").appendChild(br);

//             document.getElementById("status").innerHTML +=x[obj].myfile+"<br>";
//         }
//       }
//     }
//     xmlhttp.open("GET","http://127.0.0.1:8000/api/v1/filesdatadetailed/",true);
//     xmlhttp.send();
// } 


const inpFile =document.getElementById("file");
const previewContainer=document.getElementById("imagePreview");
const previewImage=previewContainer.querySelector('.image-preview__image');
const previewDefaultText=previewContainer.querySelector(".image-preview__default-text");

  function posting()
  {

      const img = document.getElementById("file").files[0];
      if(img)
      {
          const reader = new FileReader();
          previewDefaultText.style.display="none";
          previewImage.style.display="block";

          reader.addEventListener("load",function(){
          const photo=document.getElementById("preview");
          previewImage.setAttribute("src",this.result);

         value={
            "sfile":(this.result),
            "sname":document.getElementById("name").value,
            }
            
              
              var xmlhttp=new XMLHttpRequest();
              xmlhttp.onreadystatechange=function()
              {   
                 document.getElementById("status1").innerHTML= xmlhttp.responseText;
              }
                xmlhttp.open("POST","https://getfertilizeritems.herokuapp.com/api/v1/slidedatadetailed/");
                xmlhttp.setRequestHeader("Content-type","application/json");
                xmlhttp.setRequestHeader("X-CSRFToken", csrfcookie());
                xmlhttp.send(JSON.stringify(value));
     
          });
          reader.readAsDataURL(img);
          timeFunction()

       
      }
      
      else{
          document.getElementById("error").innerHTML="<h1>Error Found when uploading the image Please Check<h1>";
      }
  }



  function timeFunction() {
    setTimeout(function(){ location.reload(); alert("successfully added the photo"); }, 3000);
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
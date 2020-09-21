
function change()
{
    xmlhttp= new XMLHttpRequest();
    xmlhttp.onreadystatechange=function()
    {
        document.getElementById("data").innerHTML="";                                                

        if(xmlhttp.readyState==4 && xmlhttp.status==200)
          {
            var x=JSON.parse(xmlhttp.responseText);
            var table=document.getElementById("mytable")
            for(var obj in x)
            {
                var row=table.insertRow();
                var cell1=row.insertCell();
                var cell2=row.insertCell();
                var cell3=row.insertCell();
                var cell4=row.insertCell();
             
                cell1.innerHTML+=x[obj].id;
                cell2.innerHTML+=x[obj].myname;

                var img=document.createElement("img");
                img.setAttribute('src',x[obj].myfile);
                img.setAttribute('width','450');
                img.setAttribute('heigth','228');
                cell3.appendChild(img);
              
                
                var btn=document.createElement("button");
                btn.setAttribute("onclick","todo(this.id)");
                btn.setAttribute("id",x[obj].id);
                btn.innerHTML="Delete";
                cell4.appendChild(btn);
                 var space=document.createTextNode("  ");
                 cell4.appendChild(space);
                var btn=document.createElement("button");
                btn.setAttribute("id",x[obj].id);
                btn.setAttribute("name",obj);
                btn.setAttribute("onclick","update(this.id,this.name)");
                btn.innerHTML="Update";
                cell4.appendChild(btn);

            }
        }
    }
    xmlhttp.open("GET","https://getfertilizeritems.herokuapp.com/api/v1/filesdatadetailed/",true);
    xmlhttp.setRequestHeader("X-CSRFToken", csrfcookie());
    xmlhttp.send();
}

function todo(id)
{
    Delete(id);
    location.reload();
}

var array=[];

function update(id,name)
{
    if(!array.includes(id) && array.length<1)
    {   
    alert("Allow to update the values of id  "+id);
    array.push(id);
    var table=document.getElementById("mytable");
    var row=table.insertRow(parseInt(name)+2);
    var cell1=row.insertCell();
    var cell2=row.insertCell();
    var cell3=row.insertCell();
    var cell4=row.insertCell();
    

    cell1.innerHTML=id;
    cell1.setAttribute("id","id1");

    var input = document.createElement("input");
    input.setAttribute("id","name1");
    cell2.append(input);

    var input = document.createElement("input");
    input.setAttribute("type","file");
    input.setAttribute("id","file1");
    cell3.append(input);
    
    var btn1 = document.createElement("button");
    btn1.innerHTML="Submit";
    btn1.setAttribute('onclick',"put('id1','name1','file1')");
    cell4.appendChild(btn1);

    var space=document.createTextNode(" ");
    cell4.appendChild(space);

    var btn2=document.createElement("button");
    btn2.innerHTML="Cancel";
    btn2.setAttribute("onclick","cancel("+name+","+id+")");
    cell4.appendChild(btn2);
   
    }
}



function cancel(name,id)
{
    var i = array.indexOf(id);
    array.splice(i, 1); 
    document.getElementById("mytable").deleteRow(parseInt(name)+2);    
}


function put(id,name,file)
{
    var getid=document.getElementById(id).innerHTML;
    var getname = document.getElementById(name).value;
    var getimage = document.getElementById(file).files[0];

    if(getimage)
      {
          const reader = new FileReader();
          reader.addEventListener("load",function(){
          
              var updatedata= {
                    "id": getid,
                    "myname": getname,
                    "myfile": (this.result),
                    }

         
    xmlhttp = new XMLHttpRequest();
    xmlhttp.onreadystatechange=function()
    {
        if(xmlhttp.readyState==4 && xmlhttp.status==200)
        {
          //  document.getElementById("status").innerHTML=JSON.parse(xmlhttp.reponseText);
        }
    }


    xmlhttp.open("PUT","https://getfertilizeritems.herokuapp.com/api/v1/filesdataMoredetail/"+getid+"/",true);
    xmlhttp.setRequestHeader("Content-type","application/json");
    xmlhttp.setRequestHeader("X-CSRFToken", csrfcookie());
    console.log(JSON.stringify(updatedata));
    xmlhttp.send(JSON.stringify(updatedata));
    location.reload();
   })
   reader.readAsDataURL(getimage);
  }
    
 else{
        document.getElementById("status").innerHTML="error";
    }


}


function Delete(id)
{
    alert("the data of  " +id+"  id is deleting");
    xmlhttp=new XMLHttpRequest();
    xmlhttp.onreadystatechange=function()
    {
        document.getElementById("mydelete").innerHTML=xmlhttp.reponseText;
    }
    xmlhttp.open("DELETE","https://getfertilizeritems.herokuapp.com/api/v1/filesdataMoredetail/"+id+"/",true);
    xmlhttp.setRequestHeader("Content-type","application/json");
    xmlhttp.setRequestHeader("X-CSRFToken", csrfcookie());
    xmlhttp.send();
    
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



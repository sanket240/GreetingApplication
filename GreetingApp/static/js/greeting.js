function validateform(){
  var name=document.form.name.value;
  var msg=document.form.msg.value;
  if (name==null || name==""){
    alert("Name field can't be empty");
    return false;
  }else if(msg==null|| msg==""){
    alert("Message field can't be empty!");
    return false;
    }
  }



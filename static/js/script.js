function send(endpoint) {

  let name = document.getElementById("name").value;
  let subject = document.getElementById("subject").value;
  let post = document.getElementById("para").value;

  $.post(endpoint, 
  {
    name: name,
    subject: subject,
    post: post

  }).done( function (){
    window.location.href = endpoint;
  })
  
}
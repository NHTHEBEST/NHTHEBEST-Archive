function myFunction() {
  var x = document.getElementById("navDemo");
  if (x.className.indexOf("w3-show") == -1) {
    x.className += " w3-show";
  } else { 
    x.className = x.className.replace(" w3-show", "");
  }
}



function update_search(){
// Get the <datalist> and <input> elements.
var dataList = document.getElementById('json-datalist');
var input = document.getElementById('ajax');
var data = input.value;

// check length
if (data.length <= 4){return}


// Create a new XMLHttpRequest.
var request = new XMLHttpRequest();

// Handle state changes for the request.
request.onreadystatechange = function(response) {
  if (request.readyState === 4) {
    if (request.status === 200) {

      dataList.innerHTML = request.responseText;
    } 
  }
};
var url = '/searchin/'
// Update the placeholder text
url = url.concat(data)
console.log(url);
// Set up and make the request.
request.open('GET', url, true);
request.send();
}
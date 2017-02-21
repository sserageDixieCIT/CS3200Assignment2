// var request = new XMLHttpRequest();
//
// request.onreadystatechange(function ()){
//   if (request.readyState == XMLHttpRequest.DONE){
//     if (request.status >= 200 && request.stat < 400) {
//       console.log("SUCCESS");
//     } else {
//       console.error("FAILURE")
//     }
//   }
// };
//
// // function () {
// //   if (request.readyState == XMLHttpRequest.DONE) {
// //     console.log("SUCCESS");
// //   } else {
// //     console.error("FAILURE");
// //   }
// // }
//
// request.open("POST", "http://localhost8080/plants");
// var v =
var items = null;
var itemList = document.getElementById("my-item-list");

var displayDataFromServer = function(){
  request.onreadystatechange = function() {
    if (request.readyState == XMLHttpRequest.DONE) {
      if (request.status >= 200 && request.status < 400) {
        console.log("displayed data");
        itemList.innerHTML = "";
        items = JSON.parse(request.responseText);
        for(i = 0; i < items.length; i++){
          var newListItem = document.createElement("li");
          newListItem.innerHTML = items[i];
          itemList.appendChild(newListItem);
        }
        console.log(request.responseText)

      } else {
        console.error("that didn't work...");
      }
    }
  };
  request.open("GET", "http://localhost:8080/items");
  request.send();
};

var sendDataToServer = function(){
  var request = new XMLHttpRequest();

  request.onreadystatechange = function() {
    if (request.readyState == XMLHttpRequest.DONE) {
      if (request.status >= 200 && request.status < 400) {
        console.log("sent data");
      } else {
        console.error("that didn't work...");
      }
    }
  };
  var userInput = document.getElementById("question");
  var inputValue = userInput.value;
  var data = "item=" + encodeURIComponent(inputValue);

  request.open("POST", "http://localhost:8080/items");
  request.send(data);
}

var myButton = document.getElementById("my-button");
myButton.onclick = function() {
  console.log("the button was clicked!")
  sendDataToServer()

  displayDataFromServer()
};


var request = new XMLHttpRequest();
request.onreadystatechange = function () {
  if (request.readyState == XMLHttpRequest.DONE) {
    if (request.status == 200) {
      console.log("hey, something worked...");
      items = JSON.parse(request.responseText);
      console.log(request.responseText);
      console.log(items);
      displayDataFromServer();
    } else {
      console.error("that didn't work...");
    }
  }
};

request.open("GET", "http://localhost:8080/items");
request.send();

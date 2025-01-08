/*
  your PPTASK:
  
  First, familiarize yourself with the given html file for this work.

      then...

  Test drive each bit of code in this file,
  and insert comments galore, indicating anything
  you discover,
  have questions about,
  or otherwise deem notable.

  Have the given html file open as you work.
  
  Write with your future self or teammates in mind.
  
  If you find yourself falling out of flow mode, consult 
  - other teams
  - MDN

  A few comments have been pre-filled for you...
  
  (delete this block comment once you are done)
*/





// Team TJMax :: Tracy Ye, Jessica Yu
// SoftDev pd5
// K28 -- Manipulating the DOM
// 2025-01-07t
// --------------------------------------------------


//send diagnostic output to console
//(Ctrl-Shift-K in Firefox to reveal console)
console.log("AYO");

var i = "hello";
var j = 20;


//assign an anonymous fxn to a var
var f = function(x)			// printing will open debugger and highlight this function
{
    var j=30;
    return j+x;
};


//instantiate an object			the clickdown for o is populated with this information
var o = { 'name' : 'Thluffy',
          age : 1024,
          items : [10, 20, 30, 40],
          morestuff : {a : 1, b : 'ayo'},
          func : function(x) {
              return x+30;
          }
        };

//create a new node in the tree
var addItem = function(text)		// --> adds the new string to the list
{
    var list = document.getElementById("thelist");
    var newitem = document.createElement("li");
    newitem.innerHTML = text;
    list.appendChild(newitem);
};

//prune a node from the tree
var removeItem = function(n)		// --> removes the list element
{
    var listitems = document.getElementsByTagName('li');		// compiles a list of every 'li', meaning you can 
    listitems[n].remove();										// remove from other lists too by increasing index
};

//color selected elements red
var red = function()		// if the element does not already have a red class, appends
{
    var items = document.getElementsByTagName("li");
    // console.log(items)
    for(var i = 0; i < items.length; i++) {
	items[i].classList.add('red');
    }
    // console.log(items)
};

//color a collection in alternating colors
var stripe = function()
{
    var items = document.getElementsByTagName("li");
    for(var i = 0; i < items.length; i++) {
	if (i%2==0) {
	    items[i].classList.add('red');
	} else {
	    items[i].classList.add('blue');
	}
    }
};


//insert your implementations here for...
// FIB
var fib = function(n){
  if(n == 0){
    return 0;
  }
    if(n == 1){
    return 1;
  }
  return fib(n-1)+fib(n-2);
}; 
// FAC
var fact = function(n){
  if(n == 1){
    return 1;
  }
    return (n*fact(n-1));
};
// GCD
var GCD = function(n1, n2){
  if (n1 <= n2) {
    var min = n1;
    var max = n2;
  }
  else {
    var min = n2;
    var max = n1;
  }
  for (var i = min; i > 0; i--) {
    if (min%i == 0 && max%i == 0) {
      return i;
    }
  }
  return 1;
};

// In addition to the style shown above,
//  you are encouraged to test drive the "arrow function syntax" as shown below.
//  Note anything notable.
const myFxn = (param1, param2) => {
    var retVal = "do cats like humans as much as humans like cats?"
    if (param1 > param2) {
        console.log("The magic 8 ball says: alas, they do not");
    }
    else { console.log("The magic 8 ball says: of course!"); }
    return retVal;
};
        // no body --> retVal not defined error
        // nothing ever requires the parameters to be filled out.... which is annoying that it still runs

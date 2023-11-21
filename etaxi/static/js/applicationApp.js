const bodynovalid = document.querySelector("body");
const headernovalid = document.querySelector("#header-section");


function showShadow() {
   headernovalid.style.position = "relative";
   headernovalid.style.backgroundColor =  'rgba(0, 0, 0, 0.01)';
   bodynovalid.style.backgroundColor =  'rgba(0, 0, 0, 0.1)';
 }

showShadow();


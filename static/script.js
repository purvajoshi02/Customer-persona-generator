document.addEventListener("DOMContentLoaded",()=>{

const form=document.querySelector("form");

const loading=document.getElementById("loading");

const result=document.getElementById("result");

form.addEventListener("submit",()=>{

result.style.display="none";

loading.style.display="flex";

});

});
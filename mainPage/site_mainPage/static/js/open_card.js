function openForm() {
  document.getElementById("order_Form").style.display = "block";
  document.getElementById("blur_time").style.filter = "blur(10px)";
  document.getElementById('blur_time').style.pointerEvents = 'none';
}

function closeForm() {
  document.getElementById("order_Form").style.display = "none";
  document.getElementById("blur_time").style.filter = "blur(0px)";
  document.getElementById('blur_time').style.pointerEvents = 'auto';
}
function openForm_menu() {
  document.getElementById("myForm").style.display = "block";
  document.getElementById("blur_time").style.filter = "blur(10px)";
  document.getElementById('blur_time').style.pointerEvents = 'none';
}

function closeForm_menu() {
  document.getElementById("myForm").style.display = "none";
  document.getElementById("blur_time").style.filter = "blur(0px)";
  document.getElementById('blur_time').style.pointerEvents = 'auto';
}
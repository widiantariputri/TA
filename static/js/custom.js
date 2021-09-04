// Handling bobot form
const bobot = document.querySelectorAll("#bobot");
const sub = document.querySelectorAll("#sub");
sub[0].style.display = "none";

function toggleSub() {
  sub[0].style.display = "block";
  bobot[0].style.display = "none";
}

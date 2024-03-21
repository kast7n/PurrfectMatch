window.onload = function () {
  changeImg();
};

var i = 0;
var images = [];

images[0] = "imgs/Pets/Dogs/goldebBud.jpg";
images[1] = "imgs/Pets/Cats/hitlerCat.jpg";
images[2] = "imgs/Pets/Cats/bingus.jpg";
images[3] = "imgs/Pets/Others/froufrou.jpg";
function changeImg() {
  document.getElementsByClassName("returns")[0].src = images[i];
  console.log(i);
  if (i < images.length - 1) {
    i++;
  } else {
    i = 0;
  }
  setTimeout(changeImg, 3000);
}

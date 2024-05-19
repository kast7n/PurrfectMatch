window.onload = function () {
  changeImg();
  console.log("teststs")
};

var i = 0;
var images = [];

images[0] = "static/imgs/Pets/Dogs/goldebBud.jpg";
images[1] = "static/imgs/Pets/Cats/hitlerCat.jpg";
images[2] = "static/imgs/Pets/Cats/bingus.jpg";
images[3] = "static/imgs/Pets/Others/froufrou.jpg";
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

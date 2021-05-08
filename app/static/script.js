function init() {
  scroll();
  dropMenu();
  titleParallax();
  setInterval(animate, 2000);
}

function scroll() {
  let progress = document.getElementById("progressbar");
  let totalHeight = document.body.scrollHeight - window.innerHeight;
  window.onscroll = function () {
    progress.style.height = (window.pageYOffset / totalHeight) * 100 + "%";
  };
}

function dropMenu() {
  $(document).ready(function () {
    $(".menu-toggle").click(function () {
      $("nav").toggleClass("active");
    });
  });
}

function titleParallax() {
  $("body").mousemove(function (e) {
    var valueX = (e.pageX * -1) / 75;
    var valueY = (e.pageY * -1) / 75;

    $("#title").css({
      transform: "translate(" + valueX + "px," + valueY + "px)",
    });
  });
}

function animate() {
  $("#animate-1").html(
    '<img class="diagram" src="{{ url_for("static", filename="diagrams/Diagram_1.1.png") }}">' );
  setTimeout(function() {$("#animate-1").html(
    '<img class="diagram" src="{{ url_for("static", filename="diagrams/Diagram_1.2.png") }}">')}, 1000);
}
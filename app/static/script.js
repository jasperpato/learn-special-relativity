function init() {
	scroll();
	dropMenu();
	titleParallax();
	setInterval(animate, 1000);
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
	// animation 1 in lesson-2
	if ($("#animate-1").find("img")[0].id == "img-1") {
		$("#animate-1").find("img")[0].id = "img-2";
		$("#animate-1").find("img")[0].src = "/static/diagrams/Diagram_1.2.png";
	} else {
		$("#animate-1").find("img")[0].id = "img-1";
		$("#animate-1").find("img")[0].src = "/static/diagrams/Diagram_1.1.png";
	}
}

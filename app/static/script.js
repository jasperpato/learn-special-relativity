function init() {
	scroll();
	dropMenu();
	titleParallax();
	setInterval(animate, 1500);

	$("#prev-2").click({ param1: "2" }, loadPrevPage);
	$("#next-2").click({ param1: "2" }, loadNextPage);
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
	// animation 1
	if ($("#animate-1").find("img")[0].id == "img-1.1") {
		$("#animate-1").find("img")[0].id = "img-1.2";
		$("#animate-1").find("img")[0].src = "/static/diagrams/Diagram_1.2.png";
	} else {
		$("#animate-1").find("img")[0].id = "img-1.1";
		$("#animate-1").find("img")[0].src = "/static/diagrams/Diagram_1.1.png";
	}

	// animation 2
	if ($("#animate-2").find("img")[0].id == "img-2.1") {
		$("#animate-2").find("img")[0].id = "img-2.2";
		$("#animate-2").find("img")[0].src = "/static/diagrams/Diagram_2.2.png";
	} else if ($("#animate-2").find("img")[0].id == "img-2.2") {
		$("#animate-2").find("img")[0].id = "img-2.3";
		$("#animate-2").find("img")[0].src = "/static/diagrams/Diagram_2.3.png";
	} else {
		$("#animate-2").find("img")[0].id = "img-2.1";
		$("#animate-2").find("img")[0].src = "/static/diagrams/Diagram_2.1.png";
	}
}

function loadPrevPage(lnum) {
	let lid = "#l" + lnum.data.param1;
	if ($(lid + "2").is(":visible")) {
		$("#prev-" + lnum.data.param1).toggle();
		$(lid + "2").toggle();
		$(lid + "1").toggle();
	} else if ($(lid + "3").is(":visible")) {
		$(lid + "3").toggle();
		$(lid + "2").toggle();
	} else if ($(lid + "4").is(":visible")) {
		$("#next-" + lnum.data.param1).toggle();
		$("#go-test-" + lnum.data.param1).toggle();
		$(lid + "4").toggle();
		$(lid + "3").toggle();
	}
}

function loadNextPage(lnum) {
	let lid = "#l" + lnum.data.param1;
	if ($(lid + "1").is(":visible")) {
		$("#prev-" + lnum.data.param1).toggle();
		$(lid + "1").toggle();
		$(lid + "2").toggle();
	} else if ($(lid + "2").is(":visible")) {
		$(lid + "2").toggle();
		$(lid + "3").toggle();
	} else if ($(lid + "3").is(":visible")) {
		$("#next-" + lnum.data.param1).toggle();
		$("#go-test-" + lnum.data.param1).toggle();
		$(lid + "3").toggle();
		$(lid + "4").toggle();
	}
}

function init() {
	scroll();
	dropMenu();
	titleParallax();
	setInterval(animate, 1500);
	$("#prev-2").click(loadPrevPage2);
	$("#next-2").click(loadNextPage2);
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

function loadPrevPage2() {
	if ($("#l22").is(":visible")) {
		$("#prev-2").toggle();
		$("#l22").toggle();
		$("#l21").toggle();
	} else if ($("#l23").is(":visible")) {
		$("#l23").toggle();
		$("#l22").toggle();
	} else if ($("#l24").is(":visible")) {
		$("#next-2").toggle();
		$("#l24").toggle();
		$("#l23").toggle();
	}
}

function loadNextPage2() {
	if ($("#l21").is(":visible")) {
		$("#prev-2").toggle();
		$("#l21").toggle();
		$("#l22").toggle();
	} else if ($("#l22").is(":visible")) {
		$("#l22").toggle();
		$("#l23").toggle();
	} else if ($("#l23").is(":visible")) {
		$("#next-2").toggle();
		$("#go-test-2").show();
		$("#l23").toggle();
		$("#l24").toggle();
	}
}

function init() {
	scroll();
	dropMenu();
	titleParallax();
	setInterval(animate, 1500);

	$("#prev-2").click({ lNum: "2", numPages: 4 }, loadPrevPage);
	$("#next-2").click({ lNum: "2", numPages: 4 }, loadNextPage);
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

function loadPrevPage(lessonData) {
	let lNum = lessonData.data.lNum;
	let numPages = lessonData.data.numPages;
	let lid = "#l" + lNum;

	for (p = 2; p <= numPages; ++p) {
		if (p == 2) $("#prev-" + lNum).toggle();
		if (p == numPages) {
			$("#next-" + lNum).toggle();
			$("#go-test-" + lNum).toggle();
		}
		$(lid + p).toggle();
		$(lid + (p - 1)).toggle();
	}
}

function loadNextPage(lessonData) {
	let lNum = lessonData.data.lNum;
	let numPages = lessonData.data.numPages;
	let lid = "#l" + lNum;

	for (p = 1; p < numPages; ++p) {
		if (p == 1) $("#prev-" + lNum).toggle();
		if (p == numPages - 1) {
			$("#next-" + lNum).toggle();
			$("#go-test-" + lNum).toggle();
		}
		$(lid + p).toggle();
		$(lid + (p + 1)).toggle();
	}
}

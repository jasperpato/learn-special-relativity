function init() {
	scroll();
	dropMenu();
	titleMove();
	setInterval(animations, 1500);

	$("#prev-1").click({ lessonNum: "1", numPages: 2 }, loadPrevPage);
	$("#next-1").click({ lessonNum: "1", numPages: 2 }, loadNextPage);
	$("#prev-2").click({ lessonNum: "2", numPages: 4 }, loadPrevPage);
	$("#next-2").click({ lessonNum: "2", numPages: 4 }, loadNextPage);
	$("#prev-3").click({ lessonNum: "3", numPages: 3 }, loadPrevPage);
	$("#next-3").click({ lessonNum: "3", numPages: 3 }, loadNextPage);

	$(".logo").click(function () {
		window.location.href = "http://127.0.0.1:5000";
	});

	$(".pageArrowLeftLabel").click(function () {
		hr = window.location.href;
		window.location.href = hr.slice(0, hr.length - 1) + (parseInt(hr[hr.length - 1]) - 1);
	});

	$(".pageArrowRightLabel").click(function () {
		hr = window.location.href;
		window.location.href = hr.slice(0, hr.length - 1) + (parseInt(hr[hr.length - 1]) + 1);
	});
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

function titleMove() {
	$("body").mousemove(function (e) {
		var valueX = (e.pageX * -1) / 75;
		var valueY = (e.pageY * -1) / 75;

		$("#title").css({
			transform: "translate(" + valueX + "px," + valueY + "px)",
		});
	});
}

function animations() {
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
	let lessonNum = lessonData.data.lessonNum;
	let numPages = lessonData.data.numPages;
	let pageNum = 1;

	// find visible page
	for (pageNum; pageNum < numPages; ++pageNum) {
		if ($("#l" + lessonNum + pageNum).is(":visible")) break;
	}

	if (pageNum == 1) return;
	if (pageNum == 2) $("#prev-" + lessonNum).toggle();
	if (pageNum == numPages) {
		$("#next-" + lessonNum).toggle();
		//$("#go-test-" + lessonNum).toggle();
	}
	$("#l" + lessonNum + pageNum).toggle();
	$("#l" + lessonNum + (pageNum - 1)).toggle();
}

function loadNextPage(lessonData) {
	let lessonNum = lessonData.data.lessonNum;
	let numPages = lessonData.data.numPages;
	let pageNum = 1;

	// find visible page
	for (pageNum; pageNum < numPages; ++pageNum) {
		if ($("#l" + lessonNum + pageNum).is(":visible")) break;
	}

	if (pageNum == numPages) return;
	if (pageNum == 1) $("#prev-" + lessonNum).toggle();
	if (pageNum == numPages - 1) {
		$("#next-" + lessonNum).toggle();
		//$("#go-test-" + lessonNum).toggle();
	}
	$("#l" + lessonNum + pageNum).toggle();
	$("#l" + lessonNum + (pageNum + 1)).toggle();
}

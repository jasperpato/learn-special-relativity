function init() {
	scroll();
	dropMenu();
	titleMove();

	let hr = window.location.href;
	let title = document.getElementById("title").innerHTML;
	let num = 0;

	if (title.includes("Test") || title.includes("Lesson")) {
		num = parseInt(title[title.length - 1]);

		if (title.includes("Lesson")) {
			let numPages = [2, 4, 3];

			$("#prev").click(function () {
				loadPrevPage(numPages[num - 1]);
			});
			$("#next").click(function () {
				loadNextPage(numPages[num - 1]);
			});

			$(".pageArrowLeftLabel").click(function () {
				window.location.href = hr.slice(0, hr.length - 1) + (num - 1);
			});

			$(".pageArrowRightLabel").click(function () {
				window.location.href = hr.slice(0, hr.length - 1) + (num + 1);
			});

			if (title.includes("Lesson 2")) setInterval(animations, 1500);
		}
		if (title.includes("Test")) {
			document.getElementById("quiz").onsubmit = function () {
				scoreTest(num);
			};
		}
	}

	$(".logo").click(function () {
		window.location.href = "http://127.0.0.1:5000";
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

function loadPrevPage(numPages) {
	let pageNum = 1;

	// find visible page
	for (pageNum; pageNum < numPages; ++pageNum) {
		if ($("#l" + pageNum).is(":visible")) break;
	}

	if (pageNum == 1) return;
	if (pageNum == 2) $("#prev").toggle();
	if (pageNum == numPages) {
		$("#next").toggle();
		//$("#go-test-" + lessonNum).toggle();
	}
	$("#l" + pageNum).toggle();
	$("#l" + (pageNum - 1)).toggle();
}

function loadNextPage(numPages) {
	let pageNum = 1;

	// find visible page
	for (pageNum; pageNum < numPages; ++pageNum) {
		if ($("#l" + pageNum).is(":visible")) break;
	}

	if (pageNum == numPages) return;
	if (pageNum == 1) $("#prev").toggle();
	if (pageNum == numPages - 1) {
		$("#next").toggle();
		//$("#go-test-" + lessonNum).toggle();
	}
	$("#l" + pageNum).toggle();
	$("#l" + (pageNum + 1)).toggle();
}

function scoreTest(testNum) {
	let answers = [
		["B", "A", "B", "B", 4],
		["A", "A", "B", "A", "A"],
		[2, "A", "A", 20, 20],
	];
	console.log("some");

	answers = answers[testNum - 1];

	var score = 0;

	for (var i = 0; i < answers.length; i++) {
		if (getElementById("quiz-" + testNum).elements[i] == answers[i]) {
			console.log(getElementById("quiz-" + testNum).elements[i]);
			score++;
		}
	}
	console.log(score);
}

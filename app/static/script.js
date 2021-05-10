function init() {
	scroll();
	dropMenu();
	titleParallax();
	setInterval(animate, 1500);
	$("#prev").click(loadPrevPage);
	$("#next").click(loadNextPage);
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

function loadContent() {
	let lesson2_1 =
		'<p>\
		Consider an observer who is inside a moving train, and another observer standing stationary outside \
		of the train.\
		<br /><br />\
		Using the theory of special relativity, they can perform many experiments with light waves that show\
		that ‘time’ is flowing at different relative speeds between them.\
		<br /><br />\
		Here is one such experiment. The observer on the train places a mirror flat on the train floor, and\
		flashes a light bulb on the roof of the train such that a light wave travels from the bulb, directly\
		down onto the mirror, and back up to the bulb.\
		<br /><br />\
	</p>\
	<div class="diagramBox" id="animate-1">\
		<img class="diagram" id="img-1" src="/static/diagrams/Diagram_1.1.png" />\
	</div>';

	let lesson2_2 =
		"<p>\
		From the observer inside the train’s perspective, the light travelled directly downwards and then\
		directly upwards. The distance traveled by the light beam is d0=2h, and the speed it travelled at is\
		always constant at c. Using time = distance / speed, the time elapsed for this observer is t0 =\
		2h/c.\
		<br /><br />\
		However the observer outside the train would witness this event in a different way because while the\
		light is making its journey up and down, the train is also moving within their reference frame from\
		left to right.\
	</p>";
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

function loadPrevPage() {
	if ($("#lesson-2.2").display == "block") {
		$("#lesson-2.2").display = "none";
		$("#lesson-2.1").display = "block";
	} else if ($("#lesson-2.3").display == "block") {
		$("#lesson-2.3").display = "none";
		$("#lesson-2.2").display = "block";
	} else if ($("#lesson-2.4").display == "block") {
		$("#lesson-2.4").display = "none";
		$("#lesson-2.3").display = "block";
	}
}

function loadNextPage() {
	if ($("#lesson-2.1").display == "block") {
		$("#lesson-2.1").display = "none";
		$("#lesson-2.2").display = "block";
	} else if ($("#lesson-2.2").display == "block") {
		$("#lesson-2.2").display = "none";
		$("#lesson-2.3").display = "block";
	} else if ($("#lesson-2.3").display == "block") {
		$("#lesson-2.3").display = "none";
		$("#lesson-2.4").display = "block";
	}
}

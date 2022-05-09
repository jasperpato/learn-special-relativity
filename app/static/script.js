function scroll() {
	let progress = document.getElementById('progressbar');
	let totalHeight = document.body.scrollHeight - window.innerHeight;
	window.onscroll = function () {
		progress.style.height = (window.pageYOffset / totalHeight) * 100 + '%';
	};
}

function dropMenu() {
	$(document).ready(function () {
		$('.menu-toggle').click(function () {$('nav').toggleClass('active');});
	});
}

function setTheme(theme) {
	const properties = {
	'Green': {
		'--background': "url('backgrounds/BackgroundGreen.jpg')",
		'--colour1': '#20df27',
		'--colour2': '#05ab48',
		'--colour3': '#7ca57e',
		'--boxShadow': 'rgba(9, 241, 28, 0.75)'
	},
	'Red': {
		'--background': "url('backgrounds/BackgroundRed.jpg')",
		'--colour1': '#da1818',
		'--colour2': '#bd1010',
		'--colour3': '#a26363',
		'--boxShadow': 'rgba(241, 32, 9, 0.75)'
	},
	'Blue': {
		'--background': "url('backgrounds/BackgroundBlue.jpg')",
		'--colour1': '#00eeff',
		'--colour2': '#1da9eb',
		'--colour3': '#5b7e8e',
		'--boxShadow': 'rgba(9, 241, 203, 0.75)'
	},
	'Purple': {
		'--background': "url('backgrounds/BackgroundPurple.jpg')",
		'--colour1': '#9918da',
		'--colour2': '#6a0496',
		'--colour3': '#926e9a',
		'--boxShadow': 'rgba(144, 9, 241, 0.75)'
	}}
	for (const p in properties[theme])
		{document.documentElement.style.setProperty(p, properties[theme][p]);}
}

function init(theme) {
	scroll();
	dropMenu();
	setTheme(theme);
}

function makeActive(page) {
	for (const p in ['Home', 'Learn', 'Stats', 'Login']) $('.nav'+p).removeClass('active');
	$('.nav'+page).addClass('active');
}

function titleMove() {
	$('body').mousemove(function (e) {
		var valueX = (e.pageX * -1) / 75;
		var valueY = (e.pageY * -1) / 75;
		$('#homeTitle').css({transform: 'translate(' + valueX + 'px,' + valueY + 'px)'});
	});
}

function init_home(theme) {
	init(theme);
	makeActive('Home');
	titleMove();
}

function init_learn(theme) {
	init(theme);
	makeActive('Learn');
}

function addHover(name) {
	$('#'+name+'Label').mouseenter(function () {$('#'+name).toggle();});
	$('#'+name+'Label').mouseleave(function () {$('#'+name).toggle();});
}

function hoverBoxes(num) {
	if (num == 1) {
		addHover('speedOfLight');
		addHover('inertial');
		addHover('spaceTime');
	} else if (num == 2) {
		addHover('trig');
		addHover('time');
		addHover('dilation');
	} else if (num == 3) addHover('lorentz');
}

function loadPrevPage(numPages) {
	let pageNum = 1;
	// find visible page
	for (pageNum; pageNum < numPages; ++pageNum)
		{if ($('#l' + pageNum).is(':visible')) break;}
	if (pageNum == 1) return;
	if (pageNum == 2) $('#prev').toggle();
	if (pageNum == numPages) $('#next').toggle();
	$('#l' + pageNum).toggle();
	$('#l' + (pageNum - 1)).toggle();
}

function loadNextPage(numPages) {
	let pageNum = 1;
	// find visible page
	for (pageNum; pageNum < numPages; ++pageNum)
		{if ($('#l' + pageNum).is(':visible')) break;}
	if (pageNum == numPages) return;
	if (pageNum == 1) $('#prev').toggle();
	if (pageNum == numPages - 1) $('#next').toggle();
	$('#l' + pageNum).toggle();
	$('#l' + (pageNum + 1)).toggle();
}

function animations() {
	let img = $('#animate-1').find('img')[0];
	let len = img.id.length;
	let num = parseInt(img.id[len - 1]);

	// animation 1
	img.id = img.id.slice(0, len - 1) + (3 - num);
	img.src = img.src.slice(0, img.src.length - 5) + (3 - num) + '.png';

	// animation 2
	img = $('#animate-2').find('img')[0];
	len = img.id.length;
	num = parseInt(img.id[len - 1]);

	img.id = img.id.slice(0, len - 1) + ((num % 3) + 1);
	img.src = img.src.slice(0, img.src.length - 5) + ((num % 3) + 1) + '.png';
}

function init_lesson(theme, lesson_num) {
	init(theme);
	makeActive('Learn');
	hoverBoxes(lesson_num);
	let numPages = [2, 4, 3];
	$('#prev').click(function () {loadPrevPage(numPages[lesson_num-1]);});
	$('#next').click(function () {loadNextPage(numPages[lesson_num-1]);});
	if (lesson_num == 2) setInterval(animations, 1500);
}

function init_test(theme) {
	init(theme);
	makeActive('Learn');
	$(window).resize(function () {
		if (window.innerWidth < 1000) $('.pageArrowDown').hide();
		else $('.pageArrowDown').show();
	});
	$('.quizBox').on('scroll', function () {
		if ($(this).scrollTop() + $(this).innerHeight() >= $(this)[0].scrollHeight) {
			$('.pageArrowDown').hide();
		} else $('.pageArrowDown').show();
	});
	$(document).ready(function () {
		setTimeout(function () {$('.alert').fadeOut('slow');}, 1600);
	});
}

function init_stats(theme) {
	init(theme);
	makeActive('Stats');
}

function init_login(theme) {
	init(theme);
	makeActive('Login');
}

function validateSignUp() {
	let username = document.getElementById('username').value;
	let password = document.getElementById('password').value;
	let passwordConfirm = document.getElementById('passwordConfirm').value;
	let message = '';
	if (username.length < 4) message = 'Username must be at least 4 characters';
	if (password.length < 7) message = 'Password must be at least 7 characters';
	if (password != passwordConfirm) message = 'Passwords do not match';
	if (message) {
		document.getElementById('message').innerHTML = message;
		$('#message').show();
		setTimeout(function () {$('#message').fadeOut('slow');}, 1600);
		return false;
	} return true;
}

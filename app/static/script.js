function init(theme) {
	scroll();
	dropMenu();
	activateNavBar();
	setTheme(theme);

	let hr = window.location.href;
	let title = document.getElementById('title').innerHTML;

	if (title.includes('Home')) titleMove();

	if (title.includes('Test') || title.includes('Lesson')) {
		let num = parseInt(title[title.length - 1]);

		if (title.includes('Lesson')) {
			hoverBoxes(num);

			let numPages = [2, 4, 3];

			$('#prev').click(function () {
				loadPrevPage(numPages[num - 1]);
			});
			$('#next').click(function () {
				loadNextPage(numPages[num - 1]);
			});

			$('.pageArrowLeftLabel').click(function () {
				window.location.href = hr.slice(0, hr.length - 1) + (num - 1);
			});

			$('.pageArrowRightLabel').click(function () {
				window.location.href = hr.slice(0, hr.length - 1) + (num + 1);
			});

			if (title.includes('Lesson 2')) setInterval(animations, 1500);
		} else if (title.includes('1 Results')) {
			$('.pageArrowLeftLabel').click(function () {
				window.location.href = 'http://127.0.0.1:5000/learn/lesson-1';
			});
			$('.pageArrowRightLabel').click(function () {
				window.location.href = 'http://127.0.0.1:5000/learn/lesson-2';
			});
			fillResults1();
		} else if (title.includes('2 Results')) {
			$('.pageArrowLeftLabel').click(function () {
				window.location.href = 'http://127.0.0.1:5000/learn/lesson-2';
			});
			$('.pageArrowRightLabel').click(function () {
				window.location.href = 'http://127.0.0.1:5000/learn/lesson-3';
			});
			fillResults2();
		} else if (title.includes('3 Results')) {
			$('.pageArrowLeftLabel').click(function () {
				window.location.href = 'http://127.0.0.1:5000/learn/lesson-3';
			});
			$('.pageArrowRightLabel').click(function () {
				window.location.href = 'http://127.0.0.1:5000/stats';
			});
			fillResults3();
		} else {
			$(window).resize(function () {
				if (window.innerWidth < 1000) $('.pageArrowDown').hide();
				else $('.pageArrowDown').show();
			});
			$('.quizBox').on('scroll', function () {
				if ($(this).scrollTop() + $(this).innerHeight() >= $(this)[0].scrollHeight) {
					$('.pageArrowDown').hide();
				} else $('.pageArrowDown').show();
			});
		}
	}
	if (title.includes('Stats')) {
		stats_init();
	}

	$('.logo').click(function () {
		window.location.href = 'http://127.0.0.1:5000';
	});

	$(document).ready(function () {
		setTimeout(function () {
			$('.alert').fadeOut('slow');
		}, 1600);
	});
}

function stats_init() {
	$('#test1').click(function () {
		displayStats(1);
	});
	$('#test2').click(function () {
		displayStats(2);
	});
	$('#test3').click(function () {
		displayStats(3);
	});
	displayStats(1);
}

// testData received in script from server
function displayStats(testNum) {
	document.getElementsByClassName('chooseActive')[0].classList.remove('chooseActive');
	document.getElementById('test' + testNum).classList.add('chooseActive');

	let top = 0;
	let av = 0;
	let your = 0;
	if (testNum == 1) {
		top = testData.topScore1;
		av = testData.avScore1;
		your = testData.bestAttempt1;
	} else if (testNum == 2) {
		top = testData.topScore2;
		av = testData.avScore2;
		your = testData.bestAttempt2;
	} else if (testNum == 3) {
		top = testData.topScore3;
		av = testData.avScore3;
		your = testData.bestAttempt3;
	}
	$('#topCircle').css('stroke-dashoffset', '' + (440.0 - (440.0 * parseInt(top)) / 100.0 + 'px'));
	$('#topNum').html(top + '<span>%</span>');

	$('#avCircle').css('stroke-dashoffset', '' + (440.0 - (440.0 * parseInt(av)) / 100.0 + 'px'));
	$('#avNum').html(av + '<span>%</span>');

	$('#yourCircle').css('stroke-dashoffset', '' + (440.0 - (440.0 * parseInt(your)) / 100.0 + 'px'));
	$('#yourNum').html(your + '<span>%</span>');

	let texts = document.getElementsByClassName('progressText');
	for (i = 0; i < texts.length; ++i) {
		texts[i].innerHTML = 'Test ' + testNum;
	}
}

// answers received in script from server
function fillResults1() {
	if (answers[1] != null) document.getElementById('1' + answers[1]).checked = true;

	if (answers[1] == correct[1]) $('#mark1').html('<i class="fa fa-check check"></i>');
	else $('#mark1').html('<i class="fa fa-times times"></i>');

	if (answers[2] != null) document.getElementById('2' + answers[2]).checked = true;

	if (answers[2] == correct[2]) $('#mark2').html('<i class="fa fa-check check"></i>');
	else $('#mark2').html('<i class="fa fa-times times"></i>');

	if (answers[3] != null) document.getElementById('3' + answers[3]).checked = true;

	if (answers[3] == correct[3]) $('#mark3').html('<i class="fa fa-check check"></i>');
	else $('#mark3').html('<i class="fa fa-times times"></i>');

	if (answers[4] != null) document.getElementById('4' + answers[4]).checked = true;

	if (answers[4] == correct[4]) $('#mark4').html('<i class="fa fa-check check"></i>');
	else $('#mark4').html('<i class="fa fa-times times"></i>');

	document.getElementById('5').value = answers[5];
	if (answers[5] == correct[5]) $('#mark5').html('<i class="fa fa-check check"></i>');
	else $('#mark5').html('<i class="fa fa-times times"></i>');
}

// answers received in script from server
function fillResults2() {
	if (answers[1] != null) document.getElementById('1' + answers[1]).checked = true;
	if (answers[1] == correct[1]) $('#mark1').html('<i class="fa fa-check check"></i>');
	else $('#mark1').html('<i class="fa fa-times times"></i>');

	if (answers[2] != null) document.getElementById('2' + answers[2]).checked = true;
	if (answers[2] == correct[2]) $('#mark2').html('<i class="fa fa-check check"></i>');
	else $('#mark2').html('<i class="fa fa-times times"></i>');

	if (answers[3] != null) document.getElementById('3' + answers[3]).checked = true;
	if (answers[3] == correct[3]) $('#mark3').html('<i class="fa fa-check check"></i>');
	else $('#mark3').html('<i class="fa fa-times times"></i>');

	if (answers[4] != null) document.getElementById('4' + answers[4]).checked = true;
	if (answers[4] == correct[4]) $('#mark4').html('<i class="fa fa-check check"></i>');
	else $('#mark4').html('<i class="fa fa-times times"></i>');

	if (answers[5] != null) document.getElementById('5' + answers[5]).checked = true;
	if (answers[5] == correct[4]) $('#mark5').html('<i class="fa fa-check check"></i>');
	else $('#mark5').html('<i class="fa fa-times times"></i>');
}

// answers received in script from server
function fillResults3() {
	document.getElementById('1').value = answers[1];
	if (answers[1] == correct[1]) $('#mark1').html('<i class="fa fa-check check"></i>');
	else $('#mark1').html('<i class="fa fa-times times"></i>');

	if (answers[2] != null) document.getElementById('2' + answers[2]).checked = true;
	if (answers[2] == correct[2]) $('#mark2').html('<i class="fa fa-check check"></i>');
	else $('#mark2').html('<i class="fa fa-times times"></i>');

	if (answers[3] != null) document.getElementById('3' + answers[3]).checked = true;
	if (answers[3] == correct[3]) $('#mark3').html('<i class="fa fa-check check"></i>');
	else $('#mark3').html('<i class="fa fa-times times"></i>');

	document.getElementById('4').value = answers[4];
	if (answers[4] == correct[4]) $('#mark4').html('<i class="fa fa-check check"></i>');
	else $('#mark4').html('<i class="fa fa-times times"></i>');

	document.getElementById('5').value = answers[5];
	if (answers[5] == correct[5]) $('#mark5').html('<i class="fa fa-check check"></i>');
	else $('#mark5').html('<i class="fa fa-times times"></i>');
}

// answers received in script from server
function fillResults1() {
	if (answers[1] != null) document.getElementById('1' + answers[1]).checked = true;

	if (answers[1] == correct[1]) $('#mark1').html('<i class="fa fa-check check"></i>');
	else $('#mark1').html('<i class="fa fa-times times"></i>');

	if (answers[2] != null) document.getElementById('2' + answers[2]).checked = true;

	if (answers[2] == correct[2]) $('#mark2').html('<i class="fa fa-check check"></i>');
	else $('#mark2').html('<i class="fa fa-times times"></i>');

	if (answers[3] != null) document.getElementById('3' + answers[3]).checked = true;

	if (answers[3] == correct[3]) $('#mark3').html('<i class="fa fa-check check"></i>');
	else $('#mark3').html('<i class="fa fa-times times"></i>');

	if (answers[4] != null) document.getElementById('4' + answers[4]).checked = true;

	if (answers[4] == correct[4]) $('#mark4').html('<i class="fa fa-check check"></i>');
	else $('#mark4').html('<i class="fa fa-times times"></i>');

	document.getElementById('5').value = answers[5];
	if (answers[5] == correct[5]) $('#mark5').html('<i class="fa fa-check check"></i>');
	else $('#mark5').html('<i class="fa fa-times times"></i>');
}

function validateSignUp() {
	let username = document.getElementById('username').value;
	let password = document.getElementById('password').value;
	let passwordConfirm = document.getElementById('passwordConfirm').value;
	let message = '';
	if (username.length < 4) {
		message = 'Username must be at least 4 characters';
	}
	if (password.length < 7) {
		message = 'Password must be at least 7 characters';
	}
	if (password != passwordConfirm) {
		message = 'Passwords do not match';
	}
	if (message) {
		document.getElementById('message').innerHTML = message;
		$('#message').show();
		setTimeout(function () {
			$('#message').fadeOut('slow');
		}, 1600);
		return false;
	}
	return true;
}

function scroll() {
	let progress = document.getElementById('progressbar');
	let totalHeight = document.body.scrollHeight - window.innerHeight;
	window.onscroll = function () {
		progress.style.height = (window.pageYOffset / totalHeight) * 100 + '%';
	};
}

function dropMenu() {
	$(document).ready(function () {
		$('.menu-toggle').click(function () {
			$('nav').toggleClass('active');
		});
	});
}

function titleMove() {
	$('body').mousemove(function (e) {
		var valueX = (e.pageX * -1) / 75;
		var valueY = (e.pageY * -1) / 75;

		$('#homeTitle').css({
			transform: 'translate(' + valueX + 'px,' + valueY + 'px)',
		});
	});
}

function activateNavBar() {
	let navButtons = ['.navHome', '.navLearn', '.navStats', '.navLogout', '.navLogin'];

	let title = document.getElementById('title').innerHTML;

	if (title.includes('Home')) {
		$(navButtons[0]).addClass('active');
	} else if (title.includes('Test') || title.includes('Lesson')) {
		$(navButtons[1]).addClass('active');
	} else if (title.includes('Stats')) {
		$(navButtons[2]).addClass('active');
	} else if (title.includes('Logout')) {
		$(navButtons[3]).addClass('active');
	} else if (title.includes('Login') || title.includes('Sign Up')) {
		$(navButtons[4]).addClass('active');
	}
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

function loadPrevPage(numPages) {
	let pageNum = 1;

	// find visible page
	for (pageNum; pageNum < numPages; ++pageNum) {
		if ($('#l' + pageNum).is(':visible')) break;
	}

	if (pageNum == 1) return;
	if (pageNum == 2) $('#prev').toggle();
	if (pageNum == numPages) {
		$('#next').toggle();
		//$("#go-test-" + lessonNum).toggle();
	}
	$('#l' + pageNum).toggle();
	$('#l' + (pageNum - 1)).toggle();
}

function loadNextPage(numPages) {
	let pageNum = 1;

	// find visible page
	for (pageNum; pageNum < numPages; ++pageNum) {
		if ($('#l' + pageNum).is(':visible')) break;
	}

	if (pageNum == numPages) return;
	if (pageNum == 1) $('#prev').toggle();
	if (pageNum == numPages - 1) {
		$('#next').toggle();
		//$("#go-test-" + lessonNum).toggle();
	}
	$('#l' + pageNum).toggle();
	$('#l' + (pageNum + 1)).toggle();
}

function hoverBoxes(num) {
	if (num == 1) {
		$('#speedOfLightLabel').mouseenter(function () {
			$('#speedOfLight').toggle();
		});
		$('#speedOfLightLabel').mouseleave(function () {
			$('#speedOfLight').toggle();
		});
		$('#inertialLabel').mouseenter(function () {
			$('#inertial').toggle();
		});
		$('#inertialLabel').mouseleave(function () {
			$('#inertial').toggle();
		});
		$('#spaceTimeLabel').mouseenter(function () {
			$('#spaceTime').toggle();
		});
		$('#spaceTimeLabel').mouseleave(function () {
			$('#spaceTime').toggle();
		});
	} else if (num == 2) {
		$('#trigLabel').mouseenter(function () {
			$('#trig').toggle();
		});
		$('#trigLabel').mouseleave(function () {
			$('#trig').toggle();
		});
		$('#timeLabel').mouseenter(function () {
			$('#time').toggle();
		});
		$('#timeLabel').mouseleave(function () {
			$('#time').toggle();
		});
		$('#dilationLabel').mouseenter(function () {
			$('#dilation').toggle();
		});
		$('#dilationLabel').mouseleave(function () {
			$('#dilation').toggle();
		});
	} else if (num == 3) {
		$('#lorentzLabel').mouseenter(function () {
			$('#lorentz').toggle();
		});
		$('#lorentzLabel').mouseleave(function () {
			$('#lorentz').toggle();
		});
	}
}

function setTheme(theme) {
	if (theme == 'Green') {
		document.documentElement.style.setProperty('--background', "url('backgrounds/BackgroundGreen.jpg')");
		document.documentElement.style.setProperty('--colour1', '#20df27');
		document.documentElement.style.setProperty('--colour2', '#05ab48');
		document.documentElement.style.setProperty('--colour3', '#7ca57e');
		document.documentElement.style.setProperty('--boxShadow', 'rgba(9, 241, 28, 0.75)');
	} else if (theme == 'Red') {
		document.documentElement.style.setProperty('--background', "url('backgrounds/BackgroundRed.jpg')");
		document.documentElement.style.setProperty('--colour1', '#da1818');
		document.documentElement.style.setProperty('--colour2', '#bd1010');
		document.documentElement.style.setProperty('--colour3', '#a26363');
		document.documentElement.style.setProperty('--boxShadow', 'rgba(241, 32, 9, 0.75)');
	} else if (theme == 'Blue') {
		document.documentElement.style.setProperty('--background', "url('backgrounds/BackgroundBlue.jpg')");
		document.documentElement.style.setProperty('--colour1', '#00eeff');
		document.documentElement.style.setProperty('--colour2', '#1da9eb');
		document.documentElement.style.setProperty('--colour3', '#5b7e8e');
		document.documentElement.style.setProperty('--boxShadow', 'rgba(9, 241, 203, 0.75)');
	} else if (theme == 'Purple') {
		document.documentElement.style.setProperty('--background', "url('backgrounds/BackgroundPurple.jpg')");
		document.documentElement.style.setProperty('--colour1', '#9918da');
		document.documentElement.style.setProperty('--colour2', '#6a0496');
		document.documentElement.style.setProperty('--colour3', '#926e9a');
		document.documentElement.style.setProperty('--boxShadow', 'rgba(144, 9, 241, 0.75)');
	}
}

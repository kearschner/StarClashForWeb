
const typingSpeedMS = 75;

const lineSets = [
	[
		'You awaken on a derelect spaceship',
		'in ABANDONED space.'
	],
	[
		'In front of you lies the control terminal for the ship.',
		'Readings indicate working LOCALSPACE systems. ',
		'However, HYPERSPACE systems are inoperable.'
	],
	[
		'Alert! An enemy craft is about to drop out of HYPERSPACE.',
		'Getting warp back online may be possible,',
		'but you need more TIME.'
	],
	[
		'If you want to SURVIVE, you must FIGHT.'
	],
	[
		'This is...'
	]
]

const listElement = $("#typewriterList");

function newLineSet() {

	listElement.empty();

	if (lineSets.length == 0)
		return false;

	const newSet = lineSets.shift();

	return attachLine(newSet);
}

function attachLine(lineSet) {

	if (lineSet.length == 0)
		return false;

	const newElem = listElement.append('<li class="typewriterItem"></li>').children().last();
	const lineText = lineSet.shift();
	const lineLength = lineText.length;

	let character = 0;

	const remainingSets = lineSets.length;
	(function typeWriter() {
		let timeOut = setTimeout( function() {
			character++;
			let type = lineText.substring(0, character);
			newElem.text(type);

			if (character == lineLength) {
				clearTimeout(timeOut);
				if (remainingSets == lineSets.length)
					attachLine(lineSet);
			}
			else {
				typeWriter();
			}
		}, typingSpeedMS);
	}());

	return true;
	
}

$(document).ready( () => {

	function typewriterClickHandle() {
		if (!newLineSet()) {
			$(this).off('click', typewriterClickHandle);
			$("#content").append('<p id="title">StarClash</p>');
		}
	}

	$(document).on('click', typewriterClickHandle);
});

newLineSet();
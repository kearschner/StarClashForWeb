
const typingSpeedMS = 75;

const lineSets = [
	[
		'<li class="typewriterItem">You awaken on a derelect spaceship</li>',
		'<li class="typewriterItem">in ABANDONED space.</li>'
	],
	[
		'<li class="typewriterItem">In front of you lies the control terminal for the ship.</li>',
		'<li class="typewriterItem">Readings indicate working LOCALSPACE systems. </li>',
		'<li class="typewriterItem">However HYPERSPACE systems are inoperable.</li>'
	],
	[
		'<li class="typewriterItem">Alert! An enemy craft is about to drop out of HYPERSPACE.</li>',
		'<li class="typewriterItem">Getting warp back online may be possible,</li>',
		'<li class="typewriterItem">but you need more TIME.</li>'
	],
	[
		'<li class="typewriterItem">If you want to SURVIVE, you must FIGHT.</li>'
	],
	[
		'<li class="typewriterItem">This is... </li>'
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

	let newLine = lineSet.shift();

	const newElem = listElement.append(newLine).children().last();
	const lineLength = newElem.text().length;

	newElem.css("--typewriterCharacters", lineLength);
	newElem.css("--typewriterSpeed", (lineLength * typingSpeedMS) + "ms");
	
	newElem.on('animationend', {
		lineSet: lineSet
	}, (event) => {
		return attachLine(event.data.lineSet);
	});

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
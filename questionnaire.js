var questions = [
    { text: 'What does kitty look like?', type: 'text', placeholder: '' },
    { text: 'Describe their personality', type: 'text', placeholder: '' },
    { text: 'Boy or girl?', type: 'text', placeholder: '' },
    { text: 'Any names to avoid?', type: 'text', placeholder: '' },
    { text: 'Are there any stories, shows, movies, etc. that you enjoy?', type: 'text', placeholder: '' },
    { text: 'Is there any style or aesthetic that you enjoy?', type: 'text', placeholder: '' },
    { text: 'Is there a culture or history you would like to reference?', type: 'text', placeholder: '' },
    { text: 'What are your hobbies?', type: 'text', placeholder: '' },
    { text: 'What sort of area do you live in?', type: 'text', placeholder: '' },
    { text: 'Do you like people names?', type: 'bool', placeholder: '' },
    { text: 'Do you like serious names?', type: 'bool', placeholder: '' },
    { text: 'Do you like silly names?', type: 'bool', placeholder: '' },
    { text: 'Are cliché or popular names ok?', type: 'bool', placeholder: '' },
    { text: 'Any example names', type: 'text', placeholder: '' },
];
var answers = {};
var currentQuestion = 0;

function start() {
    document.getElementById('intro').style.display = 'none';
    document.getElementById('questionContainer').style.display = 'block';
    displayQuestion();
}

function displayQuestion() {
    var question = questions[currentQuestion];
    document.getElementById('questionText').innerText = question.text;
	
	document.getElementById('textAnswer').value = '';
    document.getElementById('yesNoAnswer').value = '';
    document.getElementById('conditionalText').value = '';
    document.getElementById('boolYes').checked = false;
    document.getElementById('boolNo').checked = false;
	
	if (currentQuestion <= 0) {
        document.getElementById('backButton').style.display = 'none';
    } else {
        document.getElementById('backButton').style.display = 'inline-block';
    }
	
    if (question.type === 'text') {
        document.getElementById('answerText').style.display = 'block';
        document.getElementById('answerText').placeholder = question.placeholder;
        document.getElementById('answerYesNo').style.display = 'none';
    } else if (question.type === 'yesno') {
        document.getElementById('answerYesNo').style.display = 'block';
        document.getElementById('conditionalText').placeholder = question.placeholder;
        document.getElementById('answerText').style.display = 'none';
        document.getElementById('conditionalText').style.display = 'none';
        document.getElementById('yesNoAnswer').value = '';
    } else if (question.type === 'bool') {
        document.getElementById('answerBool').style.display = 'block';
        document.getElementById('answerText').style.display = 'none';
        document.getElementById('answerYesNo').style.display = 'none';
    }
}

function nextQuestion() {
    var question = questions[currentQuestion];
    if (question.type === 'text') {
        answers[question.text] = document.getElementById('textAnswer').value;
    } else if (question.type === 'yesno') {
        var yesNoAnswer = document.getElementById('yesNoAnswer').value;
        if (yesNoAnswer === 'yes') {
            answers[question.text] = document.getElementById('conditionalText').value;
        } else if (yesNoAnswer === 'no') {
            answers[question.text] = 'No';
        }
    }
    currentQuestion++;
    if (currentQuestion < questions.length) {
        displayQuestion();
    } else {
        document.getElementById('questionContainer').style.display = 'none';
        sendAnswers();
    }
}

function previousQuestion() {
    if (currentQuestion <= 0) {
        return;
    }
    currentQuestion--;
    var question = questions[currentQuestion];
    var previousAnswer = answers[currentQuestion];
    document.getElementById('questionText').innerText = question.text;
    if (question.type === 'text') {
        document.getElementById('textAnswer').value = previousAnswer;
        document.getElementById('textAnswer').style.display = 'block';
        document.getElementById('answerYesNo').style.display = 'none';
        document.getElementById('answerBool').style.display = 'none';
    } else if (question.type === 'yesno') {
        document.getElementById('answerYesNo').value = previousAnswer === 'No' ? 'No' : 'Yes';
        if (previousAnswer !== 'No') {
            document.getElementById('conditionalText').value = previousAnswer;
            document.getElementById('conditionalText').style.display = 'block';
        }
        document.getElementById('answerYesNo').style.display = 'block';
        document.getElementById('textAnswer').style.display = 'none';
        document.getElementById('answerBool').style.display = 'none';
    } else if (question.type === 'bool') {
        if (previousAnswer === 'Yes') {
            document.getElementById('boolYes').checked = true;
        } else if (previousAnswer === 'No') {
            document.getElementById('boolNo').checked = true;
        }
        document.getElementById('answerBool').style.display = 'block';
        document.getElementById('textAnswer').style.display = 'none';
        document.getElementById('answerYesNo').style.display = 'none';
    }
    if (currentQuestion <= 0) {
        document.getElementById('backButton').style.display = 'none';
    }
}


function skipQuestion() {
    currentQuestion++;
    displayQuestion();
}

function sendAnswers() {
    // Modify this function to send the answers to the API and handle the response
    fetch('https://us-central1-catnames-394614.cloudfunctions.net/SubmitNames', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(answers),
    })
    .then(response => response.json())
    .then(data => displayResult(data.csv));
    /*.then(data => displayResult(`Name,Reason
        doug,It's awesome
        chuck,Just funny!`));*/
	.then(data => console.log(data));
}

function handleYesNoChange(value) {
    if (value === 'yes') {
        document.getElementById('conditionalText').style.display = 'block';
    } else {
        document.getElementById('conditionalText').style.display = 'none';
    }
}

function displayResult(csv) {
    document.getElementById('resultContainer').style.display = 'block';
    var lines = csv.split('\n');
    var header = lines[0].split(',');
    var headerHtml = '<tr>' + header.map(col => '<td><h4>' + col + '</h4></td>').join('') + '</tr>';
    document.getElementById('resultHeader').innerHTML = headerHtml;
    var bodyHtml = lines.slice(1).map(line => {
        var cols = line.split(',');
        return '<tr>' + cols.map(col => '<td>' + col + '</td>').join('') + '</tr>';
    }).join('');
    document.getElementById('resultBody').innerHTML = bodyHtml;
}

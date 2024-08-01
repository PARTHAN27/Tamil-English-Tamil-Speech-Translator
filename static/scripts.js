let mediaRecorder;
let audioChunks = [];
let isRecording = false;

const recordButton = document.getElementById('recordButton');
const recordingsList = document.getElementById('recordingsList');

recordButton.addEventListener('click', async () => {
    if (isRecording) {
        mediaRecorder.stop();
        recordButton.textContent = 'Start Recording';
    } else {
        const stream = await navigator.mediaDevices.getUserMedia({ audio: true });
        mediaRecorder = new MediaRecorder(stream);
        
        mediaRecorder.ondataavailable = event => {
            audioChunks.push(event.data);
        };
        
        mediaRecorder.onstop = () => {
            const audioBlob = new Blob(audioChunks, { type: 'audio/wav' });
            audioChunks = [];
            const audioUrl = URL.createObjectURL(audioBlob);
            const audio = document.createElement('audio');
            audio.controls = true;
            audio.src = audioUrl;

            const downloadLink = document.createElement('a');
            downloadLink.href = audioUrl;
            downloadLink.download = 'recording.wav';
            downloadLink.textContent = 'Download Recording';

            const listItem = document.createElement('li');
            listItem.appendChild(audio);
            listItem.appendChild(downloadLink);
            recordingsList.appendChild(listItem);
        };

        mediaRecorder.start();
        recordButton.textContent = 'Stop Recording';
    }
    
    isRecording = !isRecording;
});


function startTranslation() {
    const audioFile = document.getElementById('audioFile').files[0];
    if (!audioFile) {
        alert('Please upload an audio file.');
        return;
    }

    const formData = new FormData();
    formData.append('audioFile', audioFile);

    fetch('/translate', {
        method: 'POST',
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('transcribedText').innerText = 'Transcribed Text: ' + data.transcribedText;
        document.getElementById('translatedText').innerText = 'Translated Text: ' + data.translatedText;
        //document.getElementById('translatedAudio').src = data.translatedAudioUrl;
        document.getElementById('translatedAudio').src = '/uploads/' + data.translatedAudioUrl.split('/').pop();

    })
    .catch(error => {
        console.error('Error:', error);
    });
}
function startTranslation2() {
    const audioFile = document.getElementById('audioFile2').files[0];
    if (!audioFile) {
        alert('Please upload an audio file.');
        return;
    }

    const formData = new FormData();
    formData.append('audioFile2', audioFile);

    fetch('/translate2', {
        method: 'POST',
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('transcribedText2').innerText = 'Transcribed Text: ' + data.transcribedText;
        document.getElementById('translatedText2').innerText = 'Translated Text: ' + data.translatedText;
        //document.getElementById('translatedAudio').src = data.translatedAudioUrl;
        document.getElementById('translatedAudio2').src = '/uploads/' + data.translatedAudioUrl.split('/').pop();

    })
    .catch(error => {
        console.error('Error:', error);
    });
}


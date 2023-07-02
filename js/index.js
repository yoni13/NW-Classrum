// Solution from https://reurl.cc/gDRegQ
function InputGoToEnd(element) {
    const selection = window.getSelection();
    const range = document.createRange();
    selection.removeAllRanges();
    range.selectNodeContents(element);
    range.collapse(false);
    selection.addRange(range);
    element.focus();
}

function PostDataToBackEnd(CurrentLineText) {
    fetch('subject', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            'text': CurrentLineText,
        }),
    })
}

let alphablet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ';
function onloaded() {
    const InputArea = document.getElementById('inputarea');
    InputArea.textContent = '1. ';
    InputGoToEnd(InputArea);
    InputArea.addEventListener('keydown', function (e) {
        if (e.code == 'Enter' || e.code == 'NumpadEnter') {
            e.preventDefault();
            InputArea.textContent += '\n';
            var count = (InputArea.textContent.match(/\n/g) || []).length;
            InputArea.textContent += count + 1 + '. ';
            InputArea.scrollTop = InputArea.scrollHeight;
            InputGoToEnd(InputArea);
        }
        else {
            var CurrentLine =  (InputArea.textContent.match(/\n/g)||[]).length + 1;
            if (alphablet.includes(e.key)) {
            var CurrentLineText = InputArea.textContent.split('\n')[CurrentLine - 1] + e.key;
            PostDataToBackEnd(CurrentLineText);
            }
        }
    });
}

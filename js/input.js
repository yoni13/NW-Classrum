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

function PostDataToBackEnd(InputArea,CurrentLineText, count) {
    fetch('subject', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            'text': CurrentLineText,
        }),
    })
        .then((response) => response.json())
        .then((data) => {
            subject = data['subject'];
            // insert subject between last line
            InputArea.innerHTML = InputArea.innerHTML.replace(CurrentLineText, CurrentLineText + '<div id=subject>' + subject + '</div>');
            InputGoToEnd(InputArea);
        }
        )
}

function onloaded() {
    const InputArea = document.getElementById('inputarea');
    InputArea.innerHTML = '1. ';
    InputGoToEnd(InputArea);
    InputArea.addEventListener('keydown', function (e) {
        if (e.code == 'Enter' || e.code == 'NumpadEnter') {
            e.preventDefault();
            InputArea.innerHTML += '\n';
            var count = (InputArea.innerHTML.match(/\n/g) || []).length;
            InputArea.innerHTML += count + 1 + '. ';
            InputArea.scrollTop = InputArea.scrollHeight;
            InputGoToEnd(InputArea);
            var CurrentLineText = InputArea.innerHTML.split('\n')[count - 1]
            PostDataToBackEnd(InputArea,CurrentLineText, count);
       }
// Handle the `paste` event
InputArea.addEventListener('paste', function (e) {
    // Prevent the default action
    e.preventDefault();

    // Get the copied text from the clipboard
    const text = e.clipboardData
        ? (e.originalEvent || e).clipboardData.getData('text/plain')
        : // For IE
        window.clipboardData
        ? window.clipboardData.getData('Text')
        : '';

    if (document.queryCommandSupported('insertText')) {
        document.execCommand('insertText', false, text);
    } else {
        // Insert text at the current position of caret
        const range = document.getSelection().getRangeAt(0);
        range.deleteContents();

        const textNode = document.createTextNode(text);
        range.insertNode(textNode);
        range.selectNodeContents(textNode);
        range.collapse(false);

        const selection = window.getSelection();
        selection.removeAllRanges();
        selection.addRange(range);
    }
});
    });
}

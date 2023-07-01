
function onloaded() {
    const InputArea = document.getElementById('inputarea');
    InputArea.textContent = '1.';
    InputArea.addEventListener('keydown', function (e) {
        if (e.code == 'Enter' || e.code == 'NumpadEnter') {
            e.preventDefault();
            InputArea.textContent += '\n';
            var count = (InputArea.textContent.match(/\n/g) || []).length;
            InputArea.textContent += count + 1 + '.';
            InputArea.scrollTop = InputArea.scrollHeight;
            
        }
        
    });
}

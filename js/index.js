function onloaded() {
    const InputArea = document.getElementById('inputarea');
    InputArea.value = '1.';
    InputArea.addEventListener('keydown', function (e) {
        if (e.code == 'Enter' || e.code == 'NumpadEnter') {
            e.preventDefault();
            InputArea.value += '\n';
            var count = (InputArea.value.match(/\n/g) || []).length;
            InputArea.value += count + 1 + '.';
            InputArea.scrollTop = InputArea.scrollHeight
        }
        
    });
}

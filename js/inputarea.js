function onloaded() {
    let homeworkInput = document.getElementById("homeworkInput");
    let addHomeworkBtn = document.getElementById("addHomeworkBtn");
    addHomeworkBtn.onclick = function () {
        let homework = homeworkInput.value;
        if (homework.length > 0) {
            alert("Hello");
            homeworkInput.value = "";
        }
    }
    homeworkInput.addEventListener("keypress", function(event) {
        if (event.keyCode === 13) {
            event.preventDefault();
            addHomeworkBtn.click();
        }
    });
}
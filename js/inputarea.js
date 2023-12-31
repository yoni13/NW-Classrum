function onloaded() {
    let homeworkInput = document.getElementById("homeworkInput");
    let addHomeworkBtn = document.getElementById("addHomeworkBtn");
    addHomeworkBtn.onclick = function () {
        let homework = homeworkInput.value;
        if (homework.length > 0) {
            try{
                let homeworkList = document.getElementById("homeworkList");
                homeworkList.appendChild(document.createElement("br"));

                let homeworkItem = document.createElement("div");
                homeworkItem.className = "homeworkItem";

                homeworkTitleName = document.createElement("h1");
                homeworkTitleName.className = "homeworkTitleName";
                homeworkTitleName.innerText = homeworkInput.value;
                homeworkItem.appendChild(homeworkTitleName);

                fetch('subject', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                    },
                    body: JSON.stringify({
                        'text': homeworkInput.value,
                    }),
                })
                    .then((response) => response.json())
                    .then((data) => {
                        nextclasstime = data['nextclasstime'];
                        let homeworkNextTimeDateBG = document.createElement("div");
                        homeworkNextTimeDateBG.className = "homeworkNextTimeDateBG";
                        homeworkNextTimeDateBG.innerText = nextclasstime;
                        homeworkItem.appendChild(homeworkNextTimeDateBG);
                    }
                    )

                homeworkList.appendChild(homeworkItem);
                homeworkList.appendChild(document.createElement("br"));
                console.log("Homework added");
                
            }
            catch(err){

                homeworkList = document.createElement("div");
                homeworkList.id = "homeworkList";
                document.body.appendChild(homeworkList);
                console.log("Homework list created");
                
                homeworkList.appendChild(document.createElement("br"));

                let homeworkItem = document.createElement("div");
                homeworkItem.className = "homeworkItem";

                homeworkTitleName = document.createElement("h1");
                homeworkTitleName.className = "homeworkTitleName";
                homeworkTitleName.innerText = homeworkInput.value;
                homeworkItem.appendChild(homeworkTitleName);

                fetch('subject', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                    },
                    body: JSON.stringify({
                        'text': homeworkInput.value,
                    }),
                })
                    .then((response) => response.json())
                    .then((data) => {
                        nextclasstime = data['nextclasstime'];
                        let homeworkNextTimeDateBG = document.createElement("div");
                        homeworkNextTimeDateBG.className = "homeworkNextTimeDateBG";
                        homeworkNextTimeDateBG.innerText = nextclasstime;
                        homeworkItem.appendChild(homeworkNextTimeDateBG);
                    }
                    )

                homeworkList.appendChild(homeworkItem);
                homeworkList.appendChild(document.createElement("br"));
                console.log("Homework added");
            }
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
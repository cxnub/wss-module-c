let question = history.state.question;
let questionContainer = document.getElementById('question-container');


const displayQuestion = () => {
    if (!question.Title) {
        questionContainer.innerHTML = question + `<a id="link">View Submissions</a>`;
        let link = document.getElementById("link")
        link.onclick = () => {
            getSubmissions();
        }
        return;
    }

    html = `
        <h1>${question.Title}</h1>
    `

    html += `<p>${question.Description}<br>`

    for (var item of Object.keys(question)) {
        if (!["examples", "Description", "Title", "longDesc"].includes(item)) {
            html += `
            ${item}: ${question[item]}<br>
        `
        }
    }

    let longDesc = question.longDesc;
    html += `<br><br>${longDesc}</p>`
    html += "</div>"

    for (var example of question.examples) {
        html += `
            <p>Example ${question.examples.indexOf(example) + 1}</p>
            <div class="example">
                ${example}
            </div>
        `
    }

    questionContainer.innerHTML = html + `<a id="link">View Submissions</a>`;

    let link = document.getElementById("link")
    link.onclick = () => {
        getSubmissions();
    }

}



const getSubmissions = async () => {
    let title = history.state.title.replaceAll(" ", "-").toLowerCase();
    console.log(title)

    let res = await fetch('/code');
    res = await res.text();

    let parser = new DOMParser();
    let doc = parser.parseFromString(res, "text/html");
    let fileNames = Array.from(doc.querySelectorAll("span.name"));

    fileNames = fileNames
        .map((fileName) => fileName.innerText)
        .filter((fileName) => fileName.endsWith('.txt'))
        .filter((filename) => {
            return filename.split("_")[0].toLowerCase() == title;
        });

    parseSubmissions(fileNames);
}

const parseSubmissions = (filenames) => {
    let submissions = [];

    for (var filename of filenames) {
        console.log(filename);
    }
}


displayQuestion();





const debounce = (func, delay = 400) => {
    let timeout = null;
    return (...args) => {
        clearTimeout(timeout);
        timeout = setTimeout(() => {
            func(...args)
        }, delay);
    }
}

const useState = (initialValue) => {
    let value = initialValue;
    getVal = () => value;
    setVal = (newVal) => {
        value = newVal;
        displayQuestions();
    };
    return [getVal, setVal];
}

const [getQuestions, setQuestions] = useState({});
const [getFiltered, setFiltered] = useState([]);

const fetchQuestions = async () => {
    let res = await fetch('/question');
    res = await res.text();

    let parser = new DOMParser();
    let doc = parser.parseFromString(res, "text/html");
    let fileNames = Array.from(doc.querySelectorAll("span.name"));

    fileNames = fileNames
        .map((fileName) => fileName.innerText)
        .filter((fileName) => fileName.endsWith('.html') || fileName.endsWith('.txt'));

    let questions = await parseQuestions(fileNames);
    setQuestions(questions);
    setFiltered(Object.keys(questions));
}

const parseQuestions = async (filenames) => {
    let questions = {};

    for (var filename of filenames) {
        let res = await fetch(`/question/${filename}`);
        res = await res.text();

        if (filename.endsWith('.html')) {
            let parser = new DOMParser();
            let doc = parser.parseFromString(res, "text/html");

            questions[filename.split('.html')[0].split('-').join(' ')] = doc;
            continue;
        }

        let split = res.split("---");
        let metadata = split[1];
        let question = split[2];
        let newQuestion = {};

        // parse metadata
        let values = metadata.split("\r\n");
        values.splice(0, 1);

        let currentKey = "";

        for (var value of values) {
            if (value.includes(": ")) {
                let valueSplit = value.split(": ");
                let key = valueSplit[0];
                let data = valueSplit[1];
                currentKey = key;
                newQuestion[currentKey] = data;
                continue;
            }

            newQuestion[currentKey] += value;
        }

        // parse questions
        let questionSplit = question.split("Example:");
        newQuestion['longDesc'] = questionSplit[0];
        questionSplit.splice(0, 1);
        newQuestion['examples'] = questionSplit.map((example) => example.trim())

        // add new question
        questions[newQuestion.Title] = newQuestion
    }

    return questions;
}

let [getCurrentPage, setCurrentPage] = useState(0);
let max = 8;


const startBtn = document.getElementById('start');
const endBtn = document.getElementById('end');
const leftBtn = document.getElementById('left');
const rightBtn = document.getElementById('right');
let page = document.getElementById('page');

const displayQuestions = () => {
    let questions = getQuestions();
    let filtered = getFiltered();

    filtered.sort((a, b) => a.toLowerCase().localeCompare(b.toLowerCase()));

    let currentPage = getCurrentPage();

    page.innerText = "Page " + (currentPage + 1).toString();
    filtered = filtered.slice(currentPage * max, (currentPage + 1) * max);

    let table = document.getElementById('question-table');
    let header = document.getElementById('header-row');
    table.innerHTML = "";
    table.appendChild(header);


    for (var title of filtered) {
        let newRow = document.createElement('tr');
        let question = questions[title];
        newRow.className = "question-row";
        newRow.innerHTML = `
            <td class="question-title">${title}</td>
            <td>${question.Description}</td>
        `
        table.appendChild(newRow);
    }
}

const isSubsequence = (string, search) => {
    let pointer = 0;
    for (var value of string) {
        if (search[pointer] == value) {
            pointer += 1
        }
    }

    return pointer == search.length
}

const searchBox = document.getElementById('search-box');
const debouncedSearch = debounce((inputVal) => {
    let questions = getQuestions();
    let titles = Object.keys(questions);

    titles = titles.filter((title) => title.toLowerCase().includes(inputVal) || isSubsequence(title.toLowerCase(), inputVal.toLowerCase()));
    setFiltered(titles);
})
searchBox.oninput = (event) => {
    debouncedSearch(event.target.value)
}

const handlePage = (currentPage) => {
    console.log(currentPage)
    let filtered = getFiltered();
    let maxPage = Math.floor(filtered.length / max)

    if (currentPage == "end") {
        setCurrentPage(maxPage);
        return;
    }

    if (currentPage == "start") {
        setCurrentPage(0);
        return;
    }

    if (currentPage < 0) {
        currentPage = 0;
    }

    if (currentPage * max > filtered.length) {
        currentPage = maxPage
    }

    setCurrentPage(currentPage);
}

startBtn.onclick = () => {
    handlePage('start')
};
endBtn.onclick = () => {
    handlePage('end')
};
leftBtn.onclick = () => {
    let newPage = getCurrentPage() - 1;
    handlePage(newPage);
};
rightBtn.onclick = () => {
    let newPage = getCurrentPage() + 1;
    handlePage(newPage);
};

fetchQuestions().then(displayQuestions);
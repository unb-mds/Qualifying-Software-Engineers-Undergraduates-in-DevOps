'use strict';

// Fix back button cache problem
window.onunload = function () {};

// Global variable, shared between modules
const playgroundText = (playground) => {
    const codeBlock = playground.querySelector("code");
    if (window.ace && codeBlock.classList.contains("editable")) {
        const editor = window.ace.edit(codeBlock);
        return editor.getValue();
    } else {
        const text = (codeBlock.textContent[0] === '$' && codeBlock.classList.contains("language-bash"))
            ? codeBlock.textContent.slice(2)
            : codeBlock.textContent;
        return text;
    }
};

const fetchWithTimeout = async (url, options, timeout = 6000) => {
    const controller = new AbortController();
    const timeoutId = setTimeout(() => controller.abort(), timeout);

    try {
        const response = await fetch(url, { ...options, signal: controller.signal });
        return await response.json();
    } catch (error) {
        if (error.name === 'AbortError') {
            throw new Error('timeout');
        } else {
            throw error;
        }
    } finally {
        clearTimeout(timeoutId);
    }
};

const handleCrateListUpdate = (playgroundBlock, playgroundCrates) => {
    updatePlayButton(playgroundBlock, playgroundCrates);

    if (window.ace) {
        const codeBlock = playgroundBlock.querySelector("code");
        if (codeBlock.classList.contains("editable")) {
            const editor = window.ace.edit(codeBlock);
            editor.getSession().on("change", () => updatePlayButton(playgroundBlock, playgroundCrates));
            editor.commands.addCommand({
                name: "run",
                bindKey: { win: "Ctrl-Enter", mac: "Ctrl-Enter" },
                exec: () => runRustCode(playgroundBlock)
            });
        }
    }
};

const updatePlayButton = (preBlock, playgroundCrates) => {
    const playButton = preBlock.querySelector(".play-button");

    if (preBlock.querySelector('code').classList.contains("no_run")) {
        playButton.classList.add("hidden");
        return;
    }

    const txt = playgroundText(preBlock);
    const re = /extern\s+crate\s+([a-zA-Z_0-9]+)\s*;/g;
    const snippetCrates = [];
    let item;
    while (item = re.exec(txt)) {
        snippetCrates.push(item[1]);
    }

    const allAvailable = snippetCrates.every(elem => playgroundCrates.includes(elem));

    if (allAvailable) {
        playButton.classList.remove("hidden");
    } else {
        playButton.classList.add("hidden");
    }
};

const runRustCode = async (codeBlock) => {
    let resultBlock = codeBlock.querySelector(".result");
    if (!resultBlock) {
        resultBlock = document.createElement('code');
        resultBlock.className = 'result hljs language-bash';
        codeBlock.append(resultBlock);
    }

    const text = playgroundText(codeBlock);
    const classes = codeBlock.querySelector('code').classList;
    const has2018 = classes.contains("edition2018");
    const edition = has2018 ? "2018" : "2015";

    const params = {
        version: "stable",
        optimize: "0",
        code: text,
        edition: edition
    };

    if (text.includes("#![feature")) {
        params.version = "nightly";
    }

    resultBlock.innerText = "Running...";

    try {
        const response = await fetchWithTimeout("https://play.rust-lang.org/evaluate.json", {
            headers: { 'Content-Type': "application/json" },
            method: 'POST',
            mode: 'cors',
            body: JSON.stringify(params)
        });
        resultBlock.innerText = response.result;
    } catch (error) {
        resultBlock.innerText = "Playground Communication: " + error.message;
    }
};

// Rest of the code remains the same...

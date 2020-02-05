const puppeteer = require('puppeteer');
const fs = require('fs');


const login = async () => {
    const browser = await puppeteer.launch({
        headless: false,
        slowMo: 10
    });
    const page = await browser.newPage();
    await page.goto('https://web.whatsapp.com', {
        waitUntil: 'load',
        timeout: 0
    });
    console.log('right after page.goto:')

    await page.waitForSelector('._1qNwV')
    const localStorageData = await page.evaluate(() => Object.assign({}, window.localStorage));
    let data = JSON.stringify(localStorageData);
    fs.writeFileSync('localStorageData.json', data);
    await browser.close();
    alert("Success!")
}

const sendMessage = async (to, message) => {
    // Open browser
    const browser = await puppeteer.launch({
        headless: false,
        slowMo: 10
    });
    const page = await browser.newPage();
    await page.goto('https://web.whatsapp.com', {
        waitUntil: 'load',
        timeout: 0
    });
    console.log('right after page.goto:')

    // Login
    if (!fs.existsSync('localStorageData.json')) {
        alert("Not logged in!")
        return
    }
    console.log("File exists: ")
    let rawdata = fs.readFileSync('localStorageData.json');
    let localStorageDataJSON = JSON.parse(rawdata);
    for(let key of Object.keys(localStorageDataJSON)) {
        console.log('key:', key, 'value:', localStorageDataJSON[key])
        await page.evaluate((key, localStorageDataJSON) => {
            localStorage.setItem(key, localStorageDataJSON[key]);
        }, key, localStorageDataJSON)
    }
    await page.goto('https://web.whatsapp.com', {
        waitUntil: 'load',
        timeout: 0
    })

    // Send message
    await page.waitForSelector('._1qNwV')
    await page.type('input', to, {
        delay: 30
    })
    await page.keyboard.press('Enter')
    await page.keyboard.type(message)
    await page.keyboard.press('Enter')
}

console.log('running logic.js...')

document.getElementById('login').addEventListener("click", function(){
    login();
});

document.getElementById('send').addEventListener("click", function() {
    const to = document.getElementById('to').value;
    const message = document.getElementById('message').value;
    sendMessage(to, message)
    .then(alert("Sent!"))
});
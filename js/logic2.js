const puppeteer = require('puppeteer');
const fs = require('fs');

let sendMessage = () => {}


(async () => {
    const browser = await puppeteer.launch({
        headless: false,
        // slowMo: 10
    });
    const page = await browser.newPage();
    await page.goto('https://web.whatsapp.com', {
        waitUntil: 'load',
        timeout: 0
    });
    console.log('right after page.goto:')
    if (fs.existsSync('localStorageData.json')) {
        console.log("File exists: ")
        let rawdata = fs.readFileSync('localStorageData.json');
        let localStorageDataJSON = JSON.parse(rawdata);
        for(let key of Object.keys(localStorageDataJSON)) {
            console.log('key:', key, 'value:', localStorageDataJSON[key])
            await page.evaluate((key, localStorageDataJSON) => {
                localStorage.setItem(key, localStorageDataJSON[key]);
            }, key, localStorageDataJSON)
          }
    }
    await page.goto('https://web.whatsapp.com', {
        waitUntil: 'load',
        timeout: 0
    });
    await page.waitForSelector('._1qNwV')
    const localStorageData = await page.evaluate(() => Object.assign({}, window.localStorage));
    let data = JSON.stringify(localStorageData);
    fs.writeFileSync('localStorageData.json', data);
    sendMessage = async (to, message) => {
        await page.type('input', to, {
            delay: 20
        })
        await page.keyboard.press('Enter')
        await page.keyboard.type(message)
        await page.keyboard.press('Enter')
        alert("Sent!")
    }
    //   await browser.close();
})();

document.getElementById('send').addEventListener("click", function() {
    const to = document.getElementById('to').value;
    const message = document.getElementById('message').value;
    sendMessage(to, message)
});
"use strict";
console.log("Running hello.js...")

const electron = require('electron')
const { app, BrowserWindow } = require('electron')

const createWindow = async () => {
  // Create the browser window.
  let win = new BrowserWindow({
    width: 800,
    height: 600,
    webPreferences: {
      nodeIntegration: true
    }
  })

  // and load the index.html of the app.
  await win.loadFile('index2.html')
//   const button = win.document.getElementById('button')
  // console.log(win)
}

app.whenReady().then(createWindow)


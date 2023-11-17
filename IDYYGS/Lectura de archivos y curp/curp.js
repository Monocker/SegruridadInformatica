// Importamos las librerías necesarias
const puppeteer = require('puppeteer-extra');
const RecaptchaPlugin = require('puppeteer-extra-plugin-recaptcha');
const axios = require('axios');

// Configuramos puppeteer para usar el plugin de reCAPTCHA
puppeteer.use(
  RecaptchaPlugin({
    provider: { id: '2captcha', token: '6fef2c73a3fe89c12946df5a46508f22' }
  })
);

// Función para transcribir audio
async function transcribe(url) {
    try {
        const response = await axios.post('https://api.transcribir.com/', {audioUrl: url});  // Cambia la URL si es necesario
        return response.data.text;
    } catch (error) {
        console.error("Error en la transcripción:", error);
        return '';
    }
}

// Función para determinar el género después de resolver el captcha
async function checkGender(page) {
    try {
        const genderElement = await page.$x('/*[@id="ember341"]/section/div[1]/div/div[2]/form/div[2]/div[1]/div/div[2]/table/tr[5]/td[2]');
        const gender = await page.evaluate(el => el.textContent, genderElement[0]);
        
        if (gender === "MUJER") {
            console.log("Es mujer.");
        } else if (gender === "HOMBRE") {
            console.log("Es hombre.");
        } else {
            console.log("No se pudo determinar el género.");
        }
    } catch (error) {
        console.error("Error al determinar el género:", error);
    }
}

// Función principal para resolver el captcha
async function solveCaptcha() {
    const browser = await puppeteer.launch({ headless: false });
    const page = await browser.newPage();
    
    await page.goto('https://www.gob.mx/curp/');
    
    await page.type('#curpinput', 'pozd920418hdfrvv07');
    await page.click('#searchButton');
    
    await page.waitForTimeout(3000);

    const { solved, error } = await page.solveRecaptchas();
    
    if(solved) {
        console.log('✔️ El captcha ha sido resuelto');
    } else if(error) {
        console.error('Error al resolver el captcha:', error);
    }

    await page.waitForTimeout(5000);
    
    await checkGender(page);
    
    await browser.close();
}

// Manejador de errores no capturados
process.on('unhandledRejection', (reason, promise) => {
    console.log('Unhandled Rejection at:', promise, 'reason:', reason);
});

// Ejecutamos la función principal
solveCaptcha();

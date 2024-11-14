const playwright = require('playwright');
(async () => {
  const browser = await playwright['chromium'].launch({
    // headless: false, slowMo: 100, // Uncomment to visualize test
  });
  const page = await browser.newPage();

  // Load "https://accounts.google.com/v3/signin/identifier?continue=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F&emr=1&followup=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F&ifkv=AcMMx-doy8eeeEq2CKoGnO2Ke4xgLSEyHduZCLkeTyhH3igOLZmNW4fkua0BsUvSipzlIPRR3KhV&osid=1&passive=1209600&service=mail&flowName=GlifWebSignIn&flowEntry=ServiceLogin&dsh=S319048713%3A1731591776164728&ddm=1"
  await page.goto('https://accounts.google.com/v3/signin/identifier?continue=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F&emr=1&followup=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F&ifkv=AcMMx-doy8eeeEq2CKoGnO2Ke4xgLSEyHduZCLkeTyhH3igOLZmNW4fkua0BsUvSipzlIPRR3KhV&osid=1&passive=1209600&service=mail&flowName=GlifWebSignIn&flowEntry=ServiceLogin&dsh=S319048713%3A1731591776164728&ddm=1');

  // Resize window to 1920 x 970
  await page.setViewportSize({ width: 1920, height: 970 });

  // Click on <span> "Create account"
  await page.click('text=Create account');

  // Click on <span> "For my personal use"
  await Promise.all([
    page.click('text=For my personal use'),
    page.waitForNavigation()
  ]);

  // Click on <input> #firstName
  await page.click('#firstName');

  // Fill "SDAdhui123" on <input> #firstName
  await page.fill('#firstName', 'SDAdhui123');

  // Click on <input> #firstName
  await page.click('#firstName');

  // Click on <input> #firstName
  await page.click('#firstName');

  // Press c on input
  await page.press('#firstName', 'c');

  // Click on <input> #lastName
  await page.click('#lastName');

  // Fill "SDAdhui123" on <input> #lastName
  await page.fill('#lastName', 'SDAdhui123');

  // Click on <span> "Next"
  await Promise.all([
    page.click('text=Next'),
    page.waitForNavigation()
  ]);

  // Click on <select> #month
  await page.click('#month');

  // Click on <select> #month
  await page.click('#month');

  // Click on <select> #month
  await page.click('#month');

  // Fill "5" on <select> #month
  await page.selectOption('#month', '5');

  // Click on <input> #day
  await page.click('#day');

  // Fill "20" on <input> #day
  await page.fill('#day', '20');

  // Press Tab on input
  await page.press('#day', 'Tab');

  // Fill "1995" on <input> #year
  await page.fill('#year', '1995');

  // Click on <select> #gender
  await page.click('#gender');

  // Fill "1" on <select> #gender
  await page.selectOption('#gender', '1');

  // Click on <span> "Next"
  await page.click('text=Next');

  await browser.close();
})();
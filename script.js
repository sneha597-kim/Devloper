const { Builder, By } = require("selenium-webdriver");
const edge = require("selenium-webdriver/edge");

async function testPizzaForm() {

    let service = new edge.ServiceBuilder("C:\\Program Files\\WebDriver\\msedgedriver.exe");

    let driver = new Builder()
        .forBrowser("MicrosoftEdge")
        .setEdgeService(service)
        .build();

    try {
        await driver.get("file:///C:/Users/sneha/OneDrive/Desktop/Devops/pizza.html");

        await driver.findElement(By.css("input[type='text']")).sendKeys("Snehalatha");
        await driver.findElement(By.css("input[value='Medium']")).click();
        await driver.findElement(By.css("input[value='Cheese']")).click();
        await driver.findElement(By.css("input[value='Paneer']")).click();
        await driver.findElement(By.tagName("textarea")).sendKeys("Hyderabad, India");

        console.log("✅ Pizza form test completed successfully!");

        // 👉 Keep browser open for 5 seconds
        await driver.sleep(5000);

    } finally {
        await driver.quit();
    }
}

testPizzaForm();

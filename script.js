//developing
const apiKey = "747bc751227d7cb8157aa9731391e1bd";

function getWeather() {
    const city = document.getElementById("city").value;
    const result = document.getElementById("weather-result");

    if (!city) {
        result.innerHTML = "❌ Please enter a city name";
        return;
    }

    const url = `https://api.openweathermap.org/data/2.5/weather?q=${city}&units=metric&appid=${apiKey}`;

    fetch(url)
        .then(response => response.json())
       .then(data => {
    if (data.cod === "404") {
        result.innerHTML = "❌ City not found";
        return;
    }

    const temp = data.main.temp;
    const weather = data.weather[0].main.toLowerCase();

    // 🌈 Change background based on weather
    let bgImage = "";

    if (weather.includes("rain")) {
        bgImage = "https://images.unsplash.com/photo-1501594907352-04cda38ebc29";
    } else if (weather.includes("cloud")) {
        bgImage = "https://images.unsplash.com/photo-1501630834273-4b5604d2ee31";
    } else if (weather.includes("clear") && temp > 25) {
        bgImage = "https://images.unsplash.com/photo-1502082553048-f009c37129b9";
    } else if (temp < 15) {
        bgImage = "https://images.unsplash.com/photo-1519681393784-d120267933ba";
    } else {
        bgImage = "https://images.unsplash.com/photo-1500740516770-92bd004b996e";
    }

    document.body.style.backgroundImage =
        `linear-gradient(rgba(0,0,0,0.2), rgba(0,0,0,0.2)), url('${bgImage}')`;

    result.innerHTML = `
        <h3>${data.name}, ${data.sys.country}</h3>
        <p>🌡️ Temperature: ${temp} °C</p>
        <p>☁️ Weather: ${data.weather[0].description}</p>
        <p>💧 Humidity: ${data.main.humidity}%</p>
        <p>🌬️ Wind: ${data.wind.speed} m/s</p>
    `;
})}

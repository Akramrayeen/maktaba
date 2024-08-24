const countryDropdown = document.getElementById("country");
const stateDropdown = document.getElementById("state");
const cityDropdown = document.getElementById("city");

// Fetch country data from OpenWeatherMap API
fetch("https://restcountries.com/v3.1/all")
  .then(response => response.json())
  .then(data => {
    data.forEach(country => {
      const option = document.createElement("option");
      option.value = country.name.common;
      option.textContent = country.name.common;
      countryDropdown.appendChild(option);
    });
  })
  .catch(error => console.error("Error fetching countries:", error));

// Fetch states based on selected country
function fetchStates() {
  const selectedCountry = countryDropdown.value;
  stateDropdown.innerHTML = "<option value=''>Select a state</option>"; // Clear previous states

  // Fetch state data from OpenWeatherMap API
  fetch(`https://api.openweathermap.org/data/2.5/states/${selectedCountry}?appid=YOUR_API_KEY`)
    .then(response => response.json())
    .then(states => {
      states.forEach(state => {
        const option = document.createElement("option");
        option.value = state.name;
        option.textContent = state.name;
        stateDropdown.appendChild(option);
      });
    })
    .catch(error => console.error("Error fetching states:", error));
}

// Fetch cities based on selected state
function fetchCities() {
  const selectedState = stateDropdown.value;
  cityDropdown.innerHTML = "<option value=''>Select a city</option>"; // Clear previous cities

  // Fetch city data from OpenWeatherMap API
  fetch(`https://api.openweathermap.org/data/2.5/cities/${selectedState}?appid=YOUR_API_KEY`)
    .then(response => response.json())
    .then(cities => {
      cities.forEach(city => {
        const option = document.createElement("option");
        option.value = city.name;
        option.textContent = city.name;
        cityDropdown.appendChild(option);
      });
    })
    .catch(error => console.error("Error fetching cities:", error));
}

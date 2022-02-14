get_country = () => {
    let country = document.getElementById("country_select").value;
    if (country == "") {
        alert("Please select a country");
        return;
    }
    let url = "/statistics/" + country;
    window.location.href = url;
}
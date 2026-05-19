// SOCKET SETUP
var socket = io();

// NOTIFICATION FUNCTION 
function showNotification(message) {
    const notify = document.createElement("div");
    notify.classList.add("notification");
    notify.innerText = message;
    document.body.appendChild(notify);

    setTimeout(() => notify.classList.add("show"), 100);
    setTimeout(() => {
        notify.classList.remove("show");
        setTimeout(() => notify.remove(), 500);
    }, 4000);
}

//  REAL-TIME MARKER 
socket.on("new_marker", function(data){
    const marker = L.marker([data.lat, data.lng], {
        riseOnHover: true
    }).addTo(map)
      .bindPopup(`<b>Risk:</b> ${data.risk}`)
      .openPopup();

    marker.setOpacity(0);
    let opacity = 0;
    const fade = setInterval(() => {
        opacity += 0.1;
        marker.setOpacity(opacity);
        if(opacity >= 1) clearInterval(fade);
    }, 50);
});

//  RISK ALERT 
socket.on("risk_alert", function(data){
    showNotification(data.msg);
});

// SOS FUNCTION 
function triggerSOS(){
    document.getElementById("sosSound").play();

    navigator.geolocation.getCurrentPosition(function(pos){
        fetch("/predict_risk",{
            method:"POST",
            headers:{"Content-Type":"application/json"},
            body:JSON.stringify({
                lat:pos.coords.latitude,
                lng:pos.coords.longitude,
                crime_rate:Math.random()*10,
                hour:new Date().getHours()
            })
        });
    });
}

//  OFFLINE DETECTION
window.addEventListener("offline", function(){
    showNotification("⚠ You are offline. Alerts will send when internet returns.");
});

window.addEventListener("online", function(){
    showNotification(" Internet connection restored.");
});
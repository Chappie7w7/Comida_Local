document.addEventListener("DOMContentLoaded", function () {
    const lugares = window.datosLugares;

    const mapa = L.map('map');
    const grupo = L.featureGroup();

    lugares.forEach(lugar => {
        const marcador = L.marker([lugar.lat, lugar.lng]).addTo(mapa);
        marcador.bindPopup(`<strong>${lugar.nombre}</strong><br>${lugar.descripcion}`);
        grupo.addLayer(marcador);
    });

    grupo.addTo(mapa);
    mapa.fitBounds(grupo.getBounds(), { padding: [50, 50] });

    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        attribution: '&copy; OpenStreetMap contributors'
    }).addTo(mapa);
});

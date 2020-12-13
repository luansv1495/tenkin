var root = document.getElementById('root');

window.onload = () => {
    'use strict';
    //Descomente para ativar o serviceWorker, não é recomendado habilita-lo em desenvolvimento.
    //if('serviceWorker' in navigator) navigator.serviceWorker.register('./service-worker.js');
    if (typeof(root) != 'undefined' && root != null) root.innerHTML = "<strong>Ola gente</strong>"
}
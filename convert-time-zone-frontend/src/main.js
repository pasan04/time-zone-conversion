import { createApp } from 'vue';
import App from './App.vue';
import TimeZoneConversion from './components/TimeZoneConversion.vue';
import 'bootstrap'; 
import 'bootstrap/dist/css/bootstrap.min.css';

const app = createApp(App);

app.component('time-conversion', TimeZoneConversion);

app.mount('#app');


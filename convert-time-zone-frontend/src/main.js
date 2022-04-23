import { createApp } from 'vue';
import App from './App.vue';
import TimeZoneConversion from './components/TimeZoneConversion.vue';
import 'bootstrap'; 
import 'bootstrap/dist/css/bootstrap.min.css';
import VueSimpleAlert from "vue3-simple-alert";


const app = createApp(App);
app.component('time-conversion', TimeZoneConversion);
app.use(VueSimpleAlert);
app.mount('#app');


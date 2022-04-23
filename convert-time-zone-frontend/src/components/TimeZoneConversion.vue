<template>
    <div class="form-inline">
        <select style="background: #282c34; padding: 1rem; border-radius: 0.3rem; color: white; margin-right: 20px; border: #282c34; width:300px; " v-model="selectedTimeZone">
          <option selected disabled>Select Time Zone</option>
          <option v-for="(item, index) in allTimeZones" :value="item.id" :key="index">{{ item.name }}</option>
        </select>
        <button type="button" style="background: rgb(0,100,0); padding: 1rem; border-radius: 0.3rem; border: rgb(0,100,0); margin-right: 20px; margin-top: 5px;color: white; width:300px" @click="submitTimeZoneConversion">SUBMIT</button>
    </div>
    <div class="form-inline">
      <div class="box">
        <p style="margin: 20px; font-size: 30px;">{{selectedTime}}</p>
      </div>
    </div>
    <div class="form-inline">
      <p style="margin: 20px; font-size: 30px;">{{selectedDate}}</p>
    </div>
    <div class="form-inline">
      <p style="margin: 20px; font-size: 30px;">Time Zone ({{selectedDateAndTime.selectedTimeZone}})</p>
    </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      allTimeZones: [],
      selectedTimeZone: 'Select Time Zone',
      isLoading: false,
      selectedDateAndTime: '',
      selectedDate: '',
      selectedTime: ''
    };
  },
  methods: {
    loadTimeZones() {
      this.isLoading = true;
      fetch('http://localhost:8080/api/getalltimezones')
        .then((response) => {
            return response.json();
        })
        .then((data) => {
          this.isLoading = false;
          const results = [];
          for (const i in data.timeZones) {
            results.push({
              id: data.timeZones[i].id,
              name: data.timeZones[i].name,
            });
          }
          this.allTimeZones = results;
        });
    },
    submitTimeZoneConversion(){
      const currentTimezone = Intl.DateTimeFormat().resolvedOptions().timeZone;
      const currentDateAndTime = {
        currentTimeZone: currentTimezone,
        selectTimeZone: this.selectedTimeZone
      }
      axios.post('http://localhost:8080/api/getcurrentzonetime',currentDateAndTime)
      .then(response =>{
          this.selectedDateAndTime = response.data;
          this.selectedDateTimeRun(response.data.convertedDate+ ' '+ response.data.convertedTime);
      }).catch(error =>{
          console.log(error);
      });
    },
    selectedDateTimeRun(dateTime){
      setInterval(() => {
        console.log(dateTime)
        // const d = new Date(dateTime);
        this.selectedDate = new Date().toLocaleDateString(); 
        this.selectedTime = new Date().toLocaleTimeString(); 
      }, 1000)
    }
  },
  mounted(){
    this.loadTimeZones();
  }
};
</script>
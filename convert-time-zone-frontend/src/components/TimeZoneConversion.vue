<template>
    <div class="form-inline">
        <select style="background: #282c34; padding: 1rem; border-radius: 0.3rem; color: white; border: #282c34; width:300px; margin-left: 5px;" v-model="selectedTimeZone">
          <option selected disabled>Select Time Zone</option>
          <option v-for="(item, index) in allTimeZones" :value="item.id" :key="index" :disabled="!isLoadedTimeZones">{{ item.name }}</option>
        </select>
        <button type="button" style="background: rgb(0,100,0); padding: 1rem; border-radius: 0.3rem; border: rgb(0,100,0); margin-left: 5px; margin-top: 5px;color: white; width:300px" @click="submitTimeZoneConversion">SUBMIT</button>
    </div>
    <div class="welcome" v-if="isLoadingSelectedTimeZone">
      <div class="form-inline">
          <p style="margin-top:10px; font-size: 25px; font-weight: bold;">{{welcomeMsg}}</p>
      </div>
    </div>
    <div v-if="!isLoadingSelectedTimeZone">
      <div class="form-inline">
        <div class="box">
          <div class="form-inline">
              <p style="margin-top:10px; font-size: 25px; font-weight: bold;">{{selectedTime}}</p>
          </div>
        </div>
      </div>
      <div class="form-inline">
        <p style="margin: 20px; font-size: 30px; font-weight: bold;">{{selectedDate}}</p>
      </div>
      <div class="form-inline">
        <p  style="margin-bottom: 30px; font-size: 30px; font-weight: bold;">Selected Time Zone - {{selectedDateAndTime.selectedTimeZone}}</p>
      </div>
    </div>
</template>

<script>
import axios from 'axios';
import moment from 'moment';
import * as constants from '../shared/constant';

export default {
  data() {
    return {
      welcomeMsg: 'WELCOME TO TIMEZONE CONVERTER',
      allTimeZones: [],
      selectedTimeZone: 'Select Time Zone',
      isLoadedTimeZones: false,
      isLoadingSelectedTimeZone: true,
      selectedDateAndTime: '',
      selectedDate: '',
      selectedTime: '',
      alreadyRunningTime: false,
      stopRunTimeEvent: '',
    };
  },
  methods: {
    loadTimeZones() {
      this.isLoadedTimeZones = false;
      axios.get(constants.url+'/api/getalltimezones')
        .then(res =>{
          let data = res.data;
          this.isLoadedTimeZones = true;
          const results = [];
          for (const i in data.timeZones) {
            results.push({
              id: data.timeZones[i].id,
              name: data.timeZones[i].name,
            });
          }
          this.allTimeZones = results;
        }).catch(error =>{
            console.log(error);
        });
    },
    submitTimeZoneConversion(){
      this.isLoadingSelectedTimeZone = true;
      const currentDateAndTime = {
        selectTimeZone: this.selectedTimeZone
      }
      const headers = {
            'Content-Type': 'text/plain'
      };
      axios.post(constants.url+'/api/getcurrentzonetime',currentDateAndTime,
      {headers}
      ).then(response =>{
          this.selectedDateAndTime = response.data;
          this.isLoadingSelectedTimeZone = false;
          if(this.alreadyRunningTime){
            clearInterval(this.stopRunTimeEvent);
            this.selectedDateTimeRun(response.data.convertedDate+ ' '+ response.data.convertedTime);
          }else{
            this.selectedDateTimeRun(response.data.convertedDate+ ' '+ response.data.convertedTime);
          }
      }).catch(error =>{
          console.log(error);
      });
    },
    selectedDateTimeRun(selectedDateAndTime){
      this.alreadyRunningTime = true;
      let date = new Date(selectedDateAndTime);
      this.stopRunTimeEvent = setInterval(() => {
        date = new Date(date.getTime() + 1000);
        this.selectedDate = new Date(date).toLocaleDateString(); 
        this.selectedTime = new Date(date).toLocaleTimeString(); 
      }, 1000)
    },
    moment: function () {
      return moment();
    }
  },
  mounted(){
    this.loadTimeZones();
  }
};
</script>
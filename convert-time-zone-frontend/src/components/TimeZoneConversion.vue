<template>
    <div class="form-inline">
        <select style="background: #282c34; padding: 1rem; border-radius: 0.3rem; color: white; margin-right: 20px; border: #282c34; width:300px;" v-model="selectedTimeZone">
          <option selected disabled>Select Time Zone</option>
          <option v-for="(item, index) in allTimeZones" :value="item.id" :key="index">{{ item.name }}</option>
        </select>
        <button type="button" style="background: rgb(0,100,0); padding: 1rem; border-radius: 0.3rem; border: rgb(0,100,0); margin-right: 20px; margin-top: 5px;color: white; width:300px" @click="submitTimeZoneConversion">SUBMIT</button>
    </div>
</template>


<script>
export default {
  data() {
    return {
      allTimeZones: [],
      selectedTimeZone: 'Select Time Zone',
      isLoading: false
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
      const object = {
        currentTimeZone: currentTimezone,
        selectTimeZone: this.selectedTimeZone
      }
      fetch('http://localhost:8080/api/getcurrentzonetime',{
        method: 'POST',
        headers: {
          'Accept': 'application/json',
          'Content-Type': 'application/json',
          'Access-Control-Allow-Origin': '*'
      },
        body: JSON.stringify(object)
      });
    }
  },
  mounted(){
    this.loadTimeZones();
  }
};
</script>
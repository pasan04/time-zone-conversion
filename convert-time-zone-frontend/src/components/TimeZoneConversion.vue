<template>
    <div class="form-inline">
        <select style="background: #282c34; padding: 1rem; border-radius: 0.3rem; color: white; margin-right: 20px; width:300px;" v-model="selectedTimeZone">
          <option selected disabled>Select Time Zone</option>
          <option v-for="(item, index) in allTimeZones" :value="item.id" :key="index">{{ item.name }}</option>
        </select>
        <button type="button" style="background: #282c34; padding: 1rem; border-radius: 0.3rem; border: #282c34; margin-right: 20px; margin-top: 5px;color: white; width:300px" @click="submitTimeZoneConversion">Submit</button>
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
          console.log(this.allTimeZones);
        });
    },
    submitTimeZoneConversion(){
      console.log(this.selectedTimeZone);
      //post the submission




    }
  },
  mounted(){
    this.loadTimeZones();
  }
};
</script>
<template>
  <section>
    <div class= "diplay-current-time">
      <p>{{showDateTime}}</p>
    </div>
    <header>
      <h1>{{timeZoneConverterHeader}}</h1>
    </header>
    <div class= "display-time-zones">
      <time-conversion></time-conversion>
    </div>
  </section>
</template>


<script>
export default {
  name: 'App',

  data(){
    return {
      showDateTime: '',
      selectedValue: null,
      timeZoneConverterHeader: 'TIME ZONE CONVERTER'
    }
  },

  methods: {
    getCurrentDateTime(){
      this.showDateTime = new Date().toLocaleString();
    }
  },

  created(){
    setInterval(() => {
      this.getCurrentDateTime();
    }, 1000)
  }
}
</script>

<style>
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

.diplay-current-time{
  text-align: right;
  display: block;
  padding: 10px 25px;
  color: #FFF;
  font-size: 20px;
  font-weight: 00;
  margin-top: 20px;
}

.display-time-zones{
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.26);
  margin: 2rem auto;
  border-radius: 10px;
  padding: 1rem;
  background-color: rgba(255,255,255, 0.75);
  color: black;
  text-align: center;
  width: 80%;
  max-width: 100rem;
  height: 400px;
}

.display-time-zone-button{
  display: flex;
  flex-direction: row;
  flex-wrap: wrap;
  align-items: center;
  justify-content: center;
  padding: 3rem;
}

html {
  font-family: 'Jost', sans-serif;
}

body {
  margin: 0;
  background-image: url('./assets/background.jpg');
  background-size: cover;
}

header {
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.26);
  margin: 2rem auto;
  border-radius: 10px;
  padding: 1rem;
  background-color: white;
  color: black;
  text-align: center;
  width: 80%;
  max-width: 100rem;
}

#app button {
  font: inherit;
  cursor: pointer;
  border: 1px solid #ff0077;
  background-color: #ff0077;
  color: white;
  padding: 0.05rem 1rem;
  box-shadow: 1px 1px 2px rgba(0, 0, 0, 0.26);
}

#app button:hover,
#app button:active {
  background-color: #ec3169;
  border-color: #ec3169;
  box-shadow: 1px 1px 4px rgba(0, 0, 0, 0.26);
}
</style>

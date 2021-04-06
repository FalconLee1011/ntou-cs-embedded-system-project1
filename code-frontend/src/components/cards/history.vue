<template>
  <div>
    <v-tabs v-model="tab">
      <v-tab>溫度</v-tab>
      <v-tab>濕度</v-tab>
    </v-tabs>
    <v-tabs-items v-if="isReady" v-model="tab">
      <v-tab-item>
        <chartsComposer :chart-data="temp" :height="100" ></chartsComposer> 
      </v-tab-item>
      <v-tab-item>
        <chartsComposer :chart-data="humd" :height="100" ></chartsComposer> 
      </v-tab-item>
    </v-tabs-items>
    <v-progress-circular indeterminate v-else></v-progress-circular>
  </div>
</template>

<script>
// import charts from "./charts";
import chartsComposer from "./chartsComposer.js";

export default {
  components: { chartsComposer }, 
  data() {
    return {
      tab: 0, 
      temp: undefined, 
      humd: undefined, 
      isReady: false, 
    }
  },
  created() {
    setInterval(() => {
      this.fetchData();
    }, 1000);
  },
  methods: {
    async fetchData() {
      const res = await this.$axios.get("/latest");
      const data = res.data;
      let labels = res.data.timestamp;

      for (const key in data.data) {
        this[key] = {
          datasets: [
            {
              label: key,
              backgroundColor: '#10ffff', 
              borderColor: '#50bcff', 
              fill: false,
              data: data.data[key],
            }
          ], 
          labels: labels, 
        }
      }
      this.isReady = true;
    },
  },
}
</script>
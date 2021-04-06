<template>
  <v-card>
    <v-card-title primary-title>
      {{title}}
    </v-card-title>
    <v-card-text>
      <chartsComposer :chart-data="data" :height="100" ></chartsComposer> 
    </v-card-text>
  </v-card>
</template>

<script>
import chartsComposer from "./chartsComposer.js";
export default {
  components: { chartsComposer }, 
  props:{
    title: {
      type: String, 
      default: "Dummy chart"
    }, 
    data: {
      type: Array, 
    }
  }, 
  mounted() {},
}
</script>
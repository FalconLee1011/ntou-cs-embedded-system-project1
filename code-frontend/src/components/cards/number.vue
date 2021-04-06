<template>
  <v-card elevation="10">
    <v-card-title>{{title}}</v-card-title>
    <v-card-subtitle>{{subtitle}}</v-card-subtitle>
    <v-card-text>
      <div class="info-area">
        <span class="hightlight">
          <span class="primary--text">{{data}}</span>
        </span>
        <span class="unit">{{unit}}</span>
      </div>
    </v-card-text>
  </v-card>
</template>

<script>
export default {
  props:{
    title:{
      type: String, 
      default: "Title", 
    }, 
    subtitle:{
      type: String, 
      default: "Subtitle", 
    }, 
    data:{
      type: String, 
      default: "0xE88D94", 
    }, 
    unit:{
      type: String, 
      default: "草", 
    }, 
  }
}
</script>

<style scoped>
.info-area{
  margin-top: 1rem;
  text-align: center;
}
.hightlight{
  color: #50bcff;
  font-size: 400%;
}
.unit{
  font-size: 200%;
}
</style>
<template>
  <v-container style="min-width: 90%" elevation="10">
    <v-card class="mb-5">
      <v-card-title primary-title> Dashboard </v-card-title>
      <v-card-text class="mb-5">
        <v-card elevation="10" class="mb-5">
          <v-card-subtitle primary-title> 最新資料 </v-card-subtitle>
          <v-card-text>
            <v-row>
              <v-col> 
                <number 
                  title="Temperature"
                  subtitle="溫度"
                  :data="data.temp.toString()"
                  unit="°C"
                />
              </v-col>
              <v-col> 
                <number 
                  title="Humidity"
                  subtitle="濕度"
                  :data="data.humd.toString()"
                  unit="%"
                />
              </v-col>
            </v-row>
            <v-row>
              <v-col> 
                <number 
                  title="Last Update"
                  subtitle="資料更新時間"
                  :data="data.timestamp"
                  unit=""
                />
              </v-col>
            </v-row>
          </v-card-text>
        </v-card>
        <v-card elevation="10" class="mb-5">
          <v-card-subtitle primary-title> 歷史資訊 </v-card-subtitle>
          <v-card-text>
            <history />
          </v-card-text>
        </v-card>
      </v-card-text>
    </v-card>
  </v-container>
</template>

<script>
import number from "./cards/number";
import history from "./cards/history";

export default {
  components: { number, history },
  data() {
    return {
      data: {
        humd: 0, 
        temp: 0, 
      }, 
    };
  },
  created() {
    setInterval(() => {
      this.fetchData();
    }, 1000);
  },
  methods: {
    async fetchData() {
      const res = await this.$axios.get("/last");
      this.data = res.data[0];
      // humd: 58, temp: 26.9, timestamp: "Tue, 06 Apr 2021 20:22:19 GMT"}
    },
  },
};
</script>
// import { Line } from 'vue-chartjs'
import { Line, mixins } from 'vue-chartjs'
const { reactiveProp } = mixins

export default {
  mixins: [reactiveProp],
  extends: Line,
  mounted() {
    this.renderChart(
      this.chartData, 
      this.options
    )
  }
}
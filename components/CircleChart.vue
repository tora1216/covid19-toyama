<template>
  <data-view :title="title" :title-id="titleId" :date="date" :url="url" :url-text="urlText">
    <template v-slot:description>
      <div v-if="descriptions && descriptions.length > 0">
        <div v-for="text in descriptions">
         {{ $t(text) }}
        </div>
      </div>
    </template>

    <pie-chart
      :chart-id="chartId"
      :chart-data="displayData"
      :options="displayOption"
      :height="240"
    />
  </data-view>
</template>

<script>
import DataView from '@/components/DataView.vue'
import DataViewBasicInfoPanel from '@/components/DataViewBasicInfoPanel.vue'
export default {
  components: { DataView, DataViewBasicInfoPanel },
  props: {
    title: {
      type: String,
      required: false,
      default: ''
    },
    titleId: {
      type: String,
      required: false,
      default: ''
    },
    chartId: {
      type: String,
      required: false,
      default: 'pie-chart'
    },
    chartData: {
      type: Array,
      required: false,
      default: () => []
    },
    date: {
      type: String,
      required: true,
      default: ''
    },
    unit: {
      type: String,
      required: false,
      default: ''
    },
    info: {
      type: String,
      required: false,
      default: ''
    },
    url: {
      type: String,
      required: false,
      default: ''
    },
    urlText: {
      type: String,
      required: false,
      default: ''
    },
    descriptions: {
      type: Array,
      required: false,
      default: () => []
    }
  },
  computed: {
    displayInfo() {
      return {
        lText: this.chartData[
          this.chartData.length - 1
        ].cumulative.toLocaleString(),
        sText: this.info,
        unit: this.unit
      }
    },
    displayData() {
      const colorArray = ['#1b4d30', '#00a040', '#c5e2c6']
      return {
        labels: this.chartData.map(d => {
          return d.label
        }),
        datasets: [
          {
            label: this.chartData.map(d => {
              return d.label
            }),
            data: this.chartData.map(d => {
              return d.transition
            }),
            backgroundColor: this.chartData.map((d, index) => {
              return colorArray[index]
            }),
            borderWidth: 0
          }
        ]
      }
    },
    displayOption() {
      const unit = this.unit
      const chartData = this.chartData
      return {
        tooltips: {
          displayColors: false,
          callbacks: {
            label(tooltipItem) {
              return `${chartData[tooltipItem.index].transition} ${unit} (${Math.round(chartData[tooltipItem.index].transition/(chartData[0].transition +
                chartData[1].transition+chartData[2].transition)*100)} %)`
            },
            title(tooltipItem, data) {
              return data.labels[tooltipItem[0].index]
            }
          }
        },
        responsive: true,
        maintainAspectRatio: false,
        legend: {
          display: true
        }
      }
    }
  }
}
</script>

<style lang="scss" scoped>
.Graph-Desc {
  margin: 10px 0;
  font-size: 12px;
  color: $gray-3;
}
.link {
  text-decoration: none;
}
</style>

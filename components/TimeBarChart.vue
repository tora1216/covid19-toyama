<template>
  <data-view :title="title" :title-id="titleId" :date="date" :url="url">
    <template v-slot:description>
      <slot name="description" />
    </template>
    <template v-if="showButton" v-slot:button>
      <data-selector
        v-model="dataKind"
        :target-id="chartId"
        :transition-type="transitionType"
        :style="{ display: canvas ? 'inline-block' : 'none' }"
      />
    </template>
    <bar
      :style="{ display: canvas ? 'block' : 'none' }"
      :chart-id="chartId"
      :chart-data="displayData"
      :options="displayOption"
      :height="240"
    />
    <template  v-if="showButton">
      <date-select-slider
        :chart-data="chartData"
        :value="[0, sliderMax]"
        :slider-max="sliderMax"
        @sliderInput="sliderUpdate"
      />
    </template>
    <v-data-table
      :style="{ top: '-9999px', position: canvas ? 'fixed' : 'static' }"
      :headers="tableHeaders"
      :items="tableData"
      :items-per-page="-1"
      :hide-default-footer="true"
      :hide-default-header="true"
      :height="240"
      :fixed-header="true"
      :mobile-breakpoint="0"
      class="cardTable"
      item-key="name"
    />
    <template v-if="showButton" v-slot:infoPanel>
      <data-view-basic-info-panel
        :l-text="displayInfo.lText"
        :s-text="displayInfo.sText"
        :unit="displayInfo.unit"
      />
    </template>
  </data-view>
</template>

<script lang="ts">
import Vue from 'vue'
import { ThisTypedComponentOptionsWithRecordProps } from 'vue/types/options'
import { GraphDataType } from '@/utils/formatGraph'
import DataView from '@/components/DataView.vue'
import DataSelector from '@/components/DataSelector.vue'
import DateSelectSlider from '@/components/DateSelectSlider.vue'
import DataViewBasicInfoPanel from '@/components/DataViewBasicInfoPanel.vue'
import { single as color } from '@/utils/colors'
type Data = {
  dataKind: 'transition' | 'cumulative'
  canvas: boolean
  graphRange: number[]
}
type Methods = {
  formatDayBeforeRatio: (dayBeforeRatio: number) => string
  sliderUpdate: (sliderValue: number[]) => void
}
type Computed = {
  displayCumulativeRatio: string
  displayTransitionRatio: string
  displayInfo: {
    lText: string
    sText: string
    unit: string
  }
  displayData: {
    labels: string[]
    datasets: {
      label: 'transition' | 'cumulative'
      data: number[]
      backgroundColor: string
      borderWidth: number
    }[]
  }
  displayOption: {
    tooltips: {
      displayColors: boolean
      callbacks: {
        label(tooltipItem: any): string
        title(tooltipItem: any[], data: any): string | undefined
      }
    }
    responsive: boolean
    maintainAspectRatio: boolean
    legend: {
      display: boolean
    }
    scales: object
  }
  scaledTicksYAxisMax: number
  tableHeaders: {
    text: string
    value: string
  }[]
  tableData: {
    [key: number]: number
  }[]
  sliderMax: number
}
type Props = {
  title: string
  titleId: string
  chartId: string
  chartData: GraphDataType[]
  transitionType: string
  showButton: boolean
  forceDataKind: string
  date: string
  unit: string
  url: string
}
const options: ThisTypedComponentOptionsWithRecordProps<
  Vue,
  Data,
  Methods,
  Computed,
  Props
> = {
  created() {
    this.canvas = process.browser
    this.sliderUpdate([0, this.sliderMax])
  },
  components: {
    DataView,
    DataSelector,
    DateSelectSlider,
    DataViewBasicInfoPanel
  },
  props: {
    title: {
      type: String,
      default: ''
    },
    titleId: {
      type: String,
      default: ''
    },
    chartId: {
      type: String,
      default: 'time-bar-chart'
    },
    chartData: {
      type: Array,
      default: () => []
    },
    showButton: {
      type: Boolean,
      default: true
    },
    forceDataKind: {
      type: String,
      default: ''
    },
    transitionType: {
      type: String,
      default: 'daily'
    },
    date: {
      type: String,
      required: true
    },
    unit: {
      type: String,
      default: ''
    },
    url: {
      type: String,
      default: ''
    }
  },
  data: () => ({
    dataKind: 'transition',
    canvas: true,
    graphRange: [0, 1]
  }),
  computed: {
    displayCumulativeRatio() {
      const lastDay = this.chartData.slice(-1)[0].cumulative
      const lastDayBefore = this.chartData.slice(-2)[0].cumulative
      return this.formatDayBeforeRatio(lastDay - lastDayBefore)
    },
    displayTransitionRatio() {
      const lastDay = this.chartData.slice(-1)[0].transition
      const lastDayBefore = this.chartData.slice(-2)[0].transition
      return this.formatDayBeforeRatio(lastDay - lastDayBefore)
    },
    displayInfo() {
      if (this.forceDataKind !== '')
        this.dataKind =
          this.forceDataKind === 'transition' ? 'transition' : 'cumulative'
      if (this.dataKind === 'transition') {
        return {
          lText: `${this.chartData.slice(-1)[0].transition.toLocaleString()}`,
          sText: `${this.chartData.slice(-1)[0].label} ${this.$t('実績値')}（${this.$t('前日比')}: ${
            this.displayTransitionRatio
          } ${this.unit}）`,
          unit: this.unit
        }
      }
      return {
        lText: `${this.chartData.slice(-1)[0].cumulative.toLocaleString()}`,
        sText: `${this.chartData.slice(-1)[0].label} ${this.$t(
          '累計値'
        )}（${this.$t('前日比')}: ${this.displayCumulativeRatio} ${
          this.unit
        }）`,
        unit: this.unit
      }
    },
    displayData() {
      if (this.dataKind === 'transition') {
        return {
          labels: this.chartData.map(d => {
            return d.label
          }),
          datasets: [
            {
              label: this.dataKind,
              data: this.chartData.map(d => {
                return d.transition
              }),
              backgroundColor: color,
              borderWidth: 0
            }
          ]
        }
      }
      return {
        labels: this.chartData.map(d => d.label),
        datasets: [
          {
            label: this.dataKind,
            data: this.chartData.map(d => {
              return d.cumulative
            }),
            backgroundColor: color,
            borderWidth: 0
          }
        ]
      }
    },
    displayOption() {
      const unit = this.unit
      const scaledTicksYAxisMax = this.scaledTicksYAxisMax
      const options = {
        animation: false,
        tooltips: {
          displayColors: false,
          callbacks: {
            label(tooltipItem: any) {
              const labelText = `${parseInt(
                tooltipItem.value
              ).toLocaleString()} ${unit}`
              return labelText
            },
            title(tooltipItem: any, data: any) {
              return data.labels[tooltipItem[0].index]
            }
          }
        },
        responsive: true,
        maintainAspectRatio: false,
        legend: {
          display: false
        },
        scales: {
          xAxes: [
            {
              position: 'bottom',
              stacked: false,
              gridLines: {
                display: false
              },
              ticks: {
                fontColor: '#808080',
                maxRotation: 60,
                minRotation: 0,
                max: this.chartData[this.graphRange[1]].label,
                min: this.chartData[this.graphRange[0]].label
              }
            }
          ],
          yAxes: [
            {
              location: 'bottom',
              stacked: true,
              gridLines: {
                display: true,
                color: '#E5E5E5'
              },
              ticks: {
                suggestedMin: 0,
                maxTicksLimit: 8,
                fontColor: '#808080',
                suggestedMax: scaledTicksYAxisMax
              }
            }
          ]
        }
      }
      if (this.$route.query.ogp === 'true') {
        Object.assign(options, { animation: { duration: 0 } })
      }
      return options
    },
    scaledTicksYAxisMax() {
      const yAxisMax = 1.2
      const dataKind =
        this.dataKind === 'transition' ? 'transition' : 'cumulative'
      const values = this.chartData.map(d => d[dataKind])
      return Math.max(...values) * yAxisMax
    },
    tableHeaders() {
      return [
        { text: '', value: 'text' },
        { text: this.title, value: '0' }
      ]
    },
    tableData() {
      return this.displayData.datasets[0].data.map((_, i) => {
        return Object.assign(
          { text: this.displayData.labels[i] },
          { '0': this.displayData.datasets[0].data[i] }
        )
      })
    },
    sliderMax() {
      if (!this.chartData || this.chartData.length === 0) {
        return 1
      }
      return this.chartData.length - 1
    }
  },
  methods: {
    formatDayBeforeRatio(dayBeforeRatio: number): string {
      const dayBeforeRatioLocaleString = dayBeforeRatio.toLocaleString()
      switch (Math.sign(dayBeforeRatio)) {
        case 1:
          return `+${dayBeforeRatioLocaleString}`
        case -1:
          return `${dayBeforeRatioLocaleString}`
        default:
          return `${dayBeforeRatioLocaleString}`
      }
    },
    sliderUpdate(sliderValue) {
      this.graphRange = sliderValue
    }
  }
}
export default Vue.extend(options)
</script>
<template>
  <data-view :title="title" :title-id="titleId" :date="date" :url="url">
    <template v-slot:button>
      <p class="Graph-Desc">
      </p>
    </template>
    <horizontal-bar
      :style="{ display: canvas ? 'block' : 'none' }"
      :chart-id="chartId"
      :chart-data="displayData"
      :options="displayOption"
      :height="240"
    />
    <template v-slot:infoPanel>
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
import { TranslateResult } from 'vue-i18n'
import { ThisTypedComponentOptionsWithRecordProps } from 'vue/types/options'
import { GraphDataType } from '@/utils/formatGraph'
import DataView from '@/components/DataView.vue'
import DataViewBasicInfoPanel from '@/components/DataViewBasicInfoPanel.vue'
import { single as color } from '@/utils/colors'
type Data = {
  dataKind: 'transition' | 'cumulative'
  canvas: boolean
  valueOfEach: number[]
}
type Methods = {}
type Computed = {
  displayInfo: {
    lText: string
    sText: string
    unit: string
  }
  displayData: {
    labels: string[]
    datasets: {
      label: TranslateResult
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
    legend: {
      display: boolean
    }
    scales: object
  }
}
type Props = {
  title: string
  titleId: string
  chartId: string
  chartData: GraphDataType[]
  date: string
  unit: string
  info: string
  labels: string[]
  url: string
  description: string
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
  },
  components: { DataView, DataViewBasicInfoPanel },
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
      default: 'horizontal-bar-chart'
    },
    chartData: {
      type: Array,
      default: () => []
    },
    date: {
      type: String,
      required: true
    },
    unit: {
      type: String,
      default: ''
    },
    info: {
      type: String,
      default: ''
    },
    labels: {
      type: Array,
      default: () => []
    },
    url: {
      type: String,
      default: ''
    },
    description: {
      type: String,
      default: ''
    }
  },
  data: () => ({
    dataKind: 'transition',
    canvas: true,
    valueOfEach: []
  }),
  computed: {
    displayInfo() {
      return {
        lText: '',
        sText: '',
        unit: ''
      }
    },
    displayData() {
      this.valueOfEach = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
      this.chartData.map((d: any) => {
        switch (d['居住地']) {
          case '舟橋村':
            this.valueOfEach[14] += 1
            break
          case '朝日町':
            this.valueOfEach[13] += 1
            break
          case '上市町':
            this.valueOfEach[12] += 1
            break
          case '入善町':
            this.valueOfEach[11] += 1
            break
          case '立山町':
            this.valueOfEach[10] += 1
            break
          case '小矢部市':
            this.valueOfEach[9] += 1
            break
          case '滑川市':
            this.valueOfEach[8] += 1
            break
          case '黒部市':
            this.valueOfEach[7] += 1
            break
          case '魚津市':
            this.valueOfEach[6] += 1
            break
          case '氷見市':
            this.valueOfEach[5] += 1
            break
          case '砺波市':
            this.valueOfEach[4] += 1
            break
          case '南砺市':
            this.valueOfEach[3] += 1
            break
          case '射水市':
            this.valueOfEach[2] += 1
            break
          case '高岡市':
            this.valueOfEach[1] += 1
            break
          case '富山市':
            this.valueOfEach[0] += 1
            break
          default:
            this.valueOfEach[15] += 1
            break
        }
      })
      return {
        labels: this.labels,
        datasets: [
          {
            label: this.$t('陽性者数'),
            data: this.valueOfEach,
            backgroundColor: color,
            borderWidth: 0
          }
        ]
      }
    },
    displayOption() {
      const unit = this.unit
      const valueOfEach = this.valueOfEach
      const _this = this
      const options = {
        tooltips: {
          displayColors: false,
          callbacks: {
            label(tooltipItem: any) {
              return `${valueOfEach[tooltipItem.index]} ${unit}`
            },
            title(tooltipItem: any, data: any) {
              return `${data.labels[tooltipItem[0].index]}`
            }
          }
        },
        legend: {
          display: false
        },
        scales: {
          xAxes: [
            {
              stacked: true,
              ticks: {
                suggestedMax: 50,
                suggestedMin: 0,
                stepSize: 5
              }
            }
          ],
          yAxes: [
            {
              stacked: true
            }
          ]
        }
      }
      return options
    }
  }
}
export default Vue.extend(options)
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
<template>
  <data-view :title="title" :title-id="titleId" :date="date">
    <template v-slot:description>
      <slot name="description" />
    </template>
    <bar
      :style="{ display: canvas ? 'block' : 'none' }"
      :chart-id="chartId"
      :chart-data="displayData"
      :options="displayOption"
      :height="240"
    />
    <v-data-table
      :style="{ top: '-9999px', position: canvas ? 'fixed' : 'static' }"
      :headers="tableHeaders"
      :items="tableData"
      :items-per-page="-1"
      :hide-default-footer="true"
      :height="240"
      :fixed-header="true"
      :mobile-breakpoint="0"
      class="cardTable"
      item-key="name"
    />
    <template v-slot:footer-description>
      <p>
        {{ $t('出典') }}：
        <a
          href="https://mobaku.jp/covid-19/"
          target="_blank"
          rel="noopenner"
          >{{ $t('NTTドコモ　モバイル空間統計') }}</a
        >
      </p>
    </template>
  </data-view>
</template>

<style module lang="scss">
.DataView {
  &Desc {
    margin-top: 10px;
    margin-bottom: 0 !important;
    font-size: 12px;
    color: $gray-3;
  }
}
</style>

<script lang="ts">
import Vue from 'vue'
import VueI18n from 'vue-i18n'
import { ChartOptions, ChartData } from 'chart.js'
import { ThisTypedComponentOptionsWithRecordProps } from 'vue/types/options'
import DataView from '@/components/DataView.vue'
import { quadruple as colors } from '@/utils/colors'

interface HTMLElementEvent<T extends HTMLElement> extends Event {
  currentTarget: T
}

type Data = {
  canvas: boolean
  i18nlabels: VueI18n.TranslateResult[]
}
type Methods = {}
type Computed = {
  displayData: {
    labels: string[]
    datasets: {
      label: string
      data: number[]
      backgroundColor: string
      borderWidth: number
    }[]
  }
  tableHeaders: {
    text: string
    value: string
  }[]
  tableData: {
    [key: number]: number
  }[]
  displayOption: {
    responsive: boolean
    legend: {
      display: boolean
      onHover: (e: HTMLElementEvent<HTMLInputElement>) => void
      onLeave: (e: HTMLElementEvent<HTMLInputElement>) => void
      labels: {
        boxWidth: number
      }
    }
    scales: {
      xAxes: object[]
      yAxes: object[]
    }
    tooltips: {
      displayColors: boolean
      callbacks: {
        title: (tooltipItems: any, data: any) => string
        label: (tooltipItems: any, data: any) => string
      }
    }
  }
}
type Props = {
  chartData: ChartData
  chartOption: ChartOptions
  chartId: string
  title: string
  titleId: string
  date: string
  unit: string
  tooltipsTitle: (tooltipItems: any, data: any) => string
  tooltipsLabel: (tooltipItems: any, data: any) => string
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
  components: { DataView },
  props: {
    title: {
      type: String,
      default: ''
    },
    titleId: {
      type: String,
      required: false,
      default: ''
    },
    chartData: Object,
    chartOption: Object,
    chartId: {
      type: String,
      default: 'population-bar-chart'
    },
    date: {
      type: String,
      required: true
    },
    unit: {
      type: String,
      required: false,
      default: '%'
    },
    tooltipsTitle: {
      type: Function,
      required: true
    },
    tooltipsLabel: {
      type: Function,
      required: true
    }
  },
  data() {
    const i18nlabels = [
      this.$t('感染拡大前比'),
      this.$t('緊急事態宣言前比'),
      this.$t('前年同月比'),
      this.$t('前日比'),
    ]
    return {
      canvas: true,
      i18nlabels,
    }
  },
  computed: {
    displayData() {
      const datasets = this.chartData.labels!.map((label, i) => {
        return {
          label: this.i18nlabels[i] as string,
          data: this.chartData.datasets!.map(d => d.data![i]) as number[],
          backgroundColor: colors[i],
          borderWidth: 0
        }
      })
      return {
        labels: this.chartData.datasets!.map(d => d.label!),
        datasets
      }
    },
    tableHeaders() {
      return [
        { text: '', value: 'text' },
        ...this.chartData.labels!.map((text, value) => {
          return { text: text as string, value: String(value) }
        })
      ]
    },
    tableData() {
      return this.displayData.datasets[0].data.map((_, i) => {
        return Object.assign(
          { text: this.chartData.datasets![i].label as string },
          ...this.chartData.datasets!.map((_, j) => {
            return {
              [j]: this.displayData.datasets[0].data[i]
            }
          })
        )
      })
    },
    displayOption() {
      const self = this
      const options = {
        responsive: true,
        legend: {
          display: true,
          onHover: (e: HTMLElementEvent<HTMLInputElement>) => {
            e.currentTarget.style.cursor = 'pointer'
          },
          onLeave: (e: HTMLElementEvent<HTMLInputElement>) => {
            e.currentTarget.style.cursor = 'default'
          },
          labels: {
            boxWidth: 20
          }
        },
        scales: {
          xAxes: [
            {
              position: 'bottom',
              stacked: false,
              gridLines: {
                display: true
              },
              ticks: {
                fontSize: 10,
                maxTicksLimit: 20,
                fontColor: '#808080'
              }
            }
          ],
          yAxes: [
            {
              stacked: false,
              gridLines: {
                display: true
              },
              ticks: {
                fontSize: 12,
                maxTicksLimit: 10,
                fontColor: '#808080',
                callback(value: any) {
                  return value + self.unit
                }
              }
            }
          ]
        },
        tooltips: {
          displayColors: false,
          callbacks: {
            title: self.tooltipsTitle,
            label: self.tooltipsLabel
          }
        }
      }
      if (this.$route.query.ogp === 'true') {
        Object.assign(options, { animation: { duration: 0 } })
      }
      return options
    }
  }
}

export default Vue.extend(options)
</script>

<template>
  <v-col cols="12" md="6" class="DataCard">
    <population-bar-chart
      :title="$t('富山駅付近の人口の推移')"
      :title-id="'changes-of-population-around-toyama-station'"
      :chart-id="'population-bar-chart'"
      :chart-data="populationGraph"
      :date="populationGraph.date"
      :tooltips-title="populationGraphTooltipTitle"
      :tooltips-label="populationGraphTooltipLabel"
      :url="''"
      :unit="$t('%')"
    >
      <template v-slot:description>
        <ul>
          <li>
            {{
              $t('（注）感染拡大前比：{range}の平日における平均との比較', {
                range: $t(populationGraph.base_period)
              })
            }}
          </li>
          <li>
            {{ $t('（注）緊急事態宣言前比：2020年4月6日~2020年4月7日との比較') }}
          </li>
          <li>
            {{ $t('（注）前年同月比：前年同月の平日における平均との比較') }}
          </li>
        </ul>
      </template>
    </population-bar-chart>
  </v-col>
</template>

<script>
import Data from '@/data/data.json'
import PopulationData from '@/data/population.json'
import PopulationBarChart from '@/components/PopulationBarChart.vue'

export default {
  components: {
    PopulationBarChart
  },
  data() {
    // 人口の推移
    const populationGraph = PopulationData
    // populationGraph ツールチップ title文字列
    // this.$t を使うため populationGraphOption の外側へ
    const populationGraphTooltipTitle = (tooltipItems, _) => {
      const label = tooltipItems[0].label
      return this.$t('期間: {duration}', {
        duration: this.$t(label)
      })
    }
    // populationGraph ツールチップ label文字列
    // this.$t を使うため populationGraphOption の外側へ
    const populationGraphTooltipLabel = (tooltipItem, data) => {
      const currentData = data.datasets[tooltipItem.datasetIndex]
      const percentage = `${currentData.data[tooltipItem.index]}%`

      return this.$t('{duration}の利用者数との相対値: {percentage}', {
        duration: this.$t(populationGraph.base_period),
        percentage
      })
    }

    const data = {
      Data,
      populationGraph,
      populationGraphTooltipTitle,
      populationGraphTooltipLabel
    }
    return data
  }
}
</script>

<template>
  <v-col cols="12" md="6" class="DataCard">
    <population-bar-chart
      :title="$t('富山駅周辺の人口の推移（参考値）')"
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
            {{ $t('（注）NTTドコモの携帯電話ネットワークのしくみを使用して作成される、人口の統計情報を元にした直近1週間の増減率') }}
          </li>
          <li>
            {{ $t('（注）前日比のデータについては、休日と平日のデータの比較となる際に非常に大きな数値となる場合あり') }}
          </li> 
          <li>
            {{ $t('（注）エリアの中の人口の増減を見るもので、接触量を見るものではない') }}
          </li>     
          <li>
            {{ $t('（注）感染拡大前比：2020年1月18日~2020年2月14日における平日の平均との比較') }}
          </li>
          <li>
            {{ $t('（注）緊急事態宣言前比：2020年4月6日~2020年4月7日との比較') }}
          </li>
          <li>
            {{ $t('（注）前年同月比：前年同月における平日の平均との比較') }}
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
      return this.$t('{duration}', {
        duration: this.$t(label)
      })
    }
    // populationGraph ツールチップ label文字列
    // this.$t を使うため populationGraphOption の外側へ
    const populationGraphTooltipLabel = (tooltipItem, data) => {
      const currentData = data.datasets[tooltipItem.datasetIndex]
      const label = `${data.labels[tooltipItem.index]}`
      const percentage = `${currentData.data[tooltipItem.index]}`
      return this.$t('{label} {percentage} %', {
        label,
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

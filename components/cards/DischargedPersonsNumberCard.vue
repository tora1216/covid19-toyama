<template>
  <v-col cols="12" md="6" class="DataCard">
    <time-bar-chart
      :title="$t('退院者数')"
      :title-id="'number-of-discharged-persons'"
      :chart-id="'number-of-discharged-persons'"
      :chart-data="graphData"
      :date="Data.discharged_persons.date"
      :unit="$t('人')"
      :url="'http://opendata.pref.toyama.jp/dataset/covid19'"
    >
      <template v-slot:description>
        <ul>
          <li>
            {{ $t('（注）把握には一定の期間を要しており、更新日の情報とは異なる場合あり') }}
          </li>
        </ul>
      </template>
    </time-bar-chart>
  </v-col>
</template>

<script>
import Data from '@/data/data.json'
import formatGraph from '@/utils/formatGraph'
import TimeBarChart from '@/components/TimeBarChart.vue'
export default {
  components: {
    TimeBarChart
  },
  data() {
    // 退院者数グラフ
    const graphData = formatGraph(Data.discharged_persons.data)

    const data = {
      Data,
      graphData
    }
    return data
  }
}
</script>

<template>
  <v-col cols="12" md="6" class="DataCard">
    <time-bar-chart
      :title="$t('検査実施人数')"
      :title-id="'number-of-inspection-persons'"
      :chart-id="'number-of-inspection-persons'"
      :chart-data="graphData"
      :date="Data.inspection_persons.date"
      :unit="$t('人')"
      :url="'http://opendata.pref.toyama.jp/dataset/covid19'"
    >
      <template v-slot:description>
        <ul style="">
          <li>
            {{ $t('（注）日付は検査結果判明日を基準にしている') }}
          </li>
          <li>
            {{ $t('（注）2/27には、2/26までの累計数を含む') }}
          </li>
          <li>
            {{ $t('（注）医療機関等実施分および抗原検査分は含まれていない') }}
          </li>
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
    // 検査実施人数グラフ
    const graphData = formatGraph(Data.inspection_persons.data)

    const data = {
      Data,
      graphData
    }
    return data
  }
}
</script>

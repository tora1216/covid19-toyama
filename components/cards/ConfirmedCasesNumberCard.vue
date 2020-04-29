<template>
  <v-col cols="12" md="6" class="DataCard">
    <time-bar-chart
      :title="$t('陽性患者数')"
      :title-id="'number-of-confirmed-cases'"
      :chart-id="'time-bar-chart-patients'"
      :chart-data="patientsGraph"
      :date="Data.patients_summary.date"
      :unit="$t('人')"
      :url="'http://www.pref.toyama.jp/cms_sec/1205/kj00021798.html'"
    >
      <template v-slot:description>
        <ul>
          <li>
            {{ $t('（注）日付は検査結果判明日') }}
          </li>
          <li>
            {{ $t('（注）速報値として公開するものであり、後日確定データとして修正される場合あり') }}
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
    // 感染者数グラフ
    const patientsGraph = formatGraph(Data.patients_summary.data)

    const data = {
      Data,
      patientsGraph
    }
    return data
  }
}
</script>

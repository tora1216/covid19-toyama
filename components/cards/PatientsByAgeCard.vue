<template>
  <v-col cols="12" md="6" class="DataCard">
    <time-bar-chart
      :title="$t('年代別陽性患者数')"
      :title-id="'number-of-confirmed-cases-by-age'"
      :chart-id="'time-bar-chart-patients-by-age'"
      :chart-data="patientsGraph"
      :date="Data.patients_by_age.date"
      :unit="$t('人')"
      :url="
        'http://opendata.pref.toyama.jp/dataset/covid19/resource/f3cd8c90-bf77-4072-96a3-96bd5942ff20'
      "
      :show-button="false"
    />
  </v-col>
</template>

<script>
import Data from '@/data/data.json'
import formatGraph from '@/utils/formatAgeGraph'
import TimeBarChart from '@/components/TimeBarChart.vue'

export default {
  components: {
    TimeBarChart
  },
  data() {
    // 年代別陽性患者数グラフ
    const patientsGraph = formatGraph(Data.patients_by_age.data)

    const data = {
      Data,
      patientsGraph
    }
    return data
  }
}
</script>

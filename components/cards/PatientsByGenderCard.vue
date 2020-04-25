<template>
   <v-col cols="12" md="6" class="DataCard">
      <circle-chart
        :title="$t('陽性患者数(性別)')"
        :title-id="'number-of-confirmed-cases-by-gender'"
        :chart-data="patientsGraph"
        :date="Data.patients_by_gender.date"
        :unit="$t('人')"
        :info="''"
        :descriptions="descriptions"
        :url="'http://www.pref.toyama.jp/cms_sec/1205/kj00021798.html'"
      />
  </v-col>
</template>

<script>
import Data from '@/data/data.json'
import CircleChart from '@/components/CircleChart'
import formatVariableGraph from '@/utils/formatVariableGraph'
export default {
  components: {
    CircleChart
  },
  data() {
    const patientsGraph = formatVariableGraph(Data.patients_by_gender.data)
    const descriptions = [
        '',
    ];
    const data = {
      Data,
      patientsGraph,
      descriptions
    }
    return data
  }
}
</script>

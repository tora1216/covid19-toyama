<template>
  <v-col cols="12" md="6" class="DataCard">
    <agency-bar-chart
      :title="$t('陽性患者数(居住地別)')"
      :title-id="'number-of-confirmed-cases-by-residence'"
      :chart-id="'time-bar-chart-patients-by-residence'"
      :chart-data="residenceGraph"
      :date="residenceData.date"
      :url="'http://www.pref.toyama.jp/cms_sec/1205/kj00021798.html'"
      :unit="$t('人')"
    >
    </agency-bar-chart>
  </v-col>
</template>

<script>
import Data from '@/data/data.json'
import ResidenceBarChart from '@/components/ResidenceBarChart.vue'

export default {
  components: {
    ResidenceBarChart
  },
  data() {
    // 居住地別陽性患者数グラフ
    const residenceData = Data.patients_by_residence

    const labels = [
      this.$t('男性'),
      this.$t('女性'),
      this.$t('その他')
    ]
    residenceData.datasets.map(dataset => {
      dataset.label = this.$t(dataset.label)
    })
    return {
      residenceData,
      labels
    }
  }
}
</script>

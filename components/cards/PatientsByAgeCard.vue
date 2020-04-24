<template>
  <v-col cols="12" md="6" class="DataCard">
    <agency-bar-chart
      :title="$t('陽性患者数(年代別)')"
      :title-id="'number-of-confirmed-cases-by-age'"
      :chart-id="'time-bar-chart-patients-by-age'"
      :chart-data="ageGraph"
      :date="ageData.patients_by_age.date"
      :url="'http://opendata.pref.toyama.jp/dataset/covid19'"
      :unit="$t('人')"
    >
      <template v-slot:description>
        {{ $t('※公表日が直近数日のデータは、[新型コロナウイルス感染症の県内の患者等発生状況]富山県HP(http://www.pref.toyama.jp/cms_sec/1205/kj00021798.html)を元に作成している場合あり') }}
      </template>
    </agency-bar-chart>
  </v-col>
</template>

<script>
import Data from '@/data/data.json'
import AgencyBarChart from '@/components/AgencyBarChart.vue'

export default {
  components: {
    AgencyBarChart
  },
  data() {
    // 年代別陽性患者数グラフ
    const ageData = Data.patients_by_age

    const labels = [
      this.$t('男性'),
      this.$t('女性'),
      this.$t('その他')
    ]
    ageData.datasets.map(dataset => {
      dataset.label = this.$t(dataset.label)
    })
    return {
      ageData,
      labels
    }
  }
}
</script>

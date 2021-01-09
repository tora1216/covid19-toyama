<template>
  <v-col cols="12" md="6" class="DataCard">
    <horizontal-bar-chart
      :title="$t('陽性患者数(居住地別)')"
      :title-id="'number-of-confirmed-cases-by-residence'"
      :chart-id="'time-bar-chart-patients-by-residence'"
      :chart-data="patientsGraph"
      :date="updatedAt"
      :labels="graphLabels"
      :unit="$t('人')"
      :url="'http://www.pref.toyama.jp/cms_sec/1205/kj00021798.html'"
    />
  </v-col>
</template>

<script>
import Data from '@/data/patients.json'
import formatGraph from '@/utils/formatGraph'
import HorizontalBarChart from '@/components/HorizontalBarChart.vue'
export default {
  components: {
    HorizontalBarChart
  },
  data() {
    // グラフラベル
    const graphLabels = [
      this.$t('富山市'),
      this.$t('高岡市'),
      this.$t('射水市'),
      this.$t('南砺市'),
      this.$t('砺波市'),
      this.$t('氷見市'),
      this.$t('魚津市'),
      this.$t('黒部市'),
      this.$t('滑川市'),
      this.$t('小矢部市'),
      this.$t('立山町'),
      this.$t('入善町'),
      this.$t('上市町'),
      this.$t('朝日町'),
      this.$t('舟橋村'),
      this.$t('富山県外')
    ]
    return {
      updatedAt: Data.date,
      graphLabels,
      // 陽性患者の詳細
      patientsGraph: Data.data
    }
  }
}
</script>
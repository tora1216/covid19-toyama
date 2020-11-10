<template>
  <v-col cols="12" md="6" class="DataCard">
    <time-stacked-bar-chart
      :title="$t('検査実施数')"
      :title-id="'number-of-tested-cases'"
      :chart-id="'number-of-tested-cases'"
      :chart-data="inspectionsGraph"
      :date="Data.date"
      :items="inspectionsItems"
      :labels="inspectionsLabels"
      :unit="$t('人')"
      :data-labels="inspectionsDataLabels"
      :url="'http://opendata.pref.toyama.jp/dataset/covid19'"
    >
    </time-stacked-bar-chart>
  </v-col>
</template>

<script>
import Data from '@/data/test.json'
import TimeStackedBarChart from '@/components/TimeStackedBarChart.vue'

export default {
  components: {
    TimeStackedBarChart
  },
  data() {
    const inspectionsGraph = [
      Data.data['PCR検査数'],
      Data.data['抗原検査数'],
    ]
    const inspectionsItems = [
      this.$t('PCR検査数'),
      this.$t('抗原検査数')
    ]
    const inspectionsLabels = Data.labels
    const inspectionsDataLabels = [
      this.$t('PCR検査数'),
      this.$t('抗原検査数')
    ]

    const data = {
      Data,
      inspectionsGraph,
      inspectionsItems,
      inspectionsLabels,
      inspectionsDataLabels
    }
    return data
  }
}
</script>
<template>
  <v-col cols="12" md="6" class="DataCard">
    <time-bar-chart
      :title="$t('検査実施人数')"
      :title-id="'number-of-inspection-persons'"
      :chart-id="'number-of-inspection-persons'"
      :chart-data="inspectionPersonsGraph"
      :date="Data.inspection_persons.date"
      :unit="$t('人')"
    />
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
    // 検査人数
    const inspectionPersonsGraph = formatGraph(Data.inspection_persons.data)

    const data = {
      Data,
      inspectionPersonsGraph
    }
    return data
  }
}
</script>

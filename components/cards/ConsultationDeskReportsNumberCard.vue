<template>
  <v-col cols="12" md="6" class="DataCard">
    <time-bar-chart
      :title="$t('帰国者・接触者相談センターへの相談件数')"
      :title-id="'number-of-reports-to-covid19-consultation-desk'"
      :chart-id="'time-bar-chart-querents'"
      :chart-data="querentsGraph"
      :date="Data.querents.date"
      :unit="$t('件.reports')"
      :url="'http://opendata.pref.toyama.jp/dataset/covid19/resource/85d4c612-c174-4f73-be63-f8512d25361a'"
    >
      <template v-slot:description>
        <ul>
          <li>
            {{ $t('（注）2/27には、2/26までの累計数を含む') }}
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
    // 帰国者・接触者相談センター　相談件数
    const querentsGraph = formatGraph(Data.querents.data)

    const data = {
      Data,
      querentsGraph
    }
    return data
  }
}
</script>

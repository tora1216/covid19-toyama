<template>
  <v-col cols="12" md="6" class="DataCard">
    <time-bar-chart
      :title="$t('陽性率の推移')"
      :title-id="'rate-of-confirmed-cases'"
      :chart-id="'rate-of-confirmed-cases'"
      :chart-data="patientsGraph"
      :date="Data.positive_rate.date"
      :unit="$t('%')"
      :url="'http://opendata.pref.toyama.jp/dataset/covid19'"
    >
      <template v-slot:description>
        <ul>
          <li>
            {{ $t('（注）2/27には、2/26までの累計数を含む') }}
          </li>
          <li>
            {{ $t('（注）陽性率(実施人数に占める陽性人数の割合)は、小数点第2位で四捨五入をしている') }}
          </li>
        </ul>
      </template>
    </time-bar-chart>
  </v-col>
</template>

<script>
import Data from '@/data/data.json'
import formatGraph from '@/utils/formatGraph'
import TimeBarChart from '@/components/PositiveRateChart.vue'

export default {
  components: {
    TimeBarChart
  },
  data() {
    const patientsGraph = formatGraph(Data.positive_rate.data)

    const data = {
      Data,
      patientsGraph
    }
    return data
  }
}
</script>

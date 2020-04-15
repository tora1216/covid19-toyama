<template>
  <v-col cols="12" md="6" class="DataCard">
    <time-bar-chart
      :title="$t('居住地別陽性患者数')"
      :title-id="'number-of-confirmed-cases-by-residence'"
      :chart-id="'time-bar-chart-patients-by-residence'"
      :chart-data="patientsGraph"
      :date="Data.patients_by_residence.date"
      :unit="$t('人')"
      :url="
        'http://opendata.pref.toyama.jp/dataset/covid19/resource/f3cd8c90-bf77-4072-96a3-96bd5942ff20'
      "
      :show-button="false"
    >
      <template v-slot:description>
        <ul>
          <li>
            {{
              $t(
                '（注）A：富山市，B：高岡市，C：射水市，D：南砺市，E：砺波市，F：氷見市，G：魚津市，H：黒部市，I：滑川市，J：小矢部市，K：立山町，L：入善町，M：上市町，N：朝日町，O：船橋村，P：富山県以外 を示している'
              )
            }}
          </li>
        </ul>
      </template>
    </time-bar-chart>
  </v-col>
</template>

<script>
import Data from '@/data/data.json'
import formatGraph from '@/utils/formatResidenceGraph'
import TimeBarChart from '@/components/TimeBarChart.vue'

export default {
  components: {
    TimeBarChart
  },
  data() {
    // 居住地別陽性患者数グラフ
    const patientsGraph = formatGraph(Data.patients_by_residence.data)

    const data = {
      Data,
      patientsGraph
    }
    return data
  }
}
</script>

<template>
  <v-col cols="12" md="6" class="DataCard">
    <time-bar-chart
      :title="$t('陽性患者数(居住地別)')"
      :title-id="'number-of-confirmed-cases-by-residence'"
      :chart-id="'time-bar-chart-patients-by-residence'"
      :chart-data="residenceGraph"
      :date="Data.patients_by_residence.date"
      :unit="$t('人')"
      :url="
        'http://www.pref.toyama.jp/cms_sec/1205/kj00021798.html'
      "
      :show-button="false"
    >
      <template v-slot:description>
        <ul>
          <li>
            {{
              $t(
                '（注）A：富山市，B：高岡市，C：射水市，D：南砺市，E：砺波市，F：氷見市，G：魚津市，H：黒部市，I：滑川市，J：小矢部市，K：立山町，L：入善町，M：上市町，N：朝日町，O：舟橋村，P：富山県以外 を示している'
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
    const residenceGraph = formatGraph(Data.patients_by_residence.data)
    const data = {
      Data,
      residenceGraph
    }
    return data
  }
}
</script>

<template>
  <v-col cols="12" md="6" class="DataCard">
    <time-bar-chart
      :title="$t('陽性患者数(性別)')"
      :title-id="'number-of-confirmed-cases-by-gender'"
      :chart-id="'time-bar-chart-patients-by-gender'"
      :chart-data="patientsGraph"
      :date="Data.patients_by_gender.date"
      :unit="$t('人')"
      :url="
        'http://opendata.pref.toyama.jp/dataset/covid19'
      "
      :show-button="false"
    >
      <template v-slot:description>
        <ul>
          <li>
            {{
              $t(
                '（注）M：男性，F：女性，O：その他 を示している'
              )
            }}
          </li>
          <li>
            {{
              $t(
                '※公表日が直近数日のデータは、[新型コロナウイルス感染症の県内の患者等発生状況]富山県HP(http://www.pref.toyama.jp/cms_sec/1205/kj00021798.html)を元に作成している場合あり'
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
import formatGraph from '@/utils/formatGenderGraph'
import TimeBarChart from '@/components/TimeBarChart.vue'
export default {
  components: {
    TimeBarChart
  },
  data() {
    // 性別陽性患者数グラフ
    const patientsGraph = formatGraph(Data.patients_by_gender.data)
    const data = {
      Data,
      patientsGraph
    }
    return data
  }
}
</script>

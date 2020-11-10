<template>
  <v-col cols="12" md="6" class="DataCard">
    <time-bar-chart
      :title="$t('検査陽性率')"
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
          {{ $t('（注）2020/10/31までは、検査結果判明日ベースで計上') }}
        </li>
        <li>
          {{ $t('（注）2020/10/31のみ、検査結果判明日ベースでの2020/10/31-2020/11/02の合計で計上') }}
        </li>
        <li>
          {{ $t('（注）2020/11/01以降は、検査検体採取日ベースで計上') }}
        </li>
          <li>
            {{ $t('（注）陽性率：陽性人数の移動平均／（陽性人数＋陰性人数）の移動平均') }}
          </li>
          <li>
            {{ $t('（注）集団感染発生や曜日による件数のばらつきにより、日々の結果が変動するため、こうしたばらつきを平準化し全体の傾向を見る趣旨から、過去7日間の移動平均値を陽性率として算出（例えば、5月7日の陽性率は、5月1日から5月7日までの実績平均を用いて算出）') }}
          </li>
          <li>
            {{ $t('（注）抗原検査分は含まれていない') }}
          </li>
          <li>
            {{ $t('（注）把握には一定の期間を要しており、更新日の情報とは異なる場合あり') }}
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

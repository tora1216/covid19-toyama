  <template>
  <v-col cols="12" md="6" class="DataCard">
    <agency-bar-chart
      :title="$t('陽性患者数(居住地別)')"
      :title-id="'number-of-confirmed-cases-by-residence'"
      :chart-id="'time-bar-chart-patients-by-residence'"
      :chart-data="agencyData"
      :date="agencyData.date"
      :url="'http://www.pref.toyama.jp/cms_sec/1205/kj00021798.html'"
      :unit="$t('人')"
    >
    </agency-bar-chart>
  </v-col>
</template>

<script>
import Data from '@/data/data.json'
import ResidenceBarChart from '@/components/ResidenceBarChart.vue'
const agencyData=Data.patients_by_residence
export default {
  components: {
    AgencyBarChart
  },
  data() {
    const agencies = [
      this.$t('男性'),
      this.$t('女性'),
      this.$t('その他')
    ]
    agencyData.datasets.map(dataset => {
      dataset.label = this.$t(dataset.label)
    })
    return {
      agencyData,
      agencies
    }
  }
}
</script>

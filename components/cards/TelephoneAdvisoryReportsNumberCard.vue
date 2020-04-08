 <template>
  <v-col cols="12" md="6" class="DataCard">
    <time-bar-chart
      :title="$t('新型コロナウイルス感染症に関する一般相談件数')"
      :title-id="'number-of-reports-to-covid19-telephone-advisory-center'"
      :chart-id="'time-bar-chart-contacts'"
      :chart-data="contactsGraph"
      :date="Data.contacts.date"
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
    // 相談件数
    const contactsGraph = formatGraph(Data.contacts.data)

    const data = {
      Data,
      contactsGraph
    }
    return data
  }
}
</script>

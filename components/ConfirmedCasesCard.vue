<template>
  <data-view :title="title" :title-id="titleId" :date="date" :url="url">
    <template v-slot:button>
      <ul :class="$style.notes">
        <li>
          {{
            $t(
              '（注）入院には、入院予定を含む'
            )
          }}
        </li>
        <li>
          {{
            $t(
              '（注）症状は陽性公表時点のもの'
            )
          }}
        </li>
        <li>
          {{
            $t(
              '（注）速報値として公開するものであり、後日確定データとして修正される場合あり'
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
    <slot />
  </data-view>
</template>

<style lang="scss" module>
ul.notes {
  margin-bottom: 0;
  padding-left: 0 !important;
  font-size: 12px;
  color: $gray-3;

  > li {
    list-style-type: none;
  }
}
</style>

<script lang="ts">
import Vue from 'vue'
import DataView from '@/components/DataView.vue'
import DataViewBasicInfoPanel from '@/components/DataViewBasicInfoPanel.vue'

export default Vue.extend({
  components: { DataView, DataViewBasicInfoPanel },
  props: {
    title: {
      type: String,
      default: ''
    },
    titleId: {
      type: String,
      default: ''
    },
    date: {
      type: String,
      default: ''
    },
    info: {
      type: Object,
      default: () => {}
    },
    url: {
      type: String,
      default: ''
    }
  }
})
</script>

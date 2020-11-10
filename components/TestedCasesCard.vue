<template>
  <data-view :title="title" :title-id="titleId" :date="date" :url="url">
    <template v-slot:button>
      <ul :class="$style.notes">
        <li>
          {{ $t('（注）陽性率：陽性人数／（陽性人数＋陰性人数）') }}
        </li>
        <li>
          {{ $t('（注）医療機関で実施したPCR検査・抗原検査も含む') }}
        </li>
        <li>
          {{ $t('（注）把握には一定の期間を要しており、更新日の情報とは異なる場合あり') }}
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

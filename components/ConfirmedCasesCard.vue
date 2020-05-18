<template>
  <data-view :title="title" :title-id="titleId" :date="date" :url="url">
    <template v-slot:button>
      <ul :class="$style.notes">
        <li>
          {{ $t('（注）重症：集中治療室（ICU）等での管理又は人工呼吸器管理が必要な患者') }}
        </li>
        <li>
          {{ $t('（注）速報値として公開するものであり、後日確定データとして修正される場合あり') }}
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

<template>
  <span :class="$style.linkButton">
    <external-link
      url="http://www.pref.toyama.jp/cms_sec/1205/kj00022462.html"
    >
      {{ $t('ロードマップについて') }}
    </external-link>
  </span>
</template>

<script lang="ts">
import Vue from 'vue'
import ExternalLink from '@/components/ExternalLink.vue'
export default Vue.extend({
  components: { ExternalLink }
})
</script>

<style lang="scss" module>
.linkButton {
  display: inline-flex;
  flex: 0 1 auto;
  @include lessThan($medium) {
    margin-top: 8px;
  }
}
</style>
<template>
  <span :class="$style.linkButton">
    <external-link
      :class="$style.textLink"
      url="http://www.pref.toyama.jp/cms_sec/1205/kj00022481.html"
    >
      <span :class="$style.text">
        {{ $t('ロードマップについて') }}
      </span>
    </external-link>
  </span>
</template>

<script lang="ts">
import Vue from 'vue'
import ExternalLink from '@/components/ExternalLink.vue'
export default Vue.extend({
  components: {
    ExternalLink,
  },
})
</script>

<style lang="scss" module>
.linkButton {
  background-color: $white;
  border: 1px solid $green-1;
  color: $green-1;
  border-radius: 4px;
  padding: 4px 8px;
  margin-right: 8px;
  display: inline-flex;
  @include font-size(14);
  &:hover {
    background-color: $green-1;
  }
  .textLink {
    display: flex;
    align-items: center;
    color: $green-1 !important;
    text-decoration: none;
    margin: -10px;
    padding: 10px;
    i {
      color: inherit;
    }
    &:hover {
      color: $white !important;
    }
  }
  .text {
    margin: 0 4px;
  }
  @include lessThan($medium) {
    margin-top: 8px;
  }
}
</style>
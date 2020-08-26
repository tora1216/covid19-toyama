<template>
  <span :class="$style.linkButton">
    <external-link
      :class="$style.textLink"
      url="https://twitter.com/covid19_toyama"
    >
      <span :class="$style.text">
        {{ $t('@covid19_toyamaをフォロー') }}
      </span>
    </external-link>
  </span>
</template>

<script lang="ts">
import Vue from 'vue'
import ExternalLink from '@/components/ExternalLink.vue'
export default Vue.extend({
  components: {
    ExternalLink
  },
})
</script>

<style lang="scss" module>
.linkButton {
  background-color: #00acee;
  border: 1px solid #00acee;
  color: $white;
  border-radius: 3em;
  padding: 4px 8px;
  margin-right: 8px;
  display: inline-flex;
  @include font-size(14);
  &:hover {
    background-color: $white;
  }
  .textLink {
    display: flex;
    align-items: center;
    color: $white !important;
    text-decoration: none;
    margin: -10px;
    padding: 10px;
    i {
      color: inherit;
    }
    &:hover {
      color: #00acee !important;
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
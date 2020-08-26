<template>
  <span :class="$style.linkButton">
    <external-link
      :class="$style.textLink"
      url="https://twitter.com/covid19_toyama"
    >
      <twitter-icon aria-hidden="true" :class="$style.svgIcon" />
      <span :class="$style.text">
        {{ $t('フォローする') }}
      </span>
    </external-link>
  </span>
</template>

<script lang="ts">
import Vue from 'vue'
import ExternalLink from '@/components/ExternalLink.vue'
import TwitterIcon from '@/static/twitter.svg'
export default Vue.extend({
  components: {
    ExternalLink,
    TwitterIcon,
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
  .svgIcon path {
    fill: $white;
  }
  &:hover {
    background-color: $white;
    .svgIcon path {
      fill: #00acee;
    }
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
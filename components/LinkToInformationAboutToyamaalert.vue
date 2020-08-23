<template>
  <span :class="$style.linkButton">
    <external-link
      :class="$style.textLink"
      url="http://www.pref.toyama.jp/cms_sec/1205/kj00022462.html"
    >
      <antenna-icon aria-hidden="true" :class="$style.svgIcon" />
      <span :class="$style.text">
        {{ $t('富山アラート発動中') }}
      </span>
    </external-link>
  </span>
</template>

<script lang="ts">
import Vue from 'vue'
import ExternalLink from '@/components/ExternalLink.vue'
import AntennaIcon from '@/static/antenna.svg'
export default Vue.extend({
  components: {
    ExternalLink,
    AntennaIcon
  }
})
</script>

<style lang="scss" module>
  .ExternalLink {
    background-color: #fff;
    border: 1px solid $alert;
    color: $alert !important;
  }
  .ExternalLink:hover {
    color: #fff !important;
    background-color: $alert;
  }

.linkButton {
  .svgIcon path {
    fill: $alert;
  }
  &:hover {
    .svgIcon path {
      fill: $white;
    }
  }
}
</style>
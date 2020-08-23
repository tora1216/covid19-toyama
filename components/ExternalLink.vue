<template>
  <a class="ExternalLink" :href="url" target="_blank" rel="noopener noreferrer">
    <slot />
    <v-icon
      class="ExternalLinkIcon"
      :size="`${iconSize / 10}rem`"
      :aria-label="this.$t('別タブで開く')"
      role="img"
      :aria-hidden="false"
    >
      mdi-open-in-new
    </v-icon>
  </a>
</template>

<style lang="scss">
  .ExternalLink {
    padding: 4px 8px;
    display: inline-block;
    border-radius: 4px;
    background-color: #fff;
    border: 1px solid #00a040;
    color: #00a040 !important;
    cursor: pointer;
    text-decoration: none;
    .ExternalLinkIcon {
      vertical-align: text-bottom;
    }
  }
  .ExternalLink:hover {
    color: #fff !important;
    background-color: #00a040;
  }
</style>
<script lang="ts">
import Vue from 'vue'
export default Vue.extend({
  props: {
    url: {
      type: String,
      default: '',
    },
    iconSize: {
      type: Number,
      default: 15,
    },
  },
})
</script>
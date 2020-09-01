<template>
  <div class="Parent">
    <page-header class="mb-3">
      {{ $t('県内の医療提供体制') }}
    </page-header>
  
    <StaticCard>
     <iflame class="maps" src="https://tera-chan.com/covid19-toyama/maps/"></iflame>
    </StaticCard>
  </div>
</template>

<script lang="ts">
import Vue from 'vue'
import { MetaInfo } from 'vue-meta'
import StaticCard from '@/components/StaticCard.vue'
import PageHeader from '@/components/PageHeader.vue'

export default Vue.extend({
  components: {
    PageHeader,
    StaticCard
  },
  head(): MetaInfo {
    return {
      title: this.$t('県内の医療提供体制') as string
    }
  }
})
</script>

<style>
.maps{
  height:80vh;
  width:100%;
  border:none;
}
</style>
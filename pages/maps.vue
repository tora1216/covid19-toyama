<template>
  <div class="Parent">
    <page-header class="mb-3">
      {{ $t('県内の医療提供体制') }}
    </page-header>
  
    <StaticCard>
     <iframe class="maps" src="https://tera-chan.com/covid19-toyama/maps/"></iframe>
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
  height:60vh;
  width:100%;
  border:none;
}
</style>
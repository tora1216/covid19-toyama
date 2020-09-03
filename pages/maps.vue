<template>
  <div class="Parent">
    <page-header class="mb-3">
      {{ $t('県内の医療提供体制') }}
    </page-header>
  
    <StaticCard>
     <ul>
       <li>{{ $t('※内閣官房新型コロナウイルス感染症対策推進室のホームページで公開されている医療機関の状況を元にしています。') }}</li>
       <li>{{ $t('※都道府県の協力により調査対象医療機関を日々追加していますが、すべての入院病床を有する病院の情報を網羅しているものではありません。') }}</li>
       <li>{{ $t('※この地図に載っていない医療機関がある場合には、その病院のホームページ等でご確認ください。') }}</li>
     </ul>
     <iframe class="maps" src="https://tera-chan.com/covid19-toyama/maps/" allowfullscreen></iframe>
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
  height:70vh;
  width:100%;
  border:none;
}
</style>
<template>
  <div class="Parent">
    <page-header class="mb-3">
      {{ $t('県内の医療提供体制マップ') }}
    </page-header>
  
    <StaticCard>
     <ul class="note">
       <li>{{ $t('（注）すべての入院病床を有する医療機関の情報を網羅しているものではない') }}</li>
       <li>{{ $t('（注）把握には一定の期間を要しており、更新日の情報とは異なる場合あり') }}</li>
     </ul>
     <iframe class="maps" src="https://tera-chan.com/covid19-toyama/maps/" allowfullscreen></iframe>
     <ul class="note">
       <li><a href="https://corona.go.jp/dashboard/" target="_blank">{{ $t('[全国医療機関の医療提供体制の状況]内閣官房 新型コロナウイルス感染症対策推進室HP(https://corona.go.jp/dashboard/)を元に作成') }}</a></li>
     </ul>
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
      title: this.$t('県内の医療提供体制マップ') as string
    }
  }
})
</script>

<style>
.maps{
  height:55vh;
  width:100%;
  border:none;
}
.note{
  list-style-type: none;
  padding-left: 0 !important;
  font-size: 12px;
  color: #707070;
}
.note>a{
  text-decoration: none;
}
</style>
<template>
  <div class="MainPage">
    <div class="Header mb-3">
      <page-header :icon="headerItem.icon">
        {{ headerItem.title }}
      </page-header>
      <div class="UpdatedAt">
        <span>{{ $t('最終更新') }} </span>
        <time :datetime="updatedAt">{{ Data.lastUpdate }}</time>
      </div>
      <div v-if="!['ja', 'ja-basic'].includes($i18n.locale)" class="Annotation">
        <span>{{ $t('注釈') }} </span>
      </div>
    </div>
    <whats-new />
    <!--<toyama-alert-card />-->
    <relax-step-card :items="statusItems" />
    <!--
    <static-info
      class="mb-4"
      :url="localePath('/flow')"
      :text="$t('自分や家族の症状に不安や心配があればまずは電話相談をどうぞ')"
      :btn-text="$t('相談の手順を見る')"
    />
    -->
    <v-row class="DataBlock">
      <confirmed-cases-details-card />
      <confirmed-cases-number-card />
      <confirmed-cases-attributes-card />
      <patients-by-residence-card />
      <patients-by-age-card />
      <patients-by-gender-card />
      <dead-persons-number-card />
      <discharged-persons-number-card />
      <tested-cases-details-card />
      <positive-rate-card />
      <tested-cases-number-card />
      <telephone-advisory-reports-number-card />
      <consultation-desk-reports-number-card />
      <population-card />
    </v-row>
  </div>
</template>

<script lang="ts">
import Data from '@/data/data.json'
import StatusData from '@/data/status.json'

import Vue from 'vue'
import { MetaInfo } from 'vue-meta'
import PageHeader from '@/components/PageHeader.vue'
import WhatsNew from '@/components/WhatsNew.vue'
import ToyamaAlertCard from '@/components/ToyamaAlertCard.vue'
import RelaxStepCard from '@/components/RelaxationStepCard.vue'
import StaticInfo from '@/components/StaticInfo.vue'
import ConfirmedCasesDetailsCard from '@/components/cards/ConfirmedCasesDetailsCard.vue'
import ConfirmedCasesNumberCard from '@/components/cards/ConfirmedCasesNumberCard.vue'
import ConfirmedCasesAttributesCard from '@/components/cards/ConfirmedCasesAttributesCard.vue'
import PatientsByResidenceCard from '@/components/cards/PatientsByResidenceCard.vue'
import PatientsByAgeCard from '@/components/cards/PatientsByAgeCard.vue'
import PatientsByGenderCard from '@/components/cards/PatientsByGenderCard.vue'
import DeadPersonsNumberCard from '@/components/cards/DeadPersonsNumberCard.vue'
import DischargedPersonsNumberCard from '@/components/cards/DischargedPersonsNumberCard.vue'
import TestedCasesDetailsCard from '@/components/cards/TestedCasesDetailsCard.vue'
import PositiveRateCard from '@/components/cards/PositiveRateCard.vue'
import TestedCasesNumberCard from '@/components/cards/TestedCasesNumberCard.vue'
import TelephoneAdvisoryReportsNumberCard from '@/components/cards/TelephoneAdvisoryReportsNumberCard.vue'
import ConsultationDeskReportsNumberCard from '@/components/cards/ConsultationDeskReportsNumberCard.vue'
import PopulationCard from '@/components/cards/PopulationCard.vue'

export default Vue.extend({
  components: {
    PageHeader,
    WhatsNew,
    ToyamaAlertCard,
    RelaxStepCard,
    StaticInfo,
    ConfirmedCasesDetailsCard,
    ConfirmedCasesNumberCard,
    ConfirmedCasesAttributesCard,
    PatientsByResidenceCard,
    PatientsByAgeCard,
    PatientsByGenderCard,
    DeadPersonsNumberCard,
    DischargedPersonsNumberCard,
    TestedCasesDetailsCard,
    PositiveRateCard,
    TestedCasesNumberCard,
    TelephoneAdvisoryReportsNumberCard,
    ConsultationDeskReportsNumberCard,
    PopulationCard
  },
  data() {
    const data = {
      Data,
      headerItem: {
        icon: 'mdi-chart-timeline-variant',
        title: this.$t('県内の最新感染動向')
      },
      statusItems: StatusData.statusItems
    }
    return data
  },
  // computed: {
  //   updatedAt() {
  //     return convertDatetimeToISO8601Format(this.$data.Data.lastUpdate)
  //   }
  // },
  head(): MetaInfo {
    return {
      title: this.$t('県内の最新感染動向') as string
    }
  }
})
</script>

<style lang="scss" scoped>
.MainPage {
  .Header {
    display: flex;
    flex-wrap: wrap;
    align-items: flex-end;
    @include lessThan($small) {
      flex-direction: column;
      align-items: baseline;
    }
  }
  .UpdatedAt {
    @include font-size(14);
    color: $gray-3;
    margin-bottom: 0.2rem;
  }
  .Annotation {
    @include font-size(12);
    color: $gray-3;
    @include largerThan($small) {
      margin: 0 0 0 auto;
    }
  }
  .EmergencyBlock {
    margin: 20px 0;
    background-color: #fff;
    box-shadow: 0 0 2px rgba(112, 15, 15, 0.15);
    border: 0.5px solid #d9d9d9 !important;
    border-radius: 4px;
    padding: 10px;
    .EmergencyImage {
      display: block;
      width: 50%;
      margin: auto;
      @include lessThan($medium) {
        width: 75%;
      }
      @include lessThan($small) {
        width: 100%;
      }
    }
  }
  .DataBlock {
    margin: 20px -8px;
    .DataCard {
      @include largerThan($medium) {
        padding: 10px;
      }
      @include lessThan($small) {
        padding: 4px 8px;
      }
    }
  }
}
</style>

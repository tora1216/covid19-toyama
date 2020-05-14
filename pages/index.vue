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
    <!--<whats-new class="mb-4" :items="newsItems" />-->
    <div class="TwitterTimelineBlock mb-4">
      <h3 class="WhatsNew-heading"><i aria-hidden="true" class="v-icon notranslate WhatsNew-heading-icon mdi mdi-information theme--light" style="font-size: 24px;"></i>
        {{ $t('最新のお知らせ') }} 
      </h3>
      <div class="EmbeddedTwitterTimeline">
        <a class="twitter-timeline" data-height="300px" data-chrome="noheader nofooter" href="https://twitter.com/stopcovidtoyama?ref_src=twsrc%5Etfw">Loading...</a>
      </div>
      <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>
    </div>
    <!--<div class="EmergencyPosterBlock mb-4">
      <h3 class="WhatsNew-heading"><i aria-hidden="true" class="v-icon notranslate WhatsNew-heading-icon mdi mdi-bullhorn theme--light" style="font-size: 24px;"></i>
        {{ $t('緊急事態宣言 発令') }} 
      </h3>
      <img class="EmergencyPosterImage" src="/emergency-poster.jpg" alt="" />
    </div>-->
    <static-info
      class="mb-4"
      :url="localePath('/flow')"
      :text="$t('自分や家族の症状に不安や心配があればまずは電話相談をどうぞ')"
      :btn-text="$t('相談の手順を見る')"
    />
    <v-row class="DataBlock">
      <confirmed-cases-details-card />
      <confirmed-cases-number-card />
      <confirmed-cases-attributes-card />
      <patients-by-residence-card />
      <patients-by-age-card />
      <patients-by-gender-card />
      <tested-cases-details-card />
      <inspection-persons-number-card />
      <!-- <tested-number-card /> -->
      <telephone-advisory-reports-number-card />
      <consultation-desk-reports-number-card />
      <!-- <metro-card /> -->
      <!-- <agency-card /> -->
      <!-- <shinjuku-visitors-card /> -->
      <!-- <chiyoda-visitors-card /> -->
    </v-row>
  </div>
</template>

<script lang="ts">
import Vue from 'vue'
import { MetaInfo } from 'vue-meta'
import PageHeader from '@/components/PageHeader.vue'
// import WhatsNew from '@/components/WhatsNew.vue'
import StaticInfo from '@/components/StaticInfo.vue'
import Data from '@/data/data.json'
import News from '@/data/news.json'
import ConfirmedCasesNumberCard from '@/components/cards/ConfirmedCasesNumberCard.vue'
import ConfirmedCasesAttributesCard from '@/components/cards/ConfirmedCasesAttributesCard.vue'
// import { convertDatetimeToISO8601Format } from '@/utils/formatDate'

import ConfirmedCasesDetailsCard from '@/components/cards/ConfirmedCasesDetailsCard.vue'
import TestedCasesDetailsCard from '@/components/cards/TestedCasesDetailsCard.vue'
// import TestedNumberCard from '@/components/cards/TestedNumberCard.vue'
import InspectionPersonsNumberCard from '@/components/cards/InspectionPersonsNumberCard.vue'
import TelephoneAdvisoryReportsNumberCard from '@/components/cards/TelephoneAdvisoryReportsNumberCard.vue'
import ConsultationDeskReportsNumberCard from '@/components/cards/ConsultationDeskReportsNumberCard.vue'
// import MetroCard from '@/components/cards/MetroCard.vue'
// import AgencyCard from '@/components/cards/AgencyCard.vue'
// import ShinjukuVisitorsCard from '@/components/cards/ShinjukuVisitorsCard.vue'
// import ChiyodaVisitorsCard from '@/components/cards/ChiyodaVisitorsCard.vue'
import PatientsByResidenceCard from '@/components/cards/PatientsByResidenceCard.vue'
import PatientsByAgeCard from '@/components/cards/PatientsByAgeCard.vue'
import PatientsByGenderCard from '@/components/cards/PatientsByGenderCard.vue'

export default Vue.extend({
  components: {
    PageHeader,
    // WhatsNew,
    StaticInfo,
    ConfirmedCasesNumberCard,
    ConfirmedCasesAttributesCard,
    ConfirmedCasesDetailsCard,
    TestedCasesDetailsCard,
    // TestedNumberCard,
    InspectionPersonsNumberCard,
    TelephoneAdvisoryReportsNumberCard,
    ConsultationDeskReportsNumberCard,
    // MetroCard,
    // AgencyCard,
    // ShinjukuVisitorsCard,
    // ChiyodaVisitorsCard,
    PatientsByResidenceCard,
    PatientsByAgeCard,
    PatientsByGenderCard
  },
  data() {
    const data = {
      Data,
      headerItem: {
        icon: 'mdi-chart-timeline-variant',
        title: this.$t('県内の最新感染動向')
      },
      newsItems: News.newsItems
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

  .TwitterTimelineBlock {
    margin: 20px 0;
    background-color: #fff;
    box-shadow: 0 0 2px rgba(112, 15, 15, 0.15);
    border: 0.5px solid #d9d9d9 !important;
    border-radius: 4px;
    padding: 10px;

    .EmbeddedTwitterTimeline {
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

  .EmergencyPosterBlock {
    margin: 20px 0;
    background-color: #fff;
    box-shadow: 0 0 2px rgba(112, 15, 15, 0.15);
    border: 0.5px solid #d9d9d9 !important;
    border-radius: 4px;
    padding: 10px;

    .EmergencyPosterImage {
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

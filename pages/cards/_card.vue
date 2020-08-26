<template>
  <div>
    <confirmed-cases-details-card
      v-if="this.$route.params.card == 'details-of-confirmed-cases'"
    />
    <confirmed-cases-number-card
      v-else-if="this.$route.params.card == 'number-of-confirmed-cases'"
    />
    <confirmed-cases-attributes-card
      v-else-if="this.$route.params.card == 'attributes-of-confirmed-cases'"
    />
    <patients-by-residence-card
      v-else-if="this.$route.params.card == 'number-of-confirmed-cases-by-residence'"
    />
    <patients-by-age-card
      v-else-if="this.$route.params.card == 'number-of-confirmed-cases-by-age'"
    />
    <patients-by-gender-card
      v-else-if="this.$route.params.card == 'number-of-confirmed-cases-by-gender'"
    />
    <dead-persons-number-card
      v-else-if="this.$route.params.card == 'number-of-dead-persons'"
    />
    <discharged-persons-number-card
      v-else-if="this.$route.params.card == 'number-of-discharged-persons'"
    />
    <tested-cases-details-card
      v-else-if="this.$route.params.card == 'details-of-tested-cases'"
    />
    <positive-rate-card
      v-else-if="this.$route.params.card == 'rate-of-confirmed-cases'"
    />
    <inspection-persons-number-card
      v-else-if="this.$route.params.card == 'number-of-inspection-persons'"
    />
    <telephone-advisory-reports-number-card
      v-else-if="this.$route.params.card == 'number-of-reports-to-covid19-telephone-advisory-center'"
    />
    <consultation-desk-reports-number-card
      v-else-if="this.$route.params.card == 'number-of-reports-to-covid19-consultation-desk'"
    />
    <population-card
      v-else-if="this.$route.params.card == 'changes-of-population-around-toyama-station'"
    />
  </div>
</template>

<script>
import Data from '@/data/data.json'
import PopulationData from '@/data/population.json'

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
import InspectionPersonsNumberCard from '@/components/cards/InspectionPersonsNumberCard.vue'
import TelephoneAdvisoryReportsNumberCard from '@/components/cards/TelephoneAdvisoryReportsNumberCard.vue'
import ConsultationDeskReportsNumberCard from '@/components/cards/ConsultationDeskReportsNumberCard.vue'
import PopulationCard from '@/components/cards/PopulationCard.vue'

export default {
  components: {
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
    InspectionPersonsNumberCard,
    TelephoneAdvisoryReportsNumberCard,
    ConsultationDeskReportsNumberCard,
    PopulationCard
  },
  data() {
    let title, updatedAt
    switch (this.$route.params.card) {
      case 'details-of-confirmed-cases':
        title = this.$t('検査陽性者の状況')
        updatedAt = Data.main_summary.date
        break
      case 'number-of-confirmed-cases':
        title = this.$t('陽性患者数')
        updatedAt = Data.patients_summary.date
        break
      case 'attributes-of-confirmed-cases':
        title = this.$t('陽性患者の属性')
        updatedAt = Data.patients.date
        break
      case 'patients-by-residence':
        title = this.$t('陽性患者数(居住地別)')
        updatedAt = Data.patients_by_residence.date
        break
      case 'patients-by-age':
        title = this.$t('陽性患者数(年代別)')
        updatedAt = Data.patients_by_age.date
        break
      case 'patients-by-gender':
        title = this.$t('陽性患者数(性別)')
        updatedAt = Data.patients_by_gender.date
        break
      case 'number-of-dead-persons':
        title = this.$t('死亡者数')
        updatedAt = Data.dead_persons.date
        break
      case 'number-of-discharged-persons':
        title = this.$t('退院者数')
        updatedAt = Data.discharged_persons.date
        break
      case 'details-of-tested-cases':
        title = this.$t('検査実施状況')
        updatedAt = Data.inspection_status_summary.date
        break
      case 'rate-of-confirmed-cases':
        title = this.$t('検査陽性率')
        updatedAt = Data.positive_rate.date
        break
      case 'number-of-inspection-persons':
        title = this.$t('検査実施人数')
        updatedAt = Data.inspection_persons.date
        break
      case 'number-of-reports-to-covid19-telephone-advisory-center':
        title = this.$t('新型コロナウイルス感染症に関する一般相談件数')
        updatedAt = Data.contacts.date
        break
      case 'number-of-reports-to-covid19-consultation-desk':
        title = this.$t('帰国者・接触者相談センターへの相談件数')
        updatedAt = Data.querents.date
        break
      case 'changes-of-population-around-toyama-station':
        title = this.$t('富山駅周辺の人口の推移（参考値）')
        updatedAt = PopulationData.date
        break
    }

    const data = {
      title,
      updatedAt
    }
    return data
  },
  head() {
    const url = 'https://stopcovid19-toyama.netlify.app/'
    const timestamp = new Date().getTime()
    const ogpImage =
      this.$i18n.locale === 'ja'
        ? `${url}/ogp/${this.$route.params.card}.png?t=${timestamp}`
        : `${url}/ogp/${this.$i18n.locale}/${this.$route.params.card}.png?t=${timestamp}`
    const description = `${this.updatedAt} | ${this.$t(
      '当サイトは新型コロナウイルス感染症 (COVID-19) に関する最新情報を提供するために、有志が開設したものです。'
    )}`

    return {
      title: this.title,
      meta: [
        {
          hid: 'og:url',
          property: 'og:url',
          content: url + this.$route.path + '/'
        },
        {
          hid: 'og:title',
          property: 'og:title',
          content:
            this.title +
            ' | ' +
            this.$t('富山県公認') +
            ' ' +
            this.$t('新型コロナウイルス感染症') +
            ' ' +
            this.$t('対策サイト')
        },
        {
          hid: 'description',
          name: 'description',
          content: description
        },
        {
          hid: 'og:description',
          property: 'og:description',
          content: description
        },
        {
          hid: 'og:image',
          property: 'og:image',
          content:
            'https://raw.githubusercontent.com/Terachan0117/covid19-toyama/development/static/ogp.png'
        },
        {
          hid: 'twitter:image',
          name: 'twitter:image',
          content: ogpImage
        }
      ]
    }
  }
}
</script>

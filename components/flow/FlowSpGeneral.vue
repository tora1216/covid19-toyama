<template>
  <div :class="$style.container">
    <p :class="$style.heading">
      <span :class="[$style.icon, $style.top]" aria-hidden="true">
        <HumanIcon />
      </span>
      <span :class="$style.fzMedium">{{ $t('一般の方') }}</span>
    </p>
    <ul :class="[$style.rectContainer, $style.double]">
      <li :class="$style.symptom">
        <span>{{ $t('息苦しさ（呼吸困難）') }}</span>
      </li>
      <li :class="$style.symptom">
        <span>{{ $t('強いだるさ（倦怠感）') }}</span>
      </li>
      <li :class="$style.symptom">
        <span>{{ $t('高熱') }}</span>
      </li>
      <li :class="$style.symptom">
        <span>
          <i18n path="{cold}のような症状">
            <span :class="$style.ConditionsItemLarger" place="cold">{{
              $t('風邪')
            }}</span>
          </i18n>
        </span>
      </li>
    </ul>
    <p>{{ $t('いずれかの症状に該当する場合には、すぐに御相談ください。（これらに該当しない場合の相談も可能です。）') }}
    <p>{{ $t('症状が４日以上続く場合は必ずご相談ください。症状には個人差がありますので、強い症状と思う場合にはすぐに相談してください。解熱剤などを飲み続けなければならない方も同様です。') }}</p>
    <a
      v-scroll-to="{
        el: '#consult',
        onDone: onDoneScroll
      }"
      href="#consult"
      :class="[$style.button, $style.clickable]"
    >
      <span :class="$style.text">{{ $t('帰国者接触者相談センターへ') }}</span>
      <ArrowForwardIcon :class="$style.icon" />
    </a>
  </div>
</template>

<script lang="ts">
import { onDoneScroll } from '@/utils/vueScrollTo'
import HumanIcon from '@/static/flow/responsive/accessibility.svg'
import ArrowForwardIcon from '@/static/flow/responsive/arrow_forward.svg'
export default {
  components: { HumanIcon, ArrowForwardIcon },
  methods: { onDoneScroll }
}
</script>

<style module lang="scss">
@import '@/components/flow/flow_sp.scss';
</style>

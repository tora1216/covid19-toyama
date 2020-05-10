<template>
  <div :class="$style.container">
    <p :class="$style.heading">
      <span :class="[$style.icon, $style.top]" aria-hidden="true">
        <HumanIcon />
      </span>
      <span :class="$style.fzMedium">{{ $t('一般の方') }}</span>
    </p>
    <ul :class="[$style.rectContainer, $style.triple]">
      <li :class="$style.symptom">
        {{ $t('息苦しさ(呼吸困難)') }}
      </li>
      <li :class="$style.symptom">
        {{ $t('強いだるさ(倦怠感)') }}
      </li>
      <li :class="$style.symptom">
        {{ $t('高熱') }}
      </li>
    </ul>
    <p :class="[$style.heading, $style.mt10]">
      <span :class="[$style.underline, $style.fzXLarge]">
        {{ $t('いずれかに該当する方') }}
      </span>
    </p>
    <p :class="$style.mt10">{{ $t('発熱や咳など比較的軽い風邪の症状が続く場合も、御相談ください。（これらに該当しない場合の相談も可能です。）') }}
    <p :class="$style.mt10">{{ $t('症状が４日以上続く場合は必ずご相談ください。症状には個人差がありますので、強い症状と思う場合にはすぐに相談してください。解熱剤などを飲み続けなければならない方も同様です。') }}</p>
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
.rectContainer {
  // general
  &.triple {
    margin-left: px2vw(-11);
    margin-right: px2vw(-11);

    > .symptom {
      margin-left: px2vw(11);
      margin-right: px2vw(11);
      flex-grow: 10;
    }
  }
}
</style>

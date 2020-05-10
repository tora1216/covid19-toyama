<template>
  <div :class="$style.container">
    <div :class="[$style.heading, $style.multi]">
      <span :class="[$style.item, $style.fzMedium]">
        <span :class="$style.icon">
          <DirectionsWalkIcon aria-hidden="true" />
        </span>
        {{ $t('ご高齢な方') }}
      </span>
      <span :class="[$style.item, $style.fzMedium]">
        <span :class="$style.icon">
          <AccessibleIcon aria-hidden="true" />
        </span>
        {{ $t('基礎疾患のある方') }}
      </span>
      <span :class="[$style.item, $style.fzMedium]">
        <span :class="$style.icon">
          <PregnantWomanIcon aria-hidden="true" />
        </span>
        {{ $t('妊娠中の方') }}
      </span>
    </div>
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
        {{ $t('いずれかに該当する') }}
      </span>
    </p>
    <p :class="$style.mt10">{{ $t('発熱や咳などの比較的軽い風邪の症状がある場合も、すぐに御相談ください。（これらに該当しない場合の相談も可能です。）') }}
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
import AccessibleIcon from '@/static/flow/responsive/accessible.svg'
import ArrowForwardIcon from '@/static/flow/responsive/arrow_forward.svg'
import DirectionsWalkIcon from '@/static/flow/responsive/directions_walk.svg'
import PregnantWomanIcon from '@/static/flow/responsive/pregnant_woman.svg'

export default {
  components: {
    AccessibleIcon,
    ArrowForwardIcon,
    DirectionsWalkIcon,
    PregnantWomanIcon
  },
  methods: { onDoneScroll }
}
</script>

<style module lang="scss">
@import '@/components/flow/flow_sp.scss';
.rectContainer {
  // elder
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
.heading {
  // elder
  &.multi {
    display: flex;
    flex-wrap: wrap;
    justify-content: space-around;
    margin-top: px2vw(-20);
    margin-left: px2vw(-10);
    margin-right: px2vw(-10);

    .icon {
      display: block;
      margin-bottom: 0;
      width: px2vw(50);
      height: px2vw(50);
    }

    > .item {
      display: flex;
      align-items: center;
      margin: px2vw(20) px2vw(10) 0;

      svg {
        margin-right: px2vw(5);
      }
    }
  }
}

@include largerThan($small) {
  $vw: 960;

  .heading {
    &.multi {
      margin-top: px2vw(-20, $vw);
      margin-left: px2vw(-10, $vw);
      margin-right: px2vw(-10, $vw);

      .icon {
        width: px2vw(50, $vw);
        height: px2vw(50, $vw);
      }

      > .item {
        margin: px2vw(20, $vw) px2vw(10, $vw) 0;

        svg {
          margin-right: px2vw(5, $vw);
        }
      }
    }
  }
}
</style>

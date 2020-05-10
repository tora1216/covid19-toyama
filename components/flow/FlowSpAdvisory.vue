<template>
  <div :class="$style.container">
    <h4 id="consult" :class="[$style.heading, $style.fzXLarge]">
      {{ $t('帰国者接触者相談センター') }}
    </h4>
    <p :class="[$style.open, $style.fzMedium, $style.mb10]">
      <span>{{ $t('24時間対応') }}</span>
    </p>
    <p :class="$style.mt10">
      {{ $t('※夜間・休日は、メッセージにより緊急電話番号をご案内します') }}
    </p>
    <dl :class="$style.telCenter">
      <dt>{{ $t('富山市保健所(富山市)') }}</dt>
      <dd>
          <div :class="[$style.phone, $style.fzNumeric]">
            <span :class="$style.icon">
              <PhoneIcon alt="Phone" />
            </span>
            <a href="tel:0764281152">076-428-1152</a>
          </div>
      </dd>
      <dt>{{ $t('高岡厚生センター(高岡市)') }}</dt>
      <dd>
          <div :class="[$style.phone, $style.fzNumeric]">
            <span :class="$style.icon">
              <PhoneIcon alt="Phone" />
            </span>
            <a href="tel:0766268414">0766-26-8414</a>
          </div>
      </dd>
      <dt>{{ $t('高岡厚生センター射水支所(射水市)') }}</dt>
      <dd>
          <div :class="[$style.phone, $style.fzNumeric]">
            <span :class="$style.icon">
              <PhoneIcon alt="Phone" />
            </span>
            <a href="tel:0766562666">0766-56-2666</a>
          </div>
      </dd>
      <dt>{{ $t('高岡厚生センター氷見支所(氷見市)') }}</dt>
      <dd>
          <div :class="[$style.phone, $style.fzNumeric]">
            <span :class="$style.icon">
              <PhoneIcon alt="Phone" />
            </span>
            <a href="tel:0766741780">0766-74-1780</a>
          </div>
      </dd>
      <dt>{{ $t('砺波厚生センター(砺波市、南砺市)') }}</dt>
      <dd>
          <div :class="[$style.phone, $style.fzNumeric]">
            <span :class="$style.icon">
              <PhoneIcon alt="Phone" />
            </span>
            <a href="tel:0763223512">0763-22-3512</a>
          </div>
      </dd>
      <dt>{{ $t('砺波厚生センター小矢部支所(小矢部市)') }}</dt>
      <dd>
          <div :class="[$style.phone, $style.fzNumeric]">
            <span :class="$style.icon">
              <PhoneIcon alt="Phone" />
            </span>
            <a href="tel:0766671070">0766-67-1070</a>
          </div>
      </dd>
      <dt>{{ $t('新川厚生センター(黒部市、入善町、朝日町)') }}</dt>
      <dd>
          <div :class="[$style.phone, $style.fzNumeric]">
            <span :class="$style.icon">
              <PhoneIcon alt="Phone" />
            </span>
            <a href="tel:0765522647">0765-52-2647</a>
          </div>
      </dd>
      <dt>{{ $t('新川厚生センター魚津支所(魚津市)') }}</dt>
      <dd>
          <div :class="[$style.phone, $style.fzNumeric]">
            <span :class="$style.icon">
              <PhoneIcon alt="Phone" />
            </span>
            <a href="tel:0765240359">0765-24-0359</a>
          </div>
      </dd>
      <dt>{{ $t('中部厚生センター(滑川市、舟橋村、上市町、立山町)') }}</dt>
      <dd>
          <div :class="[$style.phone, $style.fzNumeric]">
            <span :class="$style.icon">
              <PhoneIcon alt="Phone" />
            </span>
            <a href="tel:0764720637">076-472-0637</a>
          </div>
      </dd>
    </dl>
  </div>
</template>

<script lang="ts">
import PhoneIcon from '@/static/flow/responsive/phone.svg'
export default {
  components: { PhoneIcon }
}
</script>

<style module lang="scss">
@import '@/components/flow/flow_sp.scss';
// advisory
.telCenter {
  padding: 0 px2vw(10) px2vw(20);
  text-align: center;
  dt {
    padding-top: 20px;
  }
}
.open {
  margin-top: px2vw(20);
  display: flex;
  justify-content: center;
  > span {
    display: flex;
    justify-content: center;
    align-items: center;
    background-color: $white;
    color: $green-1;
    padding: px2vw(20) px2vw(40);
    border-radius: px2vw(6);
  }
}
.daytime {
  margin-top: px2vw(20);
  display: flex;
  > * {
    padding: px2vw(20) px2vw(10);
    display: flex;
    align-items: center;
    justify-content: center;
  }
  .title {
    text-align: center;
    flex-basis: 40%;
  }
  .link {
    > a {
      text-decoration: none;
    }
  }
}
.night {
  margin: px2vw(30) auto;
  padding-left: 0 !important;
  text-align: center;
  > li {
    list-style-type: none;
    &:not(:first-child) {
      margin-top: px2vw(20);
    }
  }
}
@include largerThan($small) {
  $vw: 960;
  .open {
    margin-top: px2vw(20, $vw);
    > span {
      padding: px2vw(20) px2vw(40, $vw);
      border-radius: px2vw(6, $vw);
    }
  }
  .daytime {
    margin-top: px2vw(20, $vw);
    > * {
      padding: px2vw(30) px2vw(10, $vw);
    }
  }
  .night {
    margin: px2vw(30, $vw) auto;
    > li {
      &:not(:first-child) {
        margin-top: px2vw(20, $vw);
      }
    }
  }
}
</style>

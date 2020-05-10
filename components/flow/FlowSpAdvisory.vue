<template>
  <div :class="$style.container">
    <h4 id="consult" :class="[$style.heading, $style.fzXLarge]">
      {{ $t('帰国者接触者相談センター') }}
      <!--<small :class="[$style.break, $style.fzRegular, $style.mt5]">{{
        $t('（新型コロナ受診相談窓口）')
      }}</small>-->
    </h4>
    <p :class="[$style.open, $style.fzSmall]">
      <span>{{ $t('24時間対応') }}</span>
    </p>
    <dl :class="$style.telCenter">
      <dt>富山市保健所(富山市)</dt>
      <dd>076-428-1152</dd>
      <dt>高岡厚生センター(高岡市)</dt>
      <dd>0766-26-8414</dd>
      <dt>高岡厚生センター射水支所(射水市)</dt>
      <dd>0766-56-2666</dd>
      <dt>高岡厚生センター氷見支所(氷見市)</dt>
      <dd>0766-74-1780</dd>
      <dt>砺波厚生センター(砺波市、南砺市)</dt>
      <dd>0763-22-3512</dd>
      <dt>砺波厚生センター小矢部支所(小矢部市)</dt>
      <dd>0766-67-1070</dd>
      <dt>新川厚生センター(黒部市、入善町、朝日町)</dt>
      <dd>0765-52-2647</dd>
      <dt>新川厚生センター魚津支所(魚津市)</dt>
      <dd>0765-24-0359</dd>
      <dt>中部厚生センター(滑川市、舟橋村、上市町、立山町)</dt>
      <dd>076-472-0637</dd>
    </dl>
    <dl>
      <div :class="$style.daytime">
        <dd :class="$style.link">
          <a
            href="http://www.pref.toyama.jp/cms_sec/1205/kj00021473.html#page_list"
            target="_blank"
            rel="noopener noreferrer"
          >
            {{ $t('センターの電話番号はこちら') }}
            <v-icon size="16">
              mdi-open-in-new
            </v-icon>
          </a>
        </dd>
      </div>
    </dl>
    <span>{{ $t('※夜間・休日は、メッセージにより緊急電話番号をご案内します') }}</span>
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

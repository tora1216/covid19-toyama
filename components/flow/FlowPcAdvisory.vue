<template>
  <div :class="$style.Advisory">
    <div :class="$style.AdvisoryContainer">
      <div :class="$style.AdvisoryContents">
        <div>
          <span :class="$style.AdvisoryContentsTitle">{{
            $t('帰国者・接触者相談センター')
          }}</span>
        </div>
        <div :class="[$style.AdvisoryContentsColsSentense, 'mt-4']">
          {{ $t('帰国者・接触者 電話相談センター') }}
        </div>
        <div>
          <div :class="[$style.AdvisoryBoxContainer, $style.AdvisoryWhiteBox]">
            <span :class="$style.AdvisoryWhiteBoxSentense">
              {{ $t('24時間対応') }}
            </span>
          </div>
        </div>
      </div>

      <div :class="$style.AdvisoryContents">
        <div class="py-8">
          <div :class="$style.AdvisoryContentsTitle2">
            {{ $t('平日(8:30～17:15)') }}
          </div>
          <div
            :class="[
              $style.AdvisoryLink,
              $style.AdvisoryBlockCentering,
              'mt-4'
            ]"
          >
            <a
              href="https://www.fukushihoken.metro.tokyo.lg.jp/iryo/kansen/coronasodan.html"
              target="_blank"
              rel="noopener"
            >
              <span>{{ $t('各保健所の電話番号は福祉保健局HPへ') }}</span>
              <v-icon size="18">
                mdi-open-in-new
              </v-icon>
            </a>
          </div>
        </div>
      </div>

      <div :class="$style.AdvisoryContents">
        <div :class="$style.AdvisoryContentsTitle2">
        {{ $t('平日(8:30～17:15)') }}
        </div>
        <dl>
          <dt>{{ $t('富山市保健所(富山市)') }}</dt>
          <dd>076-428-1152</dd>
          <dt>{{ $t('高岡厚生センター(高岡市)') }}</dt>
          <dd>0766-26-8414</dd>
          <dt>{{ $t('高岡厚生センター射水支所(射水市)') }}</dt>
          <dd>0766-56-2666</dd>
          <dt>{{ $t('高岡厚生センター氷見支所(氷見市)') }}</dt>
          <dd>0766-74-1780</dd>
          <dt>{{ $t('砺波厚生センター(砺波市、南砺市)') }}</dt>
          <dd>0763-22-3512</dd>
          <dt>{{ $t('砺波厚生センター小矢部支所(小矢部市)') }}</dt>
          <dd>0766-67-1070</dd>
          <dt>{{ $t('新川厚生センター(黒部市、入善町、朝日町)') }}</dt>
          <dd>0765-52-2647</dd>
          <dt>{{ $t('新川厚生センター魚津支所(魚津市)') }}</dt>
          <dd>0765-24-0359</dd>
          <dt>{{ $t('中部厚生センター(滑川市、舟橋村、上市町、立山町)') }}</dt>
          <dd>076-472-0637</dd>
        </dl>
        {{ $t('※夜間・休日は、メッセージにより緊急電話番号をご案内します。') }}
        <div v-if="!['ja', 'ja-basic'].includes($i18n.locale)" class="pt-8">
          <span>{{ $t('ひまわり') }}</span>
        </div>
      </div>
    </div>
  </div>
</template>

<style module lang="scss">
.Advisory {
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  height: 100%;
  color: $gray-2;

  &Container {
    background-color: $gray-5;
    border-radius: 4px;
    height: 100%;
    padding: 30px 20px 20px 20px;
    margin-bottom: 10px;
    text-align: center;
  }

  &Contents {
    font-weight: bold;

    &:not(:first-child) {
      border-top: 0.5px solid $gray-4;
    }

    &Title {
      font-size: 26px;
      line-height: 28px;
    }

    &Title2 {
      font-size: 18px;
    }

    &SubTitle {
      font-size: 18px;
    }

    &ColsSentense {
      line-height: 18px;
    }
  }

  &BlockCentering {
    display: flex;
    justify-content: center;
  }

  &Link {
    line-height: 22px;
    text-align: left;

    a {
      color: rgba(0, 0, 0, 0.87);
      text-decoration: none;

      &:hover {
        text-decoration: underline;
      }
    }
  }

  &TelephoneArea {
    display: inline-flex;
  }

  &Telephone {
    display: flex;
    align-items: center;
    font-size: 27px;
    font-weight: bold;

    &:link,
    &:visited,
    &:hover,
    &:active,
    &:focus {
      color: inherit;
      text-decoration: none;
      outline: 1px dotted $gray-3;
    }

    &Icon {
      display: inline-block;
      margin-right: 5px;
      width: 26px;
      height: 26px;
    }
  }

  &BoxContainer {
    border-radius: 4px;
    text-align: center;
    padding: 20px 10px;
    margin: 24px auto;
  }

  &WhiteBox {
    background-color: $white;
    width: 160px;
    padding: 10px;

    &Sentense {
      color: $green-1;
      font-size: 18px;
      font-weight: bold;
    }
  }
}
</style>

<template>
  <div class="ToyamaAlert">
    <div class="ToyamaAlert-heading">
      <h3 class="ToyamaAlert-title">
        {{ $t('富山アラート') }}
      </h3>
      <div class="ToyamaAlert-link">
        <link-to-information-about-toyamaalert />
      </div>
    </div>
    <div class="ToyamaAlert-content">
      <div class="ToyamaAlert-block">
        <p>
          {{
            $t(
              '今後さらに感染が拡大すると、「Stage2」に移行となり、夜間の外出自粛や感染拡大地域への移動自粛などをお願いせざるを得ない状況となります。以下、改めてのお願いです。'
            )
          }}
        </p>
      </div>
      <div class="ToyamaAlert-block">
        <ul>
          <li>{{ $t('3密の徹底的な回避、手洗いやマスクの着用など「新しい生活様式」の徹底') }}</li>
          <li>{{ $t('感染者が多く発生している地域との往来は特に緊要度の高いものを除き自粛') }}</li>
          <li>{{ $t('親族や友人が集まり会食する機会等における感染防止対策の徹底') }}</li>
          <li>{{ $t('業種ごとの感染拡大防止ガイドラインの遵守') }}</li>
          <li>{{ $t('重症化しやすい高齢者への感染予防行動の徹底、大声をあげる環境の徹底的な回避') }}</li>
        </ul>
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import Vue from 'vue'
import LinkToInformationAboutToyamaalert from '@/components/LinkToInformationAboutToyamaalert.vue'
export default Vue.extend({
  components: {
    LinkToInformationAboutToyamaalert
  }
})
</script>

<style lang="scss">
$mediumLarge: 900;
$tinySmall: 420;
@function px2vw($px, $vw: $mediumLarge) {
  @return $px / $vw * 100vw;
}
.ToyamaAlert {
  @include card-container();
  padding: 10px;
  margin-bottom: 20px;
  .ToyamaAlert-heading {
    display: flex;
    flex-wrap: wrap;
    align-items: center;
    justify-content: space-between;
    margin-bottom: 12px;
    .ToyamaAlert-title {
      display: flex;
      align-items: center;
      padding: 12px;
      color: $gray-2;
      @include card-h2();
      &-icon {
        margin: 3px;
      }
    }
    .ToyamaAlert-link {
      display: flex;
      flex-wrap: wrap;
      align-items: center;
      justify-content: flex-end;
      padding-left: 12px;
      @include lessThan($medium) {
        justify-content: flex-start;
      }
    }
  }
  .ToyamaAlert-content {
    @include font-size(14);
    display: flex;
    flex-wrap: wrap;
    .ToyamaAlert-block {
      flex: 1 1 100%;
      padding: 12px;
    }

  }
}
</style>